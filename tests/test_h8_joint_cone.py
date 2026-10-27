"""Exact projected seven-ray feasibility and coupled axial/torque support."""

from fractions import Fraction as Q
import unittest

from h8_four_field_map import coefficient_correction
from h8_positive_cone import GAMMA, GAMMA_THIRD


class JointConeTests(unittest.TestCase):
    def test_all_six_hexagon_vertices_have_positive_lifts(self):
        from h8_positive_cone import joint_ac_feasible, joint_ac_witness

        g, h = GAMMA, GAMMA_THIRD
        vertices = ((g/2, -g), ((5*g+h)/4, (h-g)/4),
                    (g/2, (g+h)/2))
        centres = (Q(172, 1229), Q(172, 1229), Q(236, 1229),
                   Q(172, 1229), Q(172, 1229), Q(172, 1229),
                   Q(172, 1229))
        for sign in (-1, 1):
            for a0, c0 in vertices:
                A, C = sign*a0, c0
                self.assertTrue(joint_ac_feasible(A, C, Q(1)))
                B, D = joint_ac_witness(A, C, Q(1))
                self.assertTrue(all(ci+di >= Q(1, 100) for ci, di in
                                    zip(centres, coefficient_correction(A, B, C, D))))

    def test_separate_caps_are_not_jointly_feasible(self):
        from h8_positive_cone import joint_ac_feasible

        self.assertFalse(joint_ac_feasible(
            Q(51113, 245800), Q(19171, 122900), Q(1)))

    def test_joint_support_equals_vertex_maximum_exactly(self):
        from h8_positive_cone import joint_ac_support

        g, h = GAMMA, GAMMA_THIRD
        vertices = ((s*a, c) for s in (-1, 1) for a, c in
                    ((g/2, -g), ((5*g+h)/4, (h-g)/4),
                     (g/2, (g+h)/2)))
        vs = tuple(vertices)
        for a, c in ((Q(1), Q(0)), (Q(0), Q(1)),
                     (Q(0), Q(-1)), (Q(2, 3), Q(7, 5)),
                     (Q(-4, 7), Q(-9, 8))):
            self.assertEqual(joint_ac_support(a, c, Q(1)),
                             max(a*A+c*C for A, C in vs))

    def test_zero_density_has_only_zero_projection(self):
        from h8_positive_cone import joint_ac_feasible, joint_ac_witness

        self.assertTrue(joint_ac_feasible(0, 0, 0))
        self.assertEqual(joint_ac_witness(0, 0, 0), (Q(0), Q(0)))
        self.assertFalse(joint_ac_feasible(Q(1, 3), 0, 0))


if __name__ == "__main__":
    unittest.main()
