# Reproducibility Instructions

## 1. Pinned environment

The project pins Lean, Mathlib, and the upstream Navier--Stokes repository.

Lean:

`leanprover/lean4:v4.34.0-rc2`

Mathlib commit:

`85e3a25e006c35636f0e53b0e9296caca2685bc0`

Frozen upstream Navier--Stokes repository commit:

`f9e8bc5b38b6e212696e8a30e3e91517af887bbd`

## 2. Abstract Lean replay

From a clean checkout:

```bash
lake update
lake exe cache get
lake env lean UnforcedClosure.lean
lake build
```

The abstract closure layer was successfully kernel-checked in GitHub Actions Run `#12`
(Run ID `35779131542`) at commit
`7d7f33200e4553afbb80a29ce6435b44511c2f4a`.

See `CI_CERTIFICATE.md` for the recorded certificate and scope.

## 3. Exact-arithmetic and source-hygiene replay

Python 3.13 is used by CI.

```bash
python -m pip install -r requirements-dev.txt
python verify_unforced_closure.py
python -m pytest -q test_unforced_closure.py
```

Expected Pytest result:

```text
3 passed
```

The Python script records the successful abstract Lean compile by reference to
`CI_CERTIFICATE.md`; it does not itself invoke the Lean kernel.

## 4. Frozen upstream / PDE integration replay

The staged PDE integration workflow first builds the frozen upstream library and
then type-checks the local bridge:

```bash
cd .lake/packages/NavierStokesAndEuler
lake build NavierStokes
cd ../../..
lake env lean PDEIntegration.lean
```

`PDEIntegration.lean` is currently an import/type-compatibility gate. It does not
assert the final unforced blow-up theorem.

## 5. Cryptographic file check

After downloading the complete release repository, run on Linux/macOS:

```bash
sha256sum -c SHA256SUMS.txt
```

On PowerShell, individual files can be checked with:

```powershell
Get-FileHash .\UnforcedClosure.lean -Algorithm SHA256
```

The checksum file intentionally does not contain a checksum for itself.

## 6. GitHub Actions

The workflow `.github/workflows/verify.yml` runs on pushes, pull requests, and
manual dispatch. Its staged checks include:

1. checkout;
2. pinned Lean toolchain installation;
3. pinned dependency resolution;
4. Mathlib cache retrieval;
5. compilation of `UnforcedClosure.lean`;
6. local Lake build;
7. build of the frozen upstream `NavierStokes` library;
8. compilation of `PDEIntegration.lean`;
9. exact-rational/source-hygiene replay;
10. Pytest replay.

The successful Run `#12` certifies the abstract closure layer. A later PDE
integration run is a separate gate and must not be conflated with the abstract
certificate.

## 7. Scope warning

Reproducing the abstract checks verifies the packaged abstract closure artifact.
It does not by itself verify the PDE-specific hypotheses or the complete
unforced Navier--Stokes theorem.

The current manuscript additionally requires, among other PDE-side conditions:

- the core-range compatibility
  `K_full G_reg S_r(Y) subset Y_c`;
- the corrected periodic pressure reconstruction, including `div F_*` unless
  the force has first been Leray-projected;
- the full contraction gate `4 M_G C_B eta < 1`;
- completeness of the fixed-point space and the regularity/bootstrap step.

See `FORMAL_STATUS.md` and `PDE_INTEGRATION_GATE.md`.
