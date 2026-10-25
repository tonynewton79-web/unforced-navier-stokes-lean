import UnforcedPatching.FourFieldPhysical
import UnforcedPatching.PositiveCoefficientCone
import Mathlib.Tactic

/-!
# Dual coordinate pullback through an arbitrary 3×3 frame

These are pointwise algebraic identities. The map `E` is not assumed
constant; no derivatives are taken. Orthogonality is necessary for
interpreting an isotropic source-frame gauge as physical pressure,
but not for the Frobenius conjugation identity proved here.
-/

noncomputable section

namespace UnforcedPatching

/-- Entrywise real 3×3 matrices, written as tensor components. -/
abbrev FrameMatrix := Fin 3 → Fin 3 → ℝ

/-- Physical tensor components obtained by changing the source frame:
the expression represents `E H Eᵀ`. -/
def rotateStress (E H : FrameMatrix) : FrameMatrix :=
  fun i j => ∑ a : Fin 3, ∑ b : Fin 3, E i a * H a b * E j b

/-- The physical gradient pulled back to the source frame, `Eᵀ G E`. -/
def pullbackGradient (E G : FrameMatrix) : FrameMatrix :=
  fun a b => ∑ i : Fin 3, ∑ j : Fin 3, E i a * G i j * E j b

/-- Entrywise Frobenius pairing; the gradient need not be symmetric. -/
def framePairing (H G : FrameMatrix) : ℝ :=
  ∑ i : Fin 3, ∑ j : Fin 3, H i j * G i j

/-- No orthogonality is required for this finite-dimensional identity. -/
theorem frame_pairing_pullback (E H G : FrameMatrix) :
    framePairing (rotateStress E H) G =
      framePairing H (pullbackGradient E G) := by
  simp [framePairing, rotateStress, pullbackGradient, Fin.sum_univ_succ]
  ring

/-- The exact four coefficients pairing with a general source-frame
gradient. There is no independent azimuthal diagonal coefficient. -/
theorem fourField_pairing_covector (A B C D : ℝ) (M : FrameMatrix) :
    framePairing (fourFieldPhysical A B C D) M =
      A * (M 0 2 + M 2 0) + B * (M 1 2 + M 2 1) +
      C * (M 0 1 + M 1 0) + D * (M 2 2 - M 0 0) := by
  simp [framePairing, fourFieldPhysical, Fin.sum_univ_succ]
  ring

/-- The physical rotated tensor has *exactly* the four source-coordinate
dual actions obtained from `Eᵀ G E`. This is the finite kernel bridge
needed before a weighted H8 source-matched dual PDE estimate. -/
theorem rotating_fourField_frobenius
    (E G : FrameMatrix) (A B C D : ℝ) :
    framePairing (rotateStress E (fourFieldPhysical A B C D)) G =
      let M := pullbackGradient E G
      A * (M 0 2 + M 2 0) + B * (M 1 2 + M 2 1) +
      C * (M 0 1 + M 1 0) + D * (M 2 2 - M 0 0) := by
  rw [frame_pairing_pullback]
  exact fourField_pairing_covector A B C D (pullbackGradient E G)

/-- The genuine one-sided seven-ray coefficient floor yields a sharp
pointwise dual bound for any varying source-to-physical frame.
No differentiability or PDE source is assumed, so this theorem is not
yet an integrated weighted symmetric-divergence estimate. -/
theorem rotated_oneSided_dual_upper
    (E G : FrameMatrix) (ρ A B C D : ℝ)
    (hρ : 0 ≤ ρ)
    (hFloor : ∀ i : Fin 7,
      ρ * sevenRayCenter i + sevenRayCorrection A B C D i ≥ ρ / 100) :
    -framePairing (rotateStress E (fourFieldPhysical A B C D)) G ≤
      let M := pullbackGradient E G
      oneSidedPositiveConeSupport ρ
        (-(M 0 2 + M 2 0)) (-(M 1 2 + M 2 1))
        (-(M 0 1 + M 1 0)) (-(M 2 2 - M 0 0)) := by
  let M := pullbackGradient E G
  have hs := one_sided_positive_cone_dual_upper ρ A B C D
    (-(M 0 2 + M 2 0)) (-(M 1 2 + M 2 1))
    (-(M 0 1 + M 1 0)) (-(M 2 2 - M 0 0)) hρ hFloor
  have hp : -framePairing (rotateStress E (fourFieldPhysical A B C D)) G =
      A * (-(M 0 2 + M 2 0)) + B * (-(M 1 2 + M 2 1)) +
      C * (-(M 0 1 + M 1 0)) + D * (-(M 2 2 - M 0 0)) := by
    rw [rotating_fourField_frobenius]
    ring
  rw [hp]
  exact hs

end UnforcedPatching
