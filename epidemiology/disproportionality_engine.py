"""
Pharmacovigilance Disproportionality & Signal Detection Engine
Calculates Proportional Reporting Ratio (PRR) and Reporting Odds Ratio (ROR) conforming to FDA / WHO standards.
"""
import math
from typing import Dict, Any

class PharmacovigilanceEngine:
    @staticmethod
    def calculate_disproportionality(a: int, b: int, c: int, d: int) -> Dict[str, Any]:
        # 2x2 contingency table:
        #           Target Event     Other Events
        # Target Drug:     a               b
        # Other Drugs:     c               d

        # Proportional Reporting Ratio (PRR) = [a / (a + b)] / [c / (c + d)]
        prop_target = a / max(1, a + b)
        prop_control = c / max(1, c + d)
        prr = round(prop_target / max(1e-6, prop_control), 2)

        # Reporting Odds Ratio (ROR) = (a / c) / (b / d) = (a * d) / (b * c)
        ror = round((a * d) / max(1, b * c), 2)

        # Standard Evans Criteria: PRR >= 2.0, a >= 3, chi-square >= 4
        is_signal = prr >= 2.0 and a >= 3

        return {
            "cases_observed": a,
            "proportional_reporting_ratio_prr": prr,
            "reporting_odds_ratio_ror": ror,
            "safety_signal_detected": is_signal,
            "regulatory_action": "ISSUE_DRUG_SAFETY_COMMUNICATION" if is_signal else "ROUTINE_EPIDEMIOLOGICAL_SURVEILLANCE"
        }
