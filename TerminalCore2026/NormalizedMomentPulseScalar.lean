import Mathlib

/-!
Source-native normalized moment identities (4.15)-(4.16).

This file is an algebraic layer, NOT a proof that the source integrals,
interval enclosures, analytic Appendix B or unforced Theorem 1.1 exist.
-/
namespace TerminalCore2026

theorem normalized_W
  (X E D eta d m meta g : ℝ) (hX : X ≠ 0) :
  1 - (2*D*eta*(X*E*m)+d*(X*E*(meta+g*m)))/X =
  1 - E*(2*D*eta*m+d*(meta+g*m)) := by
  field_simp [hX]
  ring

theorem normalized_Q
  (X H E h D eta d W i ieta g j jeta : ℝ)
  (hX : X ≠ 0) (hH : H ≠ 0) :
  -W + ((1-h)*(X*H*i)-D*eta*(X*H*(ieta+g*i)) -
        d*(X*H*E*(jeta+2*g*j))+
        2*(h-D)*eta*(X*H*E*j))/(X*H) =
  -W+(1-h)*i-D*eta*(ieta+g*i)-
     d*E*(jeta+2*g*j)+2*(h-D)*eta*E*j := by
  field_simp [hX, hH]
  ring

theorem normalized_N
  (X E W a D eta d m meta g h s seta A p peta : ℝ)
  (hX : X ≠ 0) (hE : E ≠ 0) :
  (-W*(E*a)+(D*((X*E*m)-eta*(X*E*(meta+g*m)))+
    4*h*eta*(X*E^2*s)-d*(X*E^2*(seta+2*g*s)))/X+
    4*A*eta*(E^2*p)-d*(E^2*(peta+2*g*p)))/E =
  -W*a+D*(m-eta*(meta+g*m))+
     E*(4*h*eta*s-d*(seta+2*g*s)+4*A*eta*p-d*(peta+2*g*p)) := by
  field_simp [hX,hE]
  ring

theorem normalized_eN
  (W R Bax D eta g m meta E t : ℝ) :
  -W*(R+Bax)+D*(m-eta*(meta+g*m))+E*t+R-
  (D-D*eta*g)*m+D*eta*meta =
  (1-W)*R-W*Bax+E*t := by
  ring

#print axioms normalized_W
#print axioms normalized_Q
#print axioms normalized_N
#print axioms normalized_eN

end TerminalCore2026
