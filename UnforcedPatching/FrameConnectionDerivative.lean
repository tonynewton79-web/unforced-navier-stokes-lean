import UnforcedPatching.RotatingFrameDual
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Prod
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Tactic

/-!
# Actual derivatives of a rotating-frame tensor

All matrices are the existing 3x3 real `FrameMatrix` tensors.
The derivative of every scalar entry of E and H is assumed, and
the product and finite-sum rules derive the derivative of E H Eᵀ.
For an orthogonal frame, its connection Ω=Eᵀ E' is skew and the
derivative is E (H' + ΩH - HΩ) Eᵀ. The commutator must not be lost.

No authentic H8 cutoff, source identity, differentiability bound,
or Navier--Stokes global PDE closure is supplied by this module.
-/

noncomputable section

namespace UnforcedPatching

/-- A matrix-aware alias, definitionally equal to the existing
`FrameMatrix` component representation. -/
abbrev DifferentialFrameMatrix := Matrix (Fin 3) (Fin 3) ℝ

/-- The existing componentwise tensor rotation agrees with matrix
multiplication `E H Eᵀ`. -/
theorem rotateStress_eq_matrixProduct (E H : DifferentialFrameMatrix) :
    rotateStress E H = E * H * E.transpose := by
  ext i j
  simp [rotateStress, Matrix.mul_apply, Matrix.transpose_apply, Fin.sum_univ_succ]
  ring

/-- The three Leibniz terms of the real scalar entry derivative. -/
def frameRawDifferential (E dE H dH : DifferentialFrameMatrix) : DifferentialFrameMatrix :=
  dE * H * E.transpose + E * dH * E.transpose + E * H * dE.transpose

/-- A matrix form of the finite double sum produced by the product rule. -/
theorem frameRawDifferential_entry (E dE H dH : DifferentialFrameMatrix) (i j : Fin 3) :
    frameRawDifferential E dE H dH i j =
      ∑ a : Fin 3, ∑ b : Fin 3,
        ((dE i a * H a b + E i a * dH a b) * E j b +
          E i a * H a b * dE j b) := by
  simp [frameRawDifferential, Matrix.mul_apply, Matrix.transpose_apply,
    Fin.sum_univ_succ]
  ring

/-- This is a *derived* physical tensor derivative, from individual
scalar entry derivatives of the frame and the coefficient tensor. -/
theorem frameRotationEntry_hasDerivAt
    (E H : ℝ → DifferentialFrameMatrix) (dE dH : DifferentialFrameMatrix) (t : ℝ)
    (hE : ∀ i a : Fin 3, HasDerivAt (fun s => E s i a) (dE i a) t)
    (hH : ∀ a b : Fin 3, HasDerivAt (fun s => H s a b) (dH a b) t)
    (i j : Fin 3) :
    HasDerivAt (fun s => rotateStress (E s) (H s) i j)
      (frameRawDifferential (E t) dE (H t) dH i j) t := by
  have hterm (a b : Fin 3) :
      HasDerivAt (fun s => E s i a * H s a b * E s j b)
        ((dE i a * H t a b + E t i a * dH a b) * E t j b +
          E t i a * H t a b * dE j b) t := by
    exact ((hE i a).mul (hH a b)).mul (hE j b)
  have hinner (a : Fin 3) :
      HasDerivAt (fun s => ∑ b : Fin 3, E s i a * H s a b * E s j b)
        (∑ b : Fin 3, ((dE i a * H t a b + E t i a * dH a b) * E t j b +
          E t i a * H t a b * dE j b)) t := by
    exact HasDerivAt.fun_sum (u := Finset.univ) (fun b _ => hterm a b)
  have houter :
      HasDerivAt (fun s => ∑ a : Fin 3, ∑ b : Fin 3,
        E s i a * H s a b * E s j b)
        (∑ a : Fin 3, ∑ b : Fin 3,
          ((dE i a * H t a b + E t i a * dH a b) * E t j b +
            E t i a * H t a b * dE j b)) t := by
    exact HasDerivAt.fun_sum (u := Finset.univ) (fun a _ => hinner a)
  simpa only [rotateStress, frameRawDifferential_entry] using houter

/-- Angular frame connection for an orthonormal frame. -/
def frameOmega (E dE : DifferentialFrameMatrix) : DifferentialFrameMatrix := E.transpose * dE

/-- The derivative of EᵀE=I forces Ω=EᵀE' to be skew-symmetric.
The differentiated orthogonality relation is an explicit hypothesis. -/
theorem frameOmega_skew (E dE : DifferentialFrameMatrix)
    (hTangent : dE.transpose * E + E.transpose * dE = 0) :
    (frameOmega E dE).transpose = -frameOmega E dE := by
  have h : dE.transpose * E = -(E.transpose * dE) := by
    exact eq_neg_of_add_eq_zero_left hTangent
  simpa [frameOmega, Matrix.transpose_mul] using h

/-- Full row orthogonality supplies E'=E Ω. -/
theorem frameVelocity_eq_frameOmega (E dE : DifferentialFrameMatrix)
    (hRow : E * E.transpose = 1) :
    dE = E * frameOmega E dE := by
  simp [frameOmega, ← mul_assoc, hRow]

/-- The connection commutator including the moving-frame terms. -/
theorem frameDifferential_commutator (E dE H dH : DifferentialFrameMatrix)
    (hRow : E * E.transpose = 1)
    (hTangent : dE.transpose * E + E.transpose * dE = 0) :
    frameRawDifferential E dE H dH =
      E * (dH + frameOmega E dE * H - H * frameOmega E dE) * E.transpose := by
  have hv := frameVelocity_eq_frameOmega E dE hRow
  have hs := frameOmega_skew E dE hTangent
  calc
    frameRawDifferential E dE H dH =
        frameRawDifferential E (E * frameOmega E dE) H dH :=
      congrArg (fun X => frameRawDifferential E X H dH) hv
    _ = E * (dH + frameOmega E dE * H - H * frameOmega E dE) * E.transpose := by
      simp only [frameRawDifferential, Matrix.transpose_mul, hs]
      noncomm_ring

/-- The complete kernel-checked moving-frame chain rule at each
physical Cartesian tensor entry, with all hypotheses visible. -/
theorem rotatingFrameStress_hasDerivAt
    (E H : ℝ → DifferentialFrameMatrix) (dE dH : DifferentialFrameMatrix) (t : ℝ)
    (hE : ∀ i a : Fin 3, HasDerivAt (fun s => E s i a) (dE i a) t)
    (hH : ∀ a b : Fin 3, HasDerivAt (fun s => H s a b) (dH a b) t)
    (hRow : E t * (E t).transpose = 1)
    (hTangent : dE.transpose * E t + (E t).transpose * dE = 0)
    (i j : Fin 3) :
    HasDerivAt (fun s => rotateStress (E s) (H s) i j)
      ((E t * (dH + frameOmega (E t) dE * H t -
         H t * frameOmega (E t) dE) * (E t).transpose) i j) t := by
  rw [← frameDifferential_commutator (E t) dE (H t) dH hRow hTangent]
  exact frameRotationEntry_hasDerivAt E H dE dH t hE hH i j

/-- With a stationary frame the commutator vanishes, as it must. -/
theorem rotatingFrame_constantFrame (E H dH : DifferentialFrameMatrix) :
    frameRawDifferential E 0 H dH = E * dH * E.transpose := by
  simp [frameRawDifferential]

/-- Generator of a counterclockwise XY rotation in 3D. -/
def framePlanarGenerator : DifferentialFrameMatrix := !![0, -1, 0; 1, 0, 0; 0, 0, 0]

/-- A diagonal source-frame stress that does not commute with rotation. -/
def frameDiagonalExample : DifferentialFrameMatrix := !![1, 0, 0; 0, 2, 0; 0, 0, 0]

/-- An explicit nonzero off-diagonal derivative. Dropping the
commutator would give zero; reversing its sign would give +1. -/
theorem frameConnection_nontrivial_example :
    (framePlanarGenerator * frameDiagonalExample -
      frameDiagonalExample * framePlanarGenerator) 0 1 = -1 := by
  norm_num [framePlanarGenerator, frameDiagonalExample,
    Matrix.mul_apply, Fin.sum_univ_succ]

/-- An actually varying 3D frame: counterclockwise planar rotation
with a stationary axial direction. -/
def planarRotation (θ : ℝ) : DifferentialFrameMatrix :=
  !![Real.cos θ, -Real.sin θ, 0;
    Real.sin θ, Real.cos θ, 0;
    0, 0, 1]

/-- Actual trigonometric stress, not a formal matrix-generator proxy.
The cross entry changes at speed -1 at angle zero; a derivative formula
without the connection would incorrectly predict zero for constant H. -/
theorem planarRotation_example_hasDerivAt :
    HasDerivAt
      (fun θ : ℝ => rotateStress (planarRotation θ) frameDiagonalExample 0 1)
      (-1 : ℝ) 0 := by
  have hfun :
      (fun θ : ℝ => rotateStress (planarRotation θ) frameDiagonalExample 0 1) =
      (fun θ : ℝ => -(Real.sin θ * Real.cos θ)) := by
    funext θ
    simp [rotateStress, planarRotation, frameDiagonalExample, Fin.sum_univ_succ]
    ring
  rw [hfun]
  convert ((Real.hasDerivAt_sin 0).mul (Real.hasDerivAt_cos 0)).neg using 1 <;>
    first | rfl | norm_num

end UnforcedPatching
