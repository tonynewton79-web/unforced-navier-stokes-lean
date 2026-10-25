"""Exact tests of the one-sided H8 positivity floor, not an absolute cap.

Regression target: any implementation replacing the third ray's larger
budget, losing the D asymmetry, or using the earlier symmetric absolute
polytope must fail these independently calculated rational examples.
"""

from fractions import Fraction as Q
import unittest

from h8_four_field_map import coefficient_correction
from h8_sharp_dual import sharp_support
from h8_positive_cone import positive_support, positive_maximizer


G = Q(15971, 122900)
H = Q(22371, 122900)


class PositiveConeTests(unittest.TestCase):
    def test_coordinate_support_is_asymmetric(self):
        cases = (
            ((1, 0, 0, 0), (H + 5*G)/4),
            ((0, 1, 0, 0), G/8),
            ((0, 0, 1, 0), (G + H)/2),
            ((0, 0, -1, 0), G),
            ((0, 0, 0, 1), (G + H)/8),
            ((0, 0, 0, -1), G/4),
        )
        for ell, expected in cases:
            with self.subTest(ell=ell):
                self.assertEqual(positive_support(*ell, Q(1)), expected)

    def test_maximizer_attains_support_under_all_seven_positive_floors(self):
        samples = (
            (Q(0), Q(0), Q(0), Q(0)),
            (Q(1), Q(0), Q(0), Q(0)),
            (Q(0), Q(0), Q(-1), Q(0)),
            (Q(0), Q(0), Q(0), Q(1)),
            (Q(2), Q(-3), Q(5), Q(-7)),
            (Q(-5, 3), Q(3, 2), Q(-7, 5), Q(13, 4)),
        )
        for ell in samples:
            for rho in (Q(0), Q(7, 19), Q(1)):
                with self.subTest(ell=ell, rho=rho):
                    A, B, C, D = positive_maximizer(*ell, rho)
                    delta = coefficient_correction(A, B, C, D)
                    for i, correction in enumerate(delta):
                        centre = Q(236, 1229) if i == 2 else Q(172, 1229)
                        self.assertGreaterEqual(centre*rho+correction, rho/100)
                    self.assertEqual(sum(x*y for x, y in zip(ell, (A, B, C, D))),
                                     positive_support(*ell, rho))

    def test_one_sided_cone_contains_absolute_budget_and_requires_nonnegative_weight(self):
        for ell in ((Q(2), Q(-3), Q(5), Q(-7)),
                    (Q(0), Q(0), Q(1), Q(0))):
            rho = Q(11, 17)
            self.assertGreaterEqual(positive_support(*ell, rho),
                                    sharp_support(*ell, G*rho))
        with self.assertRaises(ValueError):
            positive_support(1, 2, 3, 4, Q(-1))
        with self.assertRaises(ValueError):
            positive_maximizer(1, 2, 3, 4, Q(-1))


if __name__ == "__main__":
    unittest.main()
