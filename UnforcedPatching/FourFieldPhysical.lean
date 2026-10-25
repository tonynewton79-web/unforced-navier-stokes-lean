import UnforcedPatching.SevenRayCenter
import Mathlib.Tactic

/-!
# Exact four-coordinate H8 tensor in the frozen quarter-aperture frame

The seven coefficient perturbations assemble into an actual symmetric
3×3 tensor in the chosen orthonormal frame. Removing its isotropic trace
provides the trace-free representative. In the fixed co-rotating cylindrical
frame of the XXV ray source, these entries have physical labels
`(r, θ, z)`. For any other frame `E`, physical components instead require
`E * H * Eᵀ`; differentiating `E` and authentic H8 source matching remain
unproved.
-/

noncomputable section

namespace UnforcedPatching

/-- The seven-ray perturbation tensor *before* the pressure-gauge shift. -/
def quarterRayTensorCorrection (A B C D : ℝ) (a b : Fin 3) : ℝ :=
  ∑ i : Fin 7, sevenRayCorrection A B C D i *
    (quarterRay i a : ℝ) * (quarterRay i b : ℝ)

/-- The four-field symmetric, trace-free physical matrix in the fixed
co-rotating source frame `(e_r,e_θ,e_z)`. -/
def fourFieldPhysical (A B C D : ℝ) (a b : Fin 3) : ℝ :=
  if a.val = 0 then
    if b.val = 0 then -D else if b.val = 1 then C else A
  else if a.val = 1 then
    if b.val = 0 then C else if b.val = 1 then 0 else B
  else if b.val = 0 then A else if b.val = 1 then B else D

/-- Full nine-entry identity: the ray perturbation plus `D/2 I` equals
the explicit four-field tensor. The scalar `D/2` is a pressure gauge,
not an extra constitutive stress coordinate. -/
theorem quarter_fourField_gauge_exact (A B C D : ℝ) (a b : Fin 3) :
    quarterRayTensorCorrection A B C D a b +
        (if a = b then D / 2 else 0) = fourFieldPhysical A B C D a b := by
  fin_cases a <;> fin_cases b <;>
    norm_num [quarterRayTensorCorrection, fourFieldPhysical,
      sevenRayCorrection, quarterRay, Fin.sum_univ_succ] <;> ring

/-- The frozen-frame physical matrix has no larger entry than the maximum
of its four coordinates. This implication is restricted to the identified
frame; rotating an arbitrary 3×3 tensor can change individual entries. -/
theorem fourFieldPhysical_entry_bound (A B C D ε : ℝ)
    (hA : |A| ≤ ε) (hB : |B| ≤ ε) (hC : |C| ≤ ε)
    (hD : |D| ≤ ε) (a b : Fin 3) :
    |fourFieldPhysical A B C D a b| ≤ ε := by
  have hε : 0 ≤ ε := le_trans (abs_nonneg A) hA
  fin_cases a <;> fin_cases b <;>
    simp [fourFieldPhysical, abs_neg, hε] <;> assumption

/-- The pressure representative has zero trace in the source frame. -/
theorem fourFieldPhysical_trace_zero (A B C D : ℝ) :
    (∑ a : Fin 3, fourFieldPhysical A B C D a a) = 0 := by
  norm_num [fourFieldPhysical, Fin.sum_univ_succ]

/-- The reconstructed tensor is symmetric in every pair of indices. -/
theorem fourFieldPhysical_symmetric (A B C D : ℝ) (a b : Fin 3) :
    fourFieldPhysical A B C D a b = fourFieldPhysical A B C D b a := by
  fin_cases a <;> fin_cases b <;> simp [fourFieldPhysical]

/-- Recover each of the four coordinates from its corresponding physical
off-diagonal or axial component, without choosing any further gauge. -/
theorem fourFieldPhysical_recover_coordinates (A B C D : ℝ) :
    fourFieldPhysical A B C D 0 2 = A ∧
    fourFieldPhysical A B C D 1 2 = B ∧
    fourFieldPhysical A B C D 0 1 = C ∧
    fourFieldPhysical A B C D 2 2 = D := by
  norm_num [fourFieldPhysical]

/-- The four-field family is not the entire five-dimensional space of
symmetric trace-free 3×3 tensors: its azimuthal diagonal vanishes. -/
theorem fourFieldPhysical_azimuthal_diagonal_zero (A B C D : ℝ) :
    fourFieldPhysical A B C D 1 1 = 0 := by
  norm_num [fourFieldPhysical]

/-- The two meridional diagonal components cancel in the chosen frame. -/
theorem fourFieldPhysical_meridional_diagonals (A B C D : ℝ) :
    fourFieldPhysical A B C D 0 0 +
      fourFieldPhysical A B C D 2 2 = 0 := by
  norm_num [fourFieldPhysical]

end UnforcedPatching
