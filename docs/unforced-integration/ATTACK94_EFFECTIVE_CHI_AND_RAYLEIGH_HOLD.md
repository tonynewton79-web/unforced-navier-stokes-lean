# Attack 94 — an effective source-native analytic multiplier bound and a Rayleigh transfer incompatibility

**Tony Newton | 22 November 2026**  
**Result:** exact continuum coefficient estimate, conditional factorial inverse-tail, and a **source-to-Case006 incompatibility** for the unmodified upstream B.26 continuation.  
**Final status:** CERTIFIED_CHI_MULTIPLIER__RAYLEIGH_TRANSFER_INCOMPATIBLE__FULL_SOURCE_HOLD. No unforced Navier--Stokes singularity proof.

## Exact sources and vocabulary

- Original 122-page Tony Case 006, section 9.3.1 and 9.3.3, equations (183)--(210) and Appendix B.10, SHA256 `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`.
- OpenAI, *Finite Time Blowup for Navier--Stokes*, **FORCED** result, Appendix B, especially equations (B.1)--(B.9), (B.22), (B.25), (B.26), Lemma B.4 and Proposition B.5:
  https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

The actual source axes are `U*=4eta+j`, `D=1/2-h`, `H*=(4+D)eta+j-4eta^3-j eta^2`, and `chi=H*^2/(H*^2+sigma^2)`. The source's small sigma is a **positive** parameter fixed only after j and the pressure selection. In the following all conclusions are valid whenever `0<h<=1/100`, `0<j<=1/20`, and `0<sigma<=j/4`, with any extra upstream source conditions unchanged.

## Theorem 94.1 — source's actual B_rho multiplier is explicitly bounded

Take a real parameter interval containing [-1,1] but lying within [-1.0001,1.0001]. Put `delta=sigma/170`, choose `0<rho<=delta/2`, and ensure the closed rho-neighborhood also lies inside the source's prescribed pressure-analytic domain. For every real x in the interval and every complex z with |z-x|<=delta, `|z|<1001/1000`, hence

```text
|H*'(z)| <= 9/2 + 12(1001/1000)^2 + (1/10)(1001/1000) < 17,
|H*(z)-H*(x)| <= 17 delta = sigma/10.
```

Because H*(x) is real, `|H*(x) +/- i sigma|>=sigma`, so
```text
|H*(z) +/- i sigma| >= 9 sigma/10,
|chi(z)| = |1 - sigma^2/[(H*(z)-i sigma)(H*(z)+i sigma)]|
          <= 1 + 100/81 = 181/81.
```

Similarly `|L(z)|<103/100`, `L=1-2h z^2`, and the partial-fraction identity `H/(H²+sigma²)=(1/2)[(H-i sigma)^-1+(H+i sigma)^-1]` gives `|zeta*(z)| <=103/(90 sigma)` for source `zeta*=-L H/(H²+sigma²)`.

Cauchy's integral bound: `|d_eta^beta chi(x)| <= beta! (181/81) delta^-beta`; similarly `|d_eta^beta zeta*(x)| <= beta! [103/(90sigma)] delta^-beta`.

The exact source (B.4) coefficient norm for a Y-independent function f is
```text
||f||_B_rho = sup_beta sup_{eta in I} |d_eta^beta f(eta)| rho^beta (beta+1)^2 / beta!.
```
Since `rho<=delta/2` and `sup_beta (beta+1)^2/2^beta = 9/4` (attained at beta=2), it follows that
```text
||chi||_B_rho <= (181/81)(9/4) = 181/36,
||zeta*||_B_rho <= (103/(90sigma))(9/4) = 103/(40sigma).
```

From the source's B.7 convolution estimate, the B_rho Banach algebra product constant is `Csq^2` with `Csq=8 sum_(n>=1)n^-2<40/3`. Here the elementary integral comparison gives `sum_(n>=1)n^-2<5/3`, requiring no numerical pi approximation. Thus **the actual multiplication operator** obeys
```text
Mchi = ||f -> chi*f|| <= (40/3)^2*(181/36) = 72400/81 < 900.
```

This is source-specific and independent of Pstar, C, Lambda and the small sigma *after the radius rho has been scaled with sigma*. It is **not a norm bound for the entire nonlinear fixed point**.

## Corollary 94.2 — one effective inverse-tail certificate

For `T=J2 circ Mchi/2`, source equation (B.9) yields `||T^k||<=(40Mchi)^k/(k!(k+1)!)`. Put `B=72400/81`, `K=528`, `r=40B/[(K+2)(K+3)]<1`. An exact rational comparison gives
```text
|| (1+T)^(-1) - sum_(k=0)^528 (-T)^k ||
  <= [(40B)^529/(529!530!)]/(1-r) < 2^-64.
```
This closes only the factorial inverse truncation, not the source's nonlinear Lipschitz/axis majorants.

## Theorem 94.3 — the actual continued shear is incompatible with Case006's Bessel patch

Case006 equations (183)--(207) choose a curved shell `6<=Ye=chi*Y<=6.1` and require Bessel comparison exponent `a>=10`, giving `a0(6)=10.520747... `. For the companion-compatible wedge `I_j=[-j/7,-j/9]`, Attack91 independently proves `chi>16/25`. Consequently
```text
6<=Y<= (61/10)/(16/25)=305/32<100,
X=Y/Lambda<100=Xb for Lambda>=1.
```

The upstream B.22 reference cutoff ends before `Y=4.1`. Therefore **every point of this shell is after the first shear activation but before Xb**. Appendix B.6 explicitly keeps B.26 with `kappa=kappa0` on that interval, and then requires **before the Xb interpolation** that `kappa0 sup p1,r < 4/5`. Therefore the actual B.26 shear there is
```text
a = kappa0*p1,r < 4/5 < 2 < 10.
```

The Case006 Appendix B.10 discriminant for the **same angular logarithmic-shear definition** is `Phi_R=2 F^2(2-a)`, hence `Phi_R > (12/5)F^2>0` wherever F!=0. That is the opposite sign of the required Rayleigh-negative shell. Moreover, the original Bessel comparison profile is only justified on the analytic-axis range `Y<=4.1`, whereas the proposed shell begins at Y>=6.

This proves a **no-transfer result for the specific B.26 source continuation**. It does NOT rule out a different continuation, later source-matched transformation, a separately constructed strong-Rayleigh carrier, or blow-up in general. Such alternatives need an explicit replacement field, a new full source and pressure verification, and separate source-native nine-jet estimates.

## Why the complete outer exterior remains unfrozen

The original Appendix A.2--A.10 outer schedule couples radial moments, amplitude and nonlinear corrections, and the source does not identify one fully specified numerical schedule with certified complex norms and moment corrections. The B_rho chi bound does not construct these outer fields. The actual value/derivative errors a0,b0,a,b1, nine-jet stress, complete four-patch mixed pressure, nine coupling blocks of M_terminal, and singular-trace theorem remain OPEN.

A new full-PDE construction cannot validly import `a0(6)>10.52` from the Bessel comparison and simultaneously import B.26 on Y>=6. One of those ingredients must be replaced and independently certified.

## Reproducibility and release discipline

`python research/attack94/verify_attack94.py` checks the exact rational constants, factorial tail, and 16,000 rational companion geometry probes. The independent analytic argument above proves the continuum bounds. The JSON release gate keeps all outer/PDE claims unverified. Passing CI on finite arithmetic or Lean rational algebra is **not** a proof of the unforced Millennium problem. Main is unchanged.
