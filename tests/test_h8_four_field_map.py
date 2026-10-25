"""Independent rational H8 ray-to-tensor reconstruction in the XXV frame.

The identified XXV rays use the orthonormal cylindrical frame
(e_r,e_theta,e_z). A different physical rotation requires explicit
conjugation; none is silently inferred from the ray coefficients.
"""

from fractions import Fraction as Q
import unittest

from h8_four_field_map import (
    coefficient_correction,
    cylinder_tensor,
    exact_original_cone_norm,
    ray_covariance,
    recover_four_coordinates,
    rotate_tensor,
)
from meridional_h8_certificate import certificate


class FourFieldPhysicalMapTests(unittest.TestCase):
    def test_trace_free_reconstruction_and_isotropic_gauge(self):
        samples = [
            (Q(1), Q(-1), Q(0), Q(1)),
            (Q(2, 7), Q(-3, 5), Q(7, 11), Q(-5, 13)),
            (Q(0), Q(0), Q(0), Q(0)),
        ]
        for A, B, C, D in samples:
            H = cylinder_tensor(A, B, C, D)
            self.assertEqual(H, (
                (-D, C, A), (C, Q(0), B), (A, B, D)
            ))
            self.assertEqual(H[0][0] + H[1][1] + H[2][2], 0)
            S = ray_covariance(A, B, C, D)
            for i in range(3):
                for j in range(3):
                    self.assertEqual(H[i][j], S[i][j] + (D / 2 if i == j else 0))

    def test_correction_coefficients_follow_frozen_source(self):
        self.assertEqual(coefficient_correction(Q(1), Q(-1), Q(0), Q(1)),
                         (Q(-3, 2), Q(-4), Q(-4), Q(14), Q(-6), Q(-8), Q(8)))

    def test_inverse_coordinate_recovery_and_missing_diagonal_mode(self):
        coordinates = (Q(7, 11), Q(-5, 6), Q(2, 9), Q(-3, 4))
        H = cylinder_tensor(*coordinates)
        self.assertEqual(recover_four_coordinates(H), coordinates)
        self.assertEqual(H[1][1], 0)
        self.assertEqual(H[0][0] + H[2][2], 0)
        # Symmetric and trace-free does not suffice: the other diagonal
        # direction is not represented by the four-coordinate construction.
        outside = ((Q(1), Q(0), Q(0)),
                   (Q(0), Q(-2), Q(0)),
                   (Q(0), Q(0), Q(1)))
        with self.assertRaises(ValueError):
            recover_four_coordinates(outside)

    def test_exact_original_cone_norm_equals_seven_ray_maximum(self):
        samples = ((Q(a, 11), Q(b, 13), Q(c, 17), Q(d, 19))
                   for a in (-7, -1, 0, 3, 8)
                   for b in (-9, 0, 2)
                   for c in (-5, 0, 6)
                   for d in (-3, 0, 4))
        for A, B, C, D in samples:
            measured = max(map(abs, coefficient_correction(A, B, C, D)))
            self.assertEqual(measured, exact_original_cone_norm(A, B, C, D))

    def test_original_cone_allows_fourteen_times_sufficient_budget(self):
        gamma = Q(15971, 122900)
        A, B, C, D = gamma, gamma / 8, Q(0), Q(0)
        self.assertEqual(exact_original_cone_norm(A, B, C, D), gamma)
        self.assertEqual(max(map(abs, coefficient_correction(A, B, C, D))), gamma)
        self.assertEqual(max(abs(x) for row in cylinder_tensor(A, B, C, D)
                             for x in row), gamma)
        self.assertEqual(gamma, 14 * Q(15971, 1720600))

    def test_four_coordinate_budget_implies_physical_entrywise_budget(self):
        c = certificate()
        beta = c["beta"]
        for A, B, C, D in (
            (beta, -beta, Q(0), beta),
            (-beta, beta, beta, -beta),
        ):
            H = cylinder_tensor(A, B, C, D)
            self.assertLessEqual(max(abs(x) for row in H for x in row), beta)
        self.assertGreater(c["strict_margin"], 0)

    def test_conservative_gradient_bound_cannot_exclude_original_budget(self):
        c = certificate()
        gamma = Q(15971, 122900)
        self.assertLess(c["dual_source_pairing"],
                        gamma * c["dual_gradient_upper"])
        self.assertEqual(gamma * c["dual_gradient_upper"] -
                         c["dual_source_pairing"], Q(51024386641, 635933760000))
        # Only this conservative comparison is inconclusive. The separate
        # sharp-cone Bernstein test DOES exclude this manufactured source.

    def test_explicit_rotation_requires_conjugation(self):
        A, B, C, D = Q(2), Q(3), Q(5), Q(7)
        R = ((Q(0), Q(-1), Q(0)), (Q(1), Q(0), Q(0)), (Q(0), Q(0), Q(1)))
        H = cylinder_tensor(A, B, C, D)
        T = rotate_tensor(H, R)
        self.assertEqual(T, ((Q(0), -C, -B), (-C, -D, A), (-B, A, D)))
        self.assertEqual(sum(T[i][i] for i in range(3)), 0)


if __name__ == "__main__":
    unittest.main()
