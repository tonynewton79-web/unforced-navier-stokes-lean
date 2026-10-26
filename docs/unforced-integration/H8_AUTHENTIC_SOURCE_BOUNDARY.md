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

## Exact test of the larger one-sided positive-coefficient cone

The original condition on every ray is
\(c_i^{(0)}\rho+\delta c_i\ge\rho/100\), with \(\rho\ge0\).
Writing \(g=15971/122900\), \(h=22371/122900\) and \(x=A-4B\),
this is **exactly** the following asymmetric polytope:

\[
-g\rho/4\le D\le(g+h)\rho/8,\quad |B|\le g\rho/8,\quad
|x|\le g\rho/2+2D,\quad
|C-(h-g)\rho/4|\le(g+h)\rho/4-2D.
\]

Its support function, attained by rational endpoint choices, is

\[
\sigma^+_\rho(a,b,c,d)=\rho\left[
 (h-g)c/4+g|4a+b|/8+
 \max\{(3g+h)|c|/4-gd/4,\ (3g+h)|a|/4+(g+h)d/8\}\right].
\]

`UnforcedPatching/PositiveCoefficientCone.lean` kernel-checks the
**universal upper bound** directly from all seven original floors;
`h8_positive_cone.py` independently checks feasible maximizing
witnesses in exact rational arithmetic. Thus the expression is sharp
pointwise, but supplies no differential stress inverse.

For the same manufactured meridional source, the exact support in
the required dual direction is

\[
 J=\int_1^2\!\int_{-1}^1 rP\eta\,
  \sigma^+_1(-a,0,0,-d)\,dz\,dr.
\]

The rational program `h8_positive_dual_certificate.py` sums the
largest of four **signed polynomial action integrals** on each of
1600 rational rectangles and proves

\[
 J\ge
 \frac{249897750999661616493885744300330541}
 {38797083829862400000000000000000000000}
 >\frac{256}{40425}+\frac1{10000}.
\]

The same program also supplies an independent signed Bernstein upper
enclosure. The strict **positive** slack means that this particular
divergence-free dual field gives *no contradiction* under the larger
one-sided cone, unlike the absolute-budget test. It does **not** show
that a compact admissible inverse exists, and it does not settle
whether another dual field obstructs the same source.

Reproduce with:

```sh
python -m unittest discover -s tests -p 'test_h8_sharp_dual*.py' -v
python h8_sharp_dual_certificate.py
lake build UnforcedPatching.SharpCoefficientDualSmoke
python -m unittest discover -s tests -p 'test_h8_positive*.py' -v
python h8_positive_dual_certificate.py
lake build UnforcedPatching.PositiveCoefficientConeSmoke
```

## Exact rotating-frame dual, without assuming a frozen source basis

Write the trace-free source tensor as
\(H=\begin{psmallmatrix}-D&C&A\\C&0&B\\A&B&D\end{psmallmatrix}\).
If \(E(x)\) is its orthogonal source-to-physical frame and
\(K=EHE^{\mathsf T}\), then for any physical gradient \(G=\nabla v\)
the pulled-back gradient is \(M=E^{\mathsf T}GE\). The **exact** dual
coordinates are

\[
(a_E,b_E,c_E,d_E)=
(M_{rz}+M_{zr},\ M_{\theta z}+M_{z\theta},\
 M_{r\theta}+M_{\theta r},\ M_{zz}-M_{rr}),
\qquad K:G=Aa_E+Bb_E+Cc_E+Dd_E.
\]

The new `UnforcedPatching/RotatingFrameDual.lean` proves this finite
identity even for arbitrary pointwise matrices \(E\) and also proves
the one-sided upper bound
\(-K:G\le\sigma^+_\rho(-a_E,-b_E,-c_E,-d_E)\)
directly from all seven original ray floors. Orthogonality is needed
to preserve the isotropic pressure gauge, but not for the contraction
identity. `h8_rotating_frame.py` and an independent rational test
exercise the physical contraction, covector values and gauge behavior.

If \(\operatorname{div}K+\nabla q=f\), integration against any admissible
divergence-free test field yields the **necessary** inequality

\[
\int f\cdot v\,dx \le
\int\sigma^+_{\rho(x)}(-a_E,-b_E,-c_E,-d_E)\,dx.
\]

This continuum integral is **not** formalized in Lean. Moreover,
the physical divergence differentiates the frame:

\[
\partial_jK_{ij} = E_{ia}E_{jb}\partial_jH_{ab}+
(\partial_jE_{ia})H_{ab}E_{jb}+
E_{ia}H_{ab}\partial_jE_{jb}.
\]

Thus the verified pointwise algebra cannot substitute for the
missing derivative estimates, source profiles or compact stress
construction. In particular **no authentic-source dual value can be
reported** until \(g,\rho,R_*\) and \(E\) are available.

Reproduce with:

```sh
python -m unittest tests.test_h8_rotating_frame -v
lake build UnforcedPatching.RotatingFrameDualSmoke
```

## The complete axial source flux and both exact H8 budgets

For an arbitrary physical symmetric stress \(K\) and pressure \(p\)
with \(\operatorname{div}K+\nabla p=f\), set the azimuthal averages

\[
S(r)=\int_c^d\langle K_{rz}\rangle_\theta dz,\qquad
q_{\rm s}(r)=[\langle K_{zz}+p\rangle_\theta]_{c}^{d}.
\]

Direct cylindrical divergence, including its \(1/r\) term, proves

