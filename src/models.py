import re
import spacy

# importing the skills
from src.skills import TIER1_PHRASES, TIER2_EXACT_CASE, TIER3_CUSTOM

LABEL = "SKILL"


# Baseline
def baseline_extract_skills(text, skills):
    """Find skills in a text using plain dictionary matching."""
    found_skills = []

    text = text.lower()

    for skill in skills:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


# Entity Ruler
def any_case_pattern(nlp, text, skill):
    tokens = [{"LOWER": t.lower_} for t in nlp.make_doc(text)]
    return {"label": LABEL, "pattern": tokens, "id": skill}


def exact_case_pattern(nlp, text, skill):
    tokens = [{"ORTH": t.text} for t in nlp.make_doc(text)]
    return {"label": LABEL, "pattern": tokens, "id": skill}


def build_patterns(nlp):
    """Build all patterns from the three tiers."""
    patterns = []

    # Tier 1: the phrase is its own canonical name, matched in any case
    for phrase in TIER1_PHRASES:
        patterns.append(any_case_pattern(nlp, phrase, skill=phrase))

    # Tier 2: short/ambiguous words, exact spelling only
    for skill, spellings in TIER2_EXACT_CASE.items():
        for spelling in spellings:
            patterns.append(exact_case_pattern(nlp, spelling, skill))

    # Tier 3: custom aliases, each list has its own matching rule
    for skill, aliases in TIER3_CUSTOM.items():
        for text in aliases.get("any_case", []):
            patterns.append(any_case_pattern(nlp, text, skill))
        for text in aliases.get("exact_case", []):
            patterns.append(exact_case_pattern(nlp, text, skill))

    return patterns


def build_nlp():
    """Blank Swedish pipeline (tokenizer + entity ruler) with all rules added."""
    nlp = spacy.blank("sv")
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(build_patterns(nlp))
    return nlp


def entity_ruler_extract_skills(text, nlp):
    """Find skills in a text using the spaCy entity ruler pipeline.

    Args:
        text: The job ad text.
        nlp: Pipeline created with build_nlp().

    Returns:
        Sorted list of unique canonical skill names found.
    """
    doc = nlp(text)
    found_skills = sorted({ent.ent_id_ for ent in doc.ents if ent.label_ == LABEL})
    return found_skills
