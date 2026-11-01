import UnforcedPatching.AngularMean
import Mathlib.Tactic

/-!
# Exact Cartesian axial divergence with nonaxisymmetric mixed stresses

At a fixed axial height, write `m(x,y)=K_rz` and `n(x,y)=K_θz` in the
physical orthonormal cylindrical frame. Without assuming axisymmetry,
the Cartesian axial column is

  `K_xz=(x*m-y*n)/r`, `K_yz=(y*m+x*n)/r`, `r=sqrt(x²+y²)`.

Its genuine Cartesian partial derivatives satisfy

  `∂x K_xz+∂y K_yz = (x*m_x+y*m_y)/r + m/r + (-y*n_x+x*n_y)/r`.

The last term is the local angular directional derivative `∂θ n / r`.
It **does not vanish pointwise**. A separate result in `AngularMean`
proves its integrated cancellation for periodic angular profiles.

The source's independent axial `K_zz+p` derivative is retained.
No globally chosen polar angle, rotating H8 frame, pressure boundary
cancellation or source authentication is assumed here.
-/

noncomputable section

namespace UnforcedPatching

abbrev CartesianMeridionalField := ℝ → ℝ → ℝ

/-- Actual Cartesian `xz` stress component for general angular variation. -/
def cartesianGeneralMixedX (m n : CartesianMeridionalField) (x y : ℝ) : ℝ :=
  x * (m x y / cartesianRadius x y) - y * (n x y / cartesianRadius x y)

/-- Actual Cartesian `yz` stress component for general angular variation. -/
def cartesianGeneralMixedY (m n : CartesianMeridionalField) (x y : ℝ) : ℝ :=
  y * (m x y / cartesianRadius x y) + x * (n x y / cartesianRadius x y)

def cartesianGeneralAxialDiv (m n : CartesianMeridionalField) (x y : ℝ) : ℝ :=
  deriv (fun t : ℝ => cartesianGeneralMixedX m n t y) x +
    deriv (fun t : ℝ => cartesianGeneralMixedY m n x t) y

/-- A source-native, nonaxisymmetric pointwise identity derived from
Cartesian derivatives. The third term is the full angular contribution. -/
theorem cartesianGeneralAxialDivergence
    (m n : CartesianMeridionalField) (x y mx my nx ny : ℝ)
    (hxy : 0 < x ^ 2 + y ^ 2)
    (hmx : HasDerivAt (fun t : ℝ => m t y) mx x)
    (hmy : HasDerivAt (fun t : ℝ => m x t) my y)
    (hnx : HasDerivAt (fun t : ℝ => n t y) nx x)
    (hny : HasDerivAt (fun t : ℝ => n x t) ny y) :
    cartesianGeneralAxialDiv m n x y =
      (x * mx + y * my) / cartesianRadius x y +
        m x y / cartesianRadius x y +
        (-y * nx + x * ny) / cartesianRadius x y := by
  let r := cartesianRadius x y
  have hr : r ≠ 0 := ne_of_gt (cartesianRadius_pos x y hxy)
  have hrsq : r ^ 2 = x ^ 2 + y ^ 2 := cartesianRadius_sq x y
  have hx := cartesianRadius_hasDerivAt_x x y hxy
  have hy := cartesianRadius_hasDerivAt_y x y hxy
  have hMx := hmx.div hx hr
  have hNx := hnx.div hx hr
  have hMy := hmy.div hy hr
  have hNy := hny.div hy hr
  have hDx : deriv (fun t : ℝ => cartesianGeneralMixedX m n t y) x =
      m x y / r + x * ((mx * r - m x y * (x / r)) / r ^ 2) -
        y * ((nx * r - n x y * (x / r)) / r ^ 2) := by
    have h := ((hasDerivAt_id x).mul hMx).sub (hNx.const_mul y)
    have hFun :
        (id * ((fun t : ℝ => m t y) / (fun t : ℝ => cartesianRadius t y)) -
          fun t : ℝ => y * (((fun t : ℝ => n t y) /
            (fun t : ℝ => cartesianRadius t y)) t)) =
          (fun t : ℝ => cartesianGeneralMixedX m n t y) := by
      funext t
      simp [cartesianGeneralMixedX, Pi.div_apply]
    rw [hFun] at h
    simpa [r] using h.deriv
  have hDy : deriv (fun t : ℝ => cartesianGeneralMixedY m n x t) y =
      m x y / r + y * ((my * r - m x y * (y / r)) / r ^ 2) +
        x * ((ny * r - n x y * (y / r)) / r ^ 2) := by
    have h := ((hasDerivAt_id y).mul hMy).add (hNy.const_mul x)
    have hFun :
        (id * ((fun t : ℝ => m x t) / (fun t : ℝ => cartesianRadius x t)) +
          fun t : ℝ => x * (((fun t : ℝ => n x t) /
            (fun t : ℝ => cartesianRadius x t)) t)) =
          (fun t : ℝ => cartesianGeneralMixedY m n x t) := by
      funext t
      simp [cartesianGeneralMixedY, Pi.div_apply]
    rw [hFun] at h
    simpa [r] using h.deriv
  unfold cartesianGeneralAxialDiv
  rw [hDx, hDy]
  change _ = (x * mx + y * my) / r + m x y / r +
    (-y * nx + x * ny) / r
  calc
    _ = 2 * (m x y / r) +
        (x * mx + y * my - y * nx + x * ny) / r -
        (x ^ 2 + y ^ 2) * m x y / r ^ 3 := by
      field_simp [hr]
      ring
    _ = m x y / r +
        (x * mx + y * my - y * nx + x * ny) / r := by
      rw [← hrsq]
      field_simp [hr]
      ring
    _ = (x * mx + y * my) / r + m x y / r +
          (-y * nx + x * ny) / r := by ring

