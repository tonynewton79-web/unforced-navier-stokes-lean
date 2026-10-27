"""Exact sharp curl screen at a rank-one quadratic density zero.

The test fixtures are consequences of the original seven ray floors,
not of the gate under test. They describe a local necessary condition;
they do not assert an authentic Case 006 profile.
"""

from fractions import Fraction as Q
import unittest

import sympy as sp

from h8_four_field_map import coefficient_correction
from h8_vacuum_curl_gate import (
    axial_rank_one_curl_feasible,
    axial_rank_one_curl_witness,
)


G = Q(15971, 122900)
H = Q(22371, 122900)
K = (3*G + H)/4
CENTERS = (Q(172, 1229), Q(172, 1229), Q(236, 1229),
           Q(172, 1229), Q(172, 1229), Q(172, 1229),
           Q(172, 1229))


class VacuumCurlTests(unittest.TestCase):
    def test_sharp_parallelogram_corners_have_original_ray_witnesses(self):
        for radial_sign in (-1, 1):
            for slope_sign in (-1, 1):
                w_r = radial_sign*G/8
                w_theta = slope_sign*K - 4*w_r
                self.assertTrue(axial_rank_one_curl_feasible(
                    w_r, w_theta, 0, Q(1)))
                a, b, c, d = axial_rank_one_curl_witness(
                    w_r, w_theta, 0, Q(1))
                self.assertEqual((-b, a), (w_r, w_theta))
                self.assertTrue(all(z + dz >= Q(1, 100)
                    for z, dz in zip(CENTERS,
                                     coefficient_correction(a, b, c, d))))

    def test_joint_curl_screen_rejects_incompatible_sharp_marginals(self):
        # Both separate coordinate caps hold but their combination fails.
        self.assertFalse(axial_rank_one_curl_feasible(
            G/8, (5*G+H)/4, 0, Q(1)))
        with self.assertRaises(ValueError):
            axial_rank_one_curl_witness(G/8, (5*G+H)/4, 0, Q(1))

    def test_axial_curl_and_zero_curvature_are_fail_closed(self):
        self.assertFalse(axial_rank_one_curl_feasible(0, 0, 1, Q(1)))
        self.assertFalse(axial_rank_one_curl_feasible(Q(1, 1000), 0, 0, 0))
        self.assertTrue(axial_rank_one_curl_feasible(0, 0, 0, 0))
        self.assertEqual(axial_rank_one_curl_witness(0, 0, 0, 0),
                         (Q(0), Q(0), Q(0), Q(0)))
        with self.assertRaises(ValueError):
            axial_rank_one_curl_feasible(0, 0, 0, -1)

    def test_spatially_rotating_frame_leaves_vacuum_curl_jet_unchanged(self):
        # Independent Cartesian differentiation, with E(0)=I and E'(0)!=0.
        x, y, z = sp.symbols("x y z", real=True)
        a, b, c, d = sp.Rational(1, 10), sp.Rational(1, 100), 0, 0
        H0 = sp.Matrix([[-d, c, a], [c, 0, b], [a, b, d]])
        E = sp.Matrix([[sp.cos(z), -sp.sin(z), 0],
                       [sp.sin(z), sp.cos(z), 0],
                       [0, 0, 1]])
        tensor = (z**2 / 2) * E*H0*E.T
        coords = (x, y, z)
        force = sp.Matrix([sum(sp.diff(tensor[i, j], coords[j])
                               for j in range(3)) for i in range(3)])
        curl = sp.Matrix([
            sp.diff(force[2], y)-sp.diff(force[1], z),
            sp.diff(force[0], z)-sp.diff(force[2], x),
            sp.diff(force[1], x)-sp.diff(force[0], y),
        ])
        self.assertEqual(tuple(sp.simplify(v.subs(z, 0)) for v in curl),
                         (-b, a, 0))


if __name__ == "__main__":
    unittest.main()
