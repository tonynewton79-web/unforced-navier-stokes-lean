"""Exact necessary A-flux cap from the original one-sided H8 cone."""

from fractions import Fraction as Q
import unittest

from h8_four_field_map import coefficient_correction
from h8_positive_cone import (
    axial_flux_cap,
    positive_maximizer,
    positive_support,
)


class AxialFluxConeCapTests(unittest.TestCase):
    def test_sharp_meridional_stress_cap(self):
        expected = Q(51113, 245800)
        for rho in (Q(0), Q(1), Q(7, 13)):
            self.assertEqual(axial_flux_cap(rho), expected*rho)
            self.assertEqual(positive_support(-1, 0, 0, 0, rho), expected*rho)

    def test_exact_floor_attains_positive_A_cap(self):
        rho = Q(1)
        A, B, C, D = positive_maximizer(1, 0, 0, 0, rho)
        self.assertEqual(A, axial_flux_cap(rho))
        corrections = coefficient_correction(A, B, C, D)
        centers = (Q(172, 1229),)*2 + (Q(236, 1229),) + (Q(172, 1229),)*4
        self.assertTrue(all(centers[i]*rho+corrections[i] >= rho/100
                            for i in range(7)))


if __name__ == "__main__":
    unittest.main()
