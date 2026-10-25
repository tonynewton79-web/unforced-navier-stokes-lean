"""Fail-closed, exact rational enclosures for one-sided H8 dual work.

A positive lower bound on the *available dual support* (above the source
pairing) means the named test field supplies no contradiction; it is
not a primal construction or proof of a source-matched stress.
"""

from fractions import Fraction as Q
import unittest

from h8_positive_dual_certificate import (
    signed_bernstein_upper,
    integrate_weighted_terms,
    manufactured_one_sided_certificate,
)
from meridional_h8_certificate import evaluate


class PositiveDualCertificateTests(unittest.TestCase):
    def test_signed_upper_must_not_turn_negative_polynomial_positive(self):
        self.assertEqual(signed_bernstein_upper((((Q(-1),), (Q(1),)),),
                           Q(0), Q(1), Q(0), Q(1)), Q(-1))
        terms = (((Q(0), Q(1)), (Q(1), Q(-1))),
                 ((Q(-1),), (Q(0), Q(1))))
        upper = signed_bernstein_upper(terms, Q(0), Q(1), Q(0), Q(1))
        for r in (Q(0), Q(1, 3), Q(1)):
            for z in (Q(0), Q(1, 2), Q(1)):
                val = sum((evaluate(U, r)*evaluate(V, z) for U,V in terms), Q(0))
                self.assertLessEqual(val, upper)

    def test_cell_integrates_weighted_separable_signed_terms(self):
        self.assertEqual(integrate_weighted_terms(
            (((Q(0), Q(1)), (Q(0), Q(1))),),
            (Q(1),), (Q(1),), Q(0), Q(1), Q(0), Q(1)), Q(1, 4))
        self.assertEqual(integrate_weighted_terms(
            (((Q(-1),), (Q(1),)),),
            (Q(1),), (Q(1),), Q(0), Q(1), Q(0), Q(1)), Q(-1))

    def test_rational_cellwise_lower_bound_exceeds_manufactured_pairing(self):
        result = manufactured_one_sided_certificate(grid_size=40)
        self.assertEqual(result["source_kind"], "manufactured_meridional_only")
        self.assertEqual(result["dual_source_pairing"], Q(256, 40425))
        self.assertGreater(result["support_integral_lower"], result["dual_source_pairing"])
        self.assertGreaterEqual(result["support_integral_upper"],
                                result["support_integral_lower"])
        self.assertLess(result["support_integral_upper"], Q(1, 100))

    def test_rejects_invalid_mesh(self):
        with self.assertRaises(ValueError):
            manufactured_one_sided_certificate(grid_size=0)


if __name__ == "__main__":
    unittest.main()
