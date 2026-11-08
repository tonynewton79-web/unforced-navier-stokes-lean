# Source-native three-moment heat and five-moment joining systems — 8 November 2026

**Restricted partial theorem.** OpenAI's *Finite Time Blowup for Navier–Stokes* (2026) constructs a singular solution **with smooth forcing**. This document does not certify a full original exterior or a locally/globally unforced Navier–Stokes blowup.

Original source: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
Proposition A.7, (A.39)–(A.43); Corollary A.3, Proposition B.8, (A.24)–(A.25), (B.35)–(B.39).

## Exact heat (three-moment) discrepancy

Write X=X_K x, e_K=E_cl(X_K), E_cl(X_Kx)=e_K F(x), with 0<F(x)<=2x^(−A), A=1/2+h, and a=chi_K(x)[1-H(2(1−eta²)/(X_Kx))], epsilon=2a−a². The source's gamma-integral heat factor H satisfies 0<=a<=2h(1+h)/(X_Kx) and |partial_eta a|<=4h(1+h)/(X_Kx).

The actual three discrepancies BEFORE corrective bumps are precisely

Delta Cp=−(e_K²/2) int_1^∞ F(x)² epsilon(x,eta) dx/x,
Delta S=+(X_K e_K²/2) int_1^∞ F(x)² epsilon(x,eta) dx,
Delta I=−sqrt(2) X_K^(3/2)e_K int_1^∞ sqrt(x) F(x) a(x,eta) dx.

Their signs are −,+,− and they all vanish at eta=±1. Both M and J remain unchanged because U=0. Exact integral bounds yield

||Delta Cp||_C1 <= 24h(1+h)e_K²/X_K,
||Delta S||_C1 <= 24h(1+h)e_K²,
||Delta I||_C1 <= 12sqrt(2)(1+h)e_K sqrt(X_K).

Here ||v||_C1=sup|v|+sup|v_eta|. No hidden pressure remainder.

For the actual source's five-unit second reserved patch of (A.9), prescribe three smooth sigma'-bumps of log width 1/10 at positions t=(1,5/2,4) and edit E=e_* f(eta)exp(−At)+e_*sum c_j beta(t−t_j). With rows (Cp,S,I) normalized by (e_*²,X_*e_*²,X_*^(3/2)e_*), the **exact** Jacobian has slopes s=(−1/2−lambda,1/2−lambda,3/2) in exponential log coordinate and row factors (f,−f,sqrt(2))b(s). Exact Fraction Taylor intervals and Lagrange-coefficient inequalities imply row-factor-free canonical inverse <7/2, physical C0 inverse <7, physical C1 inverse <14 for 0<lambda<=1/64. The complete quadratic bilinear remainder is C1-bounded by 32000.

Let rho=X_K/X_* and theta=e_K/e_* be source-schedule-fixed positive ratios, and
K=max{24h(1+h)theta²/rho, 24h(1+h)theta², 12sqrt(2)(1+h)theta sqrt(rho)}.
Then X_*>=10^8 K gives ||d3||C1<=1e−8 and 8·14²·32000·1e−8=0.50176<1, so the exact source three-moment nonlinear correction has a unique small solution ||c||C1<=28K/X_*<=2.8e−7. The edited azimuthal field E>e*/43 on this patch. **This is not a corrected stress-cone certificate**; the source's corresponding strict cone perturbation margins have not been evaluated for a complete schedule.

## The actual five-joining source discrepancy

On original joining x=X/X_R<=e^−5, ideal U0=4eta and E0=P_* f(eta)x^(1/10), write delta U=U−U0, delta E=E−E0. The FULL exact five moment difference, with prescribed source row operations, is:

Delta Mhat=int delta U dx,
Delta Ihat=int sqrt(2x)delta E dx,
Delta(Jhat−4eta Ihat)=int sqrt(2x)delta U E dx,
Delta(Shat−8eta Mhat)=int [(delta U)²−(E²−E0²)/2] dx,
Delta Cp=int (E²−E0²)/(2x)dx.

Integrate from 0 to x=e^−5. This is the exact uncomputed source-normalized right-hand side, not a numerical discrepancy certificate; computing it requires the original analytic radial continuation U,E, including its earlier transitions.

On −6<log x<−5, select two U bumps at log coordinate t=(1/5,4/5), three E bumps at t=(1/5,1/2,4/5), all using source-compatible even sigma' copies of log width 1/20. Canonical row-scaled exponential matrices have exponents U:(0,3/5); E:(1/2,1/10,−9/10). Exact rational intervals give canonical inverse <6 and <160, and after source f-multipliers the C0 row-normalized inverses are <12 and <320. These are NOT raw unscaled physical inverse bounds.

## What can and cannot be said about stress-cone margins

For the exact ideal reference joining interval, source (A.25) and f>=1/2 give Q_s>87/50, E0>P_*/5 and a=4/5,b_s=0 for h<1/100. The sufficient relaxed-cone (A.24) margins are a−b_s w=4/5 and 2−2b_sw−b_s²/a−(a−2)w²>=2. At X_R>=4000, ideal P_c=X Q_s/L>2 for x in [e^−8,e^−5] since e^8<3000. This **does NOT establish** the corrected profile's cone after five matching coefficients or the heat edit, because the actual N_s/(EQ_s) and derivative perturbations have not been interval enclosed.

Independent exact checker and 4-page journal-style note are in the complete conversation proof packet; 232-page cumulative PDF preserves the previous 228 extracted-text page streams. The local tests are finite rational/symbolic; not a Lean proof of the PDE.

**OPEN:** source admissible numeric parameter tuple, actual radial profile and d5, quantitative five-moment nonlinear solution for that profile, corrected stress-cone margins, full G1 analytic startup and physical zero unforced residual, and the global unforced Navier–Stokes problem. Keep this research PR DRAFT.
