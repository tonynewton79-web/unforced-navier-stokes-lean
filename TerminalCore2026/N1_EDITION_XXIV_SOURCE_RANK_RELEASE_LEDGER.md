# Edition XXIV — weighted source flux, Fourier rank, smooth two-mode repair

Research status (24 October 2026): **partial source-independent exact results**.
The complete smooth, finite-energy, zero-force Navier–Stokes singularity
and the end-to-end Lean proof are **OPEN**.

## Three new certified-at-mathematical-level gates

1. For a compact annular angular Reynolds stress Q, radial-slice torque
   m=∂z T with T=∫r²Q_{θz}dr and 2|T|≤Eθ+Ez, where
   Ej=∫r²Q_{jj}dr. Hence
   sup(Eθ+Ez)≥osc(∫m), and for support r≤b,
   sup_z [2π∫r(Qθθ+Qzz)dr]≥(2π/b)osc(∫m).
   These are elementary covariance/CS consequences and a necessary
   source matching test, not an H8 cone sufficiency theorem.

2. A single co-rotating m=±1 Fourier pair has Q=2(aaᵀ+bbᵀ),
   rank(Q)≤2. It cannot directly realize Q≽μρI₃ for μρ>0.
   More radial shells at that one Fourier frequency do not remove
   this rank limit. Pressure-gauge/divergence equivalence is distinct:
   do not claim a complete projected-Stokes no-go.

3. There exist smooth real finite-energy divergence-free fields on
   R²×S¹_z, supported in a compact annulus, using m=±1 and m=±2,
   with **nonzero** radial-slice angular torque and a strict local
   covariance floor. With f,g∈C_c^∞((1/2,3/2)), f=g=1 on [3/4,5/4],
   and |λ|≤1/16, the amplitudes
       a1=f cos z,
       b1=i f cos z+λr²f cos z,
       c1=-f' sin z-iλrf sin z,
       c2=g (a2=b2=0)
   plus conjugates are exactly solenoidal.
   The covariance determinant is 8 f⁴g²cos⁴z, and
       Q ≽ (653/512) I₃
   on the plateau |z|≤π/6. The radial-slice torque is
       m(z)=2λ I_f cos(2z), I_f=∫r³f²dr>0.
   Thus local stress positivity, solenoidality and nonzero angular
   torque can coexist in a physical spatial velocity fixture.

The fixture still has nontrivial m=3,4 nonlinear leakage and has not
been evolved as an unforced NSE solution. It is *not* automatically
inside the specific seven-ray H8 cone or a source-corrected solution.

## Mandatory negative control: keep nonzero initial data

OpenAI's 2026 forced NSE Theorem 1.1 has u(0)=0 and f≠0. In a smooth
finite-energy *unforced* evolution the energy identity makes the
zero initial datum identically zero. The source cannot simply be
unforced while retaining rest initial data. A valid theorem must
construct nonzero smooth solenoidal initial data.

## Independent verification

- Gaussian angular flux and source antiderivative: exact SymPy.
- 30,000 rational PSD stress tests and scalar oscillation controls: pass.
- 5,000 rational single-pair rank tests, symbolic determinant/kernel: pass.
- Explicit smooth two-harmonic solenoidal field and determinant: pass.
- Simultaneous nonzero torque / strict rational 653/512 floor: pass.
- Separate Lean files provide only finite scalar algebra, awaiting the
  GitHub Actions kernel execution. Their mathematical correspondence
  to physical averaging, source spaces and PDE is unformalized.

## Source and release blockers

The repository's FULL_UNFORCED_SOURCE_CERTIFICATE_REQUIRED_20261022.json
still reports FAIL_CLOSED_MISSING_SOURCE_DATA; the source profile hash,
A.11/A.19 joined source, pressure and collar interval data, exact
zero-force physical PDE and end-to-end Lean closure are absent.

The next *scientifically decisive* target is not another manufactured
positive control, but to extract the genuine projected source F from
the existing forced paper, resolve its angular Fourier and radial-slice
moment ledger, test exact H8 virtual-work dual and seven-ray margin
using one source parameter tuple, then establish a convergent full
nonaxisymmetric inverse preserving a terminal singularity.
Formalization must use the genuine imported NavierStokes PDE theorems
from pinned OpenAI source and must not smuggle the forcing away
through abstract assumptions.

**No complete unforced Navier–Stokes or Lean proof is claimed.**
