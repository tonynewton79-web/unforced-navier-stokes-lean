"""Independent exact-arithmetic diagnostics for the annular H8 gauge.

The polynomial is an interior calculation, not a globally smooth compact
profile when extended by zero. This is not a test of the weighted H8 inverse.
"""

from fractions import Fraction as F
import unittest


def radial_polynomial_derivatives(r):
    u, v = r - 1, 2 - r
    p = u**4 * v**4
    p1 = 4 * u**3 * v**4 - 4 * u**4 * v**3
    p2 = 12 * u**2 * v**4 - 32 * u**3 * v**3 + 12 * u**4 * v**2
    return p, p1, p2


def axial_polynomial_derivatives(z):
    q = (1 - z**2)**4
    q1 = -8 * z * (1 - z**2)**3
    return q, q1


class CompactGaugeExactTests(unittest.TestCase):
    def test_radial_axial_derivative_exact(self):
        for r in (F(9, 8), F(5, 4), F(3, 2), F(7, 4)):
            for z in (F(-1, 2), F(0), F(1, 3), F(1, 2)):
                p, p1, p2 = radial_polynomial_derivatives(r)
                q, _ = axial_polynomial_derivatives(z)
                # K = r ∂rF; C = K + F; F = P(r)Q(z).
                k = r * p1 * q
                k_r = (p1 + r * p2) * q
                c_r = (2 * p1 + r * p2) * q
                self.assertEqual(c_r, k_r + k / r, (r, z))
                self.assertEqual(c_r, (2 * p1 + r * p2) * q)
                self.assertEqual(p * q + k, (p + r * p1) * q)

    def test_pure_radial_residual_curl_is_not_generally_zero(self):
        r, z = F(5, 4), F(1, 2)
        _, p1, p2 = radial_polynomial_derivatives(r)
        _, q1 = axial_polynomial_derivatives(z)
        # The z derivative of (∂rK + K/r) must vanish to be a
        # gradient with zero axial divergence. Here it does not.
        curl = (2 * p1 + r * p2) * q1
        self.assertEqual(curl, -F(5103, 32768))
        self.assertNotEqual(curl, F(0))

    def test_compact_radial_sign_obstruction(self):
        # For K = r ∂rF and F vanishing at radial endpoints,
        # ∫(K/r)dr = F(2,z)-F(1,z) = 0. The derivative must
        # change sign for any nontrivial nonnegative bump F.
        r_left, r_right = F(5, 4), F(7, 4)
        _, left, _ = radial_polynomial_derivatives(r_left)
        _, right, _ = radial_polynomial_derivatives(r_right)
        self.assertGreater(left, 0)
        self.assertLess(right, 0)
        p1, _, _ = radial_polynomial_derivatives(F(1))
        p2, _, _ = radial_polynomial_derivatives(F(2))
        self.assertEqual(p2 - p1, 0)


if __name__ == "__main__":
    unittest.main()
