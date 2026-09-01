from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "data" / "core_results"

wards = pd.read_csv(CORE / "Kano_Ward_2SFCA_15min.csv")
candidates = pd.read_csv(CORE / "Kano_New_PHC_Candidate_Sites.csv")
facility_ratio = pd.read_csv(CORE / "Kano_2SFCA_15min_Facility_Ratio_Summary.csv")
headline = pd.read_csv(CORE / "Kano_Validated_Headline_Findings.csv")

facility_values = dict(zip(facility_ratio["Indicator"], facility_ratio["Value"]))
headline_values = dict(zip(headline["Indicator"], headline["Value"]))

checks = {
    "Wards analysed": (len(wards), 484),
    "Candidate new PHC sites": (len(candidates), 97),
    "Total PHCs": (facility_values["Total PHCs"], 1584),
    "Baseline population-weighted 2SFCA": (
        headline_values["Baseline population-weighted 2SFCA"], 0.8438488753787575,
    ),
    "+20 PHC relative statewide 2SFCA gain (%)": (
        headline_values["+20 PHC relative statewide 2SFCA gain"], 1.2626262626262514,
    ),
    "Population benefiting from +20 PHCs": (
        headline_values["Population benefiting from +20 PHCs"], 687356.410675168,
    ),
}

for key, (actual, expected) in checks.items():
    if abs(float(actual) - float(expected)) > max(1.0, abs(expected) * 1e-6):
        raise ValueError(f"{key}: expected {expected}, found {actual}")

print("RESULT REPRODUCTION: PASSED")
print(f"Wards analysed: {len(wards)}")
print(f"Candidate new PHC sites: {len(candidates)}")
print(f"Total PHCs: {int(facility_values['Total PHCs']):,}")
print(f"Baseline population-weighted 2SFCA: {headline_values['Baseline population-weighted 2SFCA']:.4f}")
print(
    "Population benefiting from +20 PHC scenario: "
    f"{headline_values['Population benefiting from +20 PHCs']:,.0f} "
    f"({headline_values['Share of population benefiting from +20 PHCs']:.2f}%)"
)
