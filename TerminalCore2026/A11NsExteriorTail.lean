import Mathlib

/-!
Scalar implications used by the source-derived A.11 exterior-tail estimate.
The infinite integrals and source-stage hypotheses remain manuscript
obligations; this file is NOT an end-to-end Lean proof of Navier--Stokes.
-/
namespace TerminalCore2026

theorem A11_tail_budget :
    (61/100:ℚ)+1001/1000+1/100 < 2 := by norm_num

theorem A11_tail_scalar_Ns (E lam B : ℝ)
    (hE : 0 ≤ E) (hEb : E ≤ lam/4)
    (hB : B ≤ 2) : E*B ≤ lam/2 := by
  have hb := mul_le_mul_of_nonneg_left hB hE
  linarith

theorem A11_tail_Q_ratio (lam Q n : ℝ)
    (hlam : 0 < lam) (hQ : lam/2 ≤ Q)
    (hn0 : -lam/2 ≤ n) (hn1 : n ≤ lam/2) :
    -1 ≤ n/Q ∧ n/Q ≤ 1 := by
  have hqp : 0 < Q := by linarith
  constructor
  · exact (le_div_iff₀ hqp).2 (by linarith)
  · exact (div_le_iff₀ hqp).2 (by linarith)

theorem A11_tail_radial_gate (lam Q X : ℝ)
    (hlam : 0 < lam) (hQ : lam/2 ≤ Q)
    (hX : 9/lam ≤ X) : 9/2 ≤ X*Q := by
  have hpos : 0 < 9/lam := div_pos (by norm_num) hlam
  have hXpos : 0 ≤ X := by linarith
  have hstep : X*(lam/2) ≤ X*Q :=
    mul_le_mul_of_nonneg_left hQ hXpos
  have hm : 0 ≤ (X-9/lam)*lam :=
    mul_nonneg (sub_nonneg.mpr hX) (le_of_lt hlam)
  have hx : (9/lam)*lam=9 := by field_simp
  nlinarith

theorem A11_tail_margin_budget :
    (2:ℚ)*(1/2)^2-3/20 = 7/20 := by norm_num

#print axioms A11_tail_budget
#print axioms A11_tail_scalar_Ns
#print axioms A11_tail_Q_ratio
#print axioms A11_tail_radial_gate
#print axioms A11_tail_margin_budget
end TerminalCore2026
