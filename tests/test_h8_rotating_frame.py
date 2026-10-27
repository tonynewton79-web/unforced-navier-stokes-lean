"""Exact rational tests of the H8 physical-frame dual pullback."""

import unittest
from fractions import Fraction as Q


class RotatingFrameTests(unittest.TestCase):
    @staticmethod
    def _module():
        try:
            import h8_rotating_frame
        except ImportError as exc:
            raise AssertionError("H8 frame pullback module not yet implemented") from exc
        return h8_rotating_frame

    def test_diagonal_gradient_has_explicit_rotated_covector(self):
        m = self._module()
        E = ((Q(3, 5), Q(0), Q(4, 5)),
             (Q(0), Q(1), Q(0)),
             (Q(-4, 5), Q(0), Q(3, 5)))
        G = ((Q(1), Q(0), Q(0)),
             (Q(0), Q(2), Q(0)),
             (Q(0), Q(0), Q(3)))
        self.assertEqual(m.dual_covector(E, G), (Q(-48, 25), Q(0), Q(0), Q(-14, 25)))

    def test_rotation_contraction_equals_source_covector_pairing(self):
        m = self._module()
        E = ((Q(3, 5), Q(0), Q(4, 5)),
             (Q(0), Q(1), Q(0)),
             (Q(-4, 5), Q(0), Q(3, 5)))
        G = ((Q(2), Q(-1), Q(3, 4)),
             (Q(5), Q(-2), Q(7)),
             (Q(1, 3), Q(4), Q(8)))
        A, B, C, D = Q(1, 7), Q(-2, 9), Q(3, 11), Q(5, 13)
        H = ((-D, C, A), (C, Q(0), B), (A, B, D))
        a, b, c, d = m.dual_covector(E, G)
        self.assertEqual(m.frobenius(m.rotate_tensor(E, H), G),
                         A * a + B * b + C * c + D * d)

    def test_orthogonal_gauge_rotates_to_isotropic_identity(self):
        m = self._module()
        E = ((Q(3, 5), Q(0), Q(4, 5)),
             (Q(0), Q(1), Q(0)),
             (Q(-4, 5), Q(0), Q(3, 5)))
        I = ((Q(1), Q(0), Q(0)),
             (Q(0), Q(1), Q(0)),
             (Q(0), Q(0), Q(1)))
        self.assertEqual(m.rotate_tensor(E, I), I)

    def test_nonorthonormal_frame_does_not_preserve_pressure_gauge(self):
        m = self._module()
        E = ((Q(1), Q(1), Q(0)),
             (Q(0), Q(1), Q(0)),
             (Q(0), Q(0), Q(1)))
        I = ((Q(1), Q(0), Q(0)),
             (Q(0), Q(1), Q(0)),
             (Q(0), Q(0), Q(1)))
        self.assertNotEqual(m.rotate_tensor(E, I), I)

    def test_rotated_positive_support_is_attained_pointwise(self):
        m = self._module()
        from h8_positive_cone import positive_maximizer, positive_support

        E = ((Q(3, 5), Q(0), Q(4, 5)),
             (Q(0), Q(1), Q(0)),
             (Q(-4, 5), Q(0), Q(3, 5)))
        G = ((Q(2), Q(-1), Q(3)),
             (Q(4), Q(5), Q(6)),
             (Q(7), Q(8), Q(9)))
        cov = tuple(-x for x in m.dual_covector(E, G))
        A, B, C, D = positive_maximizer(*cov, Q(7, 5))
        H = ((-D, C, A), (C, Q(0), B), (A, B, D))
        self.assertEqual(-m.frobenius(m.rotate_tensor(E, H), G),
                         positive_support(*cov, Q(7, 5)))


if __name__ == "__main__":
    unittest.main()
