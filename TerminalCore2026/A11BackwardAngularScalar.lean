import Mathlib
/-!
Scalar arithmetic gates for the A.11 whole-hull backward angular moment.
Source coefficient and terminal-integral theorems are not Lean-formalized.
-/
namespace TerminalCore2026

theorem a11_backward_hull_length :
    (3:ℚ)/10+17/10+3/10=23/10 := by norm_num

theorem a11_backward_bump_jets :
    (1715200:ℚ)/9*54=10291200 ∧
    (640:ℚ)/3*54=11520 ∧ (640:ℚ)/3*6=1280 := by
  constructor
  · norm_num
  constructor <;> norm_num

theorem a11_backward_rational_r :
    (100:ℚ)/99*(23/10)*21*11000000<600000000 := by norm_num

theorem a11_backward_rational_eta :
    (2:ℚ)*(23/10)*21*1300000<130000000 := by norm_num

theorem a11_backward_angular_error :
    (130000000:ℚ)+2*1300<131000000 ∧
    (600000000:ℚ)+1/2*131000000<700000000 := by
  constructor <;> norm_num

theorem a11_backward_q_positive :
    (99:ℚ)/100-700000000/(100^27)>49/50 := by norm_num

theorem a11_backward_cone :
    (43:ℚ)/20/((9:ℚ)*(49/50))<1/4 ∧
    (503:ℚ)/2000/(49/50)=503/1960 ∧
    2*(1-(1:ℚ)/4)^2-(3/20)*(503/1960)^2=
       85676973/76832000 ∧
    (85676973:ℚ)/76832000>11/10 := by
  constructor
  · norm_num
  constructor
  · norm_num
  constructor <;> norm_num

#print axioms a11_backward_hull_length
#print axioms a11_backward_rational_r
#print axioms a11_backward_q_positive
#print axioms a11_backward_cone
end TerminalCore2026