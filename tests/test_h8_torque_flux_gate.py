"""Red/green full-circle torque compatibility and asymmetric cone bound."""

from fractions import Fraction as Q
import unittest

import sympy as sp

from h8_cylindrical_full_source import (
    azimuthal_torque_primitive,
    cylindrical_source_formula,
)
from h8_positive_cone import (
    azimuthal_shear_interval,
    positive_maximizer,
)
from h8_four_field_map import coefficient_correction


class H8TorqueFluxTests(unittest.TestCase):
    def test_full_circle_torque_cancels_angular_pressure_only(self):
        r, t, z = sp.symbols("r theta z", positive=True, real=True)
        C = r**2*z*sp.cos(4*t)+r*z**2
        B = r*z*sp.sin(4*t)+r*z**2
        p = r*z*sp.sin(t)
        ftheta = cylindrical_source_formula(0, B, C, 0, p, r, t, z)[1]
        averaged = sp.simplify(sp.integrate(ftheta, (t, 0, 2*sp.pi))/(2*sp.pi))
        self.assertEqual(sp.simplify(averaged-(3*z**2+2*r*z)), 0)
        lhs = sp.integrate(averaged, (z, 0, 1))
        rhs = azimuthal_torque_primitive(C, B, r, t, z, 0, 1)
        self.assertEqual(sp.simplify(lhs-rhs), 0)
        self.assertEqual(sp.simplify(rhs-(1+r)), 0)

    def test_torque_radial_reconstruction_retains_endcap_B(self):
        r,a = sp.symbols("r a", positive=True)
        # A fabricated Ftheta=1+r and cap B_jump=r requires C_slice=r/3,
        # once the correct r^2 geometric weight is retained.
        F = 1+r
        B_jump = r
        inner_C = a/3
        recovered = sp.simplify((a**2*inner_C+
                 sp.integrate(sp.Symbol("s")**2*(F.subs(r,sp.Symbol("s"))-
                    B_jump.subs(r,sp.Symbol("s"))),
                    (sp.Symbol("s"),a,r)))/r**2)
        self.assertEqual(sp.simplify(recovered-r/3), 0)

    def test_azimuthal_cone_is_sharp_and_asymmetric(self):
        g=Q(15971,122900)
        h=Q(22371,122900)
        for rho in (Q(0),Q(1),Q(7,5)):
            self.assertEqual(azimuthal_shear_interval(rho),(-g*rho,(g+h)*rho/2))
        for direction, limit in ((1,(g+h)/2),(-1,-g)):
            A,B,C,D=positive_maximizer(0,0,direction,0,Q(1))
            self.assertEqual(C,limit)
            delta=coefficient_correction(A,B,C,D)
            base=(Q(172,1229),)*2+(Q(236,1229),)+(Q(172,1229),)*4
            self.assertTrue(all(base[i]+delta[i]>=Q(1,100) for i in range(7)))


if __name__ == "__main__":
    unittest.main()
