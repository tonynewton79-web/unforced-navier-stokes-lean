import Mathlib

/-!
# Exact local terminal-core dynamics: finite mathematical lemmas

This file formalizes *only* specific finite identities and inequalities from
Newton, "Exact Local Unforced Terminal-Core Dynamics in Three-Dimensional
Navier--Stokes" (Zenodo 23474915, 19 October 2026).

The coefficient hierarchy, the analytic norm inequalities, its infinite
summation, and the Navier--Stokes equation for the resulting physical field
are not formalized in this file. No theorem below is a Navier--Stokes
regularity or finite-time blow-up theorem.
-/

namespace TerminalCore2026

noncomputable section

/-- Leading velocity exponent, equation (12). -/
def A (h : ℝ) : ℝ := (1 : ℝ) / 2 + h

/-- Axial length exponent, equation (12). -/
def D (h : ℝ) : ℝ := (1 : ℝ) / 2 - h

/-- Spatial velocity `L^p` exponent, equation (57). -/
def sigma (h p : ℝ) : ℝ := -A h + (1 + D h) / p

/-- Vanishing-exponent spatial threshold, equation (58). -/
def criticalP (h : ℝ) : ℝ := (3 - 2 * h) / (1 + 2 * h)

/-- The local kinetic-energy power of time, equation (62). -/
def energyPower (h : ℝ) : ℝ := (1 : ℝ) / 2 - 3 * h

/-- The coefficient of a monomial under the radial regular-singular operator. -/
def radialSymbol (nu : ℝ) (m : ℕ) : ℝ :=
  ((m : ℝ) + 1) * ((m : ℝ) + nu)

/-- Explicit coefficient inverse of the radial symbol, equation (35). -/
def inverseCoefficient (nu : ℝ) (m : ℕ) (c : ℝ) : ℝ :=
  c / radialSymbol nu m

/-- The radial inverse is defined at every natural degree for positive `nu`. -/
theorem radialSymbol_pos (nu : ℝ) (hnu : 0 < nu) (m : ℕ) :
    0 < radialSymbol nu m := by
  unfold radialSymbol
  have hm : 0 ≤ (m : ℝ) := Nat.cast_nonneg _
  apply mul_pos <;> linarith

/-- Exact coefficientwise inversion of the regular-singular radial operator. -/
theorem radial_inverse_exact (nu : ℝ) (hnu : 0 < nu)
    (m : ℕ) (c : ℝ) :
    radialSymbol nu m * inverseCoefficient nu m c = c := by
  unfold inverseCoefficient
  have hs : radialSymbol nu m ≠ 0 := ne_of_gt (radialSymbol_pos nu hnu m)
  field_simp [hs]
  ring

/-- At `p=3`, the exact velocity power is `-4h/3`, equation (59). -/
theorem sigma_three (h : ℝ) : sigma h 3 = -(4 * h) / 3 := by
  unfold sigma A D
  ring

/-- The exponent at the threshold `p*` vanishes, equation (58). -/
theorem sigma_at_critical (h : ℝ) (hh : 0 < h)
    (hsmall : h < (1 : ℝ) / 100) :
    sigma h (criticalP h) = 0 := by
  have hd : (1 : ℝ) + 2 * h ≠ 0 := by linarith
  have hn : (3 : ℝ) - 2 * h ≠ 0 := by linarith
  unfold sigma criticalP A D
  field_simp [hd, hn]
  ring

/-- The spatial threshold is strictly below three when `h>0`. -/
theorem critical_lt_three (h : ℝ) (hh : 0 < h) :
    criticalP h < 3 := by
  have hd : (0 : ℝ) < 1 + 2 * h := by linarith
  unfold criticalP
  apply (div_lt_iff₀ hd).2
  nlinarith

/-- The core's kinetic energy has strictly positive decay exponent. -/
theorem energy_decay_pos (h : ℝ) (hsmall : h < (1 : ℝ) / 100) :
    0 < energyPower h := by
  unfold energyPower
  linarith

/-- Exact relation used to derive the Serrin-critical exponent, equation (61). -/
theorem serrin_exponent_exact (h p : ℝ) (hp : 3 < p) :
    (2 * p / (p - 3)) * sigma h p =
      -1 - (2 * h * (p + 1)) / (p - 3) := by
  have hp0 : p ≠ 0 := by linarith
  have hp3 : p - 3 ≠ 0 := by linarith
  unfold sigma A D
  field_simp
  ring

/-- Serrin-critical exponents are strictly below the integrability boundary. -/
theorem serrin_exponent_strict (h p : ℝ)
    (hh : 0 < h) (hp : 3 < p) :
    (2 * p / (p - 3)) * sigma h p < -1 := by
  rw [serrin_exponent_exact h p hp]
  have hden : 0 < p - 3 := by linarith
  have hnum : 0 < 2 * h * (p + 1) := by
    apply mul_pos
    · nlinarith
    · linarith
  have hpos : 0 < (2 * h * (p + 1)) / (p - 3) :=
    div_pos hnum hden
  linarith

/-- The local `L³` power is strictly negative at positive anisotropy. -/
theorem L3_exponent_negative (h : ℝ) (hh : 0 < h) :
    sigma h 3 < 0 := by
  rw [sigma_three]
  linarith

#print axioms radial_inverse_exact
#print axioms sigma_three
#print axioms sigma_at_critical
#print axioms critical_lt_three
#print axioms energy_decay_pos
#print axioms serrin_exponent_exact
#print axioms serrin_exponent_strict
#print axioms L3_exponent_negative

end
end TerminalCore2026
