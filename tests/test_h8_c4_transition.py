"""Independent C4 normalization, compact cutoff, overlap and pressure tests."""

import unittest

import sympy as sp


x, y, z = sp.symbols("x y z", real=True)
r = sp.symbols("r", positive=True)


class C4TransitionTests(unittest.TestCase):
    @staticmethod
    def _module():
        try:
            import h8_c4_transition
        except ImportError as exc:
            raise AssertionError("the C4 source transition calculator is missing") from exc
        return h8_c4_transition

    def test_flat_annular_cutoff_has_exact_plateau_and_zero_extensions(self):
        """Detects reversed flat-step orientation or lost compact annular support."""
        m = self._module()
        chi = m.flat_annular_cutoff(r, 1, 2, 3, 4)
        values = {t: sp.simplify(chi.subs(r, t))
                  for t in (0, 1, sp.Rational(3, 2), sp.Rational(5, 2),
                            sp.Rational(7, 2), 4, 5)}
        self.assertEqual(values, {0: 0, 1: 0, sp.Rational(3, 2): sp.Rational(1, 2),
                                  sp.Rational(5, 2): 1,
                                  sp.Rational(7, 2): sp.Rational(1, 2),
                                  4: 0, 5: 0})

    def test_normalized_c4_average_retains_equivariant_core(self):
        """Detects replacing the normalized fourfold average by a fourfold sum."""
        m = self._module()
        potential = (0, 0, (x*x+y*y)/2)
        v = m.localized_c4_velocity(potential, 1, (x, y, z))
        self.assertEqual(tuple(map(sp.simplify, v)), (y, -x, 0))

    def test_curl_of_average_equals_average_rotated_curls(self):
        """Detects an incorrect push-forward rotation or curl convention."""
        m = self._module()
        potential = (0, 0, x*x)
        chi = 1-x*x-y*y
        v = m.localized_c4_velocity(potential, chi, (x, y, z))
        fields = m.rotated_local_fields(potential, chi, (x, y, z))
        expected = tuple(sp.simplify(sum(vj[i] for vj in fields)/4)
                         for i in range(3))
        self.assertEqual(tuple(map(sp.simplify, v)), expected)
        self.assertEqual(sp.simplify(sum(sp.diff(v[i], c)
                                         for i, c in enumerate((x, y, z)))), 0)

    def test_all_transport_can_come_from_four_patch_cross_terms(self):
        """Detects deletion of the twelve ordered nonlinear overlaps."""
        m = self._module()
        fields = m.rotated_local_fields((0, 0, x*x), 1, (x, y, z))
        diagonal, cross, complete = m.c4_transport_parts(fields, (x, y, z))
        self.assertEqual(tuple(map(sp.simplify, diagonal)), (0, 0, 0))
        self.assertEqual(tuple(map(sp.simplify, cross)), (-x, -y, 0))
        self.assertEqual(tuple(map(sp.simplify, complete)), (-x, -y, 0))

    def test_c4_cross_stress_is_three_quarters_for_identical_rotates(self):
        """A fully overlapping C4-invariant meridional core has nonzero cross shear."""
        m = self._module()
        potential = (-y*z, x*z, 0)
        fields = m.rotated_local_fields(potential, 1, (x, y, z))
        diagonal, cross, complete = m.c4_quadratic_stress_parts(fields)
        self.assertEqual(sp.simplify(diagonal[0, 2]+x*z/2), 0)
        self.assertEqual(sp.simplify(cross[0, 2]+3*x*z/2), 0)
        self.assertEqual(sp.simplify(complete[0, 2]+2*x*z), 0)

    def test_candidate_c4_shaper_viscous_pressure_assembled_flux(self):
        """Checks a whole *toy* flux independently of its named channel ledger."""
        from h8_exact_flux_gate import (SHEAR_CHANNELS, BOUNDARY_CHANNELS,
                                        assemble_flux)
        from h8_shaper_flux_ledger import shaper_flux

        m = self._module()
        xi = z*z*(1-z)**2
        b = (r-1)**3
        core_r, core_z = -r, 2*z
        shear_increment = shaper_flux(r, z, 0, 1, core_r, core_z, b,
                                      [(1, 1, xi)], viscosity=1)
        p_r = -b*sp.diff(xi,z)/r
        p_z = sp.diff(b,r)*xi/r
        u_r, u_z = core_r+p_r, core_z+p_z
        direct_shear = sp.simplify(sp.integrate(
            u_r*u_z-(sp.diff(u_r,z)+sp.diff(u_z,r)), (z, 0, 1)))
        self.assertEqual(sp.simplify(direct_shear+r-shear_increment.total), 0)

        # Core shear -r splits into -r/4 diagonal and -3r/4 overlaps.
        shear = dict.fromkeys(SHEAR_CHANNELS, sp.S.Zero)
        shear["reference_center"] = -r/4
        shear["four_patch_overlap"] = -3*r/4
        shear["core_shaper"] = shear_increment.gamma*sp.diff(b,r) + shear_increment.delta*b
        shear["poloidal_pairing"] = shear_increment.quadratic*b*b
        shear["viscous"] = shear_increment.viscous

        # A solid-body toroidal core U_theta=r and T_theta=r*z*(1-z) have
        # a normalized pressure representative with zero axial endpoint jump.
        p_t = m.normalized_toroidal_pressure(r, z, 1, r, r*z*(1-z))
        self.assertEqual(m.axial_pressure_jump(p_t, z, 0, 1), 0)
        boundary = dict.fromkeys(BOUNDARY_CHANNELS, sp.S.Zero)
        # K_zz=u_z^2-2*∂_z u_z; P and its first axial jet vanish at endpoints.
        boundary["axial_tensor_jump"] = sp.S(4)
        boundary["toroidal_pressure"] = m.axial_pressure_jump(p_t, z, 0, 1)

        ledger = assemble_flux(r, 1, shear, boundary)
        self.assertEqual(sp.simplify(ledger.shear-direct_shear), 0)
        self.assertEqual(sp.simplify(ledger.source_axial_marginal -
                                    (sp.diff(r*direct_shear,r)/r+4)), 0)
        self.assertEqual(sp.simplify(ledger.J -
                                    (direct_shear-direct_shear.subs(r,1)/r+
                                     2*(r*r-1)/r)), 0)

    def test_noninvariant_cutoff_is_rejected(self):
        """Detects treating rotation of an asymmetric cutoff as the same cutoff."""
        m = self._module()
        with self.assertRaisesRegex(ValueError, "C4"):
            m.localized_c4_velocity((0, 0, x*x), x, (x, y, z))

    def test_toroidal_pressure_has_zero_boundary_jump_for_axial_cutoff(self):
        """Detects a missing radial pressure primitive or spurious endpoint jet."""
        m = self._module()
        xi = (1-z*z)**2
        p = m.normalized_toroidal_pressure(r, z, 1, r, r*xi)
        expected = (r*r-1)*(2*xi+xi*xi)/2
        self.assertEqual(sp.simplify(p-expected), 0)
        self.assertEqual(sp.simplify(p.subs(r, 1)), 0)
        self.assertEqual(sp.simplify(sp.diff(p, r)-(2*r*r*xi+r*r*xi*xi)/r), 0)
        self.assertEqual(m.axial_pressure_jump(p, z, -1, 1), 0)

    def test_nonvanishing_toroidal_trace_produces_required_pressure_jump(self):
        """Detects silently setting a noncompact axial pressure trace to zero."""
        m = self._module()
        p = m.normalized_toroidal_pressure(r, z, 1, r, r*z)
        self.assertEqual(sp.simplify(m.axial_pressure_jump(p, z, -1, 1)),
                         2*(r*r-1))


if __name__ == "__main__":
    unittest.main()
