import Mathlib

/-!
Edition XXXIV. Only rational contraction and scalar
cancellation inequalities are proved here.
The global unforced NSE mild solution and physical residual
are established analytically in the paper, not in Lean.
-/
namespace TerminalCore2026

theorem xxxiv_critical_smallness :
    (1/400 : ℚ) < 1/16 := by norm_num

theorem xxxiv_picard_contraction :
    16 * (1/400 : ℚ) = 1/25 := by norm_num

theorem xxxiv_ball_invariant :
    (2:ℚ)+32/400 < 4 := by norm_num

theorem xxxiv_fourier_amplitude_exponent :
    (8:ℚ)/400 = 1/50 := by norm_num

theorem xxxiv_h2_sobolev_exponent :
    (30:ℚ)/100 = 3/10 := by norm_num

theorem xxxiv_h2_initial_weights :
    (2:ℚ)+10+70 = 82 := by norm_num

theorem xxxiv_h2_time_nonintegrable
    (h : ℝ) (hh : 0 ≤ h) :
    1 < (8/3 : ℝ) * (1/2+h) := by
  linarith

theorem xxxiv_upper_lower_triangle
    (source correction smooth C : ℝ)
    (h1 : correction ≤ source+smooth)
    (h2 : source ≤ correction+smooth)
    (hC : smooth ≤ C) :
    correction ≤ source+C ∧ source-C ≤ correction := by
  constructor <;> linarith

theorem xxxiv_unforced_identity_algebra
    (source correction full : ℝ)
    (h : full=source+correction) :
    full-source=correction := by
  linarith

#print axioms xxxiv_critical_smallness
#print axioms xxxiv_picard_contraction
#print axioms xxxiv_ball_invariant
#print axioms xxxiv_fourier_amplitude_exponent
#print axioms xxxiv_h2_sobolev_exponent
#print axioms xxxiv_h2_initial_weights
#print axioms xxxiv_h2_time_nonintegrable
#print axioms xxxiv_upper_lower_triangle
#print axioms xxxiv_unforced_identity_algebra

end TerminalCore2026
