import Mathlib

/-!
# UnforcedClosure

Abstract Lean formalization of the finite algebraic / functional-analytic closure layer
used in "Unforced Finite-Time Blow-Up for Navier--Stokes: Exact Nonlinear Closure
on the Three-Dimensional Periodic Torus".

Scope: this file certifies the scalar exponent identities, positivity margins,
the fixed-point-to-zero-residual implication, the scalar ball-invariance inequality,
and an abstract finite Neumann support-preservation lemma.  It does NOT import or
instantiate the PDE-specific hypotheses from `openai/NavierStokesAndEuler`.
-/

namespace UnforcedClosure

noncomputable section

/-- Carrier growth exponent A = 1/2 + h. -/
def A (h : ℝ) : ℝ := (1 : ℝ) / 2 + h

/-- Axial similarity exponent D = 1/2 - h. -/
def D (h : ℝ) : ℝ := (1 : ℝ) / 2 - h

/-- Weight reserved for the nonlinear correction. -/
def rho (h : ℝ) : ℝ := h / 5

/-- The cumulative-mean interaction is the exact 2/5 bottleneck. -/
theorem mean_gain_exact : (9 : ℝ) / 10 - (1 : ℝ) / 2 = (2 : ℝ) / 5 := by
  norm_num

/-- Spending 1/10 of epsilon leaves the exact 3/10 defect exponent. -/
theorem released_gain_exact : (2 : ℝ) / 5 - (1 : ℝ) / 10 = (3 : ℝ) / 10 := by
  norm_num

/-- The paper's coupling condition A/h > 2, written without division. -/
theorem coupling_margin_gt_two_mul
    {h : ℝ} (_hh : 0 < h) (hhalf : h < (1 : ℝ) / 2) :
    2 * h < A h := by
  dsimp [A]
  linarith

/-- The reserved nonlinear weight rho is positive. -/
theorem rho_pos {h : ℝ} (hh : 0 < h) : 0 < rho h := by
  dsimp [rho]
  linarith

/-- The regular-to-core coupling retains a positive release margin. -/
theorem coupling_release_pos {h : ℝ} (hh : 0 < h) :
    0 < A h - h / 10 := by
  dsimp [A]
  linarith

/-- After paying the nonlinear weight rho=h/5, coupling still has positive margin. -/
theorem coupling_minus_rho_pos {h : ℝ} (hh : 0 < h) :
    0 < (A h - h / 10) - rho h := by
  dsimp [A, rho]
  linarith

/-- All four spare exponents in the quadratic sector ledger are strictly positive. -/
theorem nonlinear_spare_margins_pos
    {h : ℝ} (hh : 0 < h) :
    0 < rho h ∧
    0 < A h + (1 : ℝ) / 2 ∧
    0 < A h ∧
    0 < 2 * A h + (1 : ℝ) / 2 - rho h := by
  dsimp [A, rho]
  constructor
  · linarith
  constructor
  · linarith
  constructor
  · linarith
  · linarith

section Residual

variable {X Y : Type*}
variable [AddCommGroup X] [Module ℝ X]
variable [AddCommGroup Y] [Module ℝ Y]

/-- If `G` is a right inverse of `L` and `v` satisfies the fixed-point equation,
then the abstract unforced residual vanishes exactly. -/
theorem fixedPoint_implies_zero_residual
    (L : X →ₗ[ℝ] Y) (G : Y →ₗ[ℝ] X)
    (B : X → X → Y) (R0 : Y) (v : X)
    (hRG : ∀ y, L (G y) = y)
    (hfix : v = - G (R0 + B v v)) :
    L v + R0 + B v v = 0 := by
  have hLv : L v = -(R0 + B v v) := by
    calc
      L v = L (-G (R0 + B v v)) := congrArg L hfix
      _ = -L (G (R0 + B v v)) := by simp
      _ = -(R0 + B v v) := by rw [hRG]
  rw [hLv]
  abel

end Residual

/-- The scalar inequality behind invariance of the radius-2*eta ball. -/
theorem ball_invariance_scalar
    {eta C : ℝ}
    (heta : 0 ≤ eta)
    (hsmall : 4 * C * eta ≤ 1) :
    eta + C * (2 * eta)^2 ≤ 2 * eta := by
  have haux : 0 ≤ eta * (1 - 4 * C * eta) :=
    mul_nonneg heta (sub_nonneg.mpr hsmall)
  nlinarith

/-- The strict smallness condition is exactly the contraction constant bound. -/
theorem contraction_constant_lt_one
    {eta C : ℝ} (hsmall : 4 * C * eta < 1) :
    4 * C * eta < 1 := hsmall

section Support

variable {X : Type*} [AddGroup X]

/-- Recursive geometric partial sum: Q_0 x=x and Q_{n+1}x=x-E(Q_n x).
For linear `E` this equals sum_{k=0}^n (-E)^k x. -/
def neumannPartial (E : X → X) : ℕ → X → X
  | 0, x => x
  | n + 1, x => x - E (neumannPartial E n x)

