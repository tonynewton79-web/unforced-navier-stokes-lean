# The certified finite H8 seven-ray centre

25 October 2026. This certificate is limited to the fixed-aperture, frozen
finite-dimensional algebra in the supplied *Carrier-Independent Structured
Stress Route* manuscript. It is not the compact H8 spatial-attachment theorem.

With aperture `t=1/4`, let the seven rays be

\[
v_1=(1,0,0),\quad v_2=(1,t,0),\quad v_3=(1,-t,0),\quad
v_4=(1,0,t),\quad v_5=(1,0,-t),\quad
v_6=(1,t,t),\quad v_7=(1,t,-t).
\]

Using the raw weights `(1,1,59/43,1,1,1,1)` gives exactly

\[
Q_0=\sum_{a=1}^7c_a v_av_a^T
=\begin{pmatrix}
317/43&35/86&0\\35/86&47/172&0\\0&0&1/4
\end{pmatrix},\qquad \operatorname{tr}Q_0=679/86.
\]

All nine entries, not merely a declared symbolic matrix, are computed and
proved by `quarter_source_covariance_exact` in
`UnforcedPatching/SevenRayCenter.lean`.

The exact identity

\[
\frac{172}{1229}\left(Q_0-\frac{\operatorname{tr}Q_0}{3}I\right)
=\frac{(35,2,0)^T(35,2,0)}{1229}-\frac13 I
\]

is the Lean theorem `quarter_tracefree_rankOne`. Rescaling the raw weights
gives six coefficients `172/1229` and a third coefficient `236/1229`.
The source-frame conversion has the exact *signed* physical product

\[
(b_*)_r(b_*)_z=-\frac{4443}{9832},\qquad
\big|(b_*)_r(b_*)_z\big|>\frac9{20}.
\]

The `Real.sqrt` cancellation is formalized in
`quarter_physical_axial_efficiency`; independent rational arithmetic confirms
the same value without approximations. Together with

\[
\frac{172}{1229}-\frac1{100}=\frac{15971}{122900},
\]

the `ConeBudget.lean` module proves a positive coefficient floor *provided*
each of the seven physical corrections obeys the weighted bound.

## Sharp four-field componentwise certificate

Write the four trace-free stress coordinates in the source notation as
`(A,B,C,D)`, and let `δc_a` denote the seven linear coefficient changes
recorded in `ConeBudget.lean`. The exact operator norm is

\[
\max_{1\le a\le 7}|\delta c_a|
\le 14\max\{|A|,|B|,|C|,|D|\}.
\]

The factor `14` cannot be reduced for this componentwise maximum norm:
the fourth ray has `δc₄=2A−8B+4D`, which equals `14` at
`(A,B,C,D)=(1,-1,0,1)`. Lean checks both the bound for all seven rays
and this exact sharpness witness in `ConeOperator.lean`.

Consequently, an explicit **sufficient**, not necessary, condition for
the seven-ray margin is

\[
\max(|A|,|B|,|C|,|D|)
\le\frac{15971}{1720600}\,\rho.
\]

This sharper numerical target is useful for testing a proposed compact
weighted inverse, but it is stronger than the original coefficientwise
condition and no such source-matched inverse has been constructed here.

## Actual cylindrical four-coordinate tensor

For the source's **frozen co-rotating frame**
`(e_1,e_2,e_3)=(e_r,e_theta,e_z)`, the correction tensor and its
trace-free pressure representative are exactly

\[
G=\sum_i\delta c_i v_i\otimes v_i
 =\begin{pmatrix}-3D/2&C&A\\C&-D/2&B\\A&B&D/2\end{pmatrix},\qquad
H=G+(D/2)I=\begin{pmatrix}-D&C&A\\C&0&B\\A&B&D\end{pmatrix}.
\]

