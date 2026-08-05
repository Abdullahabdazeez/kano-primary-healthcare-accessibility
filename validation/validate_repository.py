from pathlib import Path
import json
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "project.json", "LICENSE", "CITATION.cff", "requirements.txt",
    "assets/project-cover.png", "assets/repository-social-preview.png",
    "docs/DATA_SOURCES.md", "docs/METHODOLOGY.md", "docs/RESULTS.md", "docs/LIMITATIONS.md",
    "scripts/python/reproduce_summary.py",
    "data/processed/tables/kano_phc_master_project_results.csv",
    "data/processed/tables/kano_phc_expansion_scenario_comparison.csv",
    "outputs/maps/05_healthcare_planning_priority_wards.png"
]

failures = [f"Missing: {p}" for p in required if not (ROOT / p).exists()]

for path in ROOT.rglob("*"):
    if path.is_file() and path.stat().st_size > 24 * 1024 * 1024:
        failures.append(f"Browser-upload limit exceeded: {path.relative_to(ROOT)}")

try:
    meta = json.loads((ROOT / "project.json").read_text(encoding="utf-8"))
    if meta["headline_results"]["population"] != 18771134:
        failures.append("Unexpected population metadata")
except Exception as exc:
    failures.append(f"Invalid project metadata: {exc}")

try:
    master = pd.read_csv(ROOT/"data/processed/tables/kano_phc_master_project_results.csv")
    values = dict(zip(master["Indicator"], master["Value"]))
    if abs(float(values["Population within 10 min"]) - 97.78233) > 0.01:
        failures.append("10-minute access result does not match source table")
except Exception as exc:
    failures.append(f"Could not validate results: {exc}")

if failures:
    print("REPOSITORY VALIDATION: FAILED")
    for item in failures:
        print("-", item)
    sys.exit(1)

print("REPOSITORY VALIDATION: PASSED")
print("Required files, upload-size limits and headline results are valid.")
