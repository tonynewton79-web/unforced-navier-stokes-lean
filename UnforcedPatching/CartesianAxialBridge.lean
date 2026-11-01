import UnforcedPatching.PressureCompensatedFlux
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic

/-!
# Cartesian-to-cylindrical axial divergence for axisymmetric stress

Fix a height `z` and write `r = sqrt (x²+y²)`. For radial mixed-stress
components `M = K_rz` and `N = K_θz`, the *physical Cartesian* axial
column has entries

  `K_xz = x M(r)/r - y N(r)/r`,
  `K_yz = y M(r)/r + x N(r)/r`.

Both Cartesian partial derivatives are taken below, and the `N` terms
cancel because of axisymmetry. The separate `C(z) = K_zz + p` derivative
is retained, rather than assigning the pressure trace zero.

This does not cover nonaxisymmetric fields, rotating H8 frames,
two-dimensional source integration, or authentic Case 006 profiles.
-/

noncomputable section

namespace UnforcedPatching

/-- Cylindrical radial coordinate away from the symmetry axis. -/
def cartesianRadius (x y : ℝ) : ℝ := Real.sqrt (x ^ 2 + y ^ 2)

/-- Cartesian `xz` component of the axial stress column at fixed `z`. -/
def cartesianAxialMixedX (M N : ℝ → ℝ) (x y : ℝ) : ℝ :=
  x * (M (cartesianRadius x y) / cartesianRadius x y) -
    y * (N (cartesianRadius x y) / cartesianRadius x y)

/-- Cartesian `yz` component of the axial stress column at fixed `z`. -/
def cartesianAxialMixedY (M N : ℝ → ℝ) (x y : ℝ) : ℝ :=
  y * (M (cartesianRadius x y) / cartesianRadius x y) +
    x * (N (cartesianRadius x y) / cartesianRadius x y)

/-- The genuine Cartesian axial mixed-stress divergence, with `y`
held fixed for `∂x` and `x` held fixed for `∂y`. -/
def cartesianAxialMixedDiv (M N : ℝ → ℝ) (x y : ℝ) : ℝ :=
  deriv (fun t : ℝ => cartesianAxialMixedX M N t y) x +
    deriv (fun t : ℝ => cartesianAxialMixedY M N x t) y

theorem cartesianRadius_sq (x y : ℝ) :
    cartesianRadius x y ^ 2 = x ^ 2 + y ^ 2 := by
  unfold cartesianRadius
  exact Real.sq_sqrt (add_nonneg (sq_nonneg x) (sq_nonneg y))

theorem cartesianRadius_pos (x y : ℝ)
    (hxy : 0 < x ^ 2 + y ^ 2) : 0 < cartesianRadius x y := by
  exact Real.sqrt_pos.2 hxy

theorem cartesianRadius_hasDerivAt_x (x y : ℝ)
    (hxy : 0 < x ^ 2 + y ^ 2) :
    HasDerivAt (fun t : ℝ => cartesianRadius t y)
      (x / cartesianRadius x y) x := by
  have hr : cartesianRadius x y ≠ 0 := ne_of_gt (cartesianRadius_pos x y hxy)
  have hinside : HasDerivAt (fun t : ℝ => t ^ 2 + y ^ 2) (2 * x) x := by
    simpa using (hasDerivAt_pow 2 x).add_const (y ^ 2)
  have hcomp := (Real.hasDerivAt_sqrt (ne_of_gt hxy)).comp x hinside
  have h : HasDerivAt (fun t : ℝ => cartesianRadius t y)
      ((1 / (2 * cartesianRadius x y)) * (2 * x)) x := by
    simpa [cartesianRadius, Function.comp_def] using hcomp
  convert h using 1
  field_simp [hr]

theorem cartesianRadius_hasDerivAt_y (x y : ℝ)
    (hxy : 0 < x ^ 2 + y ^ 2) :
    HasDerivAt (fun t : ℝ => cartesianRadius x t)
      (y / cartesianRadius x y) y := by
  have hr : cartesianRadius x y ≠ 0 := ne_of_gt (cartesianRadius_pos x y hxy)
  have hinside : HasDerivAt (fun t : ℝ => x ^ 2 + t ^ 2) (2 * y) y := by
    simpa using (hasDerivAt_pow 2 y).const_add (x ^ 2)
  have hcomp := (Real.hasDerivAt_sqrt (ne_of_gt hxy)).comp y hinside
  have h : HasDerivAt (fun t : ℝ => cartesianRadius x t)
      ((1 / (2 * cartesianRadius x y)) * (2 * y)) y := by
    simpa [cartesianRadius, Function.comp_def] using hcomp
  convert h using 1
  field_simp [hr]

