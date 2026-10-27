"""Exact pressure-compensated H8 flux tests on rational model inputs."""

import unittest
from fractions import Fraction as Q

import sympy as sp


r = sp.symbols("r", positive=True)


class ExactFluxGateTests(unittest.TestCase):
    @staticmethod
    def _module():
        try:
            import h8_exact_flux_gate
        except ImportError as exc:
            raise AssertionError("the exact complete-channel flux gate is absent") from exc
        return h8_exact_flux_gate

    def _channels(self, shear=None, jumps=None):
        m = self._module()
        shear_data = {name: sp.Integer(0) for name in m.SHEAR_CHANNELS}
        jump_data = {name: sp.Integer(0) for name in m.BOUNDARY_CHANNELS}
        shear_data.update(shear or {})
        jump_data.update(jumps or {})
        return shear_data, jump_data

    @staticmethod
    def _identity():
        return ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    def test_pressure_only_residual_has_nonzero_J_but_zero_stress_flux(self):
        """Detects the incorrect omission of the axial pressure primitive."""
        m = self._module()
        shear, jumps = self._channels(jumps={"toroidal_pressure": 1})
        ledger = m.assemble_flux(r, 1, shear, jumps)
        self.assertEqual(sp.simplify(ledger.J - (r*r-1)/(2*r)), 0)
        self.assertEqual(sp.simplify(ledger.source_axial_marginal-1), 0)
        self.assertEqual(ledger.shear, 0)
        gate = m.pointwise_cone_gate(ledger, r, 2, 0, self._identity())
        self.assertEqual(gate.J, Q(3, 4))
        self.assertEqual(gate.shear, Q(0))
        self.assertEqual(gate.boundary_primitive, Q(3, 4))
        self.assertEqual((gate.lower, gate.upper), (Q(0), Q(0)))
        self.assertTrue(gate.admissible_at_point)

    def test_inner_edge_trace_is_retained(self):
        """Detects dropping the nonzero S(a)/r contribution."""
        m = self._module()
        shear, jumps = self._channels(shear={"core_transition": 2/r})
        ledger = m.assemble_flux(r, 1, shear, jumps)
        self.assertEqual(ledger.J, 0)
        self.assertEqual(ledger.shear_at_a, 2)
        self.assertEqual(ledger.shear, 2/r)

    def test_symbolic_marginal_matches_radial_conservation_identity(self):
        """Detects an incorrect cylindrical r Jacobian or jump sign."""
        m = self._module()
        shear, jumps = self._channels(
            shear={"core_shaper": (r-1)**3, "viscous": -(r-1)**2},
            jumps={"axial_tensor_jump": r, "four_patch_overlap": r*r},
        )
        ledger = m.assemble_flux(r, 1, shear, jumps)
        self.assertEqual(sp.simplify(sp.diff(r*ledger.J, r)/r
                                     - ledger.source_axial_marginal), 0)
        self.assertEqual(sp.simplify(ledger.source_axial_marginal
                                     - (sp.diff(r*ledger.shear, r)/r
                                        + ledger.axial_jump)), 0)

    def test_radially_rotating_frame_has_asymmetric_exact_shear_support(self):
        """Detects frozen-frame substitution or loss of one-sided D asymmetry."""
        m = self._module()
        from h8_positive_cone import GAMMA, GAMMA_THIRD

        t = r-1
        c = (1-t*t)/(1+t*t)
        s = 2*t/(1+t*t)
        E = ((c, 0, s), (0, 1, 0), (-s, 0, c))
        shear, jumps = self._channels()
        ledger = m.assemble_flux(r, 1, shear, jumps)
        gate = m.pointwise_cone_gate(ledger, r, sp.Rational(3, 2), 1, E)
        self.assertEqual(gate.lower, -(19*GAMMA)/50)
        self.assertEqual(gate.upper, (19*GAMMA_THIRD+47*GAMMA)/100)
        self.assertEqual(gate.absolute_upper, 19*GAMMA/50)
        self.assertEqual(gate.absolute_lower, -19*GAMMA/50)
        self.assertTrue(gate.admissible_at_point)

    def test_exact_rational_point_rejects_insufficient_cone_weight(self):
        """Detects incorrectly accepting a flux above the sharp cone support."""
        m = self._module()
        shear, jumps = self._channels(shear={"core_shaper": (r-1)**2})
        ledger = m.assemble_flux(r, 1, shear, jumps)
        gate = m.pointwise_cone_gate(ledger, r, 2, sp.Rational(1, 100), self._identity())
        self.assertEqual(gate.J, Q(1))
        self.assertFalse(gate.admissible_at_point)
        self.assertLess(gate.upper, Q(1))

    def test_original_absolute_cone_can_fail_when_one_sided_cone_passes(self):
        """Detects silently replacing the original H8 coefficient cap by positivity."""
        m = self._module()
        shear, jumps = self._channels(shear={"core_shaper": sp.Rational(17, 1000)*(r-1)**2})
        ledger = m.assemble_flux(r, 1, shear, jumps)
        gate = m.pointwise_cone_gate(ledger, r, 2, sp.Rational(1, 10), self._identity())
        self.assertTrue(gate.admissible_at_point)
        self.assertFalse(gate.absolute_admissible_at_point)

    def test_missing_channel_fails_closed(self):
        """Detects accepting a partial source ledger as complete."""
        m = self._module()
        shear, jumps = self._channels()
        del shear["four_patch_overlap"]
        with self.assertRaisesRegex(ValueError, "four_patch_overlap"):
            m.assemble_flux(r, 1, shear, jumps)
        shear, jumps = self._channels()
        del jumps["toroidal_pressure"]
        with self.assertRaisesRegex(ValueError, "toroidal_pressure"):
            m.assemble_flux(r, 1, shear, jumps)

    def test_nonorthogonal_frame_is_rejected(self):
        """Detects accepting a deformed frame that invalidates pressure gauge."""
        m = self._module()
        shear, jumps = self._channels()
        ledger = m.assemble_flux(r, 1, shear, jumps)
        with self.assertRaisesRegex(ValueError, "orthogonal"):
            m.pointwise_cone_gate(ledger, r, 2, 1,
                                  ((1, 1, 0), (0, 1, 0), (0, 0, 1)))

    def test_irrational_point_requires_a_separate_certified_enclosure(self):
        """Detects silently turning a nonanalytic profile into a float verdict."""
        m = self._module()
        shear, jumps = self._channels(shear={"core_shaper": sp.exp(-r)})
        ledger = m.assemble_flux(r, 1, shear, jumps)
        with self.assertRaisesRegex(ValueError, "rational"):
            m.pointwise_cone_gate(ledger, r, 2, 1, self._identity())


if __name__ == "__main__":
    unittest.main()
