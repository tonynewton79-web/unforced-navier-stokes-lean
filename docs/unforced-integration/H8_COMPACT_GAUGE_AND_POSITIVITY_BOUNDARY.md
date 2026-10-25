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
theorem and prints its axioms. The full cylindrical divergence formula,
smooth cutoff/support claims and radial integral are mathematical
calculations in this note, **not Lean theorems**.

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
