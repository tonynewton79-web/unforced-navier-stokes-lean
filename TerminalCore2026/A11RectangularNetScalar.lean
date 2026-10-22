import Mathlib

/-!
# A.11 two-coordinate source-hull scalar certification

This file formalizes only an exact rational release margin and a
conditional finite-net inequality. It does NOT construct the actual
A.11 source profile, its derivative constants, or an unforced
Navier--Stokes solution.
-/
namespace TerminalCore2026

theorem a11_strict_release_margin (lam b0 corr : ℝ)
    (hlam : 0 < lam)
    (hbase : b0 ≤ lam / 500)
    (hcorr : corr ≤ (4979 : ℝ) * lam / 10000) :
    b0 + corr ≤ lam / 2 - lam / 10000 := by
  linarith

theorem a11_rectangular_net_lower
    (f : ℝ × ℝ → ℝ) (H V : Set (ℝ × ℝ))
    (ry re Ly Le δ : ℝ)
    (hLy : 0 ≤ Ly) (hLe : 0 ≤ Le)
    (hcover : ∀ z ∈ H, ∃ v ∈ V,
      |z.1 - v.1| ≤ ry ∧ |z.2 - v.2| ≤ re)
    (hLip : ∀ z ∈ H, ∀ v ∈ V,
      |f z - f v| ≤ Ly * |z.1 - v.1| + Le * |z.2 - v.2|)
    (hnodes : ∀ v ∈ V, δ + Ly * ry + Le * re ≤ f v) :
    ∀ z ∈ H, δ ≤ f z := by
  intro z hz
  obtain ⟨v, hv, hy, he⟩ := hcover z hz
  have hf := hLip z hz v hv
  have hby := mul_le_mul_of_nonneg_left hy hLy
  have hbe := mul_le_mul_of_nonneg_left he hLe
  have hlow := neg_abs_le (f z - f v)
  have hn := hnodes v hv
  linarith

#print axioms a11_strict_release_margin
#print axioms a11_rectangular_net_lower

end TerminalCore2026