In this frame, the inverse map is
`(A,B,C,D)=(H_rz,H_theta,z,H_r,theta,H_zz)` and
`max_ij |H_ij| = max(|A|,|B|,|C|,|D|)`. This is a *four-dimensional*
subspace of trace-free symmetric tensors; the independent azimuthal
diagonal direction is absent (`H_theta,theta=0`). The seven Lean theorems
in `UnforcedPatching/FourFieldPhysical.lean` verify the nine-entry gauge
identity, the bound, symmetry, trace, inverse recovery and diagonal
constraints. The independent exact rational `h8_four_field_map.py` test
rejects attempted inversion outside that subspace.

The first source-matched meridional dual test excludes the stronger
sufficient four-coordinate cap for one explicitly manufactured compact
axial source. A subsequent sharp dual test, described below, also
excludes the original **absolute coefficient budget** for that same
manufactured source. Neither test authenticates the genuine H8 residual.
Tensor conjugation and derivatives of a tilted frame remain separate.

The **exact**, unrelaxed original cone is now verified in
`UnforcedPatching/ExactCoefficientCone.lean`: writing `τ≥0` for the allowed
absolute coefficient perturbation, all seven `|delta c_i|≤τ` hold if and
only if

\[
 4|D|+2|C|\le\tau,\quad
 4|D|+2|A-4B|\le\tau,\quad
 8|B|\le\tau.
\]

For example `(A,B,C,D)=(τ,τ/8,0,0)` meets the original bound exactly
even though its maximum four-coordinate magnitude is `τ`, fourteen
times the sufficient bound `τ/14`. These coupled inequalities have
the exact support function

\[
 \sigma_\tau(a,b,c,d)=\tau\left[
 \max\left(\frac{|a|+|c|}{2},\frac{|d|}{4}\right)
 +\frac{|4a+b|}{8}\right].
\]

`UnforcedPatching/SharpCoefficientDual.lean` proves the upper bound;
independent rational extremizers give equality. The meridional
solenoidal test has only `a` and `d` nonzero, so the pointwise maximum
becomes `τ*max(|a|, |a|/2+|d|/4)`. A 40×40 exact Bernstein certificate
gives `S<1/25`, while the manufactured source pairing is `256/40425`.
The strict original-budget discrepancy therefore exceeds
`5637293/4968232500>0`. This is a nonexistence result under the
**absolute** coefficient perturbation cap for this manufactured
source, not for every one-sided positive ray-coefficient allocation.
See [`H8_AUTHENTIC_SOURCE_BOUNDARY.md`](H8_AUTHENTIC_SOURCE_BOUNDARY.md)
for the genuine-source authentication blocker.

A separate exact radial-derivative calculation now identifies a compact
two-diagonal pressure-neutral gauge and a restricted sign obstruction:
see [`H8_COMPACT_GAUGE_AND_POSITIVITY_BOUNDARY.md`](H8_COMPACT_GAUGE_AND_POSITIVITY_BOUNDARY.md).
Lean also checks the cylindrical divergence identities and the finite
four-field map, but not the full spatial inverse or cone attachment.
The compact physical source match and positivity-constrained H8 inverse
remain open.

## Exact release boundary

Nothing here provides a compact symmetric tensor `H` with

\[
\mathbb P\nabla\cdot H = g-\mathbb P\nabla\cdot(\rho R_*),
\qquad \max_a|\delta c_a(H)|\le\frac{15971}{122900}\rho,
\]

or the requisite support and derivative estimates. To close H8 one still
must select explicit smooth source and shell profiles, establish the force,
torque and trace-free moment compatibilities, and construct or obstruct a
scale-sharp weighted compact symmetric-divergence inverse. The periodic
projection and global time-dependent PDE geometry also require separate
proof. These remain `OPEN` in `proof_gates.json`.

Reproduction: build `UnforcedPatching.SevenRayCenterSmoke`,
`UnforcedPatching.ConeBudgetSmoke`, and
`UnforcedPatching.FourFieldPhysicalSmoke` and
`UnforcedPatching.ExactCoefficientConeSmoke`, and
`UnforcedPatching.SharpCoefficientDualSmoke` under the pinned Lean toolchain, and run
`python -m unittest discover -s tests -v`. A successful finite calculation
must never promote the H8 analytic gate to complete.
