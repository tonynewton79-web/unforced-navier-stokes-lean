import Mathlib

/-!
Exact A.29--A.30 source-normalized pulse algebra and centerline precision gates.
This is a CANDIDATE Lean file, not a completed analytic or PDE proof.
-/
namespace TerminalCore2026

theorem normalized_pulse_ratio_cleared
    (q beta lam S Cd R Rp m NE Q em en eq w0 e : ℝ)
    (hbeta : 2*beta+2*lam=1)
    (hq : S-beta=q*(1-lam))
    (hCd : Cd*q*beta^2=S*lam)
    (hem : em*beta^2=m*beta^2-R*beta+lam*Rp)
    (hen : en=NE+R-S*m-e)
    (heq : eq=Q-q)
    (hw : w0=2*R-Cd*Rp) :
    (NE-w0*Q)*beta^2 =
      q*lam*R*beta+S*(em*beta^2)+e*beta^2+
      en*beta^2-w0*eq*beta^2 := by
  have hcoef : S-beta-q*(2*beta+lam)=0 := by
    calc
      S-beta-q*(2*beta+lam) = q*(1-2*beta-2*lam) := by rw [hq]; ring
      _ = 0 := by
        have h : 1-2*beta-2*lam=0 := by linarith
        rw [h]
        ring
  have hspecial :
      R*beta*(S-beta-q*(2*beta+lam))+
      Rp*(Cd*q*beta^2-S*lam)=0 := by
    rw [hcoef, hCd]
    ring
  have hdiff :
    (NE-w0*Q)*beta^2 -
      (q*lam*R*beta+S*(em*beta^2)+e*beta^2+
       en*beta^2-w0*eq*beta^2) =
      R*beta*(S-beta-q*(2*beta+lam))+
      Rp*(Cd*q*beta^2-S*lam) := by
    rw [hem, hen, heq, hw]
    ring
  linarith

theorem centerline_eQ_scale :
    (9999/10000:ℚ)/10^24 <
       (((1:ℚ)/10^14 - 1/(10^14*10000))/(1-1/10^14))/10^10 ∧
       (((1:ℚ)/10^14 - 1/(10^14*10000))/(1-1/10^14))/10^10 <
         (10001/10000:ℚ)/10^24 := by
  constructor <;> norm_num

theorem centerline_eN_scale :
    (((1:ℚ)/10^14 - 1/(10^14*10000))/(1-1/10^14))/10^7 <
      (10001/10000:ℚ)/10^21 := by norm_num

theorem axial_source_c_nonnegative (D eta : ℝ) (hD : 0 ≤ D) :
    0 ≤ 2*D*eta^2/(1+eta^2) := by positivity

#print axioms normalized_pulse_ratio_cleared
#print axioms centerline_eQ_scale
#print axioms centerline_eN_scale
#print axioms axial_source_c_nonnegative
end TerminalCore2026
