import Mathlib
/-! Certified arithmetic implications for source A.11 N_s/E. The source
tail integral inequalities and unforced PDE are NOT proved here. -/
namespace TerminalCore2026
theorem A11_tail_budget (a b c : ℝ)
    (ha : a ≤ 61/100) (hb : b ≤ 1001/1000)
    (hc : c ≤ 1/100) :
    a+b+c ≤ 1621/1000 := by linarith

theorem A11_Ns_strict_slack (lam E n B : ℝ)
    (hl : 0 < lam) (hE : 0 ≤ E) (hcap : E ≤ lam/4)
    (hn : |n| ≤ E*B) (hB : B ≤ 1621/1000) :
    |n| + (379/4000)*lam ≤ lam/2 := by
  have hm : E*B ≤ E*(1621/1000:ℝ) :=
    mul_le_mul_of_nonneg_left hB hE
  have hq : E*(1621/1000:ℝ) ≤ (1621/4000)*lam := by nlinarith
  linarith

theorem A11_Ns_three_budget_slack (lam E n a b c : ℝ)
    (hl : 0 < lam) (hE : 0 ≤ E) (hcap : E ≤ lam/4)
    (hn : |n| ≤ E*(a+b+c))
    (ha : a ≤ 61/100) (hb : b ≤ 1001/1000)
    (hc : c ≤ 1/100) :
    |n|+(379/4000)*lam ≤ lam/2 := by
  exact A11_Ns_strict_slack lam E n (a+b+c) hl hE hcap hn
    (A11_tail_budget a b c ha hb hc)

theorem A11_Ns_Q_ratio (lam Q n : ℝ)
    (hl : 0 < lam) (hQ : lam/2 ≤ Q)
    (hn : |n| ≤ (1621/4000)*lam) :
    |n/Q| ≤ 1621/2000 := by
  have hqp : 0 < Q := by linarith
  rw [abs_div, abs_of_pos hqp]
  apply (div_le_iff₀ hqp).2
  linarith

theorem A11_normalized_cone_margin (u theta w : ℝ)
    (hu : u ≤ 1/2) (ht0 : 0 ≤ theta) (ht : theta ≤ 3/20)
    (hw : |w| ≤ 1621/2000) :
    (32117077/80000000:ℝ) ≤ 2*(1-u)^2-theta*w^2 := by
  have hwl : -(1621/2000:ℝ) ≤ w := (abs_le.mp hw).1
  have hwr : w ≤ (1621/2000:ℝ) := (abs_le.mp hw).2
  have hp : 0 ≤ ((1621/2000:ℝ)+w)*((1621/2000:ℝ)-w) :=
    mul_nonneg (by linarith) (by linarith)
  have hw2 : w^2 ≤ (1621/2000:ℝ)^2 := by nlinarith
  have hprd : theta*w^2 ≤ (3/20:ℝ)*(1621/2000:ℝ)^2 := by
    calc
      theta*w^2 ≤ theta*(1621/2000:ℝ)^2 :=
        mul_le_mul_of_nonneg_left hw2 ht0
      _ ≤ (3/20:ℝ)*(1621/2000:ℝ)^2 :=
        mul_le_mul_of_nonneg_right ht (sq_nonneg _)
  have hdiff : 0 ≤ (1-u-(1/2:ℝ))*(1-u+(1/2:ℝ)) :=
    mul_nonneg (by linarith) (by linarith)
  have hq : (1/4:ℝ) ≤ (1-u)^2 := by nlinarith
  nlinarith

theorem A11_cone_margin_over_two_fifths :
    (2/5:ℝ) < 32117077/80000000 := by norm_num

#print axioms A11_tail_budget
#print axioms A11_Ns_strict_slack
#print axioms A11_Ns_Q_ratio
#print axioms A11_normalized_cone_margin
#print axioms A11_cone_margin_over_two_fifths
end TerminalCore2026
