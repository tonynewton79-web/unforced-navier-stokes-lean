# An exact compact-gauge identity and a restricted positivity obstruction

25 October 2026. This note addresses a differential obstruction within G4,
not the weighted, source-matched H8 symmetric-divergence inverse.

Let `F(r,z)` be smooth and compactly supported in an annular cylindrical
region with `r>0`, independent of the azimuthal angle. Define

\[
K=r\partial_rF,\qquad C=K+F,\qquad
S=K\,e_r\otimes e_r+C\,e_z\otimes e_z.
\]

The divergence of this axisymmetric symmetric tensor, with its hoop and
mixed components zero, is

\[
\nabla\cdot S=(\partial_rK+K/r)e_r+(\partial_z C)e_z.
\]

Because `K=r F_r`, differentiation yields

\[
\partial_r C=\partial_rK+K/r,
\qquad\text{therefore}\qquad\nabla\cdot S=\nabla C.
\]

Thus `S` is a compact, symmetric two-diagonal stress whose divergence is
a pressure gradient; its solenoidal contribution vanishes. The identity
does **not** produce the nonzero prescribed right-hand side for H8, and
it contains no weighted estimate, seven-ray positivity theorem, or
periodic Navier–Stokes correction.

## What is kernel checked

`UnforcedPatching.CompactGauge` defines `radialCarrier F Fr r = r * Fr r`
and `axialCarrier F Fr r = radialCarrier F Fr r + F r`. Under explicit
pointwise derivative hypotheses `F_r=Fr(r)` and `Fr_r=a`, and `r≠0`,
Lean proves

\[
\operatorname{deriv}_r C
=\operatorname{deriv}_r K+K/r.
\]

`UnforcedPatching.CompactGaugeSmoke` compiles that actual derivative
theorem and prints its axioms. An additional compilation target,
`UnforcedPatching.MeridionalInverseSmoke`, now checks both meridional
cylindrical coordinate-divergence identities, the axial interval-integral
fundamental theorem of calculus, the radial moment integral, and the
mixed-carrier product identity. The Cartesian tensor calculus bridge,
smooth compact cutoff/support claims, and H8 weighted cone estimate
remain outside those Lean theorems.

For a reproducible exact interior check take
`P(r)=(r-1)^4(2-r)^4`, `Q(z)=(1-z²)^4`, `F=P Q`.
The standard-library `fractions.Fraction` regression verifies the
identity at rational points. The pure-radial tensor with component
`K=r F_r` but without `C` has nonzero curl of its divergence:

\[
\partial_z(\partial_rK+K/r)
\big|_{(r,z)=(5/4,1/2)}=-5103/32768.
\]

Extending this **fourth-order boundary-vanishing polynomial** by zero is only finitely
differentiable at the support boundary; it is **not** claimed to be a
globally smooth cutoff. Smooth versions use a standard flat bump,
for example `F=exp(-1/((r-1)(2-r)(1-z²)))` in the open region
`1<r<2`, `|z|<1`, and zero elsewhere. The differential identity
holds for any such smooth `F` by the same chain and product rules.

## A restricted necessary sign condition

Suppose both `K` and `C` vanish at the two radial ends of a fixed
annulus and obey `C_r=K_r+K/r`. Integrating at fixed `z` gives

\[
0=[C]_{r_1}^{r_2}=[K]_{r_1}^{r_2}
  +\int_{r_1}^{r_2}K(r,z)/r\,dr
=\int_{r_1}^{r_2}K(r,z)/r\,dr.
\]

Because `r>0`, a nonzero nonnegative `K` cannot satisfy this
condition. In the explicit gauge `K=rF_r`, the same condition reads
`[F]_{r_1}^{r_2}=0`; any nonconstant bump has radial derivative of
both signs. This obstructs a **nonnegative, compact, purely radial
two-diagonal compensator** of this restricted type. It does not exclude
sign-changing small corrections to a strictly positive base tensor,
nor stresses with mixed shear or hoop components. Those remain possible
H8 constructions to investigate.

## Open source-matching problem

For the genuine residual `g - P div(ρR_*)`, one must first select and
verify the actual source, identify the force/torque and moment
compatibilities, and solve the compact weighted symmetric inverse with
seven-ray coefficient floor. In particular the sharp sufficient
four-field coordinate target from `ConeOperator` remains
`max(|A|,|B|,|C|,|D|) ≤ (15971/1720600)ρ`.

These requirements, all of G4, and the final unforced finite-time
singularity theorem retain status **OPEN**.

## Source-matched dual test and its exact limitation

