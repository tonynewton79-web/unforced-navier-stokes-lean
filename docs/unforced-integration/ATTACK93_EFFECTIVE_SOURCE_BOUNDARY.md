# Attack 93 — effective partial source certificates and angular-shear transfer HOLD

**22 November 2026 | Tony Newton**  
**Release:** EFFECTIVE_SUBCERTIFICATES_ONLY__FULL_SOURCE_OPEN.  
**No claimed solution of unforced 3D Navier–Stokes. No complete Lean PDE theorem.**

## Authentication and the previously overlooked hierarchy

Primary source is OpenAI, *Finite Time Blowup for Navier–Stokes*, **FORCED** theorem, Appendix A.5 and B.1–B.5:
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

User source: Tony Newton, *Carrier-Independent Structured Stress Route, Case006*, 122-page original, SHA-256 `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`, especially (199)–(210), (255)–(257).

Source Lemma 4.8 requires `T_d=exp(M_d)+10, Pstar>exp(T_d), 0<h<min(1/100,lambda,exp(-T_d))`. If `M_d>=0`, necessary bounds are `Pstar>2^11` and `h<2^-11`. Earlier **illustrations** using `Pstar=2`, `h=1/1000` or `h=1/10` must never be presented as actual fully admissible source choices. Source Appendix B.2 also requires `C>=sup_{eta in Omega}|phi_star|`, with a genuine complex neighborhood and the B.2 axis selector constraints. The outer profile, analytic contraction constants, Gamma-majorants, complex Mchi and complete numerical tuple are not fixed by the supplied sources.

## Certified exact inner-pressure interval, not full outer integral

Source (4.31) prescribes for `0<X<=X_R` the inner *exterior* branch `E_o=Pstar*(1+eta²)^(-1)*(X/X_R)^(1/10)`. Its pressure contribution and first two derivatives are **exact**:

```text
Pi_in/Pstar² = -5/[2(1+eta²)²]
Pi_in'/Pstar² = 10eta/(1+eta²)³
Pi_in''/Pstar² = 10(1-5eta²)/(1+eta²)^4
```

For the diagnostic endpoint `j0=1/20` on `eta in [-1/140,-1/180]`, exact rational lower/upper intervals are:

```text
Pi_in/Pstar²:  [-2624400000/1049824801, -960400000/384199201]
Pi_in'/Pstar²: [-537824000000/7530688538801, -1889568000000/34015373377201]
Pi_in''/Pstar²: [1475412579200000000/147609026049038401,
                 11018259964800000000/1102132112794689601]
```

For every `0<j0<=1/20` and `eta in [-j0/7,-j0/9]`, the A.5 outer factorization `E_o=c(y)(1+eta²)^(-theta(y))`, `0<=theta<=1`, proves that each outer contribution to `Pi0''` is nonnegative on that interval. Thus the **actual full source-family pressure** satisfies `Pi0''> (1999/200)*Pstar²=9.995 Pstar²`. This is a genuine one-sided partial source certificate, NOT a two-sided full Pi0 enclosure and NOT a numerical choice of j0.

## New effective operator-majorant module

Appendix B.3 yields for `T=J2*Mchi/2` the **complex weighted coefficient norm** estimate `||T^k|| <= (40 B)^k/[k!(k+1)!]` provided `B>=||Mchi||_(B_rho->B_rho)`. If `r=40B/[(K+2)(K+3)]<1`, the exact finite rational Neumann tail is:

```text
|| (1+T)^(-1) - sum_{k=0}^K (-T)^k ||
  <= (40B)^(K+1)/((K+1)!(K+2)!)/(1-r)
```

Diagnostic-only: `B=1,K=30`, `B=10,K=69` and `B=100,K=187` all give tails below `2^-64`. The source's actual analytic multiplication norm B is UNKNOWN; using only real `sup chi<=1` is invalid. The local full verifier also supplies an exact-rational exponential upper tail to implement (B.16) once a source-compliant complex contour bound on `zeta_star` has been produced.

## Newly isolated release-critical Case006 shell mismatch

The original upstream reference cutoff (B.22) makes `partial_y log(phi_r)=0` **exactly after the short cutoff**. Its end lies before `Y=4.1`, while the proposed Case006 strong-Rayleigh shell has `6<=Y_e<=6.1` and thus `Y>=6`. Therefore the reference angular logarithmic shear is exactly zero there. The source's subsequent modified field uses `a=kappa*p1_r` (B.26), NOT the uncontinued Bessel-profile expression `a0(Y_e)`. The Case006 value `a0(6)~10.5207` is an authentic calculation for the *Bessel comparison profile* but is **not yet established** for the actual continuation.

This does not refute the forced construction or prove a negative angular shear; the actual `a=kappa p1_r` and its full-gradient principal flag must be rigorously evaluated. The original H8 and full PDE gates remain OPEN.

## Effective numerical certification is still open

A complete parameter tuple must specify: the original A.5 outer schedule and moment corrections; the hierarchy `M_d,Pstar,lambda,h,j0,delta_star,sigma_star,Omega,rho`; certified complex norms and explicit nonlinear fixed-point contraction constants from (B.14)-(B.15); a source-compliant `Lambda`; certified (B.16) amplitude C; and `t1,kappa0` with complete ninth-jet budget. Only then can a validated interval computation bound `a0,b0,a,b1`, actual continued angular and axial shear, twelve physical four-patch terms and pressure, nine true M_terminal couplings, spectral radius, and terminal singular trace.

The committed Python verifier is an exact partial proof checker, not a substitute for that missing numerical source. The companion JSON release gate records null values for the actual errors and forbids upgrading the unforced theorem. **Main branch is unchanged.**
