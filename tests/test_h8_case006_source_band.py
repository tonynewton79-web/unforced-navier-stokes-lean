"""Independent exact arithmetic for the Case 006 axial source band.

Only finite rational identities are checked here.  The authentic Case 006
transition profile and compact weighted inverse are not supplied by this test.
"""

import unittest
from fractions import Fraction as Q


ALPHA = Q(-4443, 9832)
KAPPA = Q(15971, 122900)
G = KAPPA
H = Q(22371, 122900)


class Case006SourceBandTests(unittest.TestCase):
    def test_exact_source_native_interval(self):
        self.assertEqual(ALPHA - KAPPA, Q(-143017, 245800))
        self.assertEqual(ALPHA + KAPPA, Q(-79133, 245800))
        self.assertLess(ALPHA + KAPPA, 0)

    def test_absolute_coefficient_cap_implies_axial_shear_cap(self):
        # On the boundary of the symmetric seven-ray cap, this is sharp.
        b = KAPPA / 8
        a = 4 * b + KAPPA / 2
        c = d = Q(0)
        deltas = (
            -Q(3, 2) * d,
            2 * c - 4 * d,
            -2 * c - 4 * d,
            2 * a - 8 * b + 4 * d,
            -2 * a + 8 * b + 4 * d,
            8 * b,
            -8 * b,
        )
        self.assertEqual(max(map(abs, deltas)), KAPPA)
        self.assertEqual(a, KAPPA)

    def test_one_sided_positive_cone_is_strictly_larger(self):
        # A sharp *positive*-cone witness violates the absolute |A| cap.
        d = (G + H) / 8
        b = G / 8
        c = (H - G) / 4
        a = (5 * G + H) / 4
        deltas = (
            -Q(3, 2) * d,
            2 * c - 4 * d,
            -2 * c - 4 * d,
            2 * a - 8 * b + 4 * d,
            -2 * a + 8 * b + 4 * d,
            8 * b,
            -8 * b,
        )
        baseline = [Q(v, 1229) for v in (172, 172, 236, 172, 172, 172, 172)]
        self.assertEqual(a, Q(51113, 245800))
        self.assertGreater(a, KAPPA)
        self.assertEqual(min(x + y for x, y in zip(baseline, deltas)), Q(1, 100))

    def test_full_pressure_boundary_primitive(self):
        # S(r)=r^2+1 and q(r)=2r on a=1; the same identity is evaluated
        # from the physical axial source F=(r S)'/r+q, independently.
        for r in (Q(5, 4), Q(3, 2), Q(2)):
            s = r * r + 1
            q_primitive = Q(2, 3) * (r**3 - 1) / r
            j_from_shear = s - Q(2) / r + q_primitive
            j_from_source = (Q(5, 3) * (r**3 - 1) + (r - 1)) / r
            self.assertEqual(j_from_shear, j_from_source)


if __name__ == "__main__":
    unittest.main()
