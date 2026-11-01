import UnforcedPatching.NonaxisymmetricAxialBridge
import Mathlib.Analysis.Calculus.Deriv.Prod
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Tactic

/-!
# Physical-circle angular derivative and its exact vanishing mean

For each radius `r`, the actual Cartesian circle is
`γ_r(θ)=(r cos θ,r sin θ)`. Its tangent is
`γ'_r(θ)=(-r sin θ,r cos θ)=(-y,x)`.

Composing a Frechet-differentiable physical stress component
`n : ℝ×ℝ→ℝ` with this circle supplies the angular derivative
assumption of `AngularMean`, and trigonometric endpoint identities
supply its endpoint equality automatically. The field's derivative
still needs genuine integrability; authentic H8 data is not assumed.

No axial integration, radial derivative interchange, rotating H8
frame source match or global PDE conclusion is established here.
-/

noncomputable section

open MeasureTheory
open scoped Interval

namespace UnforcedPatching

/-- The physical Cartesian circle at cylindrical radius `r`. -/
def physicalCircle (r θ : ℝ) : ℝ × ℝ :=
  (r * Real.cos θ, r * Real.sin θ)

/-- Its actual tangential Cartesian velocity. -/
def physicalCircleTangent (r θ : ℝ) : ℝ × ℝ :=
  (-r * Real.sin θ, r * Real.cos θ)

/-- Kernel-checked trigonometric circle derivative. -/
theorem physicalCircle_hasDerivAt (r θ : ℝ) :
    HasDerivAt (physicalCircle r) (physicalCircleTangent r θ) θ := by
  have hc := (Real.hasDerivAt_cos θ).const_mul r
  have hs := (Real.hasDerivAt_sin θ).const_mul r
  have h := hc.prodMk hs
  have hfun : (fun t : ℝ => (r * Real.cos t, r * Real.sin t)) =
      physicalCircle r := by rfl
  have hval : (r * (-Real.sin θ), r * Real.cos θ) =
      physicalCircleTangent r θ := by
    ext <;> simp [physicalCircleTangent]
  rw [hfun, hval] at h
  exact h

/-- The true Frechet chain rule supplies the stress's angular derivative
along the physical circle. The derivative is an evaluated linear map,
not a newly postulated scalar angular function. -/
theorem physicalCirclePullback_hasDerivAt (n : (ℝ × ℝ) → ℝ)
    (L : (ℝ × ℝ) →L[ℝ] ℝ) (r θ : ℝ)
    (hN : HasFDerivAt n L (physicalCircle r θ)) :
    HasDerivAt (fun t : ℝ => n (physicalCircle r t))
      (L (physicalCircleTangent r θ)) θ := by
  exact hN.comp_hasDerivAt θ (physicalCircle_hasDerivAt r θ)

/-- The linear-map angular tangent derivative equals the Cartesian
directional expression `-y*n_x + x*n_y`, where the two scalar
directional coefficients are the derivative along the coordinate axes. -/
theorem physicalCircleDirectionalCoordinates
    (L : (ℝ × ℝ) →L[ℝ] ℝ) (r θ : ℝ) :
    L (physicalCircleTangent r θ) =
      (-r * Real.sin θ) * L (1, 0) +
      (r * Real.cos θ) * L (0, 1) := by
  have hdecomp : physicalCircleTangent r θ =
      (-r * Real.sin θ) • ((1, 0) : ℝ × ℝ) +
        (r * Real.cos θ) • ((0, 1) : ℝ × ℝ) := by
    ext <;> simp [physicalCircleTangent, smul_eq_mul]
  rw [hdecomp, map_add, map_smul, map_smul]
  simp [smul_eq_mul]

/-- The normalized physical angular term coincides exactly with the
last term of `cartesianGeneralAxialDivergence` at points on a circle.
The physical radius is assumed positive when applying the divergence
identity, but the algebraic equality itself holds at every radius. -/
theorem physicalCircleAngularTermMatchesCartesian
    (L : (ℝ × ℝ) →L[ℝ] ℝ) (r θ : ℝ) :
    L (physicalCircleTangent r θ) / r =
      (-(physicalCircle r θ).2 * L (1, 0) +
        (physicalCircle r θ).1 * L (0, 1)) / r := by
  rw [physicalCircleDirectionalCoordinates]
  simp only [physicalCircle]
  ring

/-- The full physical circle has *identical Cartesian endpoints*.
No separate assumption that a scalar pullback is periodic is needed. -/
theorem physicalCircle_period (r : ℝ) :
    physicalCircle r (2 * Real.pi) = physicalCircle r 0 := by
  ext <;> simp [physicalCircle, Real.sin_two_pi, Real.cos_two_pi]

theorem physicalCircle_periodicEndpoints (n : (ℝ × ℝ) → ℝ) (r : ℝ) :
    n (physicalCircle r (2 * Real.pi)) = n (physicalCircle r 0) := by
  rw [physicalCircle_period r]

/-- For an actually differentiable Cartesian mixed stress along the
circle, the genuine tangential derivative has zero angular integral.
Its interval integrability remains an explicit analytic hypothesis. -/
theorem physicalCircleAngularIntegral_zero
    (n : (ℝ × ℝ) → ℝ)
    (L : ℝ → (ℝ × ℝ) →L[ℝ] ℝ) (r : ℝ)
    (hN : ∀ θ ∈ Set.uIcc (0 : ℝ) (2 * Real.pi),
      HasFDerivAt n (L θ) (physicalCircle r θ))
    (hInt : IntervalIntegrable
      (fun θ : ℝ => L θ (physicalCircleTangent r θ)) volume 0 (2 * Real.pi)) :
    (∫ θ in (0 : ℝ)..(2 * Real.pi),
      L θ (physicalCircleTangent r θ)) = 0 := by
  apply angularDerivativeIntegral_zero
    (fun θ => n (physicalCircle r θ))
    (fun θ => L θ (physicalCircleTangent r θ))
  · intro θ hθ
    exact physicalCirclePullback_hasDerivAt n (L θ) r θ (hN θ hθ)
  · exact hInt
  · exact physicalCircle_periodicEndpoints n r

/-- The actual physical-circle angular stress derivative disappears
from the full azimuthal source mean. The remaining source `A` can
include the radial mixed stress and the full axial pressure trace. -/
theorem physicalCircleMean_derivative_vanishes
    (A : ℝ → ℝ) (n : (ℝ × ℝ) → ℝ)
    (L : ℝ → (ℝ × ℝ) →L[ℝ] ℝ) (r : ℝ) (hr : 0 < r)
    (hA : IntervalIntegrable A volume 0 (2 * Real.pi))
    (hN : ∀ θ ∈ Set.uIcc (0 : ℝ) (2 * Real.pi),
      HasFDerivAt n (L θ) (physicalCircle r θ))
    (hInt : IntervalIntegrable
      (fun θ : ℝ => L θ (physicalCircleTangent r θ)) volume 0 (2 * Real.pi)) :
    azimuthalMean (fun θ => A θ +
        (1 / r) * L θ (physicalCircleTangent r θ)) = azimuthalMean A := by
  apply angularMean_derivative_vanishes A
    (fun θ => n (physicalCircle r θ))
    (fun θ => L θ (physicalCircleTangent r θ)) r hr hA hInt
  · intro θ hθ
    exact physicalCirclePullback_hasDerivAt n (L θ) r θ (hN θ hθ)
  · exact physicalCircle_periodicEndpoints n r

end UnforcedPatching
