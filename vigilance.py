import argparse
import json
import os
from epidemiology.disproportionality_engine import PharmacovigilanceEngine

def main():
    parser = argparse.ArgumentParser(description="Pharma Adverse Vigilance CLI")
    parser.add_argument("--demo", action="store_true", help="Audit sample FDA FAERS adverse event reports")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "medwatch", "fda_faers_reports.json")

    if args.demo:
        with open(data_file, "r") as f:
            cases = json.load(f)
        print("=== PHARMACOVIGILANCE ADVERSE EVENT SIGNAL AUDIT ===\n")
        for c in cases:
            res = PharmacovigilanceEngine.calculate_disproportionality(c["a"], c["b"], c["c"], c["d"])
            print(f"Drug: {c['drug']} | Adverse Event: {c['adverse_event']}")
            print(f"  Target Cases: {res['cases_observed']} | PRR: {res['proportional_reporting_ratio_prr']} | ROR: {res['reporting_odds_ratio_ror']}")
            print(f"  Safety Signal Flag: {res['safety_signal_detected']} | Action: {res['regulatory_action']}")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
