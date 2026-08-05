from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
TABLES = ROOT / "data" / "processed" / "tables"

master = pd.read_csv(TABLES / "kano_phc_master_project_results.csv")
values = dict(zip(master["Indicator"], master["Value"]))

checks = {
    "Study population": 18771134,
    "Primary healthcare facilities": 1584,
    "LGAs analysed": 44,
    "Wards analysed": 484,
    "Demand origins": 16789,
}

for key, expected in checks.items():
    actual = float(values[key])
    if abs(actual - expected) > 1:
        raise ValueError(f"{key}: expected {expected}, found {actual}")

scenario = pd.read_csv(TABLES / "kano_phc_expansion_scenario_comparison.csv")
preferred = scenario.loc[scenario["Scenario"] == "Top_10_New_PHCs"].iloc[0]

print("RESULT REPRODUCTION: PASSED")
print(f"Population: {int(values['Study population']):,}")
print(f"PHCs: {int(values['Primary healthcare facilities']):,}")
print(f"Population within 10 min: {values['Population within 10 min']:.2f}%")
print(f"Population-weighted 2SFCA: {values['Population-weighted 2SFCA score']:.4f}")
print(
    "Population benefiting from preferred +10 PHC scenario: "
    f"{preferred['Population_With_Improved_2SFCA']:,.0f}"
)
