"""Independent exact tests of the second-derivative flat-edge shear gate."""

import unittest

import sympy as sp

from h8_shaper_flux_ledger import shaper_edge_coefficients


r = sp.symbols("r", positive=True)
z = sp.symbols("z", real=True)


def source_profiles():
    return [(1, 1, (1-z*z)**2), (2, r, z*(1-z*z)**2)]


class FlatEdgeGateTests(unittest.TestCase):
    def test_independently_calculated_coefficients_include_viscous_second_jet(self):
        """Would fail if the viscous b'' coefficient or first-jet term were lost."""
        value = shaper_edge_coefficients(r, z, -1, 1, -2*r, 4*z,
                                         source_profiles(), viscosity=1)
        self.assertEqual(sp.simplify(value.second + 16/(15*r)), 0)
        self.assertEqual(sp.simplify(value.first + sp.Rational(32, 15)
                                     - 16/(15*r*r)), 0)
        self.assertEqual(sp.simplify(value.zero - 64/(15*r)), 0)
        self.assertEqual(sp.simplify(value.square - 256/(315*r*r)), 0)
        self.assertEqual(sp.simplify(value.viscous_mass - sp.Rational(16, 15)), 0)
        self.assertEqual(value.second.subs(r, 1), -sp.Rational(16, 15))

    def test_original_rational_diagnostic_remains_exact(self):
        """Would fail if combining the jet coefficients altered -2036/315."""
        coeff = shaper_edge_coefficients(r, z, -1, 1, -2*r, 4*z,
                                          source_profiles(), viscosity=1)
        cutoff = (r-1)**3
        shear = (coeff.second*sp.diff(cutoff, r, 2) +
                 coeff.first*sp.diff(cutoff, r) +
                 coeff.zero*cutoff + coeff.square*cutoff**2)
        self.assertEqual(sp.simplify(shear.subs(r, 2)), -sp.Rational(2036, 315))

    def test_jets_reproduce_independent_physical_shear_for_other_cutoff(self):
        """Would fail on an incorrect decomposition hidden by the cubic fixture."""
        coeff = shaper_edge_coefficients(r, z, -1, 1, -2*r, 4*z,
                                          source_profiles(), viscosity=1)
        cutoff = (r-1)**4 + 2*(r-1)**3
        potential = sum(K*a*cutoff*Xi for K, a, Xi in source_profiles())
        p_r = -sp.diff(potential, z)/r
        p_z = sp.diff(potential, r)/r
        direct = sp.integrate(
            (-2*r+p_r)*(4*z+p_z)-(-2*r)*(4*z)
            -sp.diff(p_r, z)-sp.diff(p_z, r), (z, -1, 1))
        from_coeff = (coeff.second*sp.diff(cutoff, r, 2) +
                      coeff.first*sp.diff(cutoff, r) +
                      coeff.zero*cutoff + coeff.square*cutoff**2)
        self.assertEqual(sp.simplify(direct-from_coeff), 0)


if __name__ == "__main__":
    unittest.main()
