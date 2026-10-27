"""Exact rational cross-checks for the paper's restricted meridional inverse.

These finite polynomial samples are diagnostics. They do not establish
the theorem for arbitrary C-infinity sources or the weighted H8 estimate.
"""

from fractions import Fraction as Q
import unittest


def fixture(r, z):
    """Independent local source, stress, and first derivatives at rationals."""
    u, v, q = r - 1, 2 - r, 1 - z * z
    p = u**4 * v**4
    p_r = 4 * u**3 * v**4 - 4 * u**4 * v**3
    eta = Q(35, 32) * q**3
    eta_z = -Q(105, 16) * z * q**2
    k = p * q**4
    k_r = p_r * q**4
    m = p * eta
    m_r = p_r * eta
    m_z = p * eta_z
    c_z = p * (q**4 - 8 * z*z * q**3)
    source_r = p * q**3
    source_z = (p_r + p/r) * eta + c_z
    hoop = k + r * (k_r + m_z - source_r)
    return (k, k_r, m, m_r, m_z, c_z, hoop, source_r, source_z)


class MeridionalInverseExactTests(unittest.TestCase):
    def test_both_divergence_components_match_independent_source(self):
        for r in (Q(9, 8), Q(5, 4), Q(3, 2), Q(7, 4)):
            for z in (Q(-1, 2), Q(0), Q(1, 3), Q(1, 2)):
                k, kr, m, mr, mz, cz, ell, fr, fz = fixture(r, z)
                self.assertEqual(kr + (k - ell)/r + mz, fr, (r, z))
                self.assertEqual(mr + m/r + cz, fz, (r, z))

    def test_missing_hoop_component_breaks_the_radial_equation(self):
        r, z = Q(5, 4), Q(1, 2)
        k, kr, _, _, mz, _, _, fr, _ = fixture(r, z)
        self.assertNotEqual(kr + k/r + mz, fr)

    def test_axial_profile_has_unit_integral(self):
        # 35/32 times (1-z^2)^3 integrates to one on [-1,1].
        integral = Q(35, 32) * (Q(2) - 3*Q(2, 3)
                                   + 3*Q(2, 5) - Q(2, 7))
        self.assertEqual(integral, Q(1))

    def test_weighted_axial_force_compatibility_at_radial_ends(self):
        # J(r) = P'(r) + P(r)/r, so r J = (r P)' and the
        # total weighted force is [r P] evaluated at r=1,2.
        def radial_boundary(r):
            return r * (r - 1)**4 * (2 - r)**4
        self.assertEqual(radial_boundary(Q(2)) - radial_boundary(Q(1)), Q(0))


if __name__ == "__main__":
    unittest.main()
