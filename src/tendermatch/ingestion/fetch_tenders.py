
import json
from pathlib import Path

import requests

API_URL = "https://api.ted.europa.eu/v3/notices/search"

# Search only IT-related contract notices
payload = {
    "query": (
        "publication-date >= 20261001 "
        "AND notice-type = cn-standard "
        "AND (classification-cpv = 72* "
        "OR classification-cpv = 48*)"
    ),

    "fields": [
        "publication-number",
        "publication-date",
        "notice-title",
        "description-proc",
        "description-lot",
        "classification-cpv",
        "buyer-country",
        "notice-type"
    ],

    "page": 1,
    "limit": 20,
    "scope": "ALL",
    "paginationMode": "PAGE_NUMBER"
}

# STEP 1: Fetch notices from TED API
print("Fetching IT-related tender notices...")

response = requests.post(
    API_URL,
    json=payload,
    timeout=60
)

# STEP 2: Check response
if not response.ok:
    print("API error:", response.status_code)
    print(response.text[:1000])

response.raise_for_status()

# STEP 3: Convert JSON response
data = response.json()
notices = data.get("notices", [])

# STEP 4: Save original JSON
output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

output_path = output_dir / "ted_sample.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# STEP 5: Display summary
print("\n--- FETCH SUMMARY ---")
print("Fetched notices:", len(notices))
print("Saved to:", output_path)

# STEP 6: Inspect first notice
if notices:
    first_notice = notices[0]

    print("\n--- FIRST NOTICE ---")

    print(
        "Tender ID:",
        first_notice.get("publication-number")
    )

    print(
        "Title:",
        first_notice.get("notice-title")
    )

    print(
        "CPV Codes:",
        first_notice.get("classification-cpv")
    )

    print(
        "Notice Type:",
        first_notice.get("notice-type")
    )

    print(
        "Publication Date:",
        first_notice.get("publication-date")
    )

else:
    print("No notices found for this query.")
