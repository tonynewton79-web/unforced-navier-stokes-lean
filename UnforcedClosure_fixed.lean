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
