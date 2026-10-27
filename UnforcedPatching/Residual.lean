import UnforcedPatching.Definitions
import Mathlib.Analysis.Calculus.FDeriv.Add

/-!
# Algebra of the physical Navier--Stokes residual

The identities in this file are about the full viscosity-one physical
operator defined upstream, not an abstract fixed-point surrogate.
Differentiability hypotheses are explicit: Fréchet derivatives do not obey
an unrestricted addition identity at nondifferentiable functions.
-/

noncomputable section

namespace UnforcedPatching

open NavierStokes.ProblemStatement

/-- Hypotheses sufficient to linearize time derivatives, spatial first and
second derivatives, and the pressure gradient at a physical spacetime point.
Global spatial first differentiability ensures that the identity for the
first derivative can itself be differentiated at the selected point. -/
structure ResidualRegularAt (u : VelocityField) (p : PressureField)
    (t : ℝ) (x : Space) : Prop where
  time : DifferentiableAt ℝ (fun s : ℝ => u (s, x)) t
  space : ∀ y : Space, DifferentiableAt ℝ (fun z : Space => u (t, z)) y
  second : ∀ i : Fin 3,
    DifferentiableAt ℝ
      (fun y : Space => spatialDerivative u t y (coordinateVector i)) x
  pressure : DifferentiableAt ℝ (fun y : Space => p (t, y)) x

theorem temporalDerivative_add (u v : VelocityField) (t : ℝ) (x : Space)
    (hu : DifferentiableAt ℝ (fun s : ℝ => u (s, x)) t)
    (hv : DifferentiableAt ℝ (fun s : ℝ => v (s, x)) t) :
    temporalDerivative (u + v) t x =
      temporalDerivative u t x + temporalDerivative v t x := by
  change (fderiv ℝ (fun s : ℝ => u (s, x) + v (s, x)) t) 1 = _
  have hf : (fun s : ℝ => u (s, x) + v (s, x)) =
      (fun s : ℝ => u (s, x)) + (fun s : ℝ => v (s, x)) := rfl
  rw [hf, fderiv_add hu hv, add_apply]
  rfl

theorem spatialDerivative_add (u v : VelocityField) (t : ℝ) (x : Space)
    (hu : DifferentiableAt ℝ (fun y : Space => u (t, y)) x)
    (hv : DifferentiableAt ℝ (fun y : Space => v (t, y)) x) :
    spatialDerivative (u + v) t x =
      spatialDerivative u t x + spatialDerivative v t x := by
  change fderiv ℝ (fun y : Space => u (t, y) + v (t, y)) x = _
  have hf : (fun y : Space => u (t, y) + v (t, y)) =
      (fun y : Space => u (t, y)) + (fun y : Space => v (t, y)) := rfl
  rw [hf, fderiv_add hu hv]
  rfl

theorem spatialLaplacian_add (u v : VelocityField) (t : ℝ) (x : Space)
    (hu : ∀ y : Space, DifferentiableAt ℝ (fun z : Space => u (t, z)) y)
    (hv : ∀ y : Space, DifferentiableAt ℝ (fun z : Space => v (t, z)) y)
    (hu₂ : ∀ i : Fin 3, DifferentiableAt ℝ
      (fun y : Space => spatialDerivative u t y (coordinateVector i)) x)
    (hv₂ : ∀ i : Fin 3, DifferentiableAt ℝ
      (fun y : Space => spatialDerivative v t y (coordinateVector i)) x) :
    spatialLaplacian (u + v) t x =
      spatialLaplacian u t x + spatialLaplacian v t x := by
  unfold spatialLaplacian
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i _
  have hf : (fun y : Space => spatialDerivative (u + v) t y (coordinateVector i)) =
      (fun y : Space => spatialDerivative u t y (coordinateVector i) +
        spatialDerivative v t y (coordinateVector i)) := by
    funext y
    rw [spatialDerivative_add u v t y (hu y) (hv y), add_apply]
  have hsum :
      (fun y : Space => spatialDerivative u t y (coordinateVector i) +
        spatialDerivative v t y (coordinateVector i)) =
      (fun y : Space => spatialDerivative u t y (coordinateVector i)) +
        (fun y : Space => spatialDerivative v t y (coordinateVector i)) := rfl
  rw [hf, hsum, fderiv_add (hu₂ i) (hv₂ i), add_apply]

theorem pressureGradient_add (p q : PressureField) (t : ℝ) (x : Space)
    (hp : DifferentiableAt ℝ (fun y : Space => p (t, y)) x)
    (hq : DifferentiableAt ℝ (fun y : Space => q (t, y)) x) :
    pressureGradient (p + q) t x =
      pressureGradient p t x + pressureGradient q t x := by
  unfold pressureGradient
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i _
  have hsum : (fun y : Space => p (t, y) + q (t, y)) =
      (fun y : Space => p (t, y)) + (fun y : Space => q (t, y)) := rfl
  change (fderiv ℝ (fun y : Space => p (t, y) + q (t, y)) x)
      (coordinateVector i) • coordinateVector i = _
  rw [hsum, fderiv_add hp hq, add_apply, add_smul]

/-- Correct velocity addition includes both transport cross terms; the
physical viscosity and pressure pieces are linear under the regularity
hypotheses. No forcing or formal assertion of a singular solution appears. -/
theorem navierStokesResidual_add (u v : VelocityField) (p q : PressureField)
    (t : ℝ) (x : Space)
    (hu : ResidualRegularAt u p t x)
    (hv : ResidualRegularAt v q t x) :
    navierStokesResidual (u + v) (p + q) t x =
      navierStokesResidual u p t x + navierStokesResidual v q t x +
        spatialDerivative u t x (v (t, x)) +
        spatialDerivative v t x (u (t, x)) := by
  rw [navierStokesResidual, navierStokesResidual, navierStokesResidual]
  rw [temporalDerivative_add u v t x hu.time hv.time,
    spatialLaplacian_add u v t x hu.space hv.space hu.second hv.second,
    pressureGradient_add p q t x hu.pressure hv.pressure]
  unfold advection
  rw [spatialDerivative_add u v t x (hu.space x) (hv.space x)]
  simp only [Pi.add_apply, add_apply, map_add]
  abel

end UnforcedPatching
