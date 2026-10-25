import Mathlib

/-!
Edition XXX: elementary real scalar dependencies for necessary
Fourier/spectral energy tests. The actual Fourier transform,
Duhamel PDE, Leray projection, heat semigroup, shell integrals,
and unforced Navier-Stokes theorem remain UNFORMALIZED here.
-/
namespace TerminalCore2026

/-- Projecting the physical correction cannot create arbitrary shell
mass without an initial term, nonlinear transfer, or residual. -/
theorem whole_space_shell_tradeoff
    (base correction heatInit transfer residual : ℝ)
    (h : base ≤ correction + heatInit + transfer + residual) :
    base - correction ≤ heatInit + transfer + residual := by
  linarith

/-- A strict source shell surviving the correction requires nonzero
initial energy or a nonzero projected residual. This is scalar only. -/
theorem source_shell_requires_initial_or_residual
    (source remaining heatCoeff transferCoeff initial residual : ℝ)
    (hs : 0 < source - remaining)
    (hi : 0 ≤ initial) (hr : 0 ≤ residual)
    (hgate : source - remaining ≤
       heatCoeff * initial +
       transferCoeff * (initial+residual)^2 + residual)
    (ha : 0 ≤ heatCoeff) (hc : 0 ≤ transferCoeff) :
    initial ≠ 0 ∨ residual ≠ 0 := by
  by_contra hnone
  push_neg at hnone
  rcases hnone with ⟨hin, hres⟩
  simp [hin, hres] at hgate
  linarith

/-- The exact unforced case with a nonzero target and nonnegative
quadratic energy coefficient needs strictly positive initial amplitude. -/
theorem nonzero_shell_requires_nonzero_initial
    (h a c x : ℝ)
    (hh : 0 < h) (hx : 0 ≤ x)
    (hbudget : h ≤ a*x+c*x^2) :
    0 < x := by
  by_contra hnot
  have hzero : x = 0 := le_antisymm (le_of_not_gt hnot) hx
  rw [hzero] at hbudget
  norm_num at hbudget
  linarith

/-- Unit-frequency shell cost is a rational identity after the
dimension-dependent geometric factor has been extracted. -/
theorem shell_radial_integral (K : ℝ) :
    (2*K-K) = K := by
  ring

/-- The whole-space unforced source estimate is not a claimed
regularity statement: this is only its scalar algebra. -/
theorem residual_zero_reduces_budget
    (x a c h : ℝ)
    (hbudget : h ≤ a*x + c*(x+0)^2 + 0) :
    h ≤ a*x + c*x^2 := by
  simpa using hbudget

#print axioms whole_space_shell_tradeoff
#print axioms source_shell_requires_initial_or_residual
#print axioms nonzero_shell_requires_nonzero_initial
#print axioms residual_zero_reduces_budget
end TerminalCore2026
