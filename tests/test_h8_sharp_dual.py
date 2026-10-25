"""Independent exact tests for the original H8 coefficient-budget dual.

Production break caught: replacing the coupled seven-ray admissible set by
the stronger 14m sufficient box, or omitting the A/B coupling in its dual.
"""

from fractions import Fraction as Q
import unittest

from h8_four_field_map import coefficient_correction
from h8_sharp_dual import maximizer, sharp_support


class ExactSevenRayDualTests(unittest.TestCase):
    def test_support_on_coordinate_and_mixed_functionals(self):
        samples = (
            ((1, 0, 0, 0), Q(1)),
            ((0, 1, 0, 0), Q(1, 8)),
            ((0, 0, 1, 0), Q(1, 2)),
            ((0, 0, 0, 1), Q(1, 4)),
            ((1, -4, 0, 0), Q(1, 2)),
            ((2, -3, 5, -7), Q(33, 8)),
        )
        for gradients, expectation in samples:
            with self.subTest(gradients=gradients):
                self.assertEqual(sharp_support(*map(Q, gradients), Q(1)),
                                 expectation)

    def test_exact_maximizer_saturates_dual_and_obeys_all_seven_bounds(self):
        gradients = (
            (Q(0), Q(0), Q(0), Q(0)),
            (Q(1), Q(0), Q(0), Q(0)),
            (Q(0), Q(0), Q(0), Q(-1)),
            (Q(2), Q(-3), Q(5), Q(-7)),
            (Q(-5, 3), Q(3, 2), Q(-7, 5), Q(13, 4)),
        )
        for ell in gradients:
            for tau in (Q(0), Q(7, 19)):
                with self.subTest(ell=ell, tau=tau):
                    A, B, C, D = maximizer(*ell, tau)
                    self.assertLessEqual(max(map(abs, coefficient_correction(A, B, C, D))), tau)
                    self.assertEqual(sum(x*y for x, y in zip(ell, (A, B, C, D))),
                                     sharp_support(*ell, tau))

    def test_sign_symmetry_and_negative_budget_rejection(self):
        ell = (Q(1, 3), Q(-2, 5), Q(3, 7), Q(-4, 9))
        self.assertEqual(sharp_support(*ell, Q(11, 17)),
                         sharp_support(*(-x for x in ell), Q(11, 17)))
        with self.assertRaises(ValueError):
            sharp_support(*ell, Q(-1))
        with self.assertRaises(ValueError):
            maximizer(*ell, Q(-1))


if __name__ == "__main__":
    unittest.main()
