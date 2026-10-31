# H8 Attack N — physical Rayleigh and amplitude-injection gate

**Claim status:** Conditional exact physical-profile theorem; genuine singular H8 source NOT authenticated; unforced finite-time blow-up theorem OPEN.

The previous exact local-core manuscript uses tau=T-t=q(1-eta^2), z=q^(1/2-h)eta and X=r^2/(2q). The source-native H8 section instead uses q=1-t off-axis and explicitly leaves the cutoff and shell profiles arbitrary. It cannot yet provide a source-specific unique numerical answer.

## New exact reductions

For A=1/2+h, D=1/2-h, d=1-eta^2, L=1-2h eta^2, the true volume element is 2 pi tau^(1+D) L d^(-D-2) dX d eta.

Assume a FULL smooth periodic divergence-free compact similarity carrier with leading components U_r=q^(-1/2)V_r and (U_theta,U_z)=q^(-A)(V_theta,V_z), with controlled q^(2h) remainder. Its kinetic norm scales M=tau^(1/2-3h)(M0+O(tau^(2h))), and W=partial_z U has N=tau^(-A)(N0+O(tau^(2h))).

The exact physical-profile Rayleigh integrals defined in Appendix N yield
c_A=tau^(-1)[R_U/M0 -(1/4-3h/2)]+O(tau^(-1+2h)),
b_T=tau^(-1)[A/2+(R_W+S_W)/N0]+O(tau^(-1+2h)).
The translation forcing g_T and nonlinear coefficient e_T have explicit weighted profile integral formulas, including the leading cylindrical centripetal term. Numerical values remain source-dependent and undetermined.

## New strict conditional source lower bound

If the entire carrier is confined to 0<=X<=Xstar, |eta|<=etastar<1, its transverse support lies in disk r<=sqrt(2Xstar/dstar) sqrt(tau) with dstar=1-etastar^2. Scalar disk Dirichlet inequality, applied to Cartesian components, proves

||grad U||_2^2/||U||_2^2 >= j_(0,1)^2 dstar /(2 Xstar tau).

For p=1/2-3h>0, if Xstar<j_(0,1)^2*dstar/p, the exact amplitude coefficient satisfies c_A>=kappa/tau for some kappa>0. The raw Leray-projected carrier source must then obey

||G||_2>=||P_A G||_2 = |c_A| ||U||_2 >= c tau^(-3/4-3h/2).

This matches the previously recorded H8 raw L2 source exponent; under these explicit hypotheses it is a lower as well as upper power, so pressure normalization cannot provide any source-power gain. For beta'+c_A beta = F_A, forcing F_A=o(1/tau) implies beta->0, not amplitude retention. Leading injection could still rescue the programme.

## Verification / limitations

The four-page standalone PDF compiled with no unresolved references or overfull boxes, and was visually inspected. Its merge preserves the previous 83 PDF page text streams exactly and yields an 87-page cumulative PDF. Seven new symbolic/independent numerical tests pass. The combined H8 local suites pass 58 tests.

The GitHub main manuscript includes a self-contained compact Appendix N with the same exact formulas and proof, and has corresponding exact symbolic tests. The independent release ZIP contains the full Appendix N source, seven-test module and provenance files. No new Lean kernel receipt or global PDE existence proof is asserted.

**Next real gate:** freeze a complete physical source tuple (core profile, local homotopy gauge, cutoff, H8 ray stress, shell shapers and periodic pressure), compute the profile integrals and full QG, and prove the amplitude-injection, translation matching and full global L-infinity correction bounds simultaneously.
