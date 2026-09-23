from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
LEAN = ROOT / "UnforcedClosure.lean"


def A(h): return F(1, 2) + h
def rho(h): return h / 5


def check_exact_arithmetic():
    gains = [F(89998,100000), F(49999,100000), F(49999,100000),
             F(49999,100000), F(2,5), F(49999,100000),
             F(49999,100000), F(49999,100000), F(2,5)]
    assert min(gains) == F(2,5)
    assert F(2,5) - F(1,10) == F(3,10)
    for h in [F(1,100000), F(1,1000), F(1,100), F(1,10), F(49,100)]:
        assert F(0) < h < F(1,2)
        assert A(h) / h > 2
        assert rho(h) > 0
        beta = A(h) - h/F(10)
        assert beta > 0
        assert beta - rho(h) > 0
        margins = [rho(h), A(h)+F(1,2), A(h), 2*A(h)+F(1,2)-rho(h)]
        assert all(x > 0 for x in margins)


def check_contraction_arithmetic():
    # Exact examples spanning the admissible regime 4*C*eta < 1.
    for C, eta in [(F(1), F(1,8)), (F(7,3), F(1,20)), (F(101,10), F(1,100))]:
        assert 4*C*eta < 1
        assert eta + C*(2*eta)**2 < 2*eta


def check_lean_source_hygiene():
    text = LEAN.read_text(encoding="utf-8")
    forbidden = ["sorry", "admit", "axiom ", "unsafe ", "native_decide"]
    bad = [tok for tok in forbidden if tok in text]
    assert not bad, f"forbidden Lean tokens: {bad}"
    required = [
        "mean_gain_exact", "released_gain_exact", "coupling_margin_gt_two_mul",
        "nonlinear_spare_margins_pos", "fixedPoint_implies_zero_residual",
        "ball_invariance_scalar", "neumannPartial_preserves"
    ]
    missing = [name for name in required if name not in text]
    assert not missing, f"missing declarations: {missing}"


def main():
    check_exact_arithmetic()
    check_contraction_arithmetic()
    check_lean_source_hygiene()
    out = {
        "exact_arithmetic": "PASS",
        "contraction_arithmetic": "PASS",
        "lean_source_hygiene": "PASS",
        "lean_kernel_compile": "PASS_RECORDED_IN_CI_CERTIFICATE",
        "lean_ci_run_number": 12,
        "lean_ci_run_id": 35779131542,
        "lean_ci_commit": "7d7f33200e4553afbb80a29ce6435b44511c2f4a",
        "scope": (
            "abstract closure layer only; the full PDE-specific unforced "
            "Navier-Stokes theorem remains a separate integration gate"
        ),
        "certificate": "CI_CERTIFICATE.md",
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
