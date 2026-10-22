# Source-local A.11 proof dependencies — 22 October 2026

This is a live **dependency ledger**, not a full Lean certificate. The source-local full-hull theorem is proved mathematically under authentic moment/root and same-profile exact infinity-gauge hypotheses. It gives **|N_s|/E < lambda/500** on both supports AND intervening gap with an explicit small lambda choice relative to the already-fixed Pstar.

| Step | Required theorem | Status |
|---|---|---|
| 0 | Source-defined smooth step / sigma-prime bump and compact support | Paper-level; no Lean integration formalization |
| 1 | Exact Appendix A stage functions and stagewise ODE identities | Mathematical source / finite scalar replay |
| 2 | A single source-admissible Md,Td,Pstar,Tf,lambda,h and corrected pulse/root | NOT COMPLETED |
| 3 | Authentic A.11 moment root and its eta derivative | Conditional source-level proof; numerical freeze missing |
| 4 | Same-profile A.19 amplitude and exact S(infinity)=0 | NOT CERTIFIED JOINTLY |
| 5 | Same-profile pressure increment and Pi(infinity)=0 | NOT CERTIFIED JOINTLY |
| 6 | Differentiated Volterra future-integral identity for actual N_s | Paper-level math; not Lean formalized |
| 7 | Full two-support-and-gap |N_s|/E < lambda/500 | Conditional paper-level proof; Lean scalar gates submitted |
| 8 | Strict Q_s and stress cone on pulse/release/hold/terminal/far-tail | NOT CERTIFIED FOR ONE PROFILE |
| 9 | Appendix B nonlinear profile and common analytic radii | NOT COMPLETED |
| 10 | Actual unforced n=1,n=2 and all higher corrections | NOT COMPLETED |
| 11 | Cartesian unforced PDE residual and blowup hypotheses | NOT COMPLETED |
| 12 | Proposed unforced Theorem 1.1 | **OPEN; no start-to-finish Lean proof** |

GitHub module A11SourceLocalTailScalar.lean proves only rational scalar gates IF its CI run succeeds. The companion a11_source_local_future_exact.py checks these gates with exact rational arithmetic. Their successful execution is not a proof of the missing infinite-dimensional integral, analytic, or PDE theorems.

The original OpenAI theorem is a forced whole-space Navier–Stokes construction; it does not establish the proposed distinct unforced theorem.

## Update: same-profile terminal residual lift (22 October 2026)

A new analytic implication translates the A.19 normalized residual F and A.11
pressure-neutrality residual G, including their TOTAL eta derivatives, into
an exact terminal stress correction. The authentic source zero-gauge
|N_s|/E<lambda/500 conditional bound transfers to the true stress if

 alpha[(2+4h)|F|_sup+|F_eta|_sup]
 + beta[(1+2h)|G|_sup+|G_eta|_sup/2] < 249 lambda/500,

where alpha>=sup_hull[K/(XE)], beta>=sup_hull[1/E], K=Xp eb^2 f(eta)^2/lambda.
The input derivatives must be TOTAL derivatives along one common C1 corrected
A.11/A.19 root. Exact solutions for all eta make F=F_eta=G=G_eta=0.
The new fail-closed script checks the rational implication and REFUSES
missing inputs. Its passing example is synthetic, not an authenticated
interval source realization. The Lean module formalizes finite scalar
identities only and is NOT yet kernel certified unless CI succeeds.

Still absent: a jointly admissible numerical corrected profile, actual alpha
and beta, independently validated full-hull zero-gauge source bound and
stress patches, nonlinear Appendix B profile, unforced startup hierarchy,
physical PDE residual and Theorem 1.1. Do not promote the theorem.


## Cumulative continuation: two-coordinate interval-net release gate (22 October 2026)

The full A.11 support-and-gap hull is indexed by both pulse coordinate `y` and
angular parameter `eta`. The previous 1D eta-only Bernstein/fixed-y
Lipschitz tests are legitimate scalar tools, but do **not** cover the
physical 2D hull on their own.

A new source-conditional theorem uses a finite rectangular covering with
radii `r_y,r_eta` and validated coordinatewise Lipschitz envelopes for
`E`, `G_plus=lambda E+2Ns` and `G_minus=lambda E-2Ns`.
At each grid node the energy must exceed a strictly positive reserve, and
both signed stress expressions must exceed their 2D derivative-remainder
budgets. This implies `E>0` and `|Ns|/E<=lambda/2` uniformly over the hull.

A separate exact release margin strengthens the existing
`b0<=lambda/500` and source-gauge residual lift: if the authentic same-profile
residual bracket `R<=4979 lambda/10000`, then
`sup_hull |Ns|/E<=lambda/2-lambda/10000`.
Neither numerical source premise is claimed true without authenticated
interval data and total root derivatives.

New source insert:
`A11_Interval_Net_and_Release_Margin_20261022_Insert.tex`.
New Lean candidate:
`A11RectangularNetScalar.lean`.
The exact-rational local test of the scalar release implication and
2D affine transfer completed 10,000 trials each, plus three negative
controls; these are synthetic checks, **not** authentic source evidence.
GitHub CI must confirm any claim of kernel checking.

Status: **SCALAR_MATHEMATICS_PROVED / AUTHENTIC_SOURCE_HOLD /
UNFORCED_THEOREM_OPEN**. Do not mark the full theorem solved.