/-- Any support predicate closed under the local defect map and subtraction is
preserved by every finite Neumann partial sum. -/
theorem neumannPartial_preserves
    (E : X → X) (P : X → Prop)
    (hE : ∀ x, P x → P (E x))
    (hsub : ∀ x y, P x → P y → P (x - y)) :
    ∀ n x, P x → P (neumannPartial E n x) := by
  intro n
  induction n with
  | zero =>
      intro x hx
      simpa [neumannPartial] using hx
  | succ n ih =>
      intro x hx
      simpa [neumannPartial] using hsub x (E (neumannPartial E n x)) hx (hE _ (ih x hx))

end Support

#print axioms mean_gain_exact
#print axioms released_gain_exact
#print axioms coupling_margin_gt_two_mul
#print axioms nonlinear_spare_margins_pos
#print axioms fixedPoint_implies_zero_residual
#print axioms ball_invariance_scalar
#print axioms neumannPartial_preserves

end
end UnforcedClosure


/- Attack 207: scalar late-restart comparison only.
   x = delta^(1/64), m is a H^(17/8)-source inverse bound.
   The analytic estimates are hypotheses, not proved here. -/
namespace LateRestart207

theorem packet_margin {h : ℝ} (hh : 0 < h) (hsmall : h < (1 : ℝ) / 100) :
    0 < (1 + h) / 16 - h / 2 := by
  linarith

theorem restart_product_bound
    {x m M K F C eta : ℝ}
    (hx : 0 ≤ x) (hM : 0 ≤ M) (hK : 0 ≤ K) (hF : 0 ≤ F)
    (heta : 0 ≤ eta)
    (hm : m * x^16 ≤ M)
    (hC : C ≤ m * K * x^21)
    (hE : eta ≤ m * F * x^24) :
    4 * C * eta ≤ 4 * M^2 * K * F * x^13 := by
  have hc : C ≤ M * K * x^5 := calc
    C ≤ m * K * x^21 := hC
    _ = (m * x^16) * K * x^5 := by ring
    _ ≤ M * K * x^5 :=
      mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_right hm hK) (pow_nonneg hx 5)
  have he : eta ≤ M * F * x^8 := calc
    eta ≤ m * F * x^24 := hE
    _ = (m * x^16) * F * x^8 := by ring
    _ ≤ M * F * x^8 :=
      mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_right hm hF) (pow_nonneg hx 8)
  have hb : 0 ≤ M * K * x^5 := by positivity
  calc
    4 * C * eta = 4 * (C * eta) := by ring
    _ ≤ 4 * ((M * K * x^5) * (M * F * x^8)) :=
      mul_le_mul_of_nonneg_left (mul_le_mul hc he heta hb) (by norm_num)
    _ = 4 * M^2 * K * F * x^13 := by ring

theorem restart_gate
    {x m M K F C eta : ℝ}
    (hx : 0 ≤ x) (hM : 0 ≤ M) (hK : 0 ≤ K) (hF : 0 ≤ F)
    (heta : 0 ≤ eta)
    (hm : m * x^16 ≤ M)
    (hC : C ≤ m * K * x^21)
    (hE : eta ≤ m * F * x^24)
    (hsmall : 4 * M^2 * K * F * x^13 < 1) :
    4 * C * eta < 1 :=
  lt_of_le_of_lt (restart_product_bound hx hM hK hF heta hm hC hE) hsmall

#print axioms packet_margin
#print axioms restart_product_bound
#print axioms restart_gate
end LateRestart207


/- Attack 208: abstract restriction and scalar margin only.
   No singular-carrier PDE coercivity is asserted. -/
namespace OneTail208

theorem restriction_bound
    {XL XS ZL ZS : Type*}
    (nXL : XL → ℝ) (nXS : XS → ℝ)
    (nZL : ZL → ℝ) (nZS : ZS → ℝ)
    (large : XL → ZL → Prop) (small : XS → ZS → Prop)
    (restrictX : XL → XS) (extendZ : ZS → ZL)
    (M : ℝ)
    (hcontract : ∀ x, nXS (restrictX x) ≤ nXL x)
    (hisom : ∀ s, nZL (extendZ s) = nZS s)
    (hcompat : ∀ x s, large x (extendZ s) → small (restrictX x) s)
    (hsolve : ∀ z, ∃ x, large x z ∧ nXL x ≤ M * nZL z) :
    ∀ s, ∃ x, small x s ∧ nXS x ≤ M * nZS s := by
  intro s
  obtain ⟨x, hx, hb⟩ := hsolve (extendZ s)
  refine ⟨restrictX x, hcompat x s hx, ?_⟩
  calc
    nXS (restrictX x) ≤ nXL x := hcontract x
    _ ≤ M * nZL (extendZ s) := hb
    _ = M * nZS s := by rw [hisom]

