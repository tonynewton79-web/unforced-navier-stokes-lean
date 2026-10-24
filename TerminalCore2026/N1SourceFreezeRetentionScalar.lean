import Mathlib

/-!
Edition XXXII. Scalar exact consequences only; DOES NOT formalize
the original Section 10 source, the small-data global PDE theorem,
Fourier transforms or a singularity-preserving correction.
-/
namespace TerminalCore2026

theorem xxxii_nonretention_from_small_data
    (b k eps delta : ℝ)
    (hEps : eps < (1-k)*b)
    (hTriangle : b-eps ≤ delta) :
    k*b < delta := by
  linarith

theorem xxxii_source_shell_partition
    (energy low high middle : ℝ)
    (hfull : energy ≤ low+high+middle)
    (hlow : low ≤ energy/8)
    (hhigh : high ≤ energy/16) :
    (13/16 : ℝ)*energy ≤ middle := by
  linarith

theorem xxxii_retained_component_growth
    (background correction tauPow e0 : ℝ)
    (he : 0 < e0) (hp : 0 < tauPow)
    (hb : e0*tauPow/2 ≤ background)
    (hw : correction ≤ e0*tauPow/4) :
    e0*tauPow/4 ≤ background-correction := by
  nlinarith

theorem xxxii_conditional_cutoff_margin
    (qstar C0 tau0 zpowered : ℝ)
    (ht : C0*tau0 ≤ qstar/16)
    (hz : C0*zpowered = qstar/16)
    (hq : 0 < qstar) :
    C0*(tau0+zpowered) < qstar/2 := by
  nlinarith

#print axioms xxxii_nonretention_from_small_data
#print axioms xxxii_source_shell_partition
#print axioms xxxii_retained_component_growth
#print axioms xxxii_conditional_cutoff_margin

end TerminalCore2026
