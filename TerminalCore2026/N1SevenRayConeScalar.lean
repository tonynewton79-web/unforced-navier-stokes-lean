import Mathlib
/-!
Edition XXV: scalar algebra for exact seven-ray tensor components,
a carrier and pressure gauge. No physical source, Navier--Stokes
equations, analytic estimates or singularity are formalized here.
-/
namespace TerminalCore2026

def xxvC2 (r l c : ℝ) : ℝ := 1+4*l*r^2*c^2
def xxvC3 (r l c : ℝ) : ℝ := 3-4*l*r^2*c^2
def xxvC4 (r l s c : ℝ) : ℝ :=
  2+16*s^2+16*l^2*(r^2*s^2-r^4*c^2)+16*l*r*c*s
def xxvC5 (r l s c : ℝ) : ℝ :=
  2+16*s^2+16*l^2*(r^2*s^2-r^4*c^2)-16*l*r*c*s
def xxvC6 (r l s c : ℝ) : ℝ := 1-16*l*r*c*s
def xxvC7 (r l s c : ℝ) : ℝ := 1+16*l*r*c*s
def xxvPi (r l c : ℝ) : ℝ := 3/8-2*c^2*(1+l^2*r^4)
def xxvCarrier (r l s c : ℝ) : ℝ :=
  85/8+32*s^2+32*l^2*r^2*s^2-30*l^2*r^4*c^2

theorem xxv_rr (r l s c : ℝ) :
    (1:ℝ)+xxvC2 r l c+xxvC3 r l c+
      xxvC4 r l s c+xxvC5 r l s c+
      xxvC6 r l s c+xxvC7 r l s c =
    2*c^2+xxvCarrier r l s c+xxvPi r l c := by
  unfold xxvC2 xxvC3 xxvC4 xxvC5 xxvC6 xxvC7 xxvCarrier xxvPi
  ring

theorem xxv_tt (r l s c : ℝ) :
    (xxvC2 r l c+xxvC3 r l c+xxvC6 r l s c+xxvC7 r l s c)/16 =
    2*c^2*(1+l^2*r^4)+xxvPi r l c := by
  unfold xxvC2 xxvC3 xxvC6 xxvC7 xxvPi
  ring

theorem xxv_zz (r l s c : ℝ) :
    (xxvC4 r l s c+xxvC5 r l s c+xxvC6 r l s c+xxvC7 r l s c)/16 =
    2*(1+l^2*r^2*s^2)+xxvPi r l c := by
  unfold xxvC4 xxvC5 xxvC6 xxvC7 xxvPi
  ring

theorem xxv_rt (r l s c : ℝ) :
    (xxvC2 r l c-xxvC3 r l c+xxvC6 r l s c+xxvC7 r l s c)/4 =
    2*l*r^2*c^2 := by
  unfold xxvC2 xxvC3 xxvC6 xxvC7
  ring

theorem xxv_rz (r l s c : ℝ) :
    (xxvC4 r l s c-xxvC5 r l s c+xxvC6 r l s c-xxvC7 r l s c)/4 = 0 := by
  unfold xxvC4 xxvC5 xxvC6 xxvC7
  ring

theorem xxv_tz (r l s c : ℝ) :
    (xxvC6 r l s c-xxvC7 r l s c)/16 = -2*l*r*c*s := by
  unfold xxvC6 xxvC7
  ring

theorem xxv_unaugmented_gap (r l c : ℝ) :
    2*c^2-2*c^2*(1+l^2*r^4) = -2*l^2*r^4*c^2 := by
  ring

theorem xxv_ray_floor_gap (mu d1 d2 d3 d4 d5 d6 d7 : ℝ)
    (h1 : mu ≤ d1) (h2 : mu ≤ d2) (h3 : mu ≤ d3)
    (h4 : mu ≤ d4) (h5 : mu ≤ d5)
    (h6 : mu ≤ d6) (h7 : mu ≤ d7) :
    (105/16 : ℝ)*mu ≤
      d1+d2+d3+d4+d5+d6+d7-(d2+d3+d6+d7)/16 := by
  linarith

theorem xxv_rational_floor :
    (1-16*(1/16 : ℚ)*(5/4)*(1/2)) = 3/8 := by norm_num
theorem xxv_rational_c4_floor :
    (2-625/4096-5/8 : ℚ) = 5007/4096 := by norm_num
theorem xxv_carrier_positive_rational :
    (0 : ℚ) < 85/8-30*(1/256)*(625/256) := by norm_num

#print axioms xxv_rr
#print axioms xxv_tt
#print axioms xxv_zz
#print axioms xxv_rt
#print axioms xxv_rz
#print axioms xxv_tz
#print axioms xxv_ray_floor_gap
end TerminalCore2026
