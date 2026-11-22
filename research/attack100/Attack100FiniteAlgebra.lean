import Mathlib

/-!
Attack100: finite algebra ONLY, with no analytic no-go theorem
formalized in Lean. The mathematical continuum boundary-layer duality
proof appears separately. No new Navier--Stokes singularity claim.
-/
namespace UnforcedPatching.Attack100

theorem angular_source_leading_cancellation
    (c cp h hx p : ℝ) :
    cp*h^2 + 2*c*h*hx + 2*p*c*h^2
       - 2*c*h*(p*h+hx) = cp*h^2 := by
  ring

theorem gram_endpoint_strict_difference (L0 L2 : ℝ) :
    ((25:ℝ)/4*L0+(9:ℝ)/16*L2)
      - ((9:ℝ)/4*L0+(1:ℝ)/16*L2)
      = 4*L0+L2/2 := by
  ring

theorem source_h_at_upper_axial_edge (x : ℝ) :
    (2+x/2) - (1+x/2)/2 = 3/2+x/4 := by
  ring

theorem source_h_lower (x : ℝ) (hx : -1 < x) :
    (5:ℝ)/4 < 3/2+x/4 := by
  linarith

theorem original_angular_cap_positive :
    (0:ℚ) < ((15971:ℚ)/122900+(22371:ℚ)/122900)/2 := by
  norm_num

theorem original_angular_cap_exact :
    ((15971:ℚ)/122900+(22371:ℚ)/122900)/2
      = 19171/122900 := by
  norm_num

theorem vanishing_double_pole_affine
    (n0 n1 : ℝ)
    (hp : n0+n1=0)
    (hm : n0-n1=0) :
    n0=0 ∧ n1=0 := by
  constructor <;> linarith

theorem torque_affine_remaining
    (m0 m1 : ℝ)
    (h0 : m0=0)
    (h1 : m0+m1=0) :
    m1=0 := by
  linarith

#print axioms angular_source_leading_cancellation
#print axioms gram_endpoint_strict_difference
#print axioms source_h_at_upper_axial_edge
#print axioms source_h_lower
#print axioms original_angular_cap_positive
#print axioms original_angular_cap_exact
#print axioms vanishing_double_pole_affine
#print axioms torque_affine_remaining

end UnforcedPatching.Attack100
