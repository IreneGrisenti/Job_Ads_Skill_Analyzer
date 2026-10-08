"""
Download the taxonomy skills linked to SSYK 2511 and save them to JSON.
"""
 
import json
from pathlib import Path
 
import requests
 
URL = (
    "https://data.arbetsformedlingen.se/taxonomy/version/latest/query/"
    "skills-with-related-skill-headlines-and-ssyk-level-4-groups/"
    "skills-with-related-skill-headlines-and-ssyk-level-4-groups.json"
)
OCCUPATION_GROUP = "UXKZ_3zZ_ipB"  # SSYK 2511 (same ID as the ads' occupation_group)
 
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "data" / "taxonomi_2511.json"
 
 
def fetch_skills(group_id: str) -> list[dict]:
    """Return the skills related to one SSYK-4 group."""
    response = requests.get(URL, timeout=60)
    response.raise_for_status()
 
    # The file is a list of SSYK-4 groups, each group has a "related" list of skills.
    groups = response.json()["data"]["concepts"]
    group = next((g for g in groups if g["id"] == group_id), None)
    if group is None:
        raise ValueError(f"Group {group_id} not found in the taxonomy file")
 
    return [
        {
            "skill_id": s["id"],
            "skill": s["preferred_label"],
            # A skill can belong to more than one headline, so keep them all.
            "headlines": [h["preferred_label"] for h in s.get("broader", [])],
        }
        for s in group.get("related", [])
        if s.get("type") == "skill"
    ]
 
 
def main():
    skills = fetch_skills(OCCUPATION_GROUP)
    print(f"Found {len(skills)} skills for group {OCCUPATION_GROUP}")
 
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(skills, f, ensure_ascii=False, indent=2)
    print(f"Saved to {OUTPUT_FILE}")
 
 
if __name__ == "__main__":
    main()