import UnforcedPatching.NonlinearTriad22
import Mathlib.Tactic

/-!
# Attack 23: exact first mediator and an all-order polarization ray

The contents of this file are **finite rational Fourier geometry** only.
They do not formalize a Navier--Stokes solution, an infinite cascade, the
full C4 convolution, or any singularity.

The first newly forced mode is s = p + r = (2,2,1), provided the
mode coefficients at p and r are nonzero with the specified phases.
-/

namespace UnforcedPatching

def mediatorRay (m : ℚ) : Fin 3 → ℚ := ![m, 2, 1]

theorem mediator_ray_step (m : ℚ) (i : Fin 3) :
    mediatorRay (m + 1) i = triadP i + mediatorRay m i := by
  fin_cases i <;> norm_num [mediatorRay, triadP] <;> ring

theorem mediator_ray_transverse (m : ℚ) :
    dot3 (mediatorRay m) triadB = 0 := by
  norm_num [dot3, mediatorRay, triadB, Fin.sum_univ_succ]

theorem mediator_ray_active (m : ℚ) :
    dot3 (mediatorRay m) triadA = 2 := by
  norm_num [dot3, mediatorRay, triadA, Fin.sum_univ_succ]

theorem mediator_ray_norm (m : ℚ) :
    dot3 (mediatorRay m) (mediatorRay m) = m ^ 2 + 5 := by
  norm_num [dot3, mediatorRay, Fin.sum_univ_succ] <;> ring

theorem mediator_ray_leray (m : ℚ) (i : Fin 3) :
    leray3 (mediatorRay m) triadB i = triadB i := by
  unfold leray3
  rw [mediator_ray_transverse]
  simp

/-- The ordered p+r source before the outer Fourier derivative multiplier
is -2*i*A*C*b.  This is its rational vector factor (-2*b).
No full Fourier convolution identity is asserted by this lemma. -/
theorem first_mediator_vector (i : Fin 3) :
    leray3 (mediatorRay 2) (fun j => (-2 : ℚ) * triadB j) i =
      (-2 : ℚ) * triadB i := by
  fin_cases i <;>
    norm_num [leray3, dot3, mediatorRay, triadB, Fin.sum_univ_succ]

theorem first_mediator_nonzero :
    leray3 (mediatorRay 2) (fun j => (-2 : ℚ) * triadB j) 1 = -2 := by
  norm_num [leray3, dot3, mediatorRay, triadB, Fin.sum_univ_succ]

#print axioms mediator_ray_step
#print axioms mediator_ray_transverse
#print axioms mediator_ray_active
#print axioms mediator_ray_norm
#print axioms mediator_ray_leray
#print axioms first_mediator_vector
#print axioms first_mediator_nonzero

end UnforcedPatching
