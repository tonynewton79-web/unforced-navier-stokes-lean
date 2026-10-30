# Journal-style H8 research edition: exact scope and 2026 final attack

The independent LaTeX research article is titled **Pressure-driven retention obstructions and exact seven-ray stress geometry**, by Tony Newton (Newton Astro Labs, United Kingdom). It is formatted with the AMS `amsart` class and comprises **eight main sections**, three subsections per section, two fully authored two-dimensional diagrams, and two short appendices. One appendix is titled **Reproducible finite-arithmetic verification**. The journal-style revision supplements the historical 115-page H8 research archive. It does not claim to have solved the full Navier--Stokes problem.

## Main verified result (conditional)

For an anisotropically shrinking carrier `U` with `p=1/2-3h>0` and `||U||²_2=M0*tau^p(1+o(1))`, `||grad U||²_2=R0*M0*tau^(p-1)(1+o(1))`, `R0>p/2`, and an actual smooth finite-energy unforced solution `u=U+w`, assume **local relative L2 retention** and that dyad-integrated carrier-only pressure work plus all nonpressure boundary fluxes are `o(tau^p)`. Define

```
tau = T-t; I_tau=[T-tau,T-tau/2]
delta_tau=tau^(-p/2)*sup_(t in I_tau)||w(t)||_L2(Omega(t)) -> 0
S = U tensor w + w tensor U + w tensor w
pi_c = pi[U+w] - pi[U]
```

Then the exact moving local-energy identity plus boundary-to-volume pressure work and rank-one periodic Fourier multiplier prove

```
sup_(t in I_tau)||grad S(t)||_L2(T3)
  >= c*tau^(p/2-1)/delta_tau.
```

With additional global bounds `||w||_infty<=C tau^-1/2`, `||U||_infty<=C tau^(-1/2-h)`, `||grad U||_2<=C tau^((p-1)/2)`, time-integration and energy balance give

```
int_(I_tau)||grad w||²_2 dt >= c*tau^(1/2-h)/delta_tau².
```

### Strengthening from the journal revision: logarithmic dyadic barrier

For `tau_n=2^-n*tau0`, the **new sharpened necessary condition** is

```
sum_(n>=0) tau_n^(1/2-h) / delta_(tau_n)² < infinity.
```

Proof: sum lower bounds over pairwise disjoint terminal dyads; `sum int ||grad w||² < infinity` follows from `grad w=grad u-grad U`, finite global unforced dissipation and `int ||grad U||²=O(sum tau_n^p)<infinity`. Therefore the borderline rate

```
delta_tau=O(tau^(1/4-h/2)*sqrt(log(1/tau)))
```

is impossible on every sufficiently late dyad. At h=1/10 this excludes `delta_tau=O(tau^(1/5)*sqrt(log(1/tau)))`. The power-only 1/5 exclusion is a weaker special case. This theorem is **conditional** on all stated hypotheses and does not construct a singular unforced solution.

## Exact seven-ray algebra and Lean distinctions

For the one-sided original coefficient floors with `g=15971/122900`, `h_star=22371/122900`, the sharp meridional H8 component cap is

```
|A| <= ((5*g+h_star)/4)*rho = (51113/245800)*rho.
```

The polygon of allowed joint `(A,C)` components has the six rational vertices given in the manuscript. In the source frame, `H=[[-D,C,A],[C,0,B],[A,B,D]]`. This auxiliary seven-ray tensor is **not** the velocity quadratic stress `S`. Connected Lean source includes finite-dimensional cone inequalities, the exact positive center, sharp factor-14 component bound, conditional source-band implications, pressure-compensated radial identity and rotating-frame matrix product/connection identities.

**Kernel statement boundary:** Those algebraic and conditional identities do not establish the original Case006 source, spatial compact positive stress inverse, complete periodic mixed/exterior pressure, actual zero-forcing correction, or terminal retention. The repository's `proof_gates.json` marks the full theorem OPEN. New H8 module hosted CI must still finish and be independently checked before claiming the branch is fully kernel-verified.

## Reproduction and journal review

The published-chat research packet contains `H8_Pressure_Retention_JAMS_Research.tex`, a compiled PDF, `verify_h8_research.py` (10 tests passing locally), verification JSON, and the retained historical 115-page paper. The new LaTeX is self-contained for compilation with standard AMS-LaTeX/TikZ.

**Journal-facing status:** typeset in AMS style, not represented as an accepted or submission-complete JAMS article. The headline theorem is a conditional obstruction; originality and suitability for a high-selectivity journal require independent peer evaluation. This journal article does not claim an unforced Navier--Stokes finite-time blow-up example.
