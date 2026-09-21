import os
import pytest
from epidemiology.disproportionality_engine import PharmacovigilanceEngine

def test_prr_signal_detection():
    # a=100, b=1000 -> target prop = 100/1100 = 0.0909
    # c=20, d=2000 -> control prop = 20/2020 = 0.0099
    # PRR ~ 9.18 (Signal)
    res = PharmacovigilanceEngine.calculate_disproportionality(a=100, b=1000, c=20, d=2000)
    assert res["proportional_reporting_ratio_prr"] > 2.0
    assert res["safety_signal_detected"]
    assert res["regulatory_action"] == "ISSUE_DRUG_SAFETY_COMMUNICATION"
