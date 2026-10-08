"""Toy eligibility decision; intentionally not the private promotion policy."""


def eligibility(*, contract_valid, evidence_ref):
    """ACCEPT here means illustrative eligibility, never deployment approval."""
    if not isinstance(contract_valid, bool):
        raise ValueError("contract_valid must be a boolean")
    if evidence_ref is not None and (
        not isinstance(evidence_ref, str) or not evidence_ref.strip()
    ):
        raise ValueError("evidence_ref must be a nonempty string or None")
    if not contract_valid:
        outcome, reason = "REJECT", "illustrative contract check failed"
    elif evidence_ref is None:
        outcome, reason = "DEFER", "supporting evidence is unavailable"
    else:
        outcome, reason = "ACCEPT", "illustrative eligibility checks satisfied"
    return {
        "contract": "illustrative-v1",
        "stage": "eligibility",
        "outcome": outcome,
        "policy": "educational-eligibility",
        "reasons": [reason],
        "evidence_refs": [] if evidence_ref is None else [evidence_ref],
    }
