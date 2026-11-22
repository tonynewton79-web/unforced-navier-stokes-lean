import Mathlib

/-!
Attack 101: eight finite algebra lemmas only. The smooth cutoff Gram
coercivity and source flux–torque continuum theorem remain unformalized.
The original physical G and full unforced Navier–Stokes PDE remain OPEN.
-/
namespace UnforcedPatching.Attack101

theorem appendixAD_radial_A (r : ℝ) :
    2+(r-2)/2 = 1+r/2 := by ring

theorem appendixAD_radial_D (r : ℝ) :
    -(1+(r-2)/2)/2 = -r/4 := by ring

theorem appendixAD_affine_wronskian (x : ℝ) :
    (2+x/2)*(-(1:ℝ)/4) - (-(1+x/2)/2)*(1/2) = -(1:ℝ)/4 := by ring

theorem torque_flux_distributivity (M2 M3 bprime zbprime : ℝ) :
   bprime*(M2+M3/2)-zbprime*M3/4
   = bprime*M2+(bprime/2-zbprime/4)*M3 := by ring

theorem torque_test_weight (b bp z : ℝ) :
   bp/2-(b+z*bp)/4 = ((2-z)*bp-b)/4 := by ring

theorem strict_positive_for_negative_beta (beta rho I0 : ℝ)
    (hb : beta < 0) (hr : rho > 0) (hI : I0 > 0) :
    0 < -2*beta*rho*I0 := by
  nlinarith [mul_pos (neg_pos.mpr hb) hr, mul_pos (mul_pos (neg_pos.mpr hb) hr) hI]

theorem affine_nonzero_slope_forces_M3
    (M2 M3 g0 g1 : ℝ) (hm2 : M2=0)
    (hn : g0*M2+g1*M3=0) (hs : g1 ≠ 0) :
    M3=0 := by
  rw [hm2] at hn
  simp only [mul_zero, zero_add] at hn
  exact (mul_eq_zero.mp hn).resolve_left hs

theorem pointwise_torque_incompatibility
    (beta rho I0 : ℝ)
    (hbeta : beta < 0) (hrho : rho > 0) (hI : I0 > 0)
    (hflux : (0:ℝ) = -2*beta*rho*I0) : False := by
  have hpositive := strict_positive_for_negative_beta beta rho I0 hbeta hrho hI
  linarith

#print axioms appendixAD_radial_A
#print axioms appendixAD_radial_D
#print axioms appendixAD_affine_wronskian
#print axioms torque_flux_distributivity
#print axioms torque_test_weight
#print axioms strict_positive_for_negative_beta
#print axioms affine_nonzero_slope_forces_M3
#print axioms pointwise_torque_incompatibility

end UnforcedPatching.Attack101
