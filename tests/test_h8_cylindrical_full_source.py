"""Exact source geometry regressions; not authentic Case 006 data."""

import unittest

import sympy as sp

from h8_cylindrical_full_source import (
    cartesian_source,
    cartesian_source_via_connections,
    cylindrical_source_formula,
    frame_derivative_residuals,
    pressure_axial_jump,
)


class CylindricalFullSourceTests(unittest.TestCase):
    def setUp(self):
        self.r, self.theta, self.z = sp.symbols(
            "r theta z", real=True, positive=True
        )

    def test_frame_cartesian_chain_has_no_hidden_connection_residual(self):
        residuals = frame_derivative_residuals(self.r, self.theta)
        self.assertEqual(len(residuals), 5)
        for name, matrix in residuals.items():
            with self.subTest(direction=name):
                self.assertTrue(all(sp.simplify(e) == 0 for e in matrix))

    def test_arbitrary_symbolic_fields_all_three_source_components(self):
        r, t, z = self.r, self.theta, self.z
        A, B, C, D, p = (sp.Function(n)(r, t, z) for n in "ABCDp")
        actual = cartesian_source(A, B, C, D, p, r, t, z)
        expected = cylindrical_source_formula(A, B, C, D, p, r, t, z)
        for i, label in enumerate(("r", "theta", "z")):
            with self.subTest(component=label):
                self.assertEqual(sp.trigsimp(actual[i] - expected[i]), 0)

    def test_geometric_terms_survive_constant_nonzero_stress(self):
        r, t, z = self.r, self.theta, self.z
        actual = cylindrical_source_formula(0, 0, 3, 7, 0, r, t, z)
        self.assertEqual(tuple(map(sp.simplify, actual)), (-7 / r, 6 / r, 0))

    def test_actual_fourfold_angular_profile_and_pressure(self):
        r, t, z = self.r, self.theta, self.z
        A = r**2 * z * (1 + sp.cos(4 * t))
        B = r * z * sp.sin(4 * t)
        C = r**2 * z * sp.cos(4 * t)
        D = r * z**2
        p = r**2 * z
        point = {r: 2, t: 0, z: 1}
        actual = cartesian_source(A, B, C, D, p, r, t, z)
        expected = cylindrical_source_formula(A, B, C, D, p, r, t, z)
        self.assertEqual(tuple(sp.simplify(v.subs(point)) for v in actual),
                         (10, 8, 24))
        self.assertEqual(tuple(sp.simplify(v.subs(point)) for v in expected),
                         (10, 8, 24))
        self.assertEqual(pressure_axial_jump(D, p, r, t, z, -1, 1),
                         2 * r**2)

    def test_angular_mean_preserves_axial_trace(self):
        r, t, z = self.r, self.theta, self.z
        A = r**2 * z * (1 + sp.cos(4 * t))
        B = r * z * sp.sin(4 * t)
        D = r * z**2
        p = r**2 * z
        axial = cylindrical_source_formula(A, B, 0, D, p, r, t, z)[2]
        mean = sp.simplify(sp.integrate(axial, (t, 0, 2 * sp.pi)) / (2 * sp.pi))
        self.assertEqual(sp.simplify(mean - (5 * r * z + r**2)), 0)

    def test_axial_flux_balance_retains_both_pressure_and_stress_faces(self):
        r, t, z = self.r, self.theta, self.z
        A = r**2 * z * (1 + sp.cos(4*t))
        B = r*z*sp.sin(4*t)
        D = r*z**2
        p = r**2*z
        fz = cylindrical_source_formula(A, B, 0, D, p, r, t, z)[2]
        lhs = sp.integrate(fz, (z, 0, 1), (t, 0, 2*sp.pi))/(2*sp.pi)
        radial_flux = sp.diff(r*sp.integrate(A, (z, 0, 1),
                                            (t, 0, 2*sp.pi))/(2*sp.pi), r)/r
        face_flux = sp.integrate(pressure_axial_jump(D, p, r, t, z, 0, 1),
                                 (t, 0, 2*sp.pi))/(2*sp.pi)
        self.assertEqual(sp.simplify(lhs - radial_flux - face_flux), 0)
        self.assertEqual(sp.simplify(face_flux-(r+r**2)), 0)

    def test_nontrivial_spatial_tilt_uses_all_three_connections(self):
        r, t, z = self.r, self.theta, self.z
        alpha = r*z
        Q = sp.Matrix([[sp.cos(alpha), 0, sp.sin(alpha)],
                       [0, 1, 0],
                       [-sp.sin(alpha), 0, sp.cos(alpha)]])
        from h8_cylindrical_full_source import cylindrical_frame, source_tensor
        E = cylindrical_frame(t)*Q
        H = source_tensor(1, 2, 3, 4)
        p = r*z
        from_connections = cartesian_source_via_connections(E, H, p, r, t, z)
        # Direct Cartesian divergence gives an independently structured
        # expression, evaluated at two points with distinct nonzero tilt jets.
        K = E*H*E.T
        dx = lambda x: sp.cos(t)*sp.diff(x, r)-sp.sin(t)*sp.diff(x, t)/r
        dy = lambda x: sp.sin(t)*sp.diff(x, r)+sp.cos(t)*sp.diff(x, t)/r
        direct = E.T*(sp.Matrix([dx(K[i,0])+dy(K[i,1])+sp.diff(K[i,2],z)
                                   for i in range(3)]) +
                      sp.Matrix([dx(p),dy(p),sp.diff(p,z)]))
        for point in ({r:1,t:0,z:0},{r:1,t:0,z:sp.pi/2}):
            for i in range(3):
                residual = (from_connections[i]-direct[i]).subs(point)
                self.assertEqual(sp.trigsimp(sp.simplify(residual)), 0)


if __name__ == "__main__":
    unittest.main()