\[
J_f(r)=\frac1r\int_a^r s\!\int_c^d\langle f_z\rangle_\theta dz\,ds
=S(r)-\frac ar S(a)+\frac1r\int_a^r s q_{\rm s}(s)ds.
\]

**The cone constrains \(S\), not \(J_f\) alone.** Let \(\lambda_E\) be the
rotated four-coordinate covector for the physical \(rz\) matrix entry.
With the pointwise one-sided coefficient floors, define

\[
B_\pm=\int_c^d\langle\sigma^+_{\rho}(\pm\lambda_E)\rangle_\theta dz.
\]

Then the exact necessary radial condition is

\[
-B_-\le J_f+\frac arS(a)-\frac1r\int_a^r s q_{\rm s}(s)ds
\le B_+.
\]

The *original absolute* coefficient cap requires the stronger symmetric
bound with \(B_{\rm abs}=\int\langle\sigma_{g\rho}(\lambda_E)\rangle dz\),
\(g=15971/122900\). Its one-sided counterpart is asymmetric for a
tilted frame. For a source-frame rotation with
\(\cos\alpha=3/5,\sin\alpha=4/5\) the pulled-back physical shear
covector is \((-7/25,0,0,24/25)\), giving exactly

\[
B_+/\bar\rho=(19h+47g)/100,\quad
B_-/\bar\rho=B_{\rm abs}/\bar\rho=19g/50,
\qquad h=22371/122900.
\]

The new `h8_exact_flux_gate.py` accepts a complete *declared* partition of
stress-shear channels (core transition, core shaper, poloidal pairing,
toroidal pairing, viscosity, four-patch overlap, structured remainder and
subtraction of the chosen stress centre) and pressure/boundary channels
(core pressure, toroidal pressure, transition pressure, axial tensor jump,
four-patch overlap and remaining jump). Every channel is mandatory;
unknown is not silently treated as zero. The tests cover the integrated
cylindrical law, a nonzero pressure-only example, an inner trace,
rotating-frame asymmetry, and a profile that passes positivity but fails
the original absolute budget. Symbolic expressions and rational-point
results **do not certify the continuum inequality**, nor does the
presence of all field names authenticate their physical values.

## Exact Case 006 shaper term family, not the full transition residual

The source's poloidal stream-function architecture is
\(\Psi_i=K_i a_i(r)b(r)\Xi_i(z)\), with radial/axial velocity
\(P_r=-\Psi_z/r\), \(P_z=\Psi_r/r\). For a divergence-free
axisymmetric core and axial endpoint conditions
\(\Xi_i=\Xi_i'=0\), the exact additional quadratic shear is
\(\Gamma b'+\Delta b+Q_2b^2\), where

\[
\Gamma={1\over r}\sum_iK_i a_i I_i,\quad
\Delta={1\over r}\sum_iK_i[a_i'I_i-a_i(I_i'+I_i/r)],\quad
Q_2={1\over r^2}\sum_{i<j}K_iK_j(a_ja_i'-a_ia_j')J_{ij},
\]

\(I_i=\int U_r\Xi_i\,dz\) and
\(J_{ij}=\int\Xi_i'\Xi_j\,dz\). The cross-shaper coefficient has
**no** \(bb'\) term: it cancels exactly as an antisymmetric Wronskian.
The viscous \(rz\) stress adds

\[
-\nu\sum_i K_i m_i\,\partial_r((a_i b)'/r),
\qquad m_i=\int\Xi_i\,dz.
\]

It generally has a \(b''\) coefficient, which is not controlled by
\(b^2\) for a flat cutoff. For the explicitly stated local two-shaper
polynomial example in the manuscript, the exact integrated sum at
\(r=2\) is \(-2036/315\), independently reproduced by integrating
the physical velocity products and viscosity. It is a **diagnostic**
local example, not the authentic choice of global H8 profiles.

`h8_shaper_flux_ledger.py` checks the incompressible core and axial
endpoint conditions before applying these formulas. Reproduce with
`python -m unittest discover -s tests -p 'test_h8_shaper_flux_ledger.py' -v`.

Reproduce the exact finite check with SymPy:

```sh
python -m pip install sympy
python -m unittest discover -s tests -p 'test_h8_exact_flux_gate.py' -v
```

## Authentic H8 source: required data and current state

The author-supplied `Carrier_Independent_Structured_Stress_Route_FINAL_COLOUR.tex`
was inspected separately from this repository. Its SHA-256 is
`a52409301270a6408f49116b62f6abafbd5f2c37ca22087ddc294c23fb78eb2e`.
The separately supplied 65-page PDF with the same stem has SHA-256
`46ef3e409e1f50350bc73a36a3c6217b92bc25cd258250baf4214a3471bbf04b`.
It specifies the *forms* of the curl localization, the separable
poloidal/toroidal shell shapers and the toroidal radial pressure
derivative, but leaves their profiles and amplitudes as arbitrary fixed
smooth data; it does not freeze a complete source-matched H8 residual.
It is not yet tied by a checked correspondence to any distinct Case 006
PDF revision. The terminal source certificate
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

**Status: BLOCKED ON A COMPLETE FROZEN H8 SOURCE, NOT ON THE ALGEBRAIC
DUAL.** The computed rational
obstruction is a reproducible negative control, not a test result for
the missing H8 residual and not a proof of unforced Navier--Stokes
regularity or blow-up. G4 and G8 remain `OPEN`.