The cumulative manuscript now contains a complete pressure-gauge-independent
test of the **stronger physical tensor-entry cap** `|H_ij| ≤ βρ` with
`β=15971/1720600`. On the annular cylinder `1≤r≤2`, `|z|≤1`, let
`P=(r−1)²(2−r)²`, `η=(1−z²)³`, `ρ=Pη` and the exactly source-matched
`f=Pη' e_z`. The compact symmetric inverse `S=ρ e_z⊗e_z` has `div S=f`.

The compact Lipschitz, divergence-free dual field
`v_r=−rPη''`, `v_z=(2P+rP')η'` annihilates all pressure gradients.
The exact radial/axial integrals give the lower source pairing
`L=256/40425`, while the upper bound on the weighted full cylindrical
gradient is `U≤313361/470400`. Thus

\[
 L-β(313361/470400)=443015653/2967690880000>0.
\]

The entrywise cap is impossible, even after smooth nonnegative
approximation of the compact polynomial profiles. The exact arithmetic
is independently replayed in `meridional_h8_certificate.py` and
`tests/test_meridional_h8.py`.

### Exact four-field source-frame identification

For the seven source rays in the explicitly identified **co-rotating
cylindrical frame** `(e_r,e_theta,e_z)`, the coefficient perturbations
`delta c_i(A,B,C,D)` assemble into

\[
G=\sum_i\delta c_i v_i\otimes v_i
=\begin{pmatrix}-3D/2&C&A\\C&-D/2&B\\A&B&D/2\end{pmatrix}.
\]

The trace-free pressure representative is exactly

\[
H=G+(D/2)I
=\begin{pmatrix}-D&C&A\\C&0&B\\A&B&D\end{pmatrix}.
\]

The reverse map is precisely
`A=H_rz`, `B=H_theta,z`, `C=H_r,theta`, `D=H_zz`.
It applies exactly when a symmetric trace-free tensor also satisfies
`H_theta,theta=0`; thus the four coordinates omit one independent
trace-free diagonal mode. Lean now also proves the inverse recovery
and the two corresponding diagonal identities. A tensor outside this
subspace cannot be represented merely by reassigning `A,B,C,D`.

Thus the sufficient four-coordinate bound
`max(|A|,|B|,|C|,|D|)≤beta*rho` **does imply** the physical
entrywise cap `max |H_ij|≤beta*rho` in this fixed frame. The exact
pressure-gauge reconstruction, symmetry, zero trace and entrywise bound
are kernel-checked in `UnforcedPatching/FourFieldPhysical.lean` and
replayed independently by `h8_four_field_map.py` and
`tests/test_h8_four_field_map.py`.

Therefore the first dual test rules out the **sufficient
four-coordinate bound for this manufactured compact source**, even
with arbitrary pressure. A sharper test now also rules out the
original **absolute seven-coefficient correction budget** for the
same manufactured source, as recorded below.
The exact original admissible cone is independently characterized and
kernel-checked as
`4|D|+2|C|≤τ`, `4|D|+2|A-4B|≤τ`, and `8|B|≤τ`, with
`τ=(15971/122900)rho`. One may saturate it with
`(A,B,C,D)=(τ,τ/8,0,0)`, outside the sufficient `max≤τ/14` envelope.
The same conservative gradient upper bound is too large to give a
contradiction under that weaker condition: its slack is exactly
`51024386641/635933760000 > 0`. This failure belongs only to the
conservative gradient bound. The exact pointwise support is
`τ*(max((|a|+|c|)/2, |d|/4)+|4a+b|/8)`, kernel-checked as an upper
bound by `SharpCoefficientDual.lean` and independently shown sharp
by rational extremizers. The meridional dual test gives
`S≤5838537817787225523484624248207/150323855360000000000000000000000<1/25`,
so the source pairing violates the original correction budget by
more than `5637293/4968232500`. The proof and source distinctions
are in [`H8_AUTHENTIC_SOURCE_BOUNDARY.md`](H8_AUTHENTIC_SOURCE_BOUNDARY.md).

The broader **one-sided** positivity floor is different: its exact
asymmetric four-coordinate support is checked by the new
`PositiveCoefficientCone.lean` theorem and independent exact rational
maximizers. On the same manufactured meridional source and the same
dual field, signed rational polynomial cell integrals show its
available dual support exceeds the source pairing by more than
`1/10000`. Thus this diagnostic dual field cannot rule out the
one-sided cone. No positive-cone inverse is implied, and testing
other dual fields or the unavailable true H8 source remains open.

For a tilted or spatially varying orthonormal frame `E`, the physical
stress is `E H E^T`. No authentic H8 `E(r,z)`, its derivative bounds,
or the real source profile has been checked against this example.
Neither this negative control nor the absent genuine H8 source
promotes G4 or the final unforced theorem; both remain OPEN.