/-- The complete axial source retains an independently differentiated
pressure/tensor representative `C(x,y,z) = K_zz+p`. -/
def cartesianGeneralAxialPressureSource (m n : CartesianMeridionalField)
    (C : ℝ → ℝ → ℝ → ℝ) (x y z : ℝ) : ℝ :=
  cartesianGeneralAxialDiv m n x y + deriv (fun t : ℝ => C x y t) z

theorem cartesianGeneralAxialPressureBalance
    (m n : CartesianMeridionalField) (C : ℝ → ℝ → ℝ → ℝ)
    (x y z mx my nx ny cZ : ℝ)
    (hxy : 0 < x ^ 2 + y ^ 2)
    (hmx : HasDerivAt (fun t : ℝ => m t y) mx x)
    (hmy : HasDerivAt (fun t : ℝ => m x t) my y)
    (hnx : HasDerivAt (fun t : ℝ => n t y) nx x)
    (hny : HasDerivAt (fun t : ℝ => n x t) ny y)
    (hC : HasDerivAt (fun t : ℝ => C x y t) cZ z) :
    cartesianGeneralAxialPressureSource m n C x y z =
      (x * mx + y * my) / cartesianRadius x y +
        m x y / cartesianRadius x y +
        (-y * nx + x * ny) / cartesianRadius x y + cZ := by
  simp only [cartesianGeneralAxialPressureSource, hC.deriv]
  rw [cartesianGeneralAxialDivergence m n x y mx my nx ny hxy hmx hmy hnx hny]

/-- A nonzero local angular derivative: `m=0, n(x,y)=x` at `(3,4)`
produces an axial Cartesian divergence `-4/5`, not zero. -/
theorem cartesianNonzeroAngularGradientExample :
    cartesianGeneralAxialDiv (fun _ _ => (0 : ℝ)) (fun x _ => x) 3 4 =
      -(4 / 5 : ℝ) := by
  have hMx : HasDerivAt (fun t : ℝ => (0 : ℝ)) 0 3 :=
    hasDerivAt_const 3 (0 : ℝ)
  have hMy : HasDerivAt (fun t : ℝ => (0 : ℝ)) 0 4 :=
    hasDerivAt_const 4 (0 : ℝ)
  have hNx : HasDerivAt (fun t : ℝ => t) 1 3 := hasDerivAt_id 3
  have hNy : HasDerivAt (fun t : ℝ => (3 : ℝ)) 0 4 :=
    hasDerivAt_const 4 (3 : ℝ)
  have h := cartesianGeneralAxialDivergence
    (fun _ _ => (0 : ℝ)) (fun x _ => x) 3 4 0 0 1 0
    (by norm_num) (by simpa using hMx) (by simpa using hMy)
    (by simpa using hNx) (by simpa using hNy)
  norm_num [cartesianRadius] at h ⊢
  exact h

end UnforcedPatching
