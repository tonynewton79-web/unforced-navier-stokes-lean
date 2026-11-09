# Exact analytic-core initial moments and C3 error certificate

Research date: 9 November 2026. **Partial source-certified mathematics only.** The original OpenAI (2026) construction has smooth compact forcing. Neither the user's proposed *locally unforced* G1 series nor a global unforced 3D Navier–Stokes singularity is proved.

Authoritative source: OpenAI, *Finite Time Blowup for Navier–Stokes* (2026), equations (4.11), (B.11)–(B.17), (B.22), (B.25), https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf.

## Exact B.12 comparison fields

For the genuine axis functions U*=4eta+j0, L=1−2h eta², Z* defined by the actual axis pressure, chi=H*²/(H*²+sigma*²), and phi*(eta)=exp(Lambda integral zeta*), the SOURCE proves a nonlinear analytic fixed point
phi=phi* Phi(Y,eta), U=U*+Lambda^-1 u(Y,eta), Y=Lambda X.
Its **explicit comparison**, not the fully corrected solution, is
Phi0=f0(Y chi), u0=−Y z*, z*=Z*/(2L),
f0(z)=sum_k>=0 (-z/2)^k/[k!(k+1)!].
The nonlinear errors Phi−Phi0 and u−u0 are proven O(Lambda^-1) **with unpublished numeric constants** in B.13, and no one fully original-source-admissible numerical tuple has been certified here.

For integers r>=0 define F_r(chi)=∫_0^4 Y^r f0(chi Y)dY and B_r(chi)=∫_0^4 Y^r f0(chi Y)^2dY. The exact convolution
f0(z)^2=sum_n (-z/2)^n binom(2n+2,n+1)/[n!(n+2)!]
follows from Vandermonde. Also F1(chi)=−32 f0'(4chi) from the f0 regular-singular ODE.

On real chi∈[0,1], F_r and B_r decrease with chi. At chi=1, exact alternating sums with 24/25 terms give the certified intervals:
F0 ∈(2.393096190540,2.393096190542)
F1 ∈(3.836224657207,3.836224657210)
F2 ∈(9.055359580176,9.055359580179)
B0 ∈(1.602427000590,1.602427000593)
B1 ∈(2.035245417001,2.035245417004).
At chi=0, the sharp universal upper endpoints are F_r(0)=B_r(0)=4^(r+1)/(r+1). These are **not evaluated original chi(eta) functions**, only universal scalar bounds.

## Genuine source initial radial moments: exact comparison formulas

Original source moment derivative vector is (U,2X phi/C,2X U phi/C,U²−X phi²/C²,phi²/C²). Set X0=4/Lambda and z*=Z*/(2L). The five comparison moments are exactly:
M_cmp=4U*/Lambda−8z*/Lambda²
I_cmp=2phi*F1/(C Lambda²)
J_cmp=2phi*[U*F1−z*F2/Lambda]/(C Lambda²)
S_cmp=4U*²/Lambda−16U*z*/Lambda²+64z*²/(3Lambda³)−phi*² B1/(C² Lambda²)
Cp_cmp=phi*² B0/(C² Lambda).

No synthetic axis data are substituted; these are symbolic functions of the original source axis fields.

## New explicit, common C3 error-to-moment map

Use the factorial-weighted norm ||F||_(3)=sum_{j=0}^3 sup_eta|∂eta^j F|/j!, a Banach-algebra norm with product constant 1. Define m_j=||∂eta^j chi||infty for j=1,2,3. Source scalar series and alternating bound |f0^(k)(z)|≤1/[2^k(k+1)!] for k=1..3, 0≤z≤4 give
Qchi=1+m1+(m2+(2/3)m1²)/2+(m3+2m1m2+m1³/3)/6
as a bound on ||Phi0||_(3) for 0≤Y≤4.

Assume a **genuine independently certified** B.2 fixed-point error:
||Phi−Phi0||_(3)≤epsPhi, ||u−u0||_(3)≤epsu, uniform Y∈[0,4].
Also let P,U,Z be certified upper bounds on ||phi*||_(3),||U*||_(3),||z*||_(3).
Set Pc=P Qchi, Pa=P(Qchi+epsPhi), Uc=U+4Z/Lambda, Ua=U+(4Z+epsu)/Lambda, dp=P epsPhi, du=epsu/Lambda.
The actual initial five moment errors then have the following **explicit algebraic**, fully reproducible bounds:
||Delta M||_(3)≤4 du/Lambda
||Delta I||_(3)≤16 dp/(C Lambda²)
||Delta J||_(3)≤16(du Pa+Uc dp)/(C Lambda²)
||Delta S||_(3)≤4du(Ua+Uc)/Lambda+8dp(Pa+Pc)/(C² Lambda²)
||Delta Cp||_(3)≤4dp(Pa+Pc)/(C² Lambda).
All arise from original moment integrals and polynomial factorizations; none supplies the as-yet-unvalidated numerical epsPhi,epsu.

## Original source reference-stress positivity, not just comparison positivity

The actual analytic core has source Sq≥2.5+0.95 Lambda L chi (B.17), and p1=−2X ∂X logphi, with p1 transport (B.25):
d_y p1+ell p1=XSq/L, ell=1+Xphi_X/phi.
It follows by an integrating factor that d_X(Xphi p1)=Xphi Sq/L. Since Sq>0 and the axis is regular, p1>0 on X>0, so phi_X<0. Thus:
p1(X0)≥(5/4)X0=5/Lambda.
This is important where H*=0, chi=0: the *comparison* p1 vanishes but the actual source p1 remains strictly positive. Once **all** Lemma B.4 reference-construction conditions hold, its explicit comparison inequality gives p1,r(110)>131.8 for Lambda>=1. These results do NOT certify the source's later corrected cone.

## Honest numerical gate

The source B.2 fixed-point ball and contraction constants, exterior pressure schedule and original C0(Lambda) are not numerically specified. Thus **no genuine C3 nonlinear core interval**, no authentic initial five moments, no reference p1,r/ns,r C3 interval over [X0,110], no seven Xi inputs, and no corrected five-bump or cone intervals have been certified.

In the conversation, a four-page professional standalone TeX/PDF, a 245-page cumulative research PDF retaining all 241 previous pages, local exact-Fraction/SymPy verification, a source-specific rational input calculator that **REFUSES absent inputs**, JSON input specification, audit and a complete SHA256-verified ZIP were produced. The GitHub regression can certify finite universal comparisons, not an infinite-dimensional theorem. This PR must remain DRAFT.

Next genuine step: first freeze one source-admissible exterior pressure and axis tuple with actual holomorphic multiplier bounds, then obtain numeric invariant-ball and Lipschitz constants for B.12–B.16 on a single C3 domain; only then feed certified errors to the current five-moment ledger and Attack46 B.22/B.26 endpoint propagator.