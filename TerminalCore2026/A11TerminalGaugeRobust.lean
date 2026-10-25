import Mathlib

/-!
# A.11 terminal-gauge residual: finite formal gates

The proofs below are conditional on analytic source bounds supplied as
hypotheses; they DO NOT formalize infinite source integrals, A.11 roots,
the outer profile, or any unforced Navier--Stokes theorem.
-/
namespace TerminalCore2026

theorem a11_residual_budget
    (lam b g : ℝ)
    (hb : b < (11/10000:ℝ)*lam)
    (hg : g ≤ lam/100) :
    b+g < (111/10000:ℝ)*lam := by
  linarith

theorem a11_normalized_stress
    (lam E base error : ℝ)
    (hE : 0 < E)
    (hbase : |base| < (11/10000:ℝ)*lam*E)
    (herr : |error| ≤ lam/100*E) :
    |base+error| / E < (111/10000:ℝ)*lam := by
  have hh : |base+error| ≤ |base| + |error| :=
    abs_add_le base error
  apply (div_lt_iff₀ hE).mpr
  nlinarith

theorem a11_stress_slack
    (lam ratio : ℝ)
    (h : ratio < (111/10000:ℝ)*lam) :
    lam/2 - ratio > (4889/10000:ℝ)*lam := by
  linarith

theorem a11_exponential_taylor_rational :
    (1504439:ℚ)/453125 < 4 := by norm_num

theorem a11_cone_margin_arithmetic :
    (9:ℚ)/8 - (151/5000:ℚ)*(111/9700:ℚ)^2 >
      1124/1000 := by norm_num

theorem a11_cone_from_scalar_enclosures
    (r t w2 : ℝ)
    (hr : 0 ≤ r ∧ r ≤ 1/4)
    (ht : 0 ≤ t ∧ t ≤ 151/5000)
    (hw : 0 ≤ w2 ∧ w2 ≤ ((111:ℝ)/9700)^2) :
    2*(1-r)^2 - t*w2 > 1124/1000 := by
  have hsq : (3/4:ℝ)^2 ≤ (1-r)^2 := by
    nlinarith [sq_nonneg (1-r)]
  have hprod : t*w2 ≤ ((151:ℝ)/5000)*((111:ℝ)/9700)^2 := by
    calc
      t*w2 ≤ ((151:ℝ)/5000)*w2 :=
        mul_le_mul_of_nonneg_right ht.2 hw.1
      _ ≤ ((151:ℝ)/5000)*((111:ℝ)/9700)^2 :=
        mul_le_mul_of_nonneg_left hw.2 (by norm_num)
  nlinarith [hsq,hprod]

#print axioms a11_residual_budget
#print axioms a11_normalized_stress
#print axioms a11_stress_slack
#print axioms a11_cone_margin_arithmetic
#print axioms a11_cone_from_scalar_enclosures

end TerminalCore2026
