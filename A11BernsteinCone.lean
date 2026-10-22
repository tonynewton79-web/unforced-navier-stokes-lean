import Mathlib

/-!
# Conditional A.11 Bernstein stress-cone algebra

No unforced Navier--Stokes theorem is asserted. The actual physical A.11
moment and energy functions have NOT yet been identified as quadratics.
-/
namespace A11BernsteinCone

theorem bernstein_nonneg (t B0 B1 B2 : ℝ)
    (ht0 : 0 ≤ t) (ht1 : t ≤ 1)
    (h0 : 0 ≤ B0) (h1 : 0 ≤ B1) (h2 : 0 ≤ B2) :
    0 ≤ B0 * (1 - t)^2 + 2 * B1 * t * (1 - t) + B2 * t^2 := by
  have hleft : 0 ≤ 1 - t := by linarith
  have hA : 0 ≤ B0 * (1 - t)^2 :=
    mul_nonneg h0 (sq_nonneg (1 - t))
  have hB : 0 ≤ (2 * B1) * (t * (1 - t)) :=
    mul_nonneg (mul_nonneg (by norm_num : (0 : ℝ) ≤ 2) h1)
      (mul_nonneg ht0 hleft)
  have hC : 0 ≤ B2 * t^2 :=
    mul_nonneg h2 (sq_nonneg t)
  nlinarith [hA, hB, hC]

theorem quadratic_bernstein_lower (a b c eta δ : ℝ)
    (hlo : -1 ≤ eta) (hhi : eta ≤ 1)
    (h0 : δ ≤ a - b + c)
    (h1 : δ ≤ c - a)
    (h2 : δ ≤ a + b + c) :
    δ ≤ a * eta^2 + b * eta + c := by
  have ht0 : 0 ≤ (eta + 1) / 2 := by linarith
  have ht1 : (eta + 1) / 2 ≤ 1 := by linarith
  have hz := bernstein_nonneg ((eta + 1) / 2)
    ((a - b + c) - δ) ((c - a) - δ) ((a + b + c) - δ)
    ht0 ht1 (by linarith) (by linarith) (by linarith)
  have heq :
      (a * eta^2 + b * eta + c) - δ =
      ((a - b + c) - δ) * (1 - (eta + 1) / 2)^2 +
      2 * ((c - a) - δ) * ((eta + 1) / 2) * (1 - (eta + 1) / 2) +
      ((a + b + c) - δ) * ((eta + 1) / 2)^2 := by ring
  rw [← heq] at hz
  linarith

theorem two_sign_cone (λ E N : ℝ)
    (hE : 0 < E)
    (hplus : 0 ≤ λ * E + 2 * N)
    (hminus : 0 ≤ λ * E - 2 * N) :
    |N| / E ≤ λ / 2 := by
  have hbound : |N| ≤ λ * E / 2 := by
    apply abs_le.mpr
    constructor <;> linarith
  apply (div_le_iff₀ hE).2
  nlinarith

theorem uniform_quadratic_cone
    (λ ea eb ec na nb nc δ : ℝ)
    (hδ : 0 < δ)
    (hE0 : δ ≤ ea - eb + ec)
    (hE1 : δ ≤ ec - ea)
    (hE2 : δ ≤ ea + eb + ec)
    (hP0 : 0 ≤ (λ*ea + 2*na) - (λ*eb + 2*nb) + (λ*ec + 2*nc))
    (hP1 : 0 ≤ (λ*ec + 2*nc) - (λ*ea + 2*na))
    (hP2 : 0 ≤ (λ*ea + 2*na) + (λ*eb + 2*nb) + (λ*ec + 2*nc))
    (hM0 : 0 ≤ (λ*ea - 2*na) - (λ*eb - 2*nb) + (λ*ec - 2*nc))
    (hM1 : 0 ≤ (λ*ec - 2*nc) - (λ*ea - 2*na))
    (hM2 : 0 ≤ (λ*ea - 2*na) + (λ*eb - 2*nb) + (λ*ec - 2*nc))
    (eta : ℝ) (hlo : -1 ≤ eta) (hhi : eta ≤ 1) :
    |na * eta^2 + nb * eta + nc| /
      (ea * eta^2 + eb * eta + ec) ≤ λ / 2 := by
  let E : ℝ := ea * eta^2 + eb * eta + ec
  let N : ℝ := na * eta^2 + nb * eta + nc
  have hElower : δ ≤ E :=
    quadratic_bernstein_lower ea eb ec eta δ hlo hhi hE0 hE1 hE2
  have hP : 0 ≤ λ * E + 2 * N := by
    have hx := quadratic_bernstein_lower
      (λ*ea + 2*na) (λ*eb + 2*nb) (λ*ec + 2*nc)
      eta 0 hlo hhi hP0 hP1 hP2
    dsimp [E, N]
    nlinarith [hx]
  have hM : 0 ≤ λ * E - 2 * N := by
    have hx := quadratic_bernstein_lower
      (λ*ea - 2*na) (λ*eb - 2*nb) (λ*ec - 2*nc)
      eta 0 hlo hhi hM0 hM1 hM2
    dsimp [E, N]
    nlinarith [hx]
  exact two_sign_cone λ E N (lt_of_lt_of_le hδ hElower) hP hM

#print axioms bernstein_nonneg
#print axioms quadratic_bernstein_lower
#print axioms two_sign_cone
#print axioms uniform_quadratic_cone

end A11BernsteinCone
