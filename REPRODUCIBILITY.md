# Reproducibility Instructions

## 1. Lean replay

The project pins both Lean and Mathlib.

```bash
lake update
lake env lean UnforcedClosure.lean
lake build
```

A successful run should type-check `UnforcedClosure.lean` without `sorry` or `admit` in the packaged source.

## 2. Exact-arithmetic and source-hygiene replay

Python 3.13 was used for the packaged audit; the checks themselves rely only on the Python standard library plus Pytest for the wrapper tests.

```bash
python verify_unforced_closure.py
python -m pip install -r requirements-dev.txt
python -m pytest -q test_unforced_closure.py
```

Expected packaged Python result:

```text
3 passed
```

## 3. Cryptographic file check

On Linux/macOS:

```bash
sha256sum -c SHA256SUMS.txt
```

On PowerShell, compare individual hashes with:

```powershell
Get-FileHash .\UnforcedClosure.lean -Algorithm SHA256
```

## 4. GitHub Actions

The workflow `.github/workflows/verify.yml` runs on pushes, pull requests, and manual dispatch. It:

1. checks out the repository;
2. installs the Lean toolchain pinned by `lean-toolchain`;
3. obtains the Mathlib dependency pinned by `lakefile.toml`;
4. compiles the Lean closure file;
5. builds the Lake target;
6. runs the exact-rational Python replay;
7. runs the Pytest suite.

## 5. Scope warning

Reproducing these checks verifies the packaged abstract closure artifact. It does not by itself verify the PDE-specific hypotheses or the complete manuscript theorem. See `FORMAL_STATUS.md` and `PDE_INTEGRATION_GATE.md`.
