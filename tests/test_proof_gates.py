"""Release-gate regression tests for the unforced torus research ledger.

These tests check whether a gate may be *reported* as discharged.  They
are not evidence that any Navier--Stokes theorem has been proved.
"""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "tools" / "check_proof_gates.py"
LEDGER = ROOT / "docs" / "unforced-integration" / "proof_gates.json"


def run_check(path):
    return subprocess.run(
        [sys.executable, str(CHECKER), str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


class ProofGateTests(unittest.TestCase):
    def test_all_nine_gates_are_reviewable(self):
        """Removing one required G0--G8 gate must prevent a green release."""
        result = run_check(LEDGER)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["gate_count"], 9)
        self.assertEqual(report["target_theorem_status"], "OPEN")
        self.assertIn("G4", report["open_gates"])
        self.assertIn("G7", report["open_gates"])

    def test_missing_h8_gate_is_rejected(self):
        """A deleted G4 entry must be rejected rather than silently skipped."""
        data = json.loads(LEDGER.read_text(encoding="utf-8"))
        data["gates"] = [g for g in data["gates"] if g["id"] != "G4"]
        with tempfile.TemporaryDirectory() as temp:
            candidate = Path(temp) / "broken.json"
            candidate.write_text(json.dumps(data), encoding="utf-8")
            result = run_check(candidate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing gates: G4", result.stderr)

    def test_unsupported_kernel_pass_is_rejected(self):
        """A label of LEAN_KERNEL_CHECKED must carry real CI evidence."""
        data = json.loads(LEDGER.read_text(encoding="utf-8"))
        target = next(g for g in data["gates"] if g["id"] == "G4")
        target["status"] = "LEAN_KERNEL_CHECKED"
        with tempfile.TemporaryDirectory() as temp:
            candidate = Path(temp) / "wrong_pass.json"
            candidate.write_text(json.dumps(data), encoding="utf-8")
            result = run_check(candidate)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("G4: kernel-check evidence missing", result.stderr)


if __name__ == "__main__":
    unittest.main()
