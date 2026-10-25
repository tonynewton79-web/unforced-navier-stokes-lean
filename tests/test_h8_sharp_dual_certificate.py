"""Regression gates for a rational, not floating-point, dual obstruction.

The certificate concerns the named manufactured meridional source. It must
never be promoted as a source authentication of H8's unprovided residual.
"""

from fractions import Fraction as Q
import unittest

from h8_sharp_dual_certificate import (
    bernstein_coefficients,
    bound_separable_polynomial,
    manufactured_meridional_certificate,
)
from meridional_h8_certificate import certificate, evaluate


class H8SharpDualCertificateTests(unittest.TestCase):
    def test_bernstein_envelope_contains_nontrivial_interior_values(self):
        self.assertEqual(bernstein_coefficients((Q(0), Q(1)), Q(0), Q(1)),
                         (Q(0), Q(1)))
        self.assertEqual(bernstein_coefficients((Q(0), Q(0), Q(1)), Q(1), Q(2)),
                         (Q(1), Q(2), Q(4)))
        bump = (Q(0), Q(1), Q(-1))
        coeffs = bernstein_coefficients(bump, Q(0), Q(1))
        self.assertEqual(coeffs, (Q(0), Q(1, 2), Q(0)))
        for x in (Q(0), Q(1, 8), Q(1, 2), Q(7, 8), Q(1)):
            self.assertLessEqual(abs(evaluate(bump, x)), max(map(abs, coeffs)))

    def test_bivariate_bound_includes_signed_cross_term(self):
        # The signs of the two terms cancel at some points. The returned
        # envelope must still bound their exact sum everywhere.
        terms = (((Q(0), Q(1)), (Q(1), Q(-1))),
                 ((Q(1),), (Q(-1), Q(1))))
        upper = bound_separable_polynomial(terms, Q(0), Q(1), Q(0), Q(1))
        for r in (Q(0), Q(1, 3), Q(2, 3), Q(1)):
            for z in (Q(0), Q(1, 4), Q(3, 4), Q(1)):
                val = sum((evaluate(U, r)*evaluate(V, z) for U, V in terms), Q(0))
                self.assertLessEqual(abs(val), upper)

    def test_manufactured_source_original_budget_obstruction_is_strict(self):
        result = manufactured_meridional_certificate(grid_size=40)
        self.assertEqual(result["source_kind"], "manufactured_meridional_only")
        self.assertEqual(result["dual_source_pairing"], Q(256, 40425))
        self.assertEqual(result["original_budget"], Q(15971, 122900))
        self.assertLess(result["sharp_support_integral_upper"], Q(1, 25))
        self.assertGreater(result["strict_original_budget_margin"], Q(0))
        self.assertEqual(result["strict_original_budget_margin"],
                         result["dual_source_pairing"] - result["original_budget"] *
                         result["sharp_support_integral_upper"])
        self.assertEqual(result["dual_source_pairing"], certificate()["dual_source_pairing"])

    def test_rejects_unsupported_grid(self):
        with self.assertRaises(ValueError):
            manufactured_meridional_certificate(grid_size=0)


if __name__ == "__main__":
    unittest.main()
