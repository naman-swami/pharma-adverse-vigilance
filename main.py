import json
import argparse
from src.pharmacovigilance_engine import PharmacovigilanceEngine

def main():
    parser = argparse.ArgumentParser(description="PharmaVigil Pharmacovigilance Signal Detection CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated FAERS adverse reaction signal audit")
    args = parser.parse_args()

    engine = PharmacovigilanceEngine()
    report = engine.compute_prr_signal(
        cases_target_drug_target_event=18,
        cases_target_drug_other_events=180,
        cases_other_drugs_target_event=42,
        cases_other_drugs_other_events=1850
    )
    print("="*60)
    print(" PHARMAVIGIL FDA SAFETY SIGNAL AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
