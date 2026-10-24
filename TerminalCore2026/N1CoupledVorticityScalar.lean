import Mathlib

/-!
Proof Attack 5, Edition X. Finite algebraic energy/coupling checks ONLY.
The full cylindrical PDE, the source-specific collar, and global unforced
Navier--Stokes blowup have NOT been Lean-formalized.
-/
namespace TerminalCore2026

theorem n1_meridional_energy_coupling
    (vr vz w UoverR Ur Uz : ℝ) :
    2 * UoverR * vr * w -
      w * (vr * (Ur + UoverR) + vz * Uz) =
      w * (vr * (UoverR - Ur) - vz * Uz) := by
  ring

theorem n1_young_scalar (a b : ℝ) :
    2 * a * b ≤ a^2 + b^2 := by
  nlinarith [sq_nonneg (a-b)]

theorem n1_curl_radial_source
    (r UwZ : ℝ) (hr : r ≠ 0) :
    r * (2 * UwZ / r) = 2 * UwZ := by
  field_simp [hr] <;> ring

theorem n1_pressure_radial_source
    (r UwR : ℝ) (hr : r ≠ 0) :
    r * (2 * UwR / r) = 2 * UwR := by
  field_simp [hr] <;> ring

theorem n1_nonzero_coupling (r x : ℝ)
    (hr : 0 < r) (hx : x ≠ 0) :
    2 * x / r ≠ 0 := by
  apply div_ne_zero
  · exact mul_ne_zero (by norm_num) hx
  · exact ne_of_gt hr

#print axioms n1_meridional_energy_coupling
#print axioms n1_young_scalar
#print axioms n1_curl_radial_source
#print axioms n1_pressure_radial_source
#print axioms n1_nonzero_coupling
end TerminalCore2026
