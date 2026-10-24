# Edition XXII — circulation maximum-principle gate
24 October 2026 | **Restricted source-specific obstruction, not a solution of Navier–Stokes**

## The established law being applied

For a smooth axisymmetric unforced solution \(u=u_r e_r+u_\theta e_\theta+u_z e_z\) on \(\mathbb R^3\), set \(\Gamma=r u_\theta\). Its physical angular equation implies
\[
\partial_t\Gamma+u_r\partial_r\Gamma+u_z\partial_z\Gamma
=\nu(\partial_{rr}\Gamma-r^{-1}\partial_r\Gamma+\partial_{zz}\Gamma).
\]
The standard axisymmetric circulation maximum principle gives \(\|\Gamma(t)\|_\infty\le\|\Gamma(t_0)\|_\infty=:M\), under the usual comparison-principle spatial regularity/decay and bounded-circulation hypotheses. Smooth compactly supported axisymmetric initial data satisfy the initial boundedness requirement. **This maximum principle is classical prior art**; see *Quantitative Control of Solutions to the Axisymmetric Navier-Stokes Equations in Terms of the Weak L^3 Norm*, *Annals of PDE* (2023), DOI 10.1007/s40818-023-00156-7, Eq. (49). The unforced axisymmetric regime is essential.

## New restricted application to the exact source exterior

The *source-leading* exterior heat profile of Edition XX is \(U_B(r,t)=\tau^{-A}f(r/\sqrt{\tau})\), \(\tau=1-t\), \(A=1/2+h\), \(h>0\), with \(f(R)>0\) for every fixed \(R>0\) in the source exterior. For \(r_\tau=R\sqrt{\tau}\), its circulation is
\[
\Gamma_B(r_\tau,t)=r_\tau U_B(r_\tau,t)=R f(R)\tau^{-h},
\]
which diverges as \(\tau\downarrow0\).

**Conditional leading-cancellation theorem.** Let \(u=u_B+w\) be an actual smooth axisymmetric *unforced* solution with bounded initial circulation and the standard maximum-principle hypotheses. Fix an exterior similarity point \(R>0\) and a compatible axial chart, and assume the *fully chosen background* obeys
\[
(u_B)_\theta(r_\tau,z_\tau,1-\tau)=\tau^{-A}[f(R)+\delta(\tau)],
\quad \delta(\tau)\to0.
\]
The maximum principle implies the explicit estimate
\[
\left|\tau^A w_\theta(r_\tau,z_\tau,1-\tau)+f(R)\right|
\le |\delta(\tau)|+\frac{M}{R}\tau^h.
\]
Thus \(\tau^A w_\theta\to-f(R)\): the correction must cancel the source-leading exterior swirl **to leading relative order**. Any axisymmetric correction with \(\tau^A w_\theta=o(1)\) on such a chart is impossible. In particular the specific positive \(\tau^{-h}\) circulation-growth signature cannot survive in an axisymmetric unforced solution with bounded initial circulation.

The result neither excludes other singularity mechanisms, nor nonaxisymmetric corrections, nor a final profile whose leading swirl cancels but whose other components become singular. It also does not prove the as-yet-unverified fully matched source has the indicated pointwise asymptotics.

## Forced circulation budget

For an axisymmetric **forced** solution with physical azimuthal source \(F_\theta\), the scalar equation gains \(rF_\theta\). The maximum principle with a source gives
\[
\|\Gamma(t)\|_\infty
\le M+\int_{t_0}^t\|rF_\theta(s)\|_\infty\,ds,
\]
when the weighted forcing is time-integrable on compact slabs. If the full forced field preserves at a source point at least half the leading circulation, then necessarily
\[
\int_{t_0}^{1-\tau}\|rF_\theta(s)\|_\infty ds
\ge\frac{R f(R)}2\tau^{-h}-M.
\]
Hence **any** axisymmetric forced realization retaining that source circulation requires a diverging cumulative weighted azimuthal source budget as \(\tau\to0\). This is a necessary bound, not an evaluation of the actual forcing in the published source.

## A precise nonaxisymmetric escape channel

In general cylindrical coordinates, \(\Gamma=r u_\theta\) satisfies, for \(r>0\),
\[
(\partial_t+u_r\partial_r+(u_\theta/r)\partial_\theta+u_z\partial_z)\Gamma
=\nu(\Delta\Gamma-2r^{-1}\partial_r\Gamma)
+\frac{2\nu}{r}\partial_\theta u_r-\partial_\theta p+rF_\theta.
\]
Thus the source responsible for violating the *axisymmetric* circulation maximum principle includes angular meridional derivatives and angular pressure gradients. This formula is exact, but \((2\nu/r)\partial_\theta u_r\) may be singular as \(r\to0\) even for smooth Cartesian nonaxisymmetric velocities; **we do not assert a global \(L^\infty\) estimate from this equation without further axis-compatible bounds.**

## Independent tests and Lean scope

Independent SymPy differentiation checks the axisymmetric and nonaxisymmetric cylindrical identities, including viscous cross terms. The similarity exponent is checked exactly. A seeded, 50,000-case Fraction audit checks the finite circulation/correction budget, with a test at the physical \(h=1/100\) scaling on \(\tau_k=2^{-100k}\). The finite Lean declaration N1CirculationScalar.lean verifies only the conditional real-algebraic implication. The PDE maximum principle, the source gamma mixture, true physical evolution and any blow-up conclusion are **not** formalized in Lean by that scalar file.

**Updated research decision:** A source-preserving, axisymmetric, perturbatively small relative correction is ruled out by this specific circulation argument. The proof programme must demonstrate either a genuinely different terminal singularity whose leading circulation is compatible with the maximum principle, or a nonaxisymmetric mechanism with explicit pressure/angular terms and a full independent PDE certificate. The complete unforced theorem and end-to-end Lean proof remain OPEN.
