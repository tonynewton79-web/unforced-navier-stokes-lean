import Mathlib

/-!
# Attack 22: an explicit three-dimensional C4-compatible Leray triad

This module certifies finite exact rational wavevector and polarization
algebra.  The i*2*pi Fourier multiplier, continuum Fourier convolution,
3D Navier--Stokes PDE, and an unforced singular solution remain separate.
-/

namespace UnforcedPatching

def triadP : Fin 3 → ℚ := ![1, 0, 0]
def triadQ : Fin 3 → ℚ := ![0, 2, 1]
def triadR : Fin 3 → ℚ := ![1, 2, 1]
def triadA : Fin 3 → ℚ := ![0, 1, 0]
def triadB : Fin 3 → ℚ := ![0, 1, -2]

def dot3 (v w : Fin 3 → ℚ) : ℚ := ∑ i : Fin 3, v i * w i

def leray3 (k v : Fin 3 → ℚ) (i : Fin 3) : ℚ :=
  v i - (dot3 k v / dot3 k k) * k i

/-- The exact wavevector, incompressibility and coupling identities. -/
theorem active_triad_geometry :
    (∀ i : Fin 3, triadR i = triadP i + triadQ i) ∧
    dot3 triadP triadA = 0 ∧
    dot3 triadQ triadB = 0 ∧
    dot3 triadR triadB = 0 ∧
    dot3 triadQ triadA = 2 ∧
    dot3 triadP triadB = 0 := by
  constructor
  · intro i
    fin_cases i <;> norm_num [triadR, triadP, triadQ]
  all_goals norm_num [dot3, triadP, triadQ, triadR, triadA,
    triadB, Fin.sum_univ_succ]

/-- The target r=(1,2,1) Leray projection leaves the receiver
polarisation (0,1,-2) unchanged. -/
theorem triad_leray_preserves_receiver (i : Fin 3) :
    leray3 triadR triadB i = triadB i := by
  fin_cases i <;> norm_num [leray3, dot3, triadR, triadB,
    Fin.sum_univ_succ]

/-- With u_p=i*a*A and u_q=b*B, the ordered pair sum at r is
2*i*a*b*B before applying the outer Fourier factor i*2*pi.
This is an algebraic statement about the scalar polarization map. -/
theorem triad_projected_pair_nonzero :
    dot3 triadQ triadA = 2 ∧ dot3 triadP triadB = 0 ∧
    (∀ i : Fin 3, leray3 triadR (fun j => 2 * triadB j) i =
      2 * triadB i) := by
  constructor
  · norm_num [dot3, triadQ, triadA, Fin.sum_univ_succ]
  constructor
  · norm_num [dot3, triadP, triadB, Fin.sum_univ_succ]
  intro i
  fin_cases i <;> norm_num [leray3, dot3, triadR, triadB,
    Fin.sum_univ_succ]

/-- The two components of the exact 2D off-axis Leray response for
axis wavevectors (n,0,0) and (0,m,0), with positive n and m.
The signed off-axis response is nonzero if n ≠ m. -/
theorem oblique_axis_projection_x (n m : ℚ)
    (hden : n^2 + m^2 ≠ 0) :
    m / 4 - n^2 * m / (2 * (n^2 + m^2)) =
      m * (m^2 - n^2) / (4 * (n^2 + m^2)) := by
  field_simp
  ring

theorem oblique_axis_projection_y (n m : ℚ)
    (hden : n^2 + m^2 ≠ 0) :
    n / 4 - m^2 * n / (2 * (n^2 + m^2)) =
      n * (n^2 - m^2) / (4 * (n^2 + m^2)) := by
  field_simp
  ring

/-- Rational exponents only: the standalone two-dimensional migrating
halo's enstrophy would grow like tau^(-7/10), while the imposed packet
drift costs tau^(-27/20).  No PDE lemma is claimed here. -/
theorem triad_terminal_exponent_ledger :
    (1 / 5 : ℚ) - 2 * (9 / 20) = -(7 / 10) ∧
    (1 / 10 : ℚ) - (9 / 20) = -(7 / 20) ∧
    (1 / 10 : ℚ) - (9 / 20) - 1 = -(27 / 20) ∧
    (1 / 5 : ℚ) - (9 / 20) = -(1 / 4) ∧
    (1 / 10 : ℚ) - 2 * (9 / 20) = -(4 / 5) := by
  norm_num

#print axioms active_triad_geometry
#print axioms triad_leray_preserves_receiver
#print axioms triad_projected_pair_nonzero
#print axioms oblique_axis_projection_x
#print axioms oblique_axis_projection_y
#print axioms triad_terminal_exponent_ledger

end UnforcedPatching
