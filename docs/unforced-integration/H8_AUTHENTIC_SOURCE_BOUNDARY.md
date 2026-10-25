# H8 source provenance and sharp weighted dual boundary

The original H8 attachment equation in the programme is

\[
 \mathbb P\operatorname{div}H
 =g-\mathbb P\operatorname{div}(\rho R_*),
\]

where \(\mathbb P\) is the solenoidal Leray projection. The physical
four-coordinate tensor in the *frozen cylindrical source frame* is

\[
 H(A,B,C,D)=\begin{pmatrix}-D&C&A\\C&0&B\\A&B&D\end{pmatrix}.
\]

If a source-matched compact tensor is to obey the absolute coefficient
budget \(|\delta c_i|\le\tau\), its pointwise values must lie in

\[
 4|D|+2|C|\le\tau,\qquad
 4|D|+2|A-4B|\le\tau,\qquad 8|B|\le\tau.
\]

For a dual covector \((a,b,c,d)\) this compact polytope has exact support
function

\[
 \sigma_\tau(a,b,c,d)=\tau\left[
 \max\left(\frac{|a|+|c|}{2},\frac{|d|}{4}\right)
 +\frac{|4a+b|}{8}\right].
\]

Lean proves the universal upper bound in
`UnforcedPatching/SharpCoefficientDual.lean`; independent exact rational
optimizers prove equality. Neither check implies a spatial inverse exists.

## Result for a manufactured meridional source, not H8

For the explicit diagnostic source \(f=P(r)\eta'(z)e_z\),
\(\rho=P\eta\), and the exact solenoidal dual field defined in the
manuscript, \((a,b,c,d)=(a,0,0,d)\), where

\[
 a=-rP\eta'''+(3P'+rP'')\eta',\qquad
 d=(3P+2rP')\eta''.
\]

The positive-weight dual integral is

\[
 S=\int_1^2\!\int_{-1}^1
 rP\eta\max\{|a|,\;|a|/2+|d|/4\}\,dz\,dr.
\]

The exact polynomial/Bernstein program `h8_sharp_dual_certificate.py`
uses a 40-by-40 rational rectangle partition and proves

\[
 S\le\frac{5838537817787225523484624248207}
 {150323855360000000000000000000000}<\frac1{25}.
\]

Together with \(\int f\cdot v=256/40425\) and
\(\gamma=15971/122900\), this gives the strict pressure-independent
necessary-condition violation

\[
 \int f\cdot v-\gamma S
 >\frac{5637293}{4968232500}>0.
\]

Therefore the manufactured source **cannot** have a compact fixed-frame
stress satisfying the original **absolute** H8 coefficient cap. This is
stronger than the earlier result about the factor-14 sufficient cap.
It still does not refute the larger one-sided set of merely positive
coefficient allocations, or a tilted-frame construction.

Reproduce with:

```sh
python -m unittest discover -s tests -p 'test_h8_sharp_dual*.py' -v
python h8_sharp_dual_certificate.py
lake build UnforcedPatching.SharpCoefficientDualSmoke
```

## Authentic H8 source: required data and current state

The files available in this checkout reference
`Carrier_Independent_Structured_Stress_Route_FINAL_COLOUR.tex`, but do
not contain that source manuscript, the concrete \(g,\rho,R_*\) profiles,
their support/derivative parameter choices, or the actual local frame
\(E(r,z)\). The terminal source certificate
`TerminalCore2026/FULL_UNFORCED_SOURCE_CERTIFICATE_REQUIRED_20261022.json`
also records missing source hashes, cutoffs and parameters. A generic
profile name in a proof-gate reference is **not** source authentication.

The exact genuine-source test needs, at minimum:

1. An identified source revision/hash and explicit expressions for
   \(g,\rho,R_*\) (or exact, independently checkable interval bounds
   for their full distributional residual).
2. The local frame \(E\), its regularity and rotation convention, and
   whether the four coefficient coordinates represent \(H\) or
   \(EHE^{\mathsf T}\) in physical space.
3. A specified admissible set: absolute correction cap, one-sided
   coefficient floor, or a stronger weighted derivative/regularity cone.
4. Boundary, force, torque and projection/pressure conditions permitting
   the dual integration by parts and producing a finite computable
   physical source pairing.

**Status: BLOCKED ON AUTHENTIC H8 SOURCE DATA.** The computed rational
obstruction is a reproducible negative control, not a test result for
the missing H8 residual and not a proof of unforced Navier--Stokes
regularity or blow-up. G4 and G8 remain `OPEN`.
