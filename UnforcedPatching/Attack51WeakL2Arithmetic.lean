import Mathlib

/-!
Attack 51: exact quantitative arithmetic for a conditional weighted L2
obstruction to subleading unforcing of the fixed Attack49 diagnostic.
The physical source pairing, support estimates and weak-form inequality
are NOT proved here. No unforced blow-up theorem is established.
-/

namespace UnforcedPatching

theorem attack51_cutoff_mass :
    (16 : ℝ) * ((1 : ℝ) / 3 - 1 / 2 + 1 / 5) = 8 / 15 := by
  norm_num

theorem attack51_source_constant :
    ((201 : ℝ) / 4000) * (36501 / 274877906944) * (8 / 15) =
      2445567 / 687194767360000 := by
  norm_num

theorem attack51_energy_constant :
    (((83968 : ℝ) + 33 / 8 + 17 / 40) / 8 + 18) =
      1682331 / 160 := by
  norm_num

theorem attack51_exact_margin :
    ((2445567 : ℝ) / 687194767360000) / (1682331 / 160) =
      815189 / 2408518875348992000 := by
  norm_num

/-- Abstract numerical consequence of the explicitly assumed weak estimate,
not a construction of a PDE correction or an unforced singular solution. -/
theorem attack51_inequality_implies_nonzero_l2
    {q : ℝ} (hq : 0 ≤ q)
    (hweak : (2445567 : ℝ) / 687194767360000 <
      (((83968 : ℝ) + 33 / 8 + 17 / 40) / 8) * q + 18 * q ^ 2) :
    (815189 : ℝ) / 2408518875348992000 < q := by
  by_cases hq1 : q ≤ 1
  · have hsq : q ^ 2 ≤ q := by
      nlinarith [mul_nonneg hq (sub_nonneg.mpr hq1)]
    have hcap :
        (((83968 : ℝ) + 33 / 8 + 17 / 40) / 8) * q + 18 * q ^ 2 ≤
          (1682331 : ℝ) / 160 * q := by
      nlinarith
    have htotal : (2445567 : ℝ) / 687194767360000 <
        (1682331 : ℝ) / 160 * q := lt_of_lt_of_le hweak hcap
    norm_num at htotal ⊢
    nlinarith
  · have hb : (815189 : ℝ) / 2408518875348992000 < 1 := by norm_num
    linarith

#print axioms attack51_source_constant
#print axioms attack51_energy_constant
#print axioms attack51_exact_margin
#print axioms attack51_inequality_implies_nonzero_l2

end UnforcedPatching
