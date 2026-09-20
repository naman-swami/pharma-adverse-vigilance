import pytest
from src.pharmacovigilance_engine import PharmacovigilanceEngine

def test_prr_signal_trigger():
    engine = PharmacovigilanceEngine()
    res = engine.compute_prr_signal(18, 180, 42, 1850)
    assert res["safety_signal_detected"] is True
    assert res["proportional_reporting_ratio"] >= 2.0
    assert res["regulatory_action"] == "ISSUE_EXPEDITED_MEDWATCH_3500A"

def test_non_signal():
    engine = PharmacovigilanceEngine()
    res = engine.compute_prr_signal(2, 500, 20, 5000)
    assert res["safety_signal_detected"] is False
