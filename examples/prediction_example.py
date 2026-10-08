"""Construct a response from caller values; performs no model inference."""

import math


def forecast_response(value, horizon_hours, *, method, model_ref=None, evidence_ref=None):
    """Keep baseline output separate from a claimed learned-model result."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("value must be numeric")
    if not math.isfinite(value) or value <= 0:
        raise ValueError("value must be finite and positive")
    if type(horizon_hours) is not int or horizon_hours <= 0:
        raise ValueError("horizon_hours must be a positive integer")
    if method == "learned_model":
        if not all(isinstance(ref, str) and ref.strip() for ref in (model_ref, evidence_ref)):
            raise ValueError("a learned-model claim requires both references")
    elif method == "naive_persistence":
        if model_ref is not None or evidence_ref is not None:
            raise ValueError("baseline output cannot claim model provenance")
    else:
        raise ValueError("unknown forecast method")
    return {
        "contract": "illustrative-v1",
        "method": method,
        "value": value,
        "horizon_hours": horizon_hours,
        "model_ref": model_ref,
        "evidence_ref": evidence_ref,
    }