theorem one_tail_product_bound
    {x m M K F C eta : ℝ}
    (hx : 0 ≤ x) (hM : 0 ≤ M) (hK : 0 ≤ K) (hF : 0 ≤ F)
    (heta : 0 ≤ eta) (hm : m ≤ M)
    (hC : C ≤ m * K * x^21)
    (hE : eta ≤ m * F * x^24) :
    4 * C * eta ≤ 4 * M^2 * K * F * x^45 := by
  have hc : C ≤ M * K * x^21 :=
    hC.trans (mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_right hm hK) (pow_nonneg hx 21))
  have he : eta ≤ M * F * x^24 :=
    hE.trans (mul_le_mul_of_nonneg_right
      (mul_le_mul_of_nonneg_right hm hF) (pow_nonneg hx 24))
  have hb : 0 ≤ M * K * x^21 := by positivity
  calc
    4 * C * eta = 4 * (C * eta) := by ring
    _ ≤ 4 * ((M * K * x^21) * (M * F * x^24)) :=
      mul_le_mul_of_nonneg_left (mul_le_mul hc he heta hb) (by norm_num)
    _ = 4 * M^2 * K * F * x^45 := by ring

theorem heat_point_margin {h : ℝ} (hh : h < (1 : ℝ) / 100) :
    (1 : ℝ) / 16 < (1 : ℝ) / 8 - 3*h/2 := by
  linarith

#print axioms restriction_bound
#print axioms one_tail_product_bound
#print axioms heat_point_margin
end OneTail208


/- Attack 209: scalar Gram positivity and abstract norm weakening.
   This file does not formalize Sobolev duality or carrier coercivity. -/
namespace EnergySpace209

theorem annular_gram_density_pos
    {R F Fp Fpp : ℝ}
    (hR : 0 < R) (hF : 0 < F)
    (hB : 2 * F + R * Fp < 0) :
    0 < R * ((R * Fpp + 2 * Fp)^2 + 3 * Fp^2) := by
  have hp : Fp ≠ 0 := by
    intro hz
    rw [hz, mul_zero, add_zero] at hB
    linarith
  have hs : 0 < Fp^2 := by positivity
  have ht : 0 < (R * Fpp + 2 * Fp)^2 + 3 * Fp^2 := by
    nlinarith [sq_nonneg (R * Fpp + 2 * Fp)]
  exact mul_pos hR ht

theorem horizontal_trace_margin {h : ℝ}
    (hh : h < (1 : ℝ)/100) :
    0 < (5 : ℝ)/64 - 5*h := by linarith

theorem horizontal_scaling (h : ℝ) :
    -(1/2+h) - 1 + (3/2-h)/2 =
      -(3 : ℝ)/4 - 3*h/2 := by ring

theorem weakened_selection
    {X Y Z : Type*}
    (nX : X → ℝ) (nY : Y → ℝ) (nZ : Z → ℝ)
    (LX : X → Z → Prop) (LY : Y → Z → Prop)
    (incl : X → Y) (M : ℝ)
    (hdom : ∀ x, nY (incl x) ≤ nX x)
    (hcompat : ∀ x s, LX x s → LY (incl x) s)
    (hsolve : ∀ s, ∃ x, LX x s ∧ nX x ≤ M*nZ s) :
    ∀ s, ∃ y, LY y s ∧ nY y ≤ M*nZ s := by
  intro s
  obtain ⟨x, hx, hb⟩ := hsolve s
  exact ⟨incl x, hcompat x s hx, (hdom x).trans hb⟩

#print axioms annular_gram_density_pos
#print axioms horizontal_trace_margin
#print axioms horizontal_scaling
#print axioms weakened_selection
end EnergySpace209


/- Attack 210: scalar checks only. The actual finite-order PDE
   packet expansion and its remainder estimates are analytic. -/
namespace ShearPacket210

theorem crossing_sign {nu p m Fp : ℝ}
    (hn : 0 < nu) (hp : 0 < p) (hm : m < 0) (hf : Fp < 0) :
    0 < 3 * nu * p * m * Fp := by
  have h : 0 < m * Fp := mul_pos_of_neg_of_neg hm hf
  calc
    0 < (3 * nu * p) * (m * Fp) := mul_pos (by positivity) h
    _ = 3 * nu * p * m * Fp := by ring

theorem neutral_slope {nu p g b l : ℝ}
    (hl : 0 < l) (hneut : g*b = nu*l^3) :
    2*nu*p + (g*b/l^3)*p = 3*nu*p := by
  have h : g*b/l^3 = nu := (div_eq_iff (pow_ne_zero 3 (ne_of_gt hl))).2 hneut
  rw [h]
  ring

theorem packet_margin {N h : ℝ}
    (hN : 1 + h < 4*N*h) :
    0 < N*h/4 - (1+h)/16 := by
  nlinarith

#print axioms crossing_sign
#print axioms neutral_slope
#print axioms packet_margin
end ShearPacket210
