# Attack 102 — source-native quadratic torque and physical chart correction

**22 November 2026 | Tony Newton**

**Result:** exact source-derived quadratic torque identity, rigorous curved-shell rational bound, nonzero smooth quadratic torque kernel, and an explicit source-coordinate handoff countercontrol. **NOT A FULL UNFORCED NAVIER–STOKES THEOREM OR END-TO-END LEAN PROOF.**

## Original source provenance

The original 122-page Case 006 SHA256 is `56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758`. Reopen equations (199), (209), (250)–(252), and Appendix AF equation (3); also the original upstream B.25/B.26 continuation. The original H8 source and four-patch preparation remain separate.

The source writes, in its expansion regime, `G(Y,eta)=Ustar(eta)-Y*M(eta)/(2 Lambda)+O(Lambda^-2)`, where `M=Zstar/L`, `L=1-2 h eta²`, `Y=Lambda R²/2`, `R=r/sqrt(1-t)`. Define the exact remainder `E=G-Ustar+M R²/4`, so **exactly**

    G(R,eta)=Ustar(eta)-M(eta)*R²/4+E(R,eta).

The displayed big-O is NOT a frozen numerical bound. The post-cutoff source G must be matched to this same profile before numerical promotion.

## Theorem 102.1 — exact quadratic torque reduction

For `M_k(eta)=integral R^k tau(R,eta)dR` (k=2,3,4), `N=integral R² G tau dR`, `E2=integral R² E tau dR`,

    N=Ustar*M2-(M/4)*M4+E2.

Thus `M2=N=0` forces `(M/4)*M4=E2`, NOT `M3=0`. If `E=0` and `M!=0`, the two conditions are `M2=M4=0`.

**Smooth nontrivial positive control:** for any nonzero smooth compact `phi>=0` supported on a radial interval, project `R` orthogonally onto span{1,R²} for measure `dmu=R² phi dR`, yielding coefficients a,b. Then `tau=phi(R)*(R-a-bR²)` has `M2=M4=0` and `M3=||R-a-bR²||²_L²(dmu)>0`. The Gram matrix is positive definite. A distinct polynomial diagnostic `phi=(R-1)^4(3-R)^4` has `a=130257/127349, b=30511/127349, M3=12873472/5736435705` exactly. The latter is NOT smooth to all orders at its endpoints, but the projection theorem is.

## Theorem 102.2 — exact nonaffinity on the actual curved shell

Choose the shell `s=chi(eta)*Lambda*R²/2 in [6,61/10]` and centre `s0=121/20`. Put

    Rc=sqrt(121/(10 chi Lambda)),
    g0=Ustar+(M/4)*Rc²,
    g1=-M*Rc/2,
    e=E-(M/4)*(R-Rc)².

Then `G=g0+g1*R+e` and, for M!=0,

    e/g1 = (R-Rc)²/(2Rc) - 2E/(M Rc).

Rational comparisons `(239/240)² < 120/121` and `122/121 < (241/240)²` yield the strict shell enclosure `|R-Rc|<Rc/240`. Therefore

    |e/g1| <= Rc/115200 + 2|E|/(|M|Rc).

This is an evaluated **source-specific quadratic term**; the actual E remains unmeasured. It is not permissible to insert an invented value of its O(Lambda^-2) prefactor.

## Theorem 102.3 — near-affine torque-moment suppression

If `M2=N=0`, `M!=0`, and `||E||infty<=epsilonE` on that shell, put `Ltau=integral R²|tau|dR`. The exact identity `R^4-2Rc*R³+Rc²*R²=R²*(R-Rc)²` and Theorem 102.1 give

    |M3| <= [Rc/115200+2 epsilonE/(|M|Rc)]*Ltau.

This is a **conditional necessary estimate on the true source coordinate**. It is sharp enough to test against a future authenticated angular flux pairing but cannot decide feasibility without source E, physical tau and the correct flux Jacobians.

## Critical correction to the proposed Attack101 nonaffinity equality

The Appendix AD diagnostic uses a radial coordinate `r_d in (1,3)`, whereas the actual curved shell is narrow in similarity radius. On an affine physical mapping `R=Rc+ell*(r_d-2)=a+ell*r_d`, a diagnostic amplitude tau_d transported unchanged gives

    M2_phys=ell*(a²*M0_diag+2*a*ell*M1_diag+ell²*M2_diag).

Thus diagnostic M2=0 DOES NOT imply physical M2=0, nor do the test weight q_b and right-hand constant `2|beta|rho0 I0` transfer unchanged. Exact discrete witness: diagnostic masses (4,-1) at r_d=(1,2) have M2_diag=0; with Rc=2, ell=1/10 the physical M2 is 261/250, nonzero. The genuine full source chart must include the velocity amplitude and stress/flux measure.

## End-to-end formal release gate

1. Freeze one source-admissible Lambda, chi, j0, h, full continued G and E with a numerical interval constant, on the exact physical shell.
2. Freeze the actual toroidal, poloidal and all four C4 patch maps, twelve mixed stress terms, pressure gauge, angular fluxes and physical torque moments.
3. Prove one compact **weighted H8 inverse** with strict seven-ray floor across all flat boundaries.
4. Prove nine-jet nonlinear residual bounds, zero unforced force, the periodic Poisson pressure and terminal singular trace.
5. Kernel-check the entire Navier–Stokes PDE and blow-up implication in Lean using any external numerical certificates that are separately validated.

Only algebra and exact discrete moments have been staged in the Attack102 Lean file. **No full PDE Lean release exists in this branch; the complete Millennium result remains unproved.** The public Alpöge–Buckmaster claim dated 20 November 2026 has its own Lean project and an unreleased numerical certificate according to its GitHub README. Its priority and independent validity must be evaluated separately from these source-local results.

## Verification

`research/attack102/verify_attack102.py` and `verify_attack102_independent.py` replay 54,000 exact rational / symbolic torque, nonaffinity, shell and chart tests. The accompanying local PDF and editable TeX provide continuum proofs; GitHub CI does not prove them by merely checking the algebra. The source gate deliberately records null numerical E and all outstanding physical and Lean PDE obligations.
