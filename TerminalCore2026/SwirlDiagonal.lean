import Mathlib

/-!
# Exact current-order swirl-channel reorganization

This file certifies a coefficient identity for the actual swirl--swirl
source in equations (17)--(18) and (47) of Zenodo 23474915.

It is not the proof of an operator norm estimate: that requires the
concrete analytic Banach algebra, multiplier regularity, and the
regular-singular inverse in that Banach space.
-/
namespace TerminalCore2026

/-- Combine the time shift, leading radial transport and axial shift
into a zero-, one-, and radial-derivative source. Parameter g represents
V₀/X, and mu is b + 2*h*n. -/
theorem swirl_diagonal_reorganization
    (L mu D eta d U g f feta fX : ℝ) (hL : L ≠ 0) :
    ((-mu*f + D*eta*feta + fX)/L)
      + g*(fX+f)
      + U*((2*mu*eta*f + d*feta - 2*eta*fX)/L)
    =
    mu*((-1+2*eta*U)/L)*f
      + g*f
      + ((D*eta+d*U)/L)*feta
      + (((1-2*eta*U)/L)+g)*fX := by
  field_simp
  ring

/-- Exact separation of a problematic radial derivative into a
derivative of the whole product and a commutator term. -/
theorem radial_multiplier_commutator
    (g f dg df : ℝ) :
    g*df = (dg*f + g*df) - dg*f := by
  ring

/-- Analogous identity for the axial parameter derivative. -/
theorem axial_multiplier_commutator
    (g f dg df : ℝ) :
    g*df = (dg*f + g*df) - dg*f := by
  ring

#print axioms swirl_diagonal_reorganization

end TerminalCore2026
