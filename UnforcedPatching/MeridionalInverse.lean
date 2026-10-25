import UnforcedPatching.CompactGauge
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Tactic

/-!
# Meridional cylindrical divergence: pointwise inverse identities

The symmetric cylindrical stress has orthonormal-frame entries
`K = S_rr`, `L = S_θθ`, `M = S_rz = S_zr`, and `C = S_zz`.

For an axisymmetric field the radial and axial divergence components are
`∂r K + (K-L)/r + ∂z M` and `∂r M + M/r + ∂z C`.

This file kernel-checks cancellation in those two *cylindrical-coordinate
expressions*, including the actual interval-integral antiderivative
in `z`. A separate Cartesian-to-cylindrical tensor calculus bridge,
the radial moment integral, compact support, and weighted cone bounds
are still outside the scope of these theorems.
-/

noncomputable section

open MeasureTheory
open Filter
open scoped Interval
open scoped Topology

namespace UnforcedPatching

abbrev MeridionalField := ℝ → ℝ → ℝ

def partialRadial (F : MeridionalField) (r z : ℝ) : ℝ :=
  deriv (fun s : ℝ => F s z) r

def partialAxial (F : MeridionalField) (r z : ℝ) : ℝ :=
  deriv (fun s : ℝ => F r s) z

/-- Radial divergence component of a symmetric axisymmetric stress. -/
def cylindricalRadialDiv (K L M : MeridionalField) (r z : ℝ) : ℝ :=
  partialRadial K r z + (K r z - L r z) / r + partialAxial M r z

/-- Axial divergence component of the same stress. -/
def cylindricalAxialDiv (M C : MeridionalField) (r z : ℝ) : ℝ :=
  partialRadial M r z + M r z / r + partialAxial C r z

/-- The hoop stress absorbs the full radial source, including the
geometric `(K-L)/r` term. -/
def meridionalHoop (K M fr : MeridionalField) (r z : ℝ) : ℝ :=
  K r z + r * (partialRadial K r z + partialAxial M r z - fr r z)

/-- The genuine axial interval-integral primitive, with the complete
geometric term retained inside the integrand. -/
def meridionalAxialPrimitive (fz M : MeridionalField) (c : ℝ) (r z : ℝ) : ℝ :=
  ∫ s in c..z, (fz r s - partialRadial M r s - M r s / r)

theorem axialPrimitive_partialAxial (fz M : MeridionalField)
    (c r z : ℝ)
    (hInt : IntervalIntegrable
      (fun s : ℝ => fz r s - partialRadial M r s - M r s / r) volume c z)
    (hMeas : StronglyMeasurableAtFilter
      (fun s : ℝ => fz r s - partialRadial M r s - M r s / r) (𝓝 z))
    (hCont : ContinuousAt
      (fun s : ℝ => fz r s - partialRadial M r s - M r s / r) z) :
    partialAxial (meridionalAxialPrimitive fz M c) r z =
      fz r z - partialRadial M r z - M r z / r := by
  change deriv
      (fun w : ℝ => ∫ s in c..w, (fz r s - partialRadial M r s - M r s / r))
      z = _
  exact (intervalIntegral.integral_hasDerivAt_right hInt hMeas hCont).deriv

/-- Algebraic identity for the source-matched radial hoop correction. -/
theorem hoop_radial_divergence (K M fr : MeridionalField)
    (r z : ℝ) (hr : r ≠ 0) :
    cylindricalRadialDiv K (meridionalHoop K M fr) M r z = fr r z := by
  unfold cylindricalRadialDiv meridionalHoop
  field_simp [hr]
  ring

/-- Exact pointwise inverse of the two meridional cylindrical divergence
components. No compact-support or coefficient-size conclusion follows. -/
theorem meridional_correction_divergence
    (K M fr fz : MeridionalField) (c r z : ℝ) (hr : r ≠ 0)
    (hInt : IntervalIntegrable
      (fun s : ℝ => fz r s - partialRadial M r s - M r s / r) volume c z)
    (hMeas : StronglyMeasurableAtFilter
      (fun s : ℝ => fz r s - partialRadial M r s - M r s / r) (𝓝 z))
    (hCont : ContinuousAt
      (fun s : ℝ => fz r s - partialRadial M r s - M r s / r) z) :
    cylindricalRadialDiv K (meridionalHoop K M fr) M r z = fr r z ∧
    cylindricalAxialDiv M (meridionalAxialPrimitive fz M c) r z = fz r z := by
  constructor
  · exact hoop_radial_divergence K M fr r z hr
  · unfold cylindricalAxialDiv
    rw [axialPrimitive_partialAxial fz M c r z hInt hMeas hCont]
    ring

