import Mathlib
/-! Exact arithmetic implications only. The originating source integrals,
source cell enclosures and unforced Navier--Stokes PDE are NOT formalized. -/
namespace TerminalCore2026

theorem a11_robust_f_margin :
    (1:ℚ)/2-523/2000=477/2000 := by norm_num
theorem a11_robust_q_margin :
    (49:ℚ)/50-1/100=97/100 := by norm_num
theorem a11_robust_slope_margin :
    (3:ℚ)/2+1/100=151/100 ∧
    (1:ℚ)/2-1/100=49/100 := by constructor <;> norm_num
theorem a11_robust_p_lower :
    (9:ℚ)*(97/100)=873/100 := by norm_num
theorem a11_robust_ratio :
    (2151/1000:ℚ)/(873/100)=239/970 ∧
    (239:ℚ)/970<1/4 := by constructor <;> norm_num
theorem a11_robust_w_ratio :
    (523/2000:ℚ)/(97/100)=523/1940 := by norm_num
theorem a11_robust_cone_exact :
    (9:ℚ)/8-(151/1000)*(523/1940)^2 =
      4192747121/3763600000 := by norm_num
theorem a11_robust_cone_strict :
    (4192747121:ℚ)/3763600000 > 11/10 ∧
    (11:ℚ)/10>9/20 := by constructor <;> norm_num

#print axioms a11_robust_cone_exact
#print axioms a11_robust_cone_strict
end TerminalCore2026