import Mathlib

/-!
Edition XII: finite scalar startup implications only. No formalization
of the pressure-free test field, the physical NSE, source residual,
parabolic time derivative or the global blow-up theorem.
-/
namespace TerminalCore2026

theorem correction_initial_jet_nonflat (B jet : ℝ)
    (hB : 0 < B) (hjet : jet + B = 0) :
    jet < 0 := by
  linarith

theorem correction_cannot_be_time_flat (B jet : ℝ)
    (hB : 0 < B) (hjet : jet + B = 0) :
    jet ≠ 0 := by
  have hlt : jet < 0 := by linarith
  exact ne_of_lt hlt

theorem correction_near_start_lower
    (B testNorm dt velocityNorm : ℝ)
    (hB : 0 < B) (hNorm : 0 < testNorm)
    (ht : 0 < dt)
    (hdual : B * dt / 2 ≤ velocityNorm * testNorm) :
    0 < velocityNorm := by
  have hpos : 0 < B * dt / 2 := by positivity
  by_contra h
  have hv : velocityNorm ≤ 0 := le_of_not_gt h
  have hprod : velocityNorm * testNorm ≤ 0 :=
    mul_nonpos_of_nonpos_of_nonneg hv (le_of_lt hNorm)
  linarith

theorem exact_rational_witness_mass :
    (1 / 430080 : ℚ) * (1 / 630) = 1 / 270950400 := by
  norm_num

theorem local_positive_not_global_positive
    (a b : ℝ) (ha : 0 < a) (hb : b = -a) :
    a + b = 0 := by
  linarith

#print axioms correction_initial_jet_nonflat
#print axioms correction_cannot_be_time_flat
#print axioms correction_near_start_lower
#print axioms exact_rational_witness_mass
#print axioms local_positive_not_global_positive
end TerminalCore2026
