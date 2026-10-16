"""Forecast error metrics."""

import pandas as pd


def wape(real: pd.Series, forecast: pd.Series) -> float:
    """Weighted Absolute Percentage Error.

    WAPE = Σ|real - forecast| / Σ|real|

    Returns:
        WAPE value (0 = perfect, >1 = worse than zero forecast).
    """
    return (real - forecast).abs().sum() / real.abs().sum()


def bias(real: pd.Series, forecast: pd.Series) -> float:
    """Forecast bias (signed).

    Bias = Σ(real - forecast) / Σ|real|

    Positive → underestimation (forecast < real).
    Negative → overestimation (forecast > real).
    """
    return (real - forecast).sum() / real.abs().sum()