/-- The radial moment primitive used in the compact annular construction. -/
def radialMomentIntegral (J : ℝ → ℝ) (a r : ℝ) : ℝ :=
  ∫ s in a..r, s * J s

/-- The mixed-stress radial carrier `H(r) = (1/r) ∫ₐʳ s J(s) ds`. -/
def radialMomentProfile (J : ℝ → ℝ) (a r : ℝ) : ℝ :=
  radialMomentIntegral J a r / r

theorem radialMoment_hasDerivAt (J : ℝ → ℝ) (a r : ℝ) (hr : r ≠ 0)
    (hInt : IntervalIntegrable (fun s : ℝ => s * J s) volume a r)
    (hMeas : StronglyMeasurableAtFilter (fun s : ℝ => s * J s) (𝓝 r))
    (hCont : ContinuousAt (fun s : ℝ => s * J s) r) :
    HasDerivAt (radialMomentProfile J a)
      (J r - radialMomentProfile J a r / r) r := by
  have hI : HasDerivAt (radialMomentIntegral J a) (r * J r) r := by
    change HasDerivAt (fun w : ℝ => ∫ s in a..w, s * J s) (r * J r) r
    exact intervalIntegral.integral_hasDerivAt_right hInt hMeas hCont
  have hD := hI.div (hasDerivAt_id r) hr
  have heq : (r * J r * r - radialMomentIntegral J a r * 1) / r ^ 2 =
      J r - radialMomentProfile J a r / r := by
    unfold radialMomentProfile
    field_simp [hr]
  change HasDerivAt (radialMomentProfile J a)
    ((r * J r * r - radialMomentIntegral J a r * 1) / r ^ 2) r at hD
  rw [heq] at hD
  exact hD

/-- The exact radial mean-balance relation `(r H)' = r J`. -/
theorem radialMoment_relation (J : ℝ → ℝ) (a r : ℝ) (hr : r ≠ 0)
    (hInt : IntervalIntegrable (fun s : ℝ => s * J s) volume a r)
    (hMeas : StronglyMeasurableAtFilter (fun s : ℝ => s * J s) (𝓝 r))
    (hCont : ContinuousAt (fun s : ℝ => s * J s) r) :
    deriv (radialMomentProfile J a) r + radialMomentProfile J a r / r = J r := by
  rw [(radialMoment_hasDerivAt J a r hr hInt hMeas hCont).deriv]
  ring

/-- The mixed stress prescribed by the radial moment and an axial cutoff. -/
def meridionalMixedCarrier (J η : ℝ → ℝ) (a : ℝ) : MeridionalField :=
  fun r z => radialMomentProfile J a r * η z

/-- The radial component of the mixed stress balances the axial mean.
The normalization of `η` is needed only for support at the upper boundary,
not for this pointwise identity. -/
theorem mixedCarrier_radial_balance (J η : ℝ → ℝ) (a r z : ℝ) (hr : r ≠ 0)
    (hInt : IntervalIntegrable (fun s : ℝ => s * J s) volume a r)
    (hMeas : StronglyMeasurableAtFilter (fun s : ℝ => s * J s) (𝓝 r))
    (hCont : ContinuousAt (fun s : ℝ => s * J s) r) :
    partialRadial (meridionalMixedCarrier J η a) r z +
      meridionalMixedCarrier J η a r z / r = J r * η z := by
  have hH := radialMoment_hasDerivAt J a r hr hInt hMeas hCont
  have hM := hH.mul_const (η z)
  have hpartial : partialRadial (meridionalMixedCarrier J η a) r z =
      (J r - radialMomentProfile J a r / r) * η z := by
    change deriv (fun t : ℝ => radialMomentProfile J a t * η z) r = _
    exact hM.deriv
  rw [hpartial]
  unfold meridionalMixedCarrier
  ring

/-- A direct source-matched diagonal example. For any axial envelope `ρ`,
the coordinate tensor `S_zz = ρ` and all other entries zero has radial
divergence zero and axial divergence `∂z ρ`. Compact support, positivity,
and the link to the four-field H8 cone are separate obligations. -/
theorem sourceMatched_axialStress (ρ : MeridionalField) (r z : ℝ) :
    cylindricalRadialDiv (fun _ _ => 0) (fun _ _ => 0) (fun _ _ => 0) r z = 0 ∧
    cylindricalAxialDiv (fun _ _ => 0) ρ r z = partialAxial ρ r z := by
  constructor
  · simp [cylindricalRadialDiv, partialRadial, partialAxial]
  · simp [cylindricalAxialDiv, partialRadial]

end UnforcedPatching
