# Unforced Navier–Stokes

This directory contains the new cumulative, journal-style research manuscript
by Tony Newton, separate from the repository's historical `paper.tex`.

- `Unforced_Navier_Stokes.tex`: complete LaTeX source, including the proof
  of the restricted compact symmetric-divergence theorem and bibliography.
- `Unforced_Navier_Stokes.pdf`: rendered A4 manuscript.

Build reproducibly from the repository root with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=manuscript/build manuscript/Unforced_Navier_Stokes.tex
```

The main new analytic meridional inversion theorem has a mathematical proof
in the paper but is **not yet formalized in Lean**. The seven-ray coefficient
bound, radial pressure-gauge derivative, physical residual expansion, and
conditional terminal-speed retention are locally Lean-checked under the
pinned `lean-toolchain`. Passing these checks is not an unforced finite-time
blow-up proof. The physical H8 attachment and global singularity theorem
remain open. The official proof-gate ledger is in
`docs/unforced-integration/proof_gates.json`.

The accompanying independent polynomial calculation is a diagnostic of
the local formulas, not a replacement for the continuum proof or Lean.
