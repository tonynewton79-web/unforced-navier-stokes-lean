"""Independent source-moment checks for a common radial H8 envelope."""

import unittest

import sympy as sp

from h8_shared_cutoff_moment import (
    axial_curl_circulation_primitive,
    shared_cutoff_physical_shear,
)


r = sp.symbols("r", positive=True)
z, theta = sp.symbols("z theta", real=True)


class SharedCutoffMomentTests(unittest.TestCase):
    def test_core_and_shaper_second_jet_add_with_correct_sign(self):
        """Would fail if localized core viscosity were omitted from the edge coefficient."""
        xi = (1-z*z)**2
        cut = sp.Function("b")(r)
        result = shared_cutoff_physical_shear(
            r, theta, z, -1, 1, 0, 0,
            0, r, 0, [(1, 1, xi)], cut, viscosity=1)
        self.assertEqual(sp.simplify(result.core_moment-2*r), 0)
        self.assertEqual(sp.simplify(result.shaper_moment-sp.Rational(16, 15)/r), 0)
        self.assertEqual(sp.simplify(
            result.second_coefficient+2*r+sp.Rational(16, 15)/r), 0)
        self.assertFalse(result.first_order_remainder.has(sp.diff(cut, r, 2)))

    def test_fourfold_angular_overlap_has_no_new_second_jet_in_physical_shear(self):
        """Would fail if nonlinear overlap products were misclassified as viscous b''."""
        cut = sp.Function("b")(r)
        # The theta mode is C4-periodic and has a nontrivial rz overlap.
        result = shared_cutoff_physical_shear(
            r, theta, z, -1, 1, 0, 0,
            0, r*(1+sp.cos(4*theta)), sp.sin(4*theta),
            [], cut, viscosity=1)
        self.assertEqual(sp.simplify(result.second_coefficient+2*r), 0)
        self.assertEqual(sp.simplify(
            result.physical_shear-
            (result.second_coefficient*sp.diff(cut, r, 2)
             +result.first_order_remainder)), 0)
        self.assertFalse(result.first_order_remainder.has(sp.diff(cut, r, 2)))

    def test_axial_curl_moment_equals_circulation_primitive(self):
        """Would fail if the radial Stokes primitive lost its factor of r."""
        # A_theta=r*z*(1+cos 4theta), so <curl(A)_z>=2z.
        u_z = 2*z*(1+sp.cos(4*theta))
        from_curl = axial_curl_circulation_primitive(
            r, theta, z, 0, 1, 0, 0, u_z)
        self.assertEqual(sp.simplify(from_curl-r/2), 0)

    def test_annular_circulation_can_cancel_shaper_second_jet(self):
        """Would fail if a nonzero annular integration constant were discarded."""
        xi = (1-z*z)**2
        cut = sp.Function("b")(r)
        # A_theta=-8/(15r) has curl_z=0 on r>0 but nonzero circulation.
        result = shared_cutoff_physical_shear(
            r, theta, z, -1, 1, 0, 0,
            0, -sp.Rational(8, 15)/r, 0,
            [(1, 1, xi)], cut, viscosity=1)
        self.assertEqual(result.core_moment, -sp.Rational(16, 15)/r)
        self.assertEqual(result.second_coefficient, 0)
        recovered = axial_curl_circulation_primitive(
            r, theta, z, -1, 1, 1, -sp.Rational(16, 15), 0)
        self.assertEqual(sp.simplify(recovered-result.core_moment), 0)

    def test_pressure_trace_not_smuggled_into_physical_rz_shear(self):
        """Would fail if a pressure trace were treated as off-diagonal stress."""
        cut = sp.Function("b")(r)
        result = shared_cutoff_physical_shear(
            r, theta, z, -1, 1, 0, 0,
            0, r, 0, [], cut, viscosity=1)
        self.assertEqual(sp.simplify(result.second_coefficient+2*r), 0)


if __name__ == "__main__":
    unittest.main()
