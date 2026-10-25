"""Machine-readable release gate summary; not a PDE proof checker."""

import json
from pathlib import Path
import re
import sys

REQUIRED = {f"G{i}" for i in range(9)}
ALLOWED = {
    "OPEN", "PAPER_CONDITIONAL", "PROVED_PAPER", "TESTED_NUMERICALLY",
    "LEAN_KERNEL_CHECKED", "REFUTED_FOR_ROUTE",
}
TARGET_ALLOWED = {"OPEN", "LEAN_KERNEL_CHECKED"}


def has_syntactic_ci_receipt(certificate: object) -> bool:
    """Check shape only; GH job logs and theorem semantics require separate review."""
    if not isinstance(certificate, dict):
        return False
    sha = certificate.get("commit_sha")
    run_id = certificate.get("run_id")
    return (isinstance(sha, str) and re.fullmatch(r"[0-9a-f]{40}", sha) is not None
            and type(run_id) is int and run_id > 0
            and certificate.get("conclusion") == "success"
            and certificate.get("axioms_checked") is True)


def check(data: dict) -> dict:
    gates = data["gates"]
    ids = [g["id"] for g in gates]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate gate identifiers")
    absent = sorted(REQUIRED.difference(ids))
    if absent:
        raise ValueError("missing gates: " + ", ".join(absent))
    unexpected = sorted(set(ids).difference(REQUIRED))
    if unexpected:
        raise ValueError("unexpected gates: " + ", ".join(unexpected))
    if data["target_geometry"] != "T3" or data["viscosity"] != "1":
        raise ValueError("unforced target must be T3 at viscosity one")
    if data["target_theorem_status"] not in TARGET_ALLOWED:
        raise ValueError("invalid target theorem status")
    for gate in gates:
        identifier = gate["id"]
        if gate["status"] not in ALLOWED:
            raise ValueError(f"{identifier}: invalid status {gate['status']}")
        if not gate.get("geometry") or not gate.get("source") or not gate.get("remaining"):
            raise ValueError(f"{identifier}: missing provenance, geometry or obligation")
        if gate["status"] == "LEAN_KERNEL_CHECKED":
            certificate = gate.get("kernel_check")
            if not has_syntactic_ci_receipt(certificate) or not gate.get("lean_declarations"):
                raise ValueError(f"{identifier}: kernel-check evidence missing")
    if data["target_theorem_status"] == "LEAN_KERNEL_CHECKED":
        if any(g["status"] != "LEAN_KERNEL_CHECKED" for g in gates):
            raise ValueError("target theorem cannot be released with open gates")
        final = data.get("final_theorem")
        proof_hash = final.get("statement_sha256") if isinstance(final, dict) else None
        if not isinstance(final, dict) or not all([
            final.get("declaration") == "UnforcedPatching.unforcedExistenceTheorem",
            final.get("proves") == "UnforcedPatching.unforcedTargetStatement",
            has_syntactic_ci_receipt(final.get("kernel_check")),
            isinstance(proof_hash, str),
            re.fullmatch(r"[0-9a-f]{64}", proof_hash or "") is not None,
        ]):
            raise ValueError("final theorem receipt missing or malformed")
    return {
        "gate_count": len(gates),
        "open_gates": [g["id"] for g in gates if g["status"] == "OPEN"],
        "target_theorem_status": data["target_theorem_status"],
    }


def main() -> int:
    path = Path(sys.argv[1])
    try:
        report = check(json.loads(path.read_text(encoding="utf-8")))
    except (ValueError, KeyError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
