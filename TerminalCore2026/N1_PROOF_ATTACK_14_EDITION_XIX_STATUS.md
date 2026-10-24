# Edition XIX / Proof Attack 14: second projected correction

**24 October 2026 — finite algebra independently checked; full unforced PDE OPEN.**

This extends the Edition XIII first Stokes correction and Edition XIV local Picard analysis. It neither derives nor asserts a full unforced finite-time Navier–Stokes singularity. The original OpenAI Navier–Stokes source profile comes from a **forced** construction.

## The exact two-stage residual

Let \(u_B\) be a *genuine*, smooth, solenoidal periodic background, with the *full* physical residual
\[
R_B=\partial_tu_B-\nu\Delta u_B+(u_B\cdot\nabla)u_B+\nabla p_B.
\]
Let \(F=\mathbb P R_B\), \(L=\partial_t-\nu\Delta\), \(B(a,b)=\mathbb P[(a\cdot\nabla)b]\), and \(S(t)=\exp(\nu t\Delta)\) on solenoidal fields. On a time slab starting at \(t_0\), set
\[
w_1(t)=-\int_{t_0}^t S(t-s)F(s)\,ds,\quad
Q_1=B(u_B,w_1)+B(w_1,u_B)+B(w_1,w_1),
\]
\[
w_2(t)=-\int_{t_0}^t S(t-s)Q_1(s)\,ds.
\]
Provided the integrals make sense, \(Lw_1=-F,\ Lw_2=-Q_1\), and \(w_1(t_0)=w_2(t_0)=0\). Biadditivity (without any symmetry of \(B\)) yields the *exact* identity
\[
\boxed{\mathbb P R(u_B+w_1+w_2)=Q_2}
\]
where
\[
Q_2=B(u_B,w_2)+B(w_2,u_B)+B(w_1,w_2)+B(w_2,w_1)+B(w_2,w_2).
\]
The complementary gradient must be removed by a **compatible physical pressure**; the actual source pressure is not constructed by this note.

Under genuine operator estimates \(\|B(a,b)\|_Y\le C_B\|a\|_X\|b\|_X\) and \(\|L^{-1}\|_{Y\to X}\le K\), setting \(A=\|u_B\|_X,\ U=\|w_1\|_X,\ V=\|w_2\|_X\) gives
\[
V\le KC_B(2AU+U^2),\quad
\|Q_2\|_Y\le C_B[2(A+U)V+V^2].
\]
No authentic source values of \(K,C_B,A,U\) have been certified on shrinking terminal slabs.

## Independent relative-energy diagnostic

For an *exact* unforced \(u=u_B+w\), with \(w(t_0)=0\), integration by parts on the torus gives
\[
\tfrac12\partial_t\|w\|_2^2+\nu\|\nabla w\|_2^2
=-\int (w\cdot\nabla u_B)\cdot w\,dx-\langle F,w\rangle.
\]
With \(M(t)=\|\operatorname{sym}\nabla u_B(t)\|_{L^\infty,\mathrm{op}}\) and \(G(t)=\|F(t)\|_2\),
\[
\|w(t)\|_2\le\int_{t_0}^t
\exp\left(\int_s^tM(r)\,dr\right)G(s)\,ds.
\]
If \(M(t)\le K_0(1-t)^{-1-h}\) on the slab, \(h>0\), the exponential factor has exponent at most
\[
(K_0/h)\{(1-t)^{-h}-(1-s)^{-h}\}.
\]
It tends to \(K_0\log((1-s)/(1-t))\) as \(h\to0^+\). This is a **possibly weak upper bound**, not proof that any correction grows or cannot exist; it highlights that an isotropic relative-energy argument may not preserve the singular carrier without a source-specific cancellation/anisotropic estimate.

## Verification record and gates

- Independent exact Fraction test: **15,625/15,625** nonsymmetric bilinear examples.
- Two adversarial omissions of distinct mixed bilinear terms correctly fail.
- Smooth periodic solenoidal 3D trigonometric manufactured-field convection identity passes symbolically.
- Independent derivative and \(h\to0\) checks of relative-energy kernel pass.
- Lean \`N1SecondProjectedCorrection.lean\` formalizes **finite abstract biadditive algebra only**, subject to completed pinned CI. It does not formalize the physical semigroup or the source.
- Standalone CI \`n1-second-correction.yml\` tests this specific module and its independent replay without requiring earlier terminal-core modules to compile first.

**Unproved next gates:** actual full source \(F=\mathbb P R_B\) on all transition collars; pressure matching; weighted source-compatible \(L^{-1}\) and nonlinear bilinear constants; \(Q_2\) genuinely small on shrinking terminal slabs; further iteration and convergence; Appendix A/B source data, 3D unforced residual exactly zero, nonzero smooth initial data, singularity persistence and a final no-escape-hatch Lean theorem.

The separate \`TwoDerivativeWeight.lean\` natural-index fix is already on the research branch, but its full terminal-core CI completion must be assessed independently. A green finite-algebra job is **not** an end-to-end PDE proof.
