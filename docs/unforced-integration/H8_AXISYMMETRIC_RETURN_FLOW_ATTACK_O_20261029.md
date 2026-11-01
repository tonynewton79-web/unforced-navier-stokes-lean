# H8 Attack O — Axisymmetric return-flow and sharp Bessel confinement

## Exact, source-independent results (compact, smooth, axisymmetric, solenoidal class)

**Physical axial flux law:** For a field compactly supported in radius and in a proper axial subinterval, integrate the divergence equation across physical radial disks to obtain int U_z(r,z) r dr = 0 for every z. A positive axial centre must be balanced by a negative return-flow annulus.

**Gauge-fixed stream representation:** With q=tau/(1-eta²), X=r²/(2q), A=1/2+h, D=1/2-h, define Z_a F=(2a eta F+(1-eta²)F_eta-2eta X F_X)/(1-2h eta²). For compact regular Phi,B, the potential A_theta=q^-h Phi/sqrt(2X), A_z=-q^-h B produces the EXACT divergence-free profiles Vr=-Z_(1-A)Phi/sqrt(2X), Vz=Phi_X, Vtheta=sqrt(2X)B_X.

**Sharper transverse Poincare bound:** Horizontal Cartesian velocity components have angular Fourier order 1 and quotient at least j11²/R*²; axial velocity is radial and has zero disk mean, yielding the *constrained* sharp j21²/R*². Consequently

||grad U||²/||U||² >= [j11² + (j21²-j11²) theta_z]/R*²,

where theta_z=||U_z||²/||U||², j11²≈14.6819706421 and j21²≈26.3746164272. This improves the previous scalar j01²≈5.7831859629 bound and is standard Bessel spectral geometry, not a priority claim.

**Terminal dyadic amplitude injection:** If c_A=<G,U>/||U||² >=kappa/tau and a genuine unforced correction retains beta->1 in the exact two-mode equation beta'+c_A beta=F_A, then liminf int_[T-tau,T-tau/2] F_A(s)ds >= kappa log2. In particular merely o(1/tau) amplitude forcing would erase the carrier.

## One fully specified *prepared-field* prototype — not the authentic H8 source

h=.1, X*=1, eta*=.5, Phi=X exp(-X/(1-X)) exp(-4eta²/(1-4eta²)), B=Phi/4 with flat extensions. Its smooth curl is compactly supported and periodic, has U_z(t,0,0)=tau^-A, and uniquely determines the canonical periodic pressure. It is not verified to match the authentic local terminal core, H8 positive seven-ray stress or nonlinear unforced solution.

Profile quadrature at 40/64/90/128 nodes converges:
M0=.829691939536, N0=9.33098522102, R_U=22.4981774935, R_W=402.857206575,
lim tau*c_A=27.0163023544, lim tau*b_T=43.4741340312,
lim tau^A*g_T=lim tau^A*e_T=.0477816887268, axial fraction .95969941416.
Signed translation-strain and time-projection quadratures are zero by parity. These are convergent numerical diagnostics, NOT interval certificates.

## Verification and explicit remaining gaps

12 new Attack O tests passed, along with the selected earlier H8 tests: 70/70 total local pytest pass. Full standalone Appendix O compiled to four pages; appended to the previous 87-page PDF for a 91-page cumulative release, preserving all 87 earlier page text streams. The complete PDF and editable standalone appendix are available in the release ZIP.

**OPEN:** no complete authentic physical H8 tuple; no full periodic complementary residual QG, nonlinear amplitude/translation propagation, exterior pointwise control or final Lean unforced singularity proof. The GitHub source appendix is compact; it is not the exact LaTeX build source for the merged 91-page PDF.
