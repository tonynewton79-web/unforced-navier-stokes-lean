import Mathlib
/-! Scalar arithmetic implications for A.11 local-tail bounds.
The actual source profiles and all-orders PDE are NOT formalized. -/
namespace TerminalCore2026
theorem a11_local_tail_budget :
 (1+8/(10000:ℚ))*(93/40+1/1000) < 233/100 := by norm_num
theorem a11_local_h_budget :
 (4:ℚ)*(1/2000)*(233/100) < 1/200 := by norm_num
theorem a11_delta_budget :
 (40960:ℚ)*(1/20)^28 < 1/10^31 := by norm_num
theorem a11_eta_jet_budget :
 (2:ℚ)*(2560*(1/20)^28/(1-1/10^31))*
 (233/100+1/2)<1/200 := by norm_num
theorem a11_bracket_budget :
 (1:ℚ)/200+1001/1000+1/200 <51/50 := by norm_num
theorem a11_stress_slack :
 (1:ℚ)/2-51/200=49/200 := by norm_num
theorem a11_cone_exact :
 (1:ℚ)/2-(3/20)*(51/100)^2=92197/200000 := by norm_num
theorem a11_cone_margin :
 (92197:ℚ)/200000 >9/20 := by norm_num
theorem a11_abstract_ns_margin
 (lam E B:ℝ) (hlam:0≤lam) (hE:0≤E)
 (hEval:E≤lam/4) (hB:0≤B) (hBmax:B≤51/50) :
 E*B ≤(51/200)*lam := by
 have h₁ : E*B≤(lam/4)*B :=
   mul_le_mul_of_nonneg_right hEval hB
 have h₂ : (lam/4)*B≤(lam/4)*(51/50) :=
   mul_le_mul_of_nonneg_left hBmax (by positivity)
 nlinarith [h₁,h₂]
#print axioms a11_local_tail_budget
#print axioms a11_cone_exact
#print axioms a11_abstract_ns_margin
end TerminalCore2026