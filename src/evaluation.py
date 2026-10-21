"""
Evaluation utilities for skill extraction.

Shared by validation and test. Gold and predictions use the same format, {ad_id: set_of_skills}, and are normalized with the same alias map before scoring.
"""

import pandas as pd
import html
import re
from collections import Counter, defaultdict
from IPython.display import HTML, display

digit = 3
COLORS = {"tp": "#b7e4c7", "fp": "#ffb3b3", "fn": "#ffe08a"}


# Lookup table
def build_alias_to_canonical(tier1_phrases, tier2_exact_case, tier3_custom):
    """Build a lookup table from casefolded alias to canonical skill name."""

    alias_to_canonical = {}

    for skill in tier1_phrases:
        alias_to_canonical[skill.casefold()] = (
            skill  # each skill maps to itself, and the canonical form is collected in the dict
        )

    for canonical, spellings in tier2_exact_case.items():
        for spelling in spellings:
            alias_to_canonical[spelling.casefold()] = (
                canonical  # each spelling is casefolded and points to the canonical name of the dict from tier 2. The canonical form becomes the normalised verion.
            )

    for canonical, aliases in tier3_custom.items():
        for alias in aliases.get("any_case", []):
            alias_to_canonical[alias.casefold()] = canonical

        for alias in aliases.get("exact_case", []):
            alias_to_canonical[alias.casefold()] = canonical

    return alias_to_canonical


# Normalization - using the lookup table to standardise the skills
def normalize_skills_ad(skills, alias_to_canonical):
    """Convert the skills of one ad to their canonical names."""

    normalized = set()

    for skill in skills:
        clean_skill = skill.strip()

        canonical = alias_to_canonical.get(clean_skill.casefold(), clean_skill)

        normalized.add(canonical)

    return normalized


def normalize_all_ads(data, alias_to_canonical):
    """Apply normalize_skills to every ad."""

    return {
        ad_id: normalize_skills_ad(skills, alias_to_canonical)
        for ad_id, skills in data.items()
    }


# Metrics
def calculate_micro_metrics(gold, pred):
    """Micro precision, recall and F1 over all ads."""
    tp = fp = fn = 0

    for ad_id, gold in gold.items():
        prediction = pred.get(ad_id, set())
        tp += len(gold & prediction)  # found and correct
        fp += len(prediction - gold)  # found but wrong
        fn += len(gold - prediction)  # missed

    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0

    return {
        "precision": round(precision, digit),
        "recall": round(recall, digit),
        "f1": round(f1, digit),
        "tp": tp,
        "fp": fp,
        "fn": fn,
    }


def calculate_macro_metrics(gold, pred):
    """Macro precision, recall and F1: score each ad, then average."""
    scores = []

    for ad_id, g in gold.items():
        p = pred.get(ad_id, set())
        tp = len(g & p)

        precision = tp / len(p) if p else 0
        recall = tp / len(g) if g else 0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0
        scores.append((precision, recall, f1))

    n = len(scores)
    return {
        "precision": round(sum(s[0] for s in scores) / n, digit),
        "recall": round(sum(s[1] for s in scores) / n, digit),
        "f1": round(sum(s[2] for s in scores) / n, digit),
    }


# Error analysis
def create_error_analysis(gold, pred):
    """List of ads with errors: {"id", "false_positives", "false_negatives"}."""
    errors = []
    for ad_id, g in gold.items():
        p = pred.get(ad_id, set())
        if p - g or g - p:
            errors.append(
                {
                    "id": ad_id,
                    "false_positives": sorted(p - g),
                    "false_negatives": sorted(g - p),
                }
            )
    return errors


def summarize_errors(errors, alias_to_canonical, top_n=20):
    """Top FP/FN and FN categories from the output of create_error_analysis."""
    known = set(alias_to_canonical.values())
    fp = Counter(s for e in errors for s in e["false_positives"])
    fn = Counter(s for e in errors for s in e["false_negatives"])
    fn_types = Counter(
        "not in dictionary" if s not in known else "in dictionary, not matched"
        for s in fn.elements()
    )
    return {
        "top_fp": fp.most_common(top_n),
        "top_fn": fn.most_common(top_n),
        "fn_types": dict(fn_types),
    }


def errors_to_dataframe(errors):
    """Errors as a DataFrame with counts, sorted by most missed skills."""
    df = pd.DataFrame(errors)
    if df.empty:
        return df
    df["n_fp"] = df["false_positives"].str.len()
    df["n_fn"] = df["false_negatives"].str.len()
    return df.sort_values("n_fn", ascending=False).reset_index(drop=True)


# Better review entire ad description by id
def build_canonical_to_aliases(alias_to_canonical):
    """{canonical: [all casefolded aliases that map to it]}."""
    result = defaultdict(list)
    for alias, canonical in alias_to_canonical.items():
        result[canonical].append(alias)
    return result


# Visuals cues on right/wrong skills detected/missed
def review_ad(ad_id, df, gold, pred, aliases, id_col="id", text_col="description"):
    """Show one ad with skills highlighted: green = correct, red = extra, yellow = missed."""

    # Get the ad text and the skill sets. Fails if the id is not in the set
    ad_id = str(ad_id)
    row = df[df[id_col].astype(str) == ad_id]
    if row.empty:
        raise ValueError(f"No ad with id {ad_id}")
    text = row.iloc[0][text_col]

    # Identify gold and predicted skills
    g = gold[ad_id]
    p = pred.get(ad_id, set())

    # Label every skill
    labels = {}
    for skill in g & p:  # in both -> correct
        labels[skill] = "tp"
    for skill in p - g:  # only predicted -> extra
        labels[skill] = "fp"
    for skill in g - p:  # only in gold -> missed
        labels[skill] = "fn"

    # Give each written form of a skill (its name and its aliases) the same label
    form_label = {}
    for skill, label in labels.items():
        form_label[skill.casefold()] = label
        for alias in aliases.get(skill, []):
            form_label[alias.casefold()] = label

    # Highlight every form found in the text
    body = html.escape(text)  # make the text safe to show as HTML
    if form_label:
        longest_first = sorted(form_label, key=len, reverse=True)
        pattern = re.compile(
            r"(?<!\w)(" + "|".join(map(re.escape, longest_first)) + r")(?!\w)",
            re.IGNORECASE,
        )
        body = pattern.sub(
            lambda m: f'<span style="background:{COLORS[form_label[m.group(0).casefold()]]};'
            f'color:black">{m.group(0)}</span>',
            body,
        )

    display(
        HTML(
            f"<b>Ad {ad_id}</b><br>"
            f"<span style='background:{COLORS['tp']};color:black'>correct</span> "
            f"<span style='background:{COLORS['fp']};color:black'>extra</span> "
            f"<span style='background:{COLORS['fn']};color:black'>missed</span><br><br>"
            f"<div style='white-space:pre-wrap'>{body}</div>"
        )
    )
    print("gold:", sorted(g))
    print("pred:", sorted(p))
