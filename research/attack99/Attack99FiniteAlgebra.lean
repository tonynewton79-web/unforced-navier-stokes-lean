import Mathlib

/-!
Attack99 finite algebra only: the continuum flat-bump Gram coercivity
and smooth compact angular flux construction are in the mathematical
note, NOT formally proved in Lean here. Original Case006 PDE remains open.
-/
namespace UnforcedPatching.Attack99

theorem appendixAD_affine_wronskian (x : ℝ) :
    (2+x/2)*(-1/4) - (-(1+x/2)/2)*(1/2) = -1/4 := by
  ring

theorem axial_gram_offdiag (I0 : ℝ) :
    (I0/2)*(-1/4) = -I0/8 := by
  ring

theorem gram_adjugate_first
    (g11 g12 g22 beta gamma : ℝ) :
    g11*(beta*g22-gamma*g12)
      +g12*(gamma*g11-beta*g12)
      = beta*(g11*g22-g12*g12) := by
  ring

theorem gram_adjugate_second
    (g11 g12 g22 beta gamma : ℝ) :
    g12*(beta*g22-gamma*g12)
      +g22*(gamma*g11-beta*g12)
      = gamma*(g11*g22-g12*g12) := by
  ring

theorem source_rho_constant_pos :
    (0:ℚ) < 1229/4443 := by
  norm_num

theorem core_axial_source_match :
    ((4443:ℚ)/4916)*(-(1:ℚ)/2) = -(4443:ℚ)/9832 := by
  norm_num

theorem negative_rtheta_target :
    (-(214:ℚ)/1000) < (-(213:ℚ)/1000) := by
  norm_num

theorem positive_thetaz_target :
    (0:ℚ) < 189/1000 ∧ (189:ℚ)/1000 < 190/1000 := by
  norm_num

#print axioms appendixAD_affine_wronskian
#print axioms axial_gram_offdiag
#print axioms gram_adjugate_first
#print axioms gram_adjugate_second
#print axioms source_rho_constant_pos
#print axioms core_axial_source_match
#print axioms negative_rtheta_target
#print axioms positive_thetaz_target

end UnforcedPatching.Attack99
