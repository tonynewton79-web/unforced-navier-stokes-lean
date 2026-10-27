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

### A precise flat-edge restriction, conditional on the missing terms

Set $M(r)=\sum_iK_i m_i a_i(r)$. The complete kinetic-plus-viscous
shaper *increment* is exactly

\[
T_b=\kappa_2b''+\kappa_1b'+\kappa_0b+\kappa_qb^2,
\]

with

\[
\kappa_2=-\nu M/r,\quad
\kappa_1=\Gamma-\nu(2M'/r-M/r^2),\quad
\kappa_0=\Delta-\nu(M''/r-M'/r^2),\quad
\kappa_q=Q_2.
\]

**Flat-edge uniqueness lemma.** Let $b\in C^2([a,a+\delta])$ satisfy
$b(a)=b'(a)=0$, with the four coefficients bounded and
$|\kappa_2|\ge\eta>0$ throughout that collar. If a remaining term
$R$ obeys

\[
|R|\le L(|b|+|b'|+b^2),\qquad |T_b+R|\le L' b^2,
\]

then $b\equiv0$ on the collar. Indeed, boundedness of $b$ and the
nonvanishing coefficient imply
$|b''|\le C(|b|+|b'|)$; integration from $a$, followed by
Gronwall, forces $b=b'=0$. This is a direct, complete ODE argument,
not a numerical inference from finitely many cutoff samples.

For the two-shaper example, $m_1=16/15$ and $m_2=0$, so

\[
T_b=-\frac{16}{15r}b''
+\left(-\frac{32}{15}+\frac{16}{15r^2}\right)b'
+\frac{64}{15r}b+\frac{256}{315r^2}b^2.
\]

The second-derivative coefficient is nonzero on any annulus away from
the axis. Independent physical-stress integration checks this
decomposition for two distinct polynomial $b$ profiles, and the
original $r=2$ value remains exactly $-2036/315$.
`tests/test_h8_flat_edge_gate.py` reproduces the checks.

**Applicability boundary:** the original H8 one-sided cone only implies
an $O(b^2)$ shear target if *both* relevant slice supports are
$O(b^2)$ after reference-centre subtraction. The authentic density,
frame, transition cutoff, overlap stresses and common pressure have
not been fixed sufficiently to establish this. Second-jet-size
cancellation by a missing term, a vanishing combined $M$, or a
larger density budget remains possible. This is a necessary condition
for the restricted residual, **not** a disproof of the full H8 route.

### Common cutoff: the second-jet coefficient reduces to core circulation

The user-supplied three-page H8 flat-edge viscosity addendum has SHA-256
417a01820906d2ab8b7eaf8883f28006c70a9fae03500f59c2b5b603590c8525.
Its conditional Gronwall obstruction agrees with the calculation above.
The addendum cites a distinct 122-page Case 006 revision. That revision
has now been supplied and examined (source identity below). Its Appendix AD
provides explicitly frozen **diagnostic** positive shapers, but expressly
does not identify them with a globally glued, source-matched residual.

There is a more specific test when the core localization and the poloidal
shapers use the **same** radial envelope $b(r)$. Let $\mathcal A$ be
the smooth $C_4$-averaged core potential, let
$U_c=\operatorname{curl}\mathcal A$, and write
$M(r)=\sum_iK_i m_i a_i(r)$. The physical symmetric stress
$K=u\otimes u-\nu(\nabla u+\nabla u^{\mathsf T})$ has the exact
axial/angular integrated $rz$ second-jet coefficient

\[
\kappa_{2,\mathrm{eff}}(r)=
-\nu\left[
\int_{z_-}^{z_+}\langle\mathcal A_\theta\rangle_\theta\,dz
+\frac{M(r)}r\right].
\]

The core curl enters because
$\operatorname{curl}(b\mathcal A)
=b\operatorname{curl}\mathcal A+b'(e_r\times\mathcal A)$;
the axial component of the second term is $b'\mathcal A_\theta$.
Quadratic four-patch overlaps contain no $b''$ in this **physical
shear** channel, although the full source and its inverse can contain
higher derivatives.

Define $V(r)=\int_{z_-}^{z_+}\langle(U_c)_z\rangle_\theta dz$ and
$H_*=r_*\int_{z_-}^{z_+}
\langle\mathcal A_\theta(r_*,\theta,z)\rangle_\theta dz$.
Angular averaging of the axial curl gives

\[
\partial_r(r\langle\mathcal A_\theta\rangle_\theta)
=r\langle(U_c)_z\rangle_\theta,\qquad
\kappa_{2,\mathrm{eff}}(r)=
-\frac{\nu}{r}\left[
H_*+\int_{r_*}^r sV(s)\,ds+M(r)\right].
\]

Hence **identical cancellation** on a radial collar is equivalent to
one anchor moment and the exact differential condition
$rV(r)+M'(r)=0$ throughout the collar. For a globally smooth
axis-spanning potential one may set $r_*=0$ and $H_*=0$; for a
genuinely annular chart the circulation trace $H_*$ must be retained.

An exact annular negative control uses one positive shaper
$\Xi=(1-z^2)^2$, $K=a=1$, and
$\mathcal A_\theta=-8/(15r)$. Then
$M=16/15$, the axial core moment equals $-16/(15r)$, and
$\kappa_{2,\mathrm{eff}}\equiv0$. Its nonzero annular circulation is
**not** evidence for an admissible smooth axis-spanning H8 core.

The new shared-cutoff-moment Python calculator and its independent
tests compute the full physical shear, including $C_4$-periodic angular
overlaps, and verify the core moment reconstruction. Reproduce with
the test_h8_shared_cutoff_moment.py test module.
This does not insert the genuine source profiles into the four-coordinate
weighted H8 inverse.

### Source-audited split cutoffs and the nonradial second-jet terms

In the available 65-page structured-stress source, the core is localized
as curl(chi A_c), with chi a C4-invariant similarity-coordinate cutoff
equal to one on an inner region. The poloidal shell shaper is specified
separately by Psi=A_z ell^2 U Phi(r/ell) Xi(z/c). The source does not
identify chi with Phi or require chi to be radial. Its later scalar
function also named chi(eta), in the strong-Rayleigh section, is a
**different symbol**, not evidence for a common transition cutoff.

For arbitrary chi(r,theta,z), an independent radial shaper envelope b(r),
and P_theta=sum_i K_i a_i(r) Xi_i(z)/r, the exact physical rz shear
second-cutoff-derivative contribution is

\[
S_{\mathrm{jet},2}=-\nu\int_{z_-}^{z_+}\Big\langle
 A_\theta(\chi_{rr}-\chi_{zz})+
 (A_z/r)\chi_{\theta z}-(A_r/r)\chi_{r\theta}
 +P_\theta b''\Big\rangle_\theta dz.
\]

The difference S-S_jet,2 has at most first cutoff derivatives, including
products of first derivatives from all fourfold kinetic overlaps.
No estimate of that remainder in terms of b or b' alone follows:
chi is independent. In particular, without a verified relation
between chi and b the shared-envelope Gronwall obstruction is not
a theorem about the authentic source.

Pressure enters the integrated source via
q_s=[<u_z^2-2 nu partial_z u_z+p>_theta] at the axial endpoints.
The exact J_f=S-aS(a)/r+(1/r)int_a^r s q_s(s) ds must retain this
term, including its radial integration trace. An independently checked
pressure-only example has S=0, q_s=2(r^2-1), and
J_f=(r^2-1)^2/(2r) when a=1. It proves that a vanishing physical shear
cannot be substituted for a vanishing source primitive.
This J_f is the primitive of div K+grad p, not yet of the full
time-dependent residual. The latter includes the additional term

\[
T_z(r)=\int\langle\partial_tu_z\rangle_\theta dz,\qquad
J_{\mathrm{NSE}}=J_f+\frac1r\int_a^r sT_z(s)ds .
\]

The exact Python calculator leaves J_NSE as **unknown** if no time
symbol/source is given; it never silently sets T_z=0. A regression
example with u_z=t has J_f=0 but J_NSE=(r^2-1)/(2r).
Freezing the authentic time-dependent Case 006 source requires this
term as well as the spatial transition and pressure functions.

### A certified spatially varying H8 frame support enclosure

In the one-sided seven-ray H8 cone, the exact coordinate extrema are
at most the respective fractions
51113/245800, 15971/983200, 19171/122900 and 19171/491600 times
rho; hence every four-coordinate source-frame perturbation satisfies
||H||_F <= rho. If a slice is partitioned into cells with exact masses
m_j=int_cell rho, fixed orthogonal rational reference frames E_j,
and **certified** uniform frame-error bounds
sup_cell ||E-E_j||_F <= delta_j, the genuine weighted dual supports
satisfy

\[
\max(0,\widehat B_\pm-2\sum_jm_j\delta_j)
\le B_\pm\le
\widehat B_\pm+2\sum_jm_j\delta_j,
\quad
\widehat B_\pm=\sum_jm_j\sigma^+(\pm\lambda(E_j)).
\]

This is a rigorous route for continuous smooth nonanalytic frames when
valid enclosure data are supplied. It is not a numerical-grid
certificate by itself; the current source still lacks authenticated
masses, the field E and its interval/Lipschitz bounds.

The physical divergence also contains
sum_{j,a,b}[(partial_j E_ia)E_jb+E_ia(partial_j E_jb)]H_ab
besides the frozen-frame term
sum_{j,a,b} E_ia E_jb partial_j H_ab in Cartesian coordinates.
Cylindrical coordinates add their geometric connection. A rotating
stress can thus have nonzero divergence even for constant H, and
the new pointwise cone enclosure does **not** solve that PDE inverse.

The new h8_split_cutoff_gate.py calculator and
test_h8_split_cutoff_gate.py reproduce the split radial/axial jets,
the full cylindrical pressure flux, the rational two-cell support
and its frame-error enclosure, and the connection source.

## Normalized C4 transition, explicit candidate cutoff and pressure

The source localization lemma specifies averaging a vector potential
over the quarter-turn group **before** localizing with a C4-invariant
cutoff. In an equivalent order, let

\[
v_j=Q^j_*\nabla\times(\chi A),\qquad
u_b=\tfrac14\sum_{j=0}^3 v_j.
\]

The complete quadratic stress is **not** its four diagonal products:

\[
u_b\otimes u_b=\tfrac1{16}\sum_jv_j\otimes v_j+
\tfrac1{16}\sum_{j\ne k}v_j\otimes v_k.
\]

In the exact local example `A=(-yz,xz,0)`, `chi=1`, all rotated
velocities are `(-x,-y,2z)`. The four diagonal products carry one
quarter of the physical radial--axial shear and the twelve ordered
cross products carry **three quarters**. This distinguishes group
averaging from adding four disjoint supports: source symmetry alone
does not justify deleting overlaps. The example is local and not a
compactly supported H8 field.

`h8_c4_transition.py` now provides:

- the exact smooth, nonanalytic *candidate* radial cutoff
  `h(r-1) h(4-r)` with support `[1,4]`, plateau `[2,3]`, and
  `h(s)=exp(-1/s)/(exp(-1/s)+exp(-1/(1-s)))` on `(0,1)`;
- normalized rotating curls, their full quadratic stress and advective
  partitions, rejecting cutoffs that are not exactly C4-invariant;
- a particular toroidal-pressure representative
  `p_T(r,z)=int_a^r (2*u_theta*T_theta+T_theta**2)/s ds`, selected by
  `p_T(a,z)=0` rather than inferred from the source; and
- an exact pressure-endpoint jump, including nonvanishing trace tests.

The single-shaper local polynomial combination with
`U_r=-r, U_z=2z, U_theta=r, Xi=z**2*(1-z)**2, b=(r-1)**3`
and `T_theta=r*z*(1-z)` gives independent physical integration and
channel assembly as

\[
S(r)=\frac{-r^4-30r^3-2r+3}{30r^2},\quad
q_s(r)=4,\quad
J_f(r)=\frac{-r^4+30r^3-32r+3}{30r^2},
\]

with `S(3/2)=-63/40`, `J_f(3/2)=91/120` exactly. **The polynomial
combined example does not apply the new nonanalytic cutoff**; the two
checks intentionally test separate algebraic obligations. In particular,
these values do not establish whether the original H8 cone contains
an inverse for the genuine, compact, spatially varying source.

Reproduce using:

```sh
python -m unittest discover -s tests -p 'test_h8_c4_transition.py' -v
```

The authentic next input remains a fully frozen `chi` in similarity
coordinates, vector potential/transition core, toroidal pressure trace,
relative support geometry of the four rotations, and matched `rho,R_*,E`.
Only then can the complete nonanalytic flux and sharp weighted cone
be evaluated without an artificial replacement.

Reproduce the exact finite check with SymPy:

```sh
python -m pip install sympy
python -m unittest discover -s tests -p 'test_h8_exact_flux_gate.py' -v
```

## Recovered 122-page Case 006 source: exact axial band and its scope

The user-supplied **Carrier_Independent_Structured_Stress_Route_CASE006_122PAGE-3.pdf**
is a 122-page, unencrypted PDF with SHA-256
56ff24696ac58bef19bcf339d297d3af8b0401e46d5e8125c7fb1d054f01a758.
The original main-body equations (265), (269)--(273) are present, followed
by supplemental appendices including AC (PDF pp. 115--116), AD
(pp. 117--118) and AF (pp. 121--122). Appendix AC fixes the *physical*
cylindrical centre shear, not a new unknown cutoff:

\[
 \alpha=(R_*)_{rz}=-4443/9832,\qquad
 \kappa=15971/122900.
\]

For a chosen prepared symmetric stress \(T\), density \(\rho\), and
representative \(f=\operatorname{div}(T-\rho R_*)+\nabla p_0\),
define \(\mathcal T=\int\langle T_{rz}\rangle dz\),
\(\mathcal R=\int\langle\rho\rangle dz\), and
\(q=[\langle(T-\rho R_*)_{zz}+p_0\rangle]_{z_-}^{z_+}\).
Direct cylindrical divergence gives the exact source-native primitive

\[
 J_f=\mathcal T-\alpha\mathcal R
 -\frac ar[\mathcal T(a)-\alpha\mathcal R(a)]
 +\frac1r\int_a^r sq(s)\,ds.
\]

**Only under compact correction/boundary assumptions and the original
absolute coefficient cap** \(|\delta c_i|\le\kappa\rho\) does the
source-only scalar screen reduce to

\[
 -\frac{143017}{245800}\le
 \frac{\mathcal T(r)}{\mathcal R(r)}
 \le-\frac{79133}{245800}\quad(\mathcal R(r)>0).
\]

These endpoints, the full pressure-trace primitive and an attaining
absolute-budget coefficient vector are independently checked in
**tests/test_h8_case006_source_band.py**, using standard-library exact
fractions.

**Do not apply this interval to the larger one-sided positive cone.**
The positive cone in the same frozen physical frame permits a sharp
positive \(rz\) coefficient

\[
 A=(5g+h)\rho/4=51113\rho/245800>\kappa\rho,
 \quad g=15971/122900,\quad h=22371/122900.
\]

An explicit witness is \(D=(g+h)\rho/8\),
\(B=g\rho/8\), \(C=(h-g)\rho/4\); all seven original
coefficients remain at least \(\rho/100\). The independent rational
test checks all seven floors. For a genuinely rotating frame, the
pointwise physical \(rz\) entry additionally requires the pulled-back
covector and spatially varying support from the earlier section.

Appendix AD's infinitely flat two-shaper construction is intentionally
a **manufactured model**: it matches the physical centre shear at every
radius but omits the authentic core, transition, pressure and fourfold
overlap. Appendix AF proves a conditional \(b'\)-order obstruction for
positive two-shaper profiles, while explicitly leaving the actual
pressure jet, off-axis remainder and fourfold prepared stress unfrozen.
Neither appendix supplies the final \(T,\rho,p_0,E\) needed to test
the authentic weighted inverse.

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
The 122-page Case 006 revision is now identified above. It reproduces the
relevant main-body architecture and includes further diagnostic appendices,
but its Remark 9.23 still leaves the final normalized shell and
transition profiles freely chosen. The terminal source certificate
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

**Status: THE 122-PAGE REVISION IS RECOVERED; BLOCKED ON ITS UNFROZEN
PHYSICAL FUNCTIONS AND PATCH TRANSPORT, NOT ON THE ALGEBRAIC DUAL.**
The computed rational
obstruction is a reproducible negative control, not a test result for
the missing H8 residual and not a proof of unforced Navier--Stokes
regularity or blow-up. G4 and G8 remain `OPEN`.
