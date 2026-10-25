# Cumulative unforced Navier–Stokes manuscript: source and asset inventory

Date: 25 October 2026. This file distinguishes the **user-provided** source PDFs/TeX from checked-in branch files and from assets that are not presently available in the integration checkout. No original attachment has been overwritten.

| Source | Supplied form | Pages / role | Build dependency |
|---|---|---|---|
| `Carrier_Independent_Structured_Stress_Route_FINAL_COLOUR` | `.tex`, `.pdf` | 65-page carrier-independent / H8 reduction | Self-contained class and drawings in TeX as supplied; do a fresh compile and page QA before claiming reproduction. |
| `Exact_Local_Unforced_Terminal_Core_Dynamics_JFM_FINAL` | `.tex`, `.pdf` | 16-page local analytic core | External `figures/*.pdf` inputs are cited in TeX and were not among the ten individual attachments. |
| `Unforced_Finite-Time_Blow-Up_for_Navier-Stokes` | `.tex`, `.pdf` | 188-page cumulative historical volume | Uses three original mono PDFs, six separate input/figure files (itemized below), and its earlier source-pinned dependencies. |
| `Edition_XXXIX_Moving_Cylinder_And_Dyadic_Transfer` | `.pdf` | 4-page whole-space transport diagnostic | Text/TeX insert tracked in PR #1 at `TerminalCore2026/N1_Moving_Cylinder_Dyadic_Transfer_Edition_XXXIX_20261025_Insert.tex`. |
| `Edition_XL_Extended_Trace_Dissipation_Obstruction` | `.pdf` | 3-page whole-space energy-dissipation obstruction | PR #1 `N1_XL_Moving_Radius_Trace_Dissipation_Amendment_20261025_Insert.tex`. |
| `Edition_XLI_Intermittent_Radial_Transport` | `.pdf` | 3-page radial variation/axis torque | PR #1 `N1_Intermittent_Radial_Flux_Variation_Edition_XLI_20261025_Insert.tex`. |
| `Edition_XLII_Near_Axis_Projected_Evolution` | `.pdf` | 2-page short-time pressure-complete jet theorem | PR #1 `N1_Near_Axis_Projected_Jet_Evolution_Edition_XLII_20261025_Insert.tex`. |

## Explicit assets referenced by the attached 188-page LaTeX

- `part1_original_mono.pdf` (`\\includepdf`, twice)
- `part2_corrected_body.pdf` (`\\includepdf`)
- `part3_original_mono.pdf` (`\\includepdf`, twice)
- `part1_review_clarification.tex` (`\\input`)
- `appendix_L_theorem_audit.tex` (`\\input`)
- `appendix_M_physical_tests.tex` (`\\input`)
- `meridional_flow_core_schematic.png`
- `periodic_torus_patch_operator_flowchart.png`
- `divergence_free_torus_projection_flowchart.png`

The cloned branch's separate `paper.tex` uses `references.bib` (present) and six `figures/*.pdf` files (not present at the checked-out top level). It is **not** a byte-for-byte replacement for the supplied 188-page cumulative master. Neither a fresh full-source 188-page build nor visual page verification has been performed in this integration stage.

## Consolidation ordering and release gate

1. Start with exact local core and separately state its dependence on source identities.
2. Develop torus `C4` localization, stress geometry, temporal mechanism, and the H8 open weighted attachment problem.
3. State only conditional global regular handoff, physical pressure, and unforced residual consequences until each named proof gate closes.
4. Integrate October XXXIX–XLII as **independent whole-space conservation/obstruction results and positive controls**, not as positive torus terminal-growth proof steps.
5. Resolve superseded and withdrawn claims, bibliography and paper voice. Apply the publication maximum of nine main sections and seven subsections per section.
6. Only when every referenced asset is accounted for: compile LaTeX, check missing labels and formula layout, render all pages and visually inspect every page before publishing a verified PDF.

All prose and figure changes remain separate from the Lean kernel proof status. Do not claim that a PDF build certifies the mathematical arguments.
