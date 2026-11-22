import Mathlib

/-!
Attack98 finite cone algebra only. The physical source, weighted inverse
and full unforced Navier--Stokes theorem are NOT formalized here.
-/
namespace UnforcedPatching.Attack98

theorem original_flux_alpha :
  -(4443:ℚ)/9832 = -((4443:ℚ)/4916)/2 := by norm_num

theorem one_sided_upper_cap_constant :
  ((15971:ℚ)/122900 + (22371:ℚ)/122900)/2 = 19171/122900 := by norm_num

theorem angular_flux_lower_gap :
  (2597:ℚ)/12290 - 19171/122900 = 6799/122900 := by norm_num

theorem original_absolute_gap :
  (2597:ℚ)/12290 - 15971/245800 = 35969/245800 := by norm_num

theorem flat_envelope_positive_lower : (0:ℚ) < 1229/1079649 := by norm_num

theorem flat_envelope_upper_lt_two : (117984:ℚ)/72569 < 2 := by norm_num

theorem one_sided_C_cap
  (rho a b c d : ℝ)
  (h3 : -2*c-4*d ≥ -((22371:ℝ)/122900)*rho)
  (h4 : 2*a-8*b+4*d ≥ -((15971:ℝ)/122900)*rho)
  (h5 : -2*a+8*b+4*d ≥ -((15971:ℝ)/122900)*rho) :
  c ≤ ((19171:ℝ)/122900)*rho := by
  linarith

theorem source_angular_flux_incompatible
  (R beta C : ℝ)
  (hR : 0 < R)
  (hbeta : -beta > (2597:ℝ)/12290)
  (hsource : C = -beta*R)
  (hcone : C ≤ ((19171:ℝ)/122900)*R) : False := by
  have hgap : 0 < (-beta - ((19171:ℝ)/122900)) := by linarith
  have hmul : 0 < (-beta - ((19171:ℝ)/122900))*R := mul_pos hgap hR
  nlinarith

#print axioms original_flux_alpha
#print axioms one_sided_upper_cap_constant
#print axioms angular_flux_lower_gap
#print axioms original_absolute_gap
#print axioms flat_envelope_positive_lower
#print axioms flat_envelope_upper_lt_two
#print axioms one_sided_C_cap
#print axioms source_angular_flux_incompatible

end UnforcedPatching.Attack98
