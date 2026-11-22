# Attack 92 — ordered source existence versus an effective numerical certificate

**Date:** 22 November 2026  
**Research scope:** upstream **forced** reference continuation + Tony Case006 companion wedge.  
**Result:** conditional-on-source-uniformities non-effective existence and sharper rational sign margins.  
**Not proved:** any source-certified *finite numerical* tuple, full unforced 3D Navier–Stokes blow-up or end-to-end Lean PDE theorem.

## Authenticated sources

- OpenAI, *Finite Time Blowup for Navier--Stokes*, Appendix B.2–B.6, specifically (B.13), (B.18), (B.22), (B.24), (B.25), and (B.26): https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
- Tony Newton, 122-page *Carrier-Independent Structured Stress Route: Case006*, especially Proposition 9.20 and equations (255)–(257), SHA256 `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`.
- Prior Attack91 source-wedge theorem (on branch `feature/attack91-companion-pressure-wedge-20261122`). This theorem assumes source-admissible `0<h<=1/100`, `0<j=j0<=1/20`, `Pstar>=2`, `0<sigma*<=j/4` and states on `I_j=[-j/7,-j/9]`: `M=Z*/L>163j/45`, `D eta+U*>=5j/14`, `chi>16/25`. The imported Attack88 bound is `M'<-13` for the specified pressure family. **They are imported mathematical hypotheses; not inferred from O-notation alone.**

## Exact value and derivative transfer

The source defines `X partial_X n_s,r+n_s,r=S_n,r/L`, `X0=4/Lambda`, `L=1-2h eta²`, `M=Z*/L`. Let
```
a0=sup_eta |n(X0,eta)-M(eta)|
a =sup_eta |partial_eta n(X0,eta)-M'(eta)|
b0=sup_(X,eta)|S_n,r-Z*|
b1=sup_(X,eta)|partial_eta(S_n,r-Z*)|.
```
For `|eta|<=1/4`, `h<=1/6`, the bounds `L>=47/48`, `|L'|<=1/6` imply **exactly**
```
||n-M||_inf<=max(a0,(48/47)b0).
||partial_eta n-M'||_inf<=max(a,(48/47)b1+(384/2209)b0).
```
These are deterministic integrating-factor estimates with no discretization.

## New ordered existence theorem (NON-EFFECTIVE)

The upstream axis comparison (B.18) and source continuation proof following (B.24) give, after the outer and axis data are fixed, `a0,a=O(1/Lambda)` and, for fixed axial derivative orders,
```
b_k<=A_k/Lambda+B_k(Lambda)/C²+omega_k(t1;Lambda,C), k=0,1,
omega_k(t1;Lambda,C)->0 as t1->0 for fixed Lambda,C.
```
The published constants are unspecified. Interpret the estimates with finite majorants independent of the subsequent parameters in exactly this stated order.

1. Fix the source-admissible outer/axis hierarchy `h,j,delta*,sigma*,Omega` first, with `sigma*<=j/4`.
2. Increase Lambda sufficiently so every `A/Lambda<j/12`, retaining the source's analytic threshold.
3. Increase C sufficiently (also `C>=C0(Lambda)`) so every `B_k(Lambda)/C²<j/12`.
4. Choose the B.5 shear parameter `0<kappa0<1/2` using its t1-uniform family bound and then take t1 sufficiently small that `omega_k<j/12`, preserving B.22/B.26 and B.5 conditions.

Therefore *some ordered finite choice exists* with `a0,a<j/12`, `b0,b1<j/4`. The transfer estimates and earlier source-family bounds yield
```
||n-M|| < 12j/47
||partial_eta n-M'|| < 660j/2209
n_s,r > (163/45-12/47)j = 7121j/2115 > 0
partial_eta n_s,r < -13+(660/2209)j < -129/10.
```
On the Case006 shell where B.26 persists and `kappa>=kappa0>0`,
```
G_R < -(kappa0/2)*(7121/2115)*j*sqrt(12/Lambda)<0.
```
This is a **non-effective source-existence** result for the prescribed reference continuation, not a published rigorous interval tuple and not full H8 closure.

## Why numerical a0,b0<=j remains unverified

An assertion `e(Lambda)=O(1/Lambda)` without its coefficient admits **every** finite prefactor `A`; for an arbitrarily proposed finite `Lambda*` choose `A=2j Lambda*` and obtain `e(Lambda*)=2j>j` while preserving `O(1/Lambda)`. Analogous objections apply to `O(C^-2)` and `o_t1(1)`. These are abstract countercontrols to inference, **not alternative genuine upstream PDE profiles**.

An effective numerical certificate requires source-specific interval enclosures for the axis fixed point (B.14–B.15), smooth outer schedule, pressure integral (B.24), the signed source S_n,r and its eta derivative, and numerical choices in the order given. The paper supplies the qualitative existence proof, not their numerical values.

## Further full-PDE gates

Actual nine-jet radial cutoff and moving-frame norms, four authentic transported patch fields, twelve ordered mixed terms and pressure, the nine true M_terminal operator norms, spectral radius, and terminal singular trace: **OPEN**. Upstream source itself is a forced blow-up construction. The unforced Millennium question is **NOT** solved by this research.

## Reproducibility

`python research/attack92/verify_attack92.py` uses only Python stdlib exact Fractions, with 12,000 conditional hierarchy tests, 15,000 integrating-factor checks, 5,000 adversarial big-O controls, and a fail-closed JSON gate in `research/attack92/source_gate.json`. It does not sample, infer, or replace the missing physical source data. Dedicated CI success, if achieved, means **finite conditional algebra only**, not Lean kernel formalization or PDE theorem.
