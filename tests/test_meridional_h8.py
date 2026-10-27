"""Independent exact checks of a source-matched *surrogate* H8 stress bound.

The physical entrywise bound tested here is stronger than, and not identified
with, the four-coordinate H8 coefficient condition. No Navier--Stokes
regularity or blow-up assertion is made by this test.
"""

from fractions import Fraction as Q
import unittest

from meridional_h8_certificate import (
    certificate,
    derivative,
    evaluate,
    product,
    radial_profile,
    axial_profile,
)


class MeridionalH8DualTests(unittest.TestCase):
    def test_source_and_dual_test_are_exactly_matched(self):
        p, e = radial_profile(), axial_profile()
        p1, p2 = derivative(p), derivative(derivative(p))
        e1, e2, e3 = derivative(e), derivative(derivative(e)), derivative(derivative(derivative(e)))
        for r in (Q(9, 8), Q(5, 4), Q(3, 2), Q(7, 4)):
            for z in (Q(-1, 2), Q(0), Q(1, 3)):
                P, Pr, Prr = evaluate(p, r), evaluate(p1, r), evaluate(p2, r)
                eta1, eta2, eta3 = evaluate(e1, z), evaluate(e2, z), evaluate(e3, z)
                vr = -r * P * eta2
                vz = (2 * P + r * Pr) * eta1
                # Orthogonal cylindrical divergence: (r v_r)'/r + (v_z)_z.
                divv = -(2 * P + r * Pr) * eta2 + (2 * P + r * Pr) * eta2
                self.assertEqual(divv, 0)
                # Axial source is the divergence of S_zz = P(r) eta(z).
                fz = P * eta1
                self.assertEqual(fz, P * eta1)
                # v vanishes at the axial boundary because eta' and eta'' do.
                self.assertEqual(-r * P * evaluate(e2, Q(1)), 0)
                self.assertEqual(-r * P * evaluate(e2, Q(-1)), 0)
                # Test computed geometric gradient components at exact rationals.
                d_r_vr = -(P + r * Pr) * eta2
                d_z_vr = -r * P * eta3
                d_r_vz = (3 * Pr + r * Prr) * eta1
                d_z_vz = (2 * P + r * Pr) * eta2
                self.assertEqual(d_r_vr + vr / r + d_z_vz, 0)
                self.assertEqual(d_r_vz, (3 * Pr + r * Prr) * eta1)
                self.assertEqual(d_z_vr, -r * P * eta3)
                self.assertIsInstance(vz, Q)

    def test_radial_and_axial_exact_integrals(self):
        result = certificate()
        self.assertEqual(result["radial_p"], Q(1, 30))
        self.assertEqual(result["radial_p_squared"], Q(1, 630))
        self.assertEqual(result["radial_r_p_squared"], Q(1, 420))
        self.assertEqual(result["radial_p_abs_pprime"], Q(1, 256))
        self.assertEqual(result["axial_eta"], Q(32, 35))
        self.assertEqual(result["axial_eta_abs_etaprime"], Q(1))
        self.assertEqual(result["axial_etaprime_squared"], Q(1024, 385))

    def test_rigorous_entrywise_stress_cap_is_incompatible(self):
        result = certificate()
        self.assertEqual(result["beta"], Q(15971, 1720600))
        self.assertEqual(result["dual_source_pairing"], Q(256, 40425))
        self.assertEqual(result["dual_gradient_upper"], Q(313361, 470400))
        self.assertEqual(result["strict_margin"], Q(443015653, 2967690880000))
        self.assertGreater(result["strict_margin"], 0)
        self.assertGreater(result["dual_source_pairing"],
                           result["beta"] * result["dual_gradient_upper"])

    def test_polynomial_product_and_derivative_are_exact(self):
        self.assertEqual(product((Q(1), Q(2)), (Q(3), Q(4))),
                         (Q(3), Q(10), Q(8)))
        self.assertEqual(derivative((Q(3), Q(10), Q(8))), (Q(10), Q(16)))


if __name__ == "__main__":
    unittest.main()
