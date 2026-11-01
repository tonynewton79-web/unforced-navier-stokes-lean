import UnforcedPatching.CartesianAxialBridge
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Tactic

/-!
# The periodic angular derivative disappears only after averaging

The pointwise nonaxisymmetric cylindrical axial source contains
`(1/r) ∂θ K_θz`. It is generally *not* zero. For a differentiable
periodic profile whose derivative is interval integrable, however,
its integral over a complete angular period vanishes by the actual FTC.

This source-independent cancellation does not authenticate the H8
profiles or justify radial/axial differentiation under integrals.
-/

noncomputable section

open MeasureTheory
open scoped Interval

namespace UnforcedPatching

/-- Average over one complete angular period, with its physical `2π`
normalization. -/
def azimuthalMean (f : ℝ → ℝ) : ℝ :=
  (∫ θ in (0 : ℝ)..(2 * Real.pi), f θ) / (2 * Real.pi)

/-- Exact angular FTC: the integral of the derivative of a periodic
profile vanishes. All differentiability/integrability hypotheses are
explicit; the conclusion is not a pointwise zero-derivative claim. -/
theorem angularDerivativeIntegral_zero (G D : ℝ → ℝ)
    (hDeriv : ∀ θ ∈ Set.uIcc (0 : ℝ) (2 * Real.pi), HasDerivAt G (D θ) θ)
    (hInt : IntervalIntegrable D volume 0 (2 * Real.pi))
    (hPeriodic : G (2 * Real.pi) = G 0) :
    (∫ θ in (0 : ℝ)..(2 * Real.pi), D θ) = 0 := by
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hDeriv hInt]
  rw [hPeriodic]
  ring

/-- The `1/r` angular-divergence contribution disappears from the full
azimuthal mean after the periodic FTC, while the genuine source `A`
remains untouched. The radius is strictly positive in physical use. -/
theorem angularMean_derivative_vanishes (A G D : ℝ → ℝ) (r : ℝ)
    (_hr : 0 < r)
    (hA : IntervalIntegrable A volume 0 (2 * Real.pi))
    (hD : IntervalIntegrable D volume 0 (2 * Real.pi))
    (hDeriv : ∀ θ ∈ Set.uIcc (0 : ℝ) (2 * Real.pi), HasDerivAt G (D θ) θ)
    (hPeriodic : G (2 * Real.pi) = G 0) :
    azimuthalMean (fun θ => A θ + (1 / r) * D θ) = azimuthalMean A := by
  have hZero := angularDerivativeIntegral_zero G D hDeriv hD hPeriodic
  have hInt : IntervalIntegrable (fun θ => (1 / r) * D θ) volume 0
      (2 * Real.pi) := hD.const_mul (1 / r)
  have hSplit := intervalIntegral.integral_add hA hInt
  unfold azimuthalMean
  rw [hSplit, intervalIntegral.integral_const_mul, hZero]
  ring

/-- A *nonconstant* polynomial with matching angular interval endpoints
and a nonzero derivative whose integral vanishes. It is not globally
periodic; global periodicity is stronger than the FTC needs. -/
theorem angularEqualEndpointPolynomialExample :
    (∫ θ in (0 : ℝ)..(2 * Real.pi),
      (2 * Real.pi - 2 * θ)) = 0 := by
  let T : ℝ := 2 * Real.pi
  let G : ℝ → ℝ := fun θ => T * θ - θ ^ 2
  have hDeriv (θ : ℝ) (hθ : θ ∈ Set.uIcc (0 : ℝ) (2 * Real.pi)) :
      HasDerivAt G (T - 2 * θ) θ := by
    have h := ((hasDerivAt_id θ).const_mul T).sub (hasDerivAt_pow 2 θ)
    have hfun : ((fun t : ℝ => T * id t) - fun t : ℝ => t ^ 2) = G := by
      funext t
      simp [G]
    rw [hfun] at h
    simpa using h
  have hInt : IntervalIntegrable (fun θ : ℝ => T - 2 * θ) volume 0 T := by
    have hc : Continuous (fun θ : ℝ => T - 2 * θ) := by fun_prop
    exact hc.intervalIntegrable 0 T
  have hPer : G T = G 0 := by
    dsimp [G]
    ring
  change (∫ θ in (0 : ℝ)..T, (T - 2 * θ)) = 0
  exact angularDerivativeIntegral_zero G (fun θ => T - 2 * θ)
    hDeriv hInt hPer

/-- A genuinely periodic smooth angular profile `G(θ)=sin θ`:
its derivative is `cos θ` and has zero integral over a full turn. -/
theorem angularSinePeriodicExample :
    (∫ θ in (0 : ℝ)..(2 * Real.pi), Real.cos θ) = 0 := by
  have hDeriv : ∀ θ ∈ Set.uIcc (0 : ℝ) (2 * Real.pi),
      HasDerivAt Real.sin (Real.cos θ) θ := by
    intro θ _
    exact Real.hasDerivAt_sin θ
  have hInt : IntervalIntegrable Real.cos volume 0 (2 * Real.pi) :=
    Real.continuous_cos.intervalIntegrable _ _
  have hPeriodic : Real.sin (2 * Real.pi) = Real.sin 0 := by
    simp
  exact angularDerivativeIntegral_zero Real.sin Real.cos
    hDeriv hInt hPeriodic

end UnforcedPatching
