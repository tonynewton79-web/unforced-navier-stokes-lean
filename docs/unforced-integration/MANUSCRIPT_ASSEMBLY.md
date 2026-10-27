# A cumulative unforced Navier–Stokes manuscript: verified assembly boundary

25 October 2026. The 188-page supplied historical PDF exists, but its supplied
LaTeX is an *assembly master*, not a complete self-contained source archive.
Rebuilding the entire volume from the available ten attachments has not been
verified. See `SOURCE_ASSETS.md` for the missing files.

## Proposed nine-section journal structure

1. **Introduction and precise open problem.** Viscosity-one periodic torus,
   nonzero initial data, force identically zero, finite kinetic energy, and the
   exact meaning of speed blow-up; distinguish this from the forced upstream
   candidate and from existing open global regularity theory.
2. **Verified local core and scope of analytic hypotheses.** State the exact
   local theorem, pressure assumptions, n=1/2 coefficients and convergence;
   identify which results still depend on unproved source compatibility.
3. **Periodic localization and physical pressure.** One chart-to-torus lift,
   pressure gauge, periodic mean, nonlocal inverse, and actual vector residual.
4. **Carrier geometry and temporal patching.** Seven-ray algebra, two-color
   interactions, phase locking, and nontrivial physical graph-space norms.
5. **Spatial attachment and the H8 boundary.** Exact rational budget
   `15971/122900`, required compact weighted right inverse, potential dual
   obstruction, and a transparent OPEN statement.
6. **Regular correction and coupled fixed point.** Full range, Banach
   completeness, correct physical contraction and controlled pressure.
7. **Global unforced closure and terminal trace.** Formal statement of the
   target and the proof obligations for an actual zero residual and unbounded
   terminal speed. Do not state this as accomplished.
8. **Whole-space transport diagnostics.** Editions XXXIX–XLII: conservation,
   cylinder flux, energy-dissipation obstruction, radial variation and the
   pressure-complete near-axis short-time Gaussian example. These are
   independent whole-space statements, not a torus blow-up mechanism.
9. **Verification and limitations.** Source-matched numerical certificates,
   actual Lean declarations/axiom audit, proof-gate table and references.

## Exact source dependency audit

The attached 188-page LaTeX calls `\\includepdf` on three absent
`part[1-3]_*.pdf` sources, `\\input` on three absent `.tex` inserts, and
`\\includegraphics` on three absent `.png` diagrams. The 16-page local-core
TeX separately calls six `figures/*.pdf` assets, none provided in the
attachment set. The repository's original `paper.tex` is not equivalent to
this supplied historical master; substituting it would change provenance.

There is presently no defensible way to assert a fresh 188-page TeX rebuild
or whole-document visual overlap check from this incomplete asset collection.
The attached original PDF remains a reference edition. A cumulative revised
PDF should be released only when source inputs are recovered and every page
has undergone render, text/formula and figure-overlap review.

## Editorial and mathematical exclusions

- Withdraw the superseded continuous-global-axisymmetry torus account in
  favor of localized lifts and global periodic pressure, subject to proof.
- Do not import forced-source A.11/A.19 claims into an unforced argument
  without a precise theorem dependency and an explicit zero-force bridge.
- Do not reinterpret XLII's initially viscosity-driven positive jet
  derivative in a globally smooth example as terminal blow-up.
- Keep the newest local Lean results identified as **operator identities**
  and candidate **definitions**, not a completed existence theorem.
- Observe the nine-section publication bound and define technical objects
  before their first use; avoid duplicate master-PDF scans or opaque inserts.
