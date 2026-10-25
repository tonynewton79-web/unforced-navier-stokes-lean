import Mathlib

/-!
# A.11 joint smallness and sharp scalar cone consequence
Finite rational gates; not the exponential/logarithm parameter theorem,
the source interval certificate, or an unforced Navier--Stokes proof.
-/
namespace TerminalCore2026
private def qDiagnostic : ℚ := 633
private def lamDiagnostic : ℚ := 1 / (10^20 * qDiagnostic)
private def epsDiagnostic : ℚ := 1 / 1000000000
private def hDiagnostic : ℚ := lamDiagnostic * epsDiagnostic / 1000000

theorem diagnostic_smallness :
    0 < lamDiagnostic ∧ lamDiagnostic < 1/10^14 ∧
    lamDiagnostic < 1/20 ∧ lamDiagnostic < 1/(10^6*533) ∧
    lamDiagnostic < 1/(10*(1+100)) ∧
    0 < hDiagnostic ∧ hDiagnostic < lamDiagnostic/10000 ∧
    hDiagnostic < epsDiagnostic/100 ∧
    lamDiagnostic*512 < 1/10^6 := by
  norm_num [qDiagnostic,lamDiagnostic,epsDiagnostic,hDiagnostic]

theorem conditional_A11_cone_margin :
    (2:ℚ)*(1-1/4)^2-(3/20)*(4/49)^2 = 107949/96040 := by
  norm_num
theorem conditional_A11_cone_beats_threshold :
    (107949:ℚ)/96040 > 1 ∧ (107949:ℚ)/96040 > 9/20 := by
  norm_num
theorem conditional_A11_shear_ratio :
    ((2:ℚ)/25)/(49/50) = 4/49 := by norm_num
theorem conditional_A11_a_to_p_ratio :
    ((43:ℚ)/20)/(441/50) < 1/4 := by norm_num

#print axioms diagnostic_smallness
#print axioms conditional_A11_cone_margin
#print axioms conditional_A11_cone_beats_threshold
end TerminalCore2026