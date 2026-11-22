# Attack 91 — explicit source-native pressure wedge on one admissible axial interval

**22 November 2026 · Tony Newton**  
**Status:** ONE_SIDED_PRESSURE_FAMILY_ENCLOSURES_PROVED / ACTUAL_SOURCE_ERROR_ENCLOSURES_OPEN.  
**Full unforced Navier–Stokes theorem:** OPEN. This file does not certify a physical blow-up solution.

## Exact source provenance

The user-owned 122-page Case 006 source, equations (199)–(210), (255)–(257), Proposition 9.20 (SHA-256: `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`). Upstream OpenAI *Finite Time Blowup for Navier–Stokes*, Appendix A.4, Lemma A.5 and Appendix B.5–B.6 (B.25–B.26) describes a **forced** solution:
https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

The original pressure is `Pi0(eta)=-1/2 int_R c(y)^2 (1+eta^2)^(-2theta(y))dy`, with `0<=theta<=1`, and on the inner segment `y<=0`, `c(y)^2=P_*^2 exp(y/5)` and `theta=1`. The nonnegative outer moments need not be guessed. Define `J_k=int theta^k c^2 (1+eta^2)^(-2theta)dy`. Then `Pi0=-J0/2`, `Pi0'=2eta J1/(1+eta^2)`, `Pi0''=2[(1-eta^2)J1-4eta^2J2]/(1+eta^2)^2`, with `0<=J2<=J1<=J0` and `J0,J1>=5P_*^2/(1+eta^2)^2`.

## Theorem A — source-family companion-compatible interval

Assume `0<h<=1/100`, `0<j=j0<=1/20`, `P_*>=2` and `0<sigma_*<=j/4`. Set `I_j=[-j/7,-j/9]`, `alpha=1/2+h`, `D=1/2-h`, `d=1-eta^2`, `U_*=4eta+j`, `H_*=D eta+d U_*`, `L=1-2h eta^2`, `chi=H_*^2/(H_*^2+sigma_*^2)`, `M=Z_*/L`, where `Z_*=-alpha(1-2eta U_*)U_*-4H_*-d Pi0'+4alpha eta Pi0`.

**For every eta in I_j**,
- `H_*>j/3`, `D eta+U_*>=5j/14`;
- `chi>16/25 > chi_c ≈ 0.28234558927`;
- `Pi0''>9P_*^2` (one-sided exact inner-pressure estimate);
- `Z_g>-3j`, `Z_p>298j/45`, `M>163j/45`;
- the physical strong-Rayleigh shell `6<=Y_e=chi Y<=6.1` satisfies `6<=Y<=305/32<26`.

**Complete rational proof:** for eta=-jx, x in [1/9,1/7], eta²<=1/19600. The bounds `3j/7<=U_*<=5j/9` and `H_*/j >= (3/7)(19599/19600)-1/14=48997/137200>1/3` imply the first claims. The geometric pressure-free term satisfies
`Z_g >= -[(51/100)(2521/2520)(5/9)+20/9]j = -378857j/151200 >-3j`.
The inner-moment pressure contribution obeys
`Z_p>=10(-eta)P_*²[(1-eta²)/(1+eta²)^3+alpha/(1+eta²)^2]`.
For z=1/19600, `(1-z)(1-3z)+(1/2)(1-2z)=576142003/384160000>149/100`; hence
`Z_p>(149/90)P_*²j>=298j/45`.
As L in (0,1], this implies M>163j/45. Nonnegative outer curvature for eta²<1/5 and the explicit inner curvature
`10P_*²(1-5eta²)/(1+eta²)^4` give Pi0''>9P_*².

## Corollary B — conditional source-transfer with same interval

On the actual upstream B.25 reference equation `X partial_X n+n=S/L`, put `X0=4/Lambda` and
`a0=sup_(eta in I_j)|n(X0,eta)-M(eta)|`, `b0=sup_(X0<=X<=110,eta in I_j)|S-Z_*|`.
Integrating factors give
`||n-M|| <= max(a0,48 b0/47)`.
If the **actual source** satisfies `a0<=j` and `b0<=j`, then
`n>(163/45-48/47)j=5501j/2115`.
Where B.26 holds with kappa>=kappa0>0 and Y=Lambda R²/2,
`G_R=-kappa n R/2 <= -(kappa0/2)(5501/2115)j sqrt(12/Lambda)<0`.
This is a conditional continuation result, **not a numerical certification of a0,b0**.

The previous Attack90 fixed interval gave an inadmissible companion sign. The new I_j has the same sign margins on one interval and requires smallness **relative to j0**, not the previous loose <=1 gate.

## Missing numerical/physical data

Source Lemma B.4 gives asymptotics `O(Lambda^-1)+o_(t1)(1)+O(C^-2)` with unspecified constants and ordered parameters. The source still lacks a **single frozen complete numerical tuple** to rigorously interval-evaluate `a,a0,b0,b1`, the **upper** bounds of Pi0,Pi0',Pi0'', and the post-cutoff E/nine-jet source. Consequently the physical four transported patches and twelve nonlinear cross terms, full periodic Leray pressure, all nine operator norms of M_terminal, spectral radius and singular trace remain unproved. Do **not** turn the above lower enclosures into a fabricated two-sided table.

## Verification

Run `python research/attack91/verify_attack91.py`. The script independently checks every rational comparison and 12,000 adversarial pressure-moment cases plus 2,000 second-curvature cases. The analytic proof above is independent of sampling. JSON `research/attack91/source_release_gate.json` refuses promotion of missing source data. GitHub Actions success, when present, covers finite arithmetic only and is **not** a Lean kernel PDE certificate.

The full editable LaTeX paper and PDF are distributed as a separate ChatGPT research artifact to accompany this GitHub proof ledger.
