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

Reproduction: build `UnforcedPatching.SevenRayCenterSmoke` and
`UnforcedPatching.ConeBudgetSmoke` under the pinned Lean toolchain, and run
`python -m unittest discover -s tests -v`. A successful finite calculation
must never promote the H8 analytic gate to complete.
