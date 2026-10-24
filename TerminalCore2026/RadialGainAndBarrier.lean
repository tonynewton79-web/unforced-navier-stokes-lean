import Mathlib

/-!
Finite reductions underlying equations (17)-(18), (35), (43), (93)-(95)
of Zenodo 10.5281/zenodo.23474915.

These theorems do not formalize the infinite-dimensional analytic norm,
coefficient recursion, or PDE solution.
-/
namespace TerminalCore2026

noncomputable section

/-- Algebraic identity for the implicit-coordinate Jacobian L. -/
theorem Jacobian_identity (h eta : ℝ) :
    (1 - eta ^ 2) + 2 * ((1 : ℝ) / 2 - h) * eta ^ 2 =
      1 - 2 * h * eta ^ 2 := by
  ring

/-- The source coordinate Jacobian is positive on the central eta strip. -/
theorem Jacobian_pos (h eta : ℝ)
    (h_nonneg : 0 ≤ h) (h_small : h < (1 : ℝ) / 100)
    (eta_lo : -1 ≤ eta) (eta_hi : eta ≤ 1) :
    0 < 1 - 2 * h * eta ^ 2 := by
  have he1 : 0 ≤ eta + 1 := by linarith
  have he2 : 0 ≤ 1 - eta := by linarith
  have hebound : eta ^ 2 ≤ 1 := by
    nlinarith [mul_nonneg he1 he2]
  have hproduct : 0 ≤ h * (1 - eta ^ 2) :=
    mul_nonneg h_nonneg (sub_nonneg.mpr hebound)
  nlinarith

/-- An order-m regular singular symbol is at least (m+1)^2 if nu>=1. -/
theorem radial_symbol_lower (nu : ℝ) (hnu : 1 ≤ nu) (m : ℕ) :
    ((m : ℝ) + 1) ^ 2 ≤ ((m : ℝ) + 1) * ((m : ℝ) + nu) := by
  have hm : 0 ≤ (m : ℝ) := Nat.cast_nonneg _
  have hprod : 0 ≤ ((m : ℝ) + 1) * (nu - 1) :=
    mul_nonneg (by linarith) (by linarith)
  nlinarith

/-- Coefficientwise 1/(m+1)^2 gain from the radial inverse.
This is *not* yet the Banach-space estimate in manuscript equation (43). -/
theorem radial_coefficient_decay (nu : ℝ) (hnu : 1 ≤ nu)
    (m : ℕ) (c : ℝ) (hc : 0 ≤ c) :
    c / (((m : ℝ) + 1) * ((m : ℝ) + nu)) ≤
      c / (((m : ℝ) + 1) ^ 2) := by
  have hm : 0 ≤ (m : ℝ) := Nat.cast_nonneg _
  have hmp : 0 < (m : ℝ) + 1 := by linarith
  have hnp : 0 < (m : ℝ) + nu := by linarith
  have hd1 : 0 < ((m : ℝ) + 1) * ((m : ℝ) + nu) :=
    mul_pos hmp hnp
  have hd2 : 0 < ((m : ℝ) + 1) ^ 2 := sq_pos_of_pos hmp
  apply (div_le_div_iff₀ hd1 hd2).2
  exact mul_le_mul_of_nonneg_left (radial_symbol_lower nu hnu m) hc

/-- Algebraic obstruction at a proposed first zero of the axial slope.
Equation (93) plus (95) cannot hold with a nonpositive second derivative.
The derivative sign and ODE identity remain explicit assumptions. -/
theorem first_zero_barrier_algebra
    (X U Uprime Usecond W base eps delta Pprime : ℝ)
    (hX : 0 < X) (hU : 0 < U) (hfirst : Uprime = 0)
    (hsecond : Usecond ≤ 0) (hbase : eps ≤ base)
    (hmargin : delta < eps) (hpressure : -delta * U ≤ Pprime)
    (hODE : 2 * X * Usecond + (2 - X * W) * Uprime =
      base * U + Pprime) : False := by
  have hnonpos : 2 * X * Usecond ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos (by linarith) hsecond
  have hpos : 0 < (eps - delta) * U :=
    mul_pos (sub_pos.mpr hmargin) hU
  have hrest : 0 ≤ (base - eps) * U :=
    mul_nonneg (sub_nonneg.mpr hbase) (le_of_lt hU)
  rw [hfirst] at hODE
  nlinarith

#print axioms Jacobian_identity
#print axioms Jacobian_pos
#print axioms radial_symbol_lower
#print axioms radial_coefficient_decay
#print axioms first_zero_barrier_algebra

end
end TerminalCore2026
