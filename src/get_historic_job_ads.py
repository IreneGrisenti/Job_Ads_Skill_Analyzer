"""
Download job ads for SSYK 2511 (Systemanalytiker och IT-arkitekter) from the JobTech historical API and save a trimmed version to JSON.
"""

import json
import time
from datetime import date
from pathlib import Path
import requests

URL = "https://historical.api.jobtechdev.se/search"
OCCUPATION_GROUP = "UXKZ_3zZ_ipB"  # this is the code for the occupation group we identified as SSYK 2511
PAGE_SIZE = 100  # limit of ads per request


START = date(2026, 1, 1)  # Included
END = date.today()  # Included

OUTPUT_FILE = (
    Path(__file__).resolve().parent.parent / "data" / "raw_historic_ads_2511.json"
)


def month_windows(start: date, end: date):
    """I fetch one month at the time because there is a max limit of data retrieval."""
    current = start
    while current < end:
        nxt = date(
            current.year + (current.month == 12), current.month % 12 + 1, 1
        )  # calculates the beginning of the next month
        yield current, min(nxt, end)
        current = nxt


def fetch_ads(start: date, end: date) -> list[dict]:
    """Return all raw ads published between start and end."""
    ads, offset = [], 0
    while True:
        params = {
            "occupation-group": OCCUPATION_GROUP,
            "published-after": start.isoformat(),
            "published-before": end.isoformat(),
            "sort": "pubdate-asc",  # fixed order so pages don't overlap
            "limit": PAGE_SIZE,
            "offset": offset,
        }
        response = requests.get(URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        ads.extend(data["hits"])
        offset += PAGE_SIZE
        if offset >= data["total"]["value"]:
            return ads
        time.sleep(0.5)


def trim(ad: dict) -> dict:
    """Keep only the fields I need."""
    return {
        "id": ad["original_id"],  # ID of the ad itself (same across versions)
        "version_id": ad.get(
            "id"
        ),  # ID of a specific version of the ad, it is different for each republished version
        "title": ad.get("headline"),
        "employer": (ad.get("employer") or {}).get("name"),
        "municipality": (ad.get("workplace_address") or {}).get("municipality"),
        "region": (ad.get("workplace_address") or {}).get("region"),
        "occupation": (ad.get("occupation") or {}).get("label"),
        "published": ad.get("publication_date"),
        "deadline": ad.get("application_deadline"),
        "description": (ad.get("description") or {}).get("text"),
    }


def main():
    raw = []
    for start, end in month_windows(START, END):
        ads = fetch_ads(start, end)
        print(f"{start} -> {end} | {len(ads)} ads")
        raw.extend(ads)

    # drop repeated fetches based on the version_id
    # there will still be duplicates if the ad was republished (it is a limit stated for the Historical API)
    unique = {ad["id"]: ad for ad in raw}
    print(f"Removed {len(raw) - len(unique)} duplicate fetches")

    trimmed = [trim(ad) for ad in unique.values()]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(trimmed, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(trimmed)} ads to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
