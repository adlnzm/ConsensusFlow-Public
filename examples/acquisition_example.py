"""Illustrative envelope construction only; no acquisition or service calls."""

import math
from datetime import datetime


def observation(asset, price, observed_at, provider, time_basis):
    """Caller-supplied demonstration values are not platform measurements."""
    if not isinstance(asset, str) or not asset.strip():
        raise ValueError("asset is required")
    if not isinstance(provider, str) or not provider.strip():
        raise ValueError("provider is required")
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise ValueError("price must be numeric")
    if not math.isfinite(price) or price <= 0:
        raise ValueError("price must be finite and positive")
    if not isinstance(observed_at, datetime) or observed_at.utcoffset() is None:
        raise ValueError("observed_at must be a timezone-aware datetime")
    if time_basis not in {"acquisition_observation", "source_event"}:
        raise ValueError("declare which time the observation represents")
    return {
        "contract": "illustrative-v1",
        "asset": asset,
        "price": price,
        "observed_at": observed_at.isoformat(),
        "provider": provider,
        "time_basis": time_basis,
    }
