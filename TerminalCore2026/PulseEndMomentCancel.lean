import Mathlib

/-!
Finite exact algebra gates for source Appendix-A.9 translated axial
moment corrections. The source integrals and unforced Navier--Stokes
PDE are not formalized in this file.
-/
namespace TerminalCore2026

private def det2 (a b c d : ℝ) : ℝ := a*d-b*c

theorem pulse_end_first_cancel (a b c d u v : ℝ)
    (hd : det2 a b c d ≠ 0) :
    a*((-d*u+b*v)/(det2 a b c d)) +
      b*((c*u-a*v)/(det2 a b c d)) + u = 0 := by
  dsimp [det2] at hd ⊢
  field_simp [hd]
  ring

theorem pulse_end_second_cancel (a b c d u v : ℝ)
    (hd : det2 a b c d ≠ 0) :
    c*((-d*u+b*v)/(det2 a b c d)) +
      d*((c*u-a*v)/(det2 a b c d)) + v = 0 := by
  dsimp [det2] at hd ⊢
  field_simp [hd]
  ring

theorem pulse_end_first_jet_cancel (a b c d uη vη : ℝ)
    (hd : det2 a b c d ≠ 0) :
    a*((-d*uη+b*vη)/(det2 a b c d)) +
      b*((c*uη-a*vη)/(det2 a b c d)) + uη = 0 := by
  exact pulse_end_first_cancel a b c d uη vη hd

theorem pulse_end_second_jet_cancel (a b c d uη vη : ℝ)
    (hd : det2 a b c d ≠ 0) :
    c*((-d*uη+b*vη)/(det2 a b c d)) +
      d*((c*uη-a*vη)/(det2 a b c d)) + vη = 0 := by
  exact pulse_end_second_cancel a b c d uη vη hd

theorem pulse_end_det_negative (kα kβ p q : ℝ)
    (hα : 0 < kα) (hβ : 0 < kβ) (hp : q < p) :
    kα*kβ*(q-p) < 0 := by
  exact mul_neg_of_pos_of_neg (mul_pos hα hβ) (sub_neg.mpr hp)

theorem pulse_end_Q_rational_constant :
    (202:ℚ)*24*(20/247)^4 = 775680000/3722098081 := by
  norm_num

theorem pulse_end_Q_error_small :
    (775680000/3722098081:ℚ)*(1/20)^3 < 1/1000 := by
  norm_num

theorem pulse_end_Q_bracket :
    (3/2:ℚ)*(100+20/19)+50 < 202 := by
  norm_num

theorem pulse_end_Q_positive_margin :
    (99/100:ℚ)-1/1000 > 1/2 := by
  norm_num

#print axioms pulse_end_first_cancel
#print axioms pulse_end_second_cancel
#print axioms pulse_end_first_jet_cancel
#print axioms pulse_end_second_jet_cancel
#print axioms pulse_end_det_negative
#print axioms pulse_end_Q_error_small

end TerminalCore2026