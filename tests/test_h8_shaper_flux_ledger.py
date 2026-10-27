"""Independent exact velocity-flux regression for source-shaped poloidal shells."""

import unittest

import sympy as sp


r, z = sp.symbols("r z", positive=True, real=True)


class ShaperFluxTests(unittest.TestCase):
    @staticmethod
    def _module():
        try:
            import h8_shaper_flux_ledger
        except ImportError as exc:
            raise AssertionError("the source-shaped flux reduction is missing") from exc
        return h8_shaper_flux_ledger

    @staticmethod
    def _example():
        xi1 = (1-z*z)**2
        xi2 = z*(1-z*z)**2
        return (-2*r, 4*z, (r-1)**3, [(1, 1, xi1), (2, r, xi2)])

    def test_two_shaper_flux_has_independently_derived_exact_values(self):
        """Detects flipped cross-shaper Wronskian or missing viscous b-double-prime."""
        m = self._module()
        ur, uz, b, profiles = self._example()
        result = m.shaper_flux(r, z, -1, 1, ur, uz, b, profiles, viscosity=1)
        self.assertEqual(sp.simplify(result.gamma.subs(r, 2)), sp.Rational(-32, 15))
        self.assertEqual(sp.simplify(result.delta.subs(r, 2)), sp.Rational(32, 15))
        self.assertEqual(sp.simplify(result.quadratic.subs(r, 2)), sp.Rational(64, 315))
        self.assertEqual(sp.simplify(result.viscous.subs(r, 2)), sp.Rational(-12, 5))
        self.assertEqual(sp.simplify(result.total.subs(r, 2)), sp.Rational(-2036, 315))

    def test_direct_velocity_products_agree_with_reduced_ledger(self):
        """Detects an algebraically self-consistent but physically wrong flux formula."""
        m = self._module()
        ur, uz, b, profiles = self._example()
        result = m.shaper_flux(r, z, -1, 1, ur, uz, b, profiles, viscosity=1)
        psi = sum((K*a*b*xi for K, a, xi in profiles), sp.S.Zero)
        pr = -sp.diff(psi, z)/r
        pz = sp.diff(psi, r)/r
        exact = sp.integrate(
            ur*pz + uz*pr + pr*pz - (sp.diff(pr, z)+sp.diff(pz, r)),
            (z, -1, 1))
        self.assertEqual(sp.simplify(exact-result.total), 0)

    def test_invalid_core_divergence_is_rejected(self):
        """Detects applying the integrated identity to a compressible core."""
        m = self._module()
        ur, uz, b, profiles = self._example()
        with self.assertRaisesRegex(ValueError, "divergence"):
            m.shaper_flux(r, z, -1, 1, ur, uz+z, b, profiles, viscosity=1)

    def test_nonvanishing_axial_shaper_trace_is_rejected(self):
        """Detects silently discarding a nonzero axial boundary contribution."""
        m = self._module()
        ur, uz, b, _ = self._example()
        with self.assertRaisesRegex(ValueError, "axial"):
            m.shaper_flux(r, z, -1, 1, ur, uz, b, [(1, 1, z)], viscosity=1)


if __name__ == "__main__":
    unittest.main()
