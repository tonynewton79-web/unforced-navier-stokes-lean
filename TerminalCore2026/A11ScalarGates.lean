import Mathlib

/-!
# Finite Appendix A.10/A.11 scalar certificates

The smooth-step endpoint identities, integrals, Banach C¹
contraction, axial stress integrals and unforced Navier–Stokes
PDE are NOT yet formalized end-to-end. No axioms/sorry are added.
-/
namespace TerminalCore2026

theorem A11_entrance_derivative_cancellation
    (Jp C rp I J : ℝ) :
    -Jp*C*(rp+I)+Jp*C*(I-J) = -Jp*C*(rp+J) := by ring

theorem A11_pressure_quadratic_row
    (c₁ c₂ v₁ v₂ κ : ℝ) :
    v₁*(c₁+κ*c₁^2)+v₂*(c₂+κ*c₂^2) =
      v₁*c₁+v₂*c₂+κ*(v₁*c₁^2+v₂*c₂^2) := by ring

theorem A11_axial_stress_energy_identity
    (η h A d W1 W0 W1η W0η : ℝ) :
    (4*h*η*(W1/2)-d*(W1η/2))+
      4*A*η*(-W0/2)-d*(-W0η/2) =
      2*η*(h*W1-A*W0)+(d/2)*(W0η-W1η) := by ring

theorem A11_matrix_det_sign
    (u₁ u₂ v₁ v₂ : ℝ) :
    u₁*v₂-u₂*v₁ = -(u₂*v₁-u₁*v₂) := by ring

theorem A11_numeric_cone_margin :
    ((2*(5/4:ℚ)^2*((1/100:ℚ)*(93/20+(2/3:ℚ)/(100^7))+
      (51/100))+(3/5:ℚ)*(5/4))/(3/4) < 4 := by norm_num

theorem A11_slope_from_bump (λ qy q : ℝ)
    (hλ : 0 ≤ λ) (hq : -(1/4) ≤ q)
    (hqy : qy ≤ (3/8)*λ) :
    -λ+qy/(1+q) ≤ -λ/2 := by
  have hp : 0 < 1+q := by linarith
  have hprod : 0 ≤ λ*(q+1/4) := by
    apply mul_nonneg hλ
    linarith
  have hx : qy ≤ λ/2*(1+q) := by nlinarith
  have hdiv : qy/(1+q) ≤ λ/2 := (div_le_iff₀ hp).2 hx
  linarith

#print axioms A11_entrance_derivative_cancellation
#print axioms A11_pressure_quadratic_row
#print axioms A11_axial_stress_energy_identity
#print axioms A11_numeric_cone_margin
#print axioms A11_slope_from_bump

end TerminalCore2026
