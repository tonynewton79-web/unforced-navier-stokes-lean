"""Source-shaped two-cutoff shear and variable-frame cone tests."""

import unittest
from fractions import Fraction as Q

import sympy as sp


r = sp.symbols("r", positive=True)
z, theta = sp.symbols("z theta", real=True)


class SplitCutoffGateTests(unittest.TestCase):
    @staticmethod
    def _module():
        try:
            import h8_split_cutoff_gate
        except ImportError as exc:
            raise AssertionError("the split-cutoff source calculator is missing") from exc
        return h8_split_cutoff_gate

    def test_independent_radial_cutoffs_do_not_cancel_each_others_second_jets(self):
        """Catches conflating the core's chi'' with the shaper's b''."""
        m = self._module()
        chi = sp.Function("chi")(r)
        b = sp.Function("b")(r)
        xi = (1-z*z)**2
        result = m.split_cutoff_shear(
            r, theta, z, -1, 1, (0, 0),
            (0, -sp.Rational(8, 15)/r, 0), chi,
            [(1, 1, xi)], b)
        self.assertEqual(sp.simplify(
            result.core_radial_second-
            sp.Rational(16, 15)*sp.diff(chi, r, 2)/r), 0)
        self.assertEqual(sp.simplify(
            result.shaper_radial_second+
            sp.Rational(16, 15)*sp.diff(b, r, 2)/r), 0)
        self.assertEqual(result.core_nonradial_second, 0)
        self.assertFalse(result.lower_order_shear.has(
            sp.diff(chi, r, 2), sp.diff(b, r, 2)))
        # Equal cutoffs cancel, unequal polynomial cutoffs do not.
        equal = result.core_radial_second+result.shaper_radial_second
        self.assertEqual(sp.simplify(equal.subs(chi, b).doit()), 0)
        distinct = sp.simplify(equal.subs({
            chi: (r-1)**2, b: (r-1)**3}).doit())
        self.assertEqual(sp.simplify(
            distinct-sp.Rational(16, 15)*(2-6*(r-1))/r), 0)

    def test_nonradial_core_cutoff_has_axial_second_derivative(self):
        """Catches treating a similarity-space cutoff as radial automatically."""
        m = self._module()
        result = m.split_cutoff_shear(
            r, theta, z, 0, 1, (0, 0), (0, r, 0),
            r*r*z*z, [], 0)
        self.assertEqual(result.core_radial_second, -2*r/3)
        self.assertEqual(result.core_nonradial_second, 2*r**3)
        self.assertEqual(result.shaper_radial_second, 0)
        self.assertEqual(sp.simplify(
            result.shear-(-2*r**5+2*r**3-sp.Rational(8, 3)*r)), 0)
        self.assertEqual(sp.simplify(
            result.lower_order_shear+2*r**5+2*r), 0)

    def test_pressure_axial_jump_changes_source_flux_not_physical_shear(self):
        """Catches omitting the pressure trace in the cylindrical primitive."""
        m = self._module()
        from h8_c4_transition import normalized_toroidal_pressure
        p = normalized_toroidal_pressure(r, z, 1, r, r*z)
        result = m.split_cutoff_shear(
            r, theta, z, -1, 1, (0, 0), (0, 0, 0),
            0, [], 0, pressure=p, inner_radius=1)
        self.assertEqual(result.shear, 0)
        self.assertEqual(result.axial_jump, 2*(r*r-1))
        self.assertEqual(sp.simplify(result.J-(r*r-1)**2/(2*r)), 0)
        self.assertEqual(result.source_axial_marginal, 2*(r*r-1))

    def test_variable_frame_exact_mass_partition_and_enclosure(self):
        """Catches integrating one frozen frame across different cone patches."""
        m = self._module()
        identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        tilted = ((Q(3, 5), 0, Q(-4, 5)), (0, 1, 0),
                  (Q(4, 5), 0, Q(3, 5)))
        exact = m.spatial_frame_support_bounds(
            [(Q(1), identity, Q(0), ((0, 0, 1), (0, 0, 0), (0, 0, 0)), Q(0)),
             (Q(2), tilted, Q(0), ((0, 0, 1), (0, 0, 0), (0, 0, 0)), Q(0))])
        from h8_positive_cone import positive_support
        from h8_rotating_frame import dual_covector
        G = ((0, 0, 1), (0, 0, 0), (0, 0, 0))
        lam0 = dual_covector(identity, G)
        lam1 = dual_covector(tilted, G)
        expected = positive_support(*lam0, Q(1))+positive_support(*lam1, Q(2))
        self.assertEqual(exact.upper_plus, expected)
        self.assertEqual(exact.lower_plus, expected)
        self.assertEqual(exact.error, 0)

    def test_certified_frame_enclosure_contains_moving_frame_support(self):
        """Catches a wrong factor in the uniform orthogonal-frame bound."""
        m = self._module()
        from h8_positive_cone import positive_support
        from h8_rotating_frame import dual_covector
        identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        tilted = ((Q(3, 5), 0, Q(-4, 5)), (0, 1, 0),
                  (Q(4, 5), 0, Q(3, 5)))
        # ||tilted - I||_F^2=8/5; the rational 4/3 encloses it.
        bounds = m.spatial_frame_support_bounds(
            [(Q(3, 2), identity, Q(4, 3),
              ((0, 0, 1), (0, 0, 0), (0, 0, 0)), Q(0))])
        G = ((0, 0, 1), (0, 0, 0), (0, 0, 0))
        true_plus = positive_support(*dual_covector(tilted, G), Q(3, 2))
        self.assertLessEqual(bounds.lower_plus, true_plus)
        self.assertGreaterEqual(bounds.upper_plus, true_plus)
        with self.assertRaisesRegex(ValueError, "orthogonal"):
            m.spatial_frame_support_bounds([(Q(1), ((2, 0, 0),
                                                         (0, 1, 0),
                                                         (0, 0, 1)), Q(0),
                ((0, 0, 1), (0, 0, 0), (0, 0, 0)), Q(0))])

    def test_angular_test_tensor_variation_requires_separate_budget(self):
        """A constant E cannot freeze the varying physical e_r(theta)."""
        m = self._module()
        I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        G0 = ((0, 0, 1), (0, 0, 0), (0, 0, 0))
        from h8_positive_cone import positive_support
        from h8_rotating_frame import dual_covector

        with self.assertRaisesRegex(ValueError, "test tensor"):
            m.spatial_frame_support_bounds([(Q(1), I, Q(0))])
        # A full-circle test e_r(theta) \otimes e_z is within 2 of G0,
        # even though E=I has exactly zero frame error.
        bounds = m.spatial_frame_support_bounds(
            [(Q(1), I, Q(0), G0, Q(2))])
        G90 = ((0, 0, 0), (0, 0, 1), (0, 0, 0))
        true_plus = positive_support(*dual_covector(I, G90), Q(1))
        self.assertGreater(bounds.error, 0)
        self.assertLessEqual(bounds.lower_plus, true_plus)
        self.assertGreaterEqual(bounds.upper_plus, true_plus)

    def test_rotating_frame_connection_generates_source_from_constant_tensor(self):
        """Catches neglecting connection terms when taking stress divergence."""
        m = self._module()
        x, y = sp.symbols("x y", real=True)
        k, D = sp.symbols("k D", real=True)
        c, s = sp.cos(k*z), sp.sin(k*z)
        E = ((c, 0, -s), (0, 1, 0), (s, 0, c))
        H = ((-D, 0, 0), (0, 0, 0), (0, 0, D))
        split = m.rotated_stress_divergence(E, H, (x, y, z))
        self.assertEqual(split.frozen_frame, (0, 0, 0))
        self.assertEqual(sp.simplify(
            split.connection[0].subs(z, 0)+2*D*k), 0)
        self.assertEqual(split.connection[1], 0)
        self.assertEqual(sp.simplify(
            split.full[0]-split.connection[0]), 0)
        self.assertEqual(sp.simplify(
            split.full[2]+4*D*k*s*c), 0)

    def test_time_marginal_is_not_silently_lost_from_full_nse_residual(self):
        """Catches confusing div K + grad p with the time-dependent NSE source."""
        m = self._module()
        t = sp.symbols("t", real=True)
        result = m.split_cutoff_shear(
            r, theta, z, 0, 1, (0, t), (0, 0, 0), 0,
            [], 0, pressure=0, inner_radius=1, time_symbol=t)
        self.assertEqual(result.shear, 0)
        self.assertEqual(result.axial_jump, 0)
        self.assertEqual(result.J, 0)
        self.assertEqual(result.source_axial_marginal, 0)
        self.assertEqual(result.time_axial_marginal, 1)
        self.assertEqual(sp.simplify(
            result.J_full-(r*r-1)/(2*r)), 0)
        self.assertEqual(result.full_source_axial_marginal, 1)

    def test_unspecified_time_source_remains_unknown(self):
        """Catches replacing an unfrozen temporal contribution by an implicit zero."""
        m = self._module()
        result = m.split_cutoff_shear(
            r, theta, z, 0, 1, (0, 0), (0, 0, 0), 0,
            [], 0, pressure=0, inner_radius=1)
        self.assertIsNone(result.J_full)
        self.assertIsNone(result.time_axial_marginal)


if __name__ == "__main__":
    unittest.main()
