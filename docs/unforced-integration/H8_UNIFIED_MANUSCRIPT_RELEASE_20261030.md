# H8 unified manuscript layout and proof-status record

This is the presentation record for the original 114-page cumulative **working research snapshot**, not a declaration that the Navier--Stokes problem is solved.

## Single-front-matter presentation

The editable LaTeX master is `manuscript/Unforced_Navier_Stokes.tex`. It has exactly one `\\author` declaration, one `\\maketitle`, one `\\begin{abstract}` and one email address. Its running header is `H8 RESEARCH MASTER` instead of a repeated author name.

The consolidated 114-page working PDF was rebuilt from the 114-page Appendix AC research snapshot with the following source-page opening conversions:

| Original cumulative page | Unified appendix opening |
|---|---|
| 57 | E: Exterior-Pressure Analytic Radius and the Projected Linear-Carrier Gate |
| 61 | F: Authentic Terminal-Core Translation Mode and H8 Retention Gate |
| 64 | G: Periodic H8 Translation Projection and Nonlinear Modulation |
| 67 | H: Source-Frozen Projection and Terminal Modulation Gate |
| 72 | J: Translation-Mode Energy Ledger and the Remaining H8 Spectral Gate |
| 84 | Q: Two-Mode Terminal-Dyad Compatibility for Compact H8 Carriers |
| 90 | T: The Moving-Core Energy-Transfer Gate |
| 93 | U: Anisotropic Interface Transport and Pressure-Oscillation Threshold |

The interiors retain their abstract/scope **paragraphs**, source equations, proofs and test results. Standalone author, affiliation, email and `Abstract` heading blocks were removed; historical affiliation footnotes on pages 60, 66 and 84 were removed. The repeated Appendix U title on page 94 was removed, and running page numbers normalized. The overall author and abstract remain on page 1.

These page indices refer to a cumulative **PDF presentation snapshot** assembled from previously verified sections and appendices. This PDF is **not** a full native compilation from the latest GitHub LaTeX tree; the tree is the authoritative editable source.

## Checks and release boundary

- The assembled PDF contains 114 pages; 5-word shingles from the substantive source-page content are all retained, with every page exceeding 90% measured coverage and the actual measured minimum 100% for the filtered text regions.
- No page after the front cover contains `Tony Newton`, `Newton Astro Labs`, `tony.newton79@gmail.com`, or the standalone `Abstract` heading.
- The GitHub source still has a single author and abstract; appended mathematical TeX inclusions are preserved.
- PR #5 remains draft. On the latest checked commit, all listed hosted GitHub Action workflow runs were queued and not certified successful.
- Source freeze, periodic mixed/exterior pressure, signed total flux, positive one-sided seven-ray stress, an actual zero-residual nonlinear correction, and terminal retention **remain open**. Exact and conditional subresults in Appendices A--AC do not constitute an unforced finite-time blow-up construction.

## Remaining mathematical closure contract

A theorem of unforced blow-up requires one immutable original Case 006 physical source with all four-patch overlaps, radial/axial cutoffs, the physical rotating frame, density, stress centre, a correct common residual, and periodic pressure. It also requires one nonlinear exterior correction solving the genuine zero-force equation together with the required signed inward energy flux, all positive stress floors and terminal retention. The current archive does not contain this joint authenticated witness. Do not change the theorem proof gates to CLOSED solely from the Appendix AC concentration estimate.

## Appendix AD and final working snapshot

An additional conditional finite-energy theorem has been incorporated as Appendix AD: under pressure-dominated inward transport, local retention ratio `delta_tau`, and global velocity bounds `||w||_infty<=C tau^-1/2`, `||U||_infty<=C tau^(-1/2-h)`, the exact correction dissipation obeys
```
int_(I_tau) ||grad w||_2^2 dt >= c delta_tau^-2 tau^(1/2-h).
```
Thus retention `delta_tau=O(tau^(1/4-h/2))` would contradict the finite total unforced energy dissipation. For h=1/10 the excluded rate is `O(tau^1/5)`. The theorem does not produce a singular solution and requires its stated global correction bound.

The **final unified working PDF contains 115 pages**: all 114 earlier cleaned pages and one authorless Appendix AD page. The checked PDF SHA-256 is `72c27378c73bb594b61be0b9088aadc8c055ff6d2d5edb196f99f449140f927d`. Ten local Appendix AD tests pass; hosted CI is checked separately. The complete unforced singularity claim remains OPEN.
