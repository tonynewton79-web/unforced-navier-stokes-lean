# Attack 52 — an exact polynomial toroidal weak-dual obstruction

**21 November 2026.** This is a localized no-go theorem for the *frozen source-first diagnostic plateau* of Attack49/50, not the authentic B.12 G1/H8 core. It does not resolve unforced Navier–Stokes blow-up.

## Fully specified local assumptions and test

Let `tau=1-t`, `h=1/200`, `A=1/2+h`, `D=1/2-h`, `beta=1/2-2h=49/100`. On the open support of the proposed test, assume a smooth divergence-free periodic carrier `U` has the *exact* local values

`U_r=0, U_theta=(s/20)*tau^(-A), U_z=(1/20)*tau^(-A)`,
with `s=r/sqrt(tau)`, `xi=z/tau^D`.

Replace the exponential cutoff of Attack51 by `K(q)=(1-q^2)^4` for `|q|<1`, zero outside. This is globally `C^3` (sufficient for the weak integration), not `C^infty`.
Define the divergence-free toroidal test

`V_tau=r K(128(s-3/32)) K(16xi) e_theta`.

It is supported inside the local solid-rotation plateau in
`11/128<s<13/128`, `|xi|<1/16`. The periodic embedding is the same local chart as in Attack49. The source pairing is now derived directly from the local plateau, **not assumed from Attack49**:

`N(U)_theta = (201/4000) r tau^(-A-3/2)`,

because the angular advection and angular viscous term vanish identically for solid rotation. Hence

`<N(U),V_tau> = (201/4000)*J*tau^beta`

with an **exact integral**

`J=2*pi*integral(s^3 K(128(s-3/32)) K(16xi) ds dxi)=529*pi/993484800`.

Indeed `I0=int_(-1)^1 (1-q^2)^4 dq=256/315`,
`I2=int_(-1)^1 q^2(1-q^2)^4 dq=256/3465`; the change of variables `a=128(s-3/32)`, `b=16xi` gives
`J/pi=2*(1728 I0+36 I2)*I0/(128^4*16)`.
Using `pi>3`, obtain `J>529/331161600`.

## Exact conservative support and derivative bounds

For `tau in (0,1]`, the support volume is

`|S_tau|=(3*pi/8192)*tau^(3/2-h)<tau^(3/2-h)/512`

(using `pi<4`). Derivative estimates follow from `|K|<=1`, `|K'|<=8`, `|K''|<=56`:

- `|V_theta|<=sqrt(tau)/8`,
  `|partial_t V_theta|<=17/2*tau^(-1/2)`,
  `|partial_t(chi(tau/T)V_theta)|<=21/2*tau^(-1/2)`;
- `|r*partial_r W|<=128`,
  `|partial_z(rW)|<=16*tau^h`;
- `|Delta V_theta|<=119552*tau^(-1/2)`.

Here `chi(y)=16(y-1)^2(2-y)^2` for `1<=y<=2` and `0` otherwise, with `int_1^2 chi=8/15`, `0<=chi<=1`, `|chi'|<=8`. Its endpoint values vanish, so integrating by parts produces no correction trace term.

## Theorem: weighted L2 correction cannot be asymptotically negligible

Let `w` be any smooth solenoidal periodic correction such that `U+w` solves the **exact unforced** viscosity-one Navier–Stokes equation with one periodic pressure on the dyadic slab `1-2T<=t<=1-T` for `0<T<=1/2`.

Define
`q=(tau^(1/2)*w_r,tau^A*w_theta,tau^A*w_z)` and
`Q_T^2=T^(-beta-1) int_T^(2T) tau^(-1-h) int_(S_tau) |q|^2 dx dtau`.

**Conclusion:**

`Q_T > 35443/6246339052800000 > 5.67e-12`.

This is a carrier-specific obstruction to *subleading recovery*. It **does not** rule out general corrections (e.g. `w=-U`) or any unrelated blow-up construction.

### Proof ledger

The exact cylindrical contractions, valid also when `w` is nonaxisymmetric, satisfy

`|(U tensor w+w tensor U):grad V_tau| <= (17/10) tau^(-1-h) |q|`,

`|(w tensor w):grad V_tau| <= tau^(-1-h)*(128|q_r q_theta|+16|q_z q_theta|) <= 72 tau^(-1-h)|q|^2`.

The last bound has the explicit SOS identity
`72(a^2+b^2+c^2)-128ab-16bc=64(a-b)^2+8(b-c)^2+8a^2+64c^2`
for `a,b,c>=0` (and indeed for arbitrary real `a,b,c`).

The support mass normalized by `T^(beta+1)` is strictly less than `1/256`, since `0<beta<1`; its square root is less than `1/16`. Time integration by parts, spatial integration by parts and pressure elimination give

`35443/827904000000 < ((119552+21/2+17/10)/16)*Q_T+72*Q_T^2`.

For `0<=Q_T<=1`, the right-hand side is at most
`(603581/80)*Q_T`. For `Q_T>1` the desired bound is automatic. Exact division yields the conclusion.

The derivation directly evaluates the diagnostic source pairing; it does not import Attack49's earlier approximate exponential integral lower bound.

### Formal boundary

`UnforcedPatching/Attack52PolynomialDualArithmetic.lean` contains exact rational binomial moments, the SOS identity, scalar constants and the **conditional** implication from the displayed weak-form inequality. The full weak PDE calculation and analytic `pi` bounds are written here, but are **not Lean theorems**. The independent SymPy/Fraction verifier reproduces all finite arithmetic. No project axiom, `sorry` or presumed blow-up witness is inserted.

**Real full-theorem gates remain open:** authentic G1/B.12 complete field and source; periodic pressure; complete nonlinear inverse or independent certificate; energy/smoothness; terminal retention; final kernel checked *unforced* theorem. Separately, Alpöge–Buckmaster's 20 November 2026 candidate proof has a conditional Lean theorem and unreleased computational certificate according to their own README. Do not import its conditional conclusion as an unconditional theorem.
