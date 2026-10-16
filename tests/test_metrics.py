# tests/test_metrics.py
import pandas as pd
from src.lds_coding_task.evaluation.metrics import bias, wape


def test_wape_perfect() -> None:
    s = pd.Series([10.0, 20.0, 30.0])
    assert wape(s, s) == 0.0


def test_wape_known_value() -> None:
    real = pd.Series([10.0, 20.0])
    fcst = pd.Series([8.0, 22.0])
    # |10-8| + |20-22| = 4; 10+20 = 30 → 4/30
    assert wape(real, fcst) == 4 / 30


def test_bias_underestimation() -> None:
    real = pd.Series([10.0, 20.0])
    fcst = pd.Series([5.0, 15.0])
    # (5+5) / 30 = 0.333... positive → underestimating
    assert bias(real, fcst) > 0


def test_bias_overestimation() -> None:
    real = pd.Series([10.0, 20.0])
    fcst = pd.Series([15.0, 25.0])
    assert bias(real, fcst) < 0
