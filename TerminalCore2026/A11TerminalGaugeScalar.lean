import Mathlib

/-!
# A.11 terminal-gauge scalar gates
Only finite algebra and rational inequalities are formalized.
The true source integrals, normalization roots, interval soundness
and unforced Navier--Stokes reconstruction remain outside this file.
-/
namespace TerminalCore2026

theorem terminal_source_defect_split
    (h A eta d X St Set Sg Sget Pt Pet Pg Pget : ℝ) :
    (4*h*eta*(St+Sg)-d*(Set+Sget))/X+
        4*A*eta*(Pt+Pg)-d*(Pet+Pget) =
    (4*h*eta*St-d*Set)/X + 4*A*eta*Pt-d*Pet +
    (4*h*eta*Sg-d*Sget)/X + 4*A*eta*Pg-d*Pget := by
  ring

theorem conditional_support_stress_rational_gate :
    ((4*(1/2000:ℚ)*(233/100)
      + 4*((1/2:ℚ)+1/2000)*(1/2)
      + 2*(1/1000)*(233/100))/4) < 253/1000 := by
  norm_num

theorem remaining_stress_margin :
    (1/2:ℚ)-253/1000=247/1000 := by
  norm_num

#print axioms terminal_source_defect_split
#print axioms conditional_support_stress_rational_gate
#print axioms remaining_stress_margin
end TerminalCore2026