/-- The actual Cartesian partial derivatives of the mixed stress give
the radial cylindrical axial divergence, including its geometric `M/r`
term, even if the **azimuthal mixed stress** `N` is nonzero. -/
theorem cartesianAxisymmetricAxialDivergence
    (M N : ℝ → ℝ) (x y dM dN : ℝ)
    (hxy : 0 < x ^ 2 + y ^ 2)
    (hM : HasDerivAt M dM (cartesianRadius x y))
    (hN : HasDerivAt N dN (cartesianRadius x y)) :
    cartesianAxialMixedDiv M N x y =
      dM + M (cartesianRadius x y) / cartesianRadius x y := by
  let r := cartesianRadius x y
  have hr : r ≠ 0 := ne_of_gt (cartesianRadius_pos x y hxy)
  have hrsq : r ^ 2 = x ^ 2 + y ^ 2 := cartesianRadius_sq x y
  have hU := hM.div (hasDerivAt_id r) hr
  have hV := hN.div (hasDerivAt_id r) hr
  have hx := cartesianRadius_hasDerivAt_x x y hxy
  have hy := cartesianRadius_hasDerivAt_y x y hxy
  have hUx := hU.comp x hx
  have hVx := hV.comp x hx
  have hUy := hU.comp y hy
  have hVy := hV.comp y hy
  have hDx : deriv (fun t : ℝ => cartesianAxialMixedX M N t y) x =
      M r / r + x * (((dM * r - M r) / r ^ 2) * (x / r)) -
        y * (((dN * r - N r) / r ^ 2) * (x / r)) := by
    have h := ((hasDerivAt_id x).mul hUx).sub (hVx.const_mul y)
    have hfun : (id * ((M / id) ∘ (fun t : ℝ => cartesianRadius t y)) -
        fun t : ℝ => y * ((N / id) ∘ (fun t : ℝ => cartesianRadius t y)) t) =
        (fun t : ℝ => cartesianAxialMixedX M N t y) := by
      funext t
      simp [cartesianAxialMixedX, Pi.div_apply]
    rw [hfun] at h
    simpa [r] using h.deriv
  have hDy : deriv (fun t : ℝ => cartesianAxialMixedY M N x t) y =
      M r / r + y * (((dM * r - M r) / r ^ 2) * (y / r)) +
        x * (((dN * r - N r) / r ^ 2) * (y / r)) := by
    have h := ((hasDerivAt_id y).mul hUy).add (hVy.const_mul x)
    have hfun : (id * ((M / id) ∘ (fun t : ℝ => cartesianRadius x t)) +
        fun t : ℝ => x * ((N / id) ∘ (fun t : ℝ => cartesianRadius x t)) t) =
        (fun t : ℝ => cartesianAxialMixedY M N x t) := by
      funext t
      simp [cartesianAxialMixedY, Pi.div_apply]
    rw [hfun] at h
    simpa [r] using h.deriv
  unfold cartesianAxialMixedDiv
  rw [hDx, hDy]
  change _ = dM + M r / r
  calc
    _ = 2 * (M r / r) + (x ^ 2 + y ^ 2) / r *
          ((dM * r - M r) / r ^ 2) := by ring
    _ = 2 * (M r / r) + r * ((dM * r - M r) / r ^ 2) := by
      rw [← hrsq]
      field_simp [hr]
    _ = dM + M r / r := by
      field_simp [hr]
      ring

/-- The Cartesian axial source with the entire axial `K_zz+p` trace
kept as an independent differentiable scalar. -/
def cartesianAxialPressureSource (M N C : ℝ → ℝ) (x y z : ℝ) : ℝ :=
  cartesianAxialMixedDiv M N x y + deriv C z

theorem cartesianAxialPressureBalance
    (M N C : ℝ → ℝ) (x y z dM dN dC : ℝ)
    (hxy : 0 < x ^ 2 + y ^ 2)
    (hM : HasDerivAt M dM (cartesianRadius x y))
    (hN : HasDerivAt N dN (cartesianRadius x y))
    (hC : HasDerivAt C dC z) :
    cartesianAxialPressureSource M N C x y z =
      dM + M (cartesianRadius x y) / cartesianRadius x y + dC := by
  simp only [cartesianAxialPressureSource, hC.deriv]
  rw [cartesianAxisymmetricAxialDivergence M N x y dM dN hxy hM hN]

/-- An exact nonzero tangential-stress example at `(x,y)=(3,4)`.
The swirl `N(r)=7r` does not contaminate the axisymmetric axial source. -/
theorem cartesianAxisymmetricNonzeroSwirlExample :
    cartesianAxialMixedDiv (fun r : ℝ => r ^ 2) (fun r : ℝ => 7 * r) 3 4 = 15 := by
  have hM : HasDerivAt (fun r : ℝ => r ^ 2) 10 5 := by
    have h := hasDerivAt_pow 2 (5 : ℝ)
    norm_num at h
    exact h
  have hN : HasDerivAt (fun r : ℝ => 7 * r) 7 5 := by
    simpa using (hasDerivAt_id (5 : ℝ)).const_mul 7
  have hr : cartesianRadius 3 4 = 5 := by
    norm_num [cartesianRadius]
  have h := cartesianAxisymmetricAxialDivergence
    (fun r : ℝ => r ^ 2) (fun r : ℝ => 7 * r) 3 4 10 7 (by norm_num) (by
      simpa only [hr] using hM) (by
      simpa only [hr] using hN)
  norm_num [hr] at h ⊢
  exact h

end UnforcedPatching
