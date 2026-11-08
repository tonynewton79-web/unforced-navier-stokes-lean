# Attack 38: constructive exterior-pressure moments and axis-screening selector

**Research date: 8 November 2026. Status: PARTIAL SOURCE CERTIFICATE. Full local G1 convergence and global unforced 3D Navier–Stokes finite-time blow-up remain OPEN.**

Source: OpenAI, *Finite Time Blowup for Navier–Stokes* (2026), Lemma A.5, equations (A.6)–(A.7), Appendix B.1–B.3. The original theorem is about the **forced** equations: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

## Pressure datum: eliminate the unknown analytic radius

The source's reference swirl, with pressure-neutral angular bumps omitted, is E_ref(y,eta)=c(y)(1+eta²)^(−theta(y)), with 0<=theta<=1 and c,theta independent of eta. Define I0=integral c²dy and I1=integral theta*c²dy. Then the *genuine source axis pressure* is

P_axis(eta)=−(1/2) integral c(y)² (1+eta²)^(−2theta(y))dy.

The function is holomorphic on the **explicit strip** |Im eta|<1. On |Im eta|<=1/4, |P_axis|<=128 I0/225. For every real x and m>=0, |P_axis^(m)(x)| <=(128/225)I0 4^m m!. Its centre moments are P_axis(0)=−I0/2 and P_axis''(0)=2I1. All higher even derivatives are computable as Pochhammer moments.

Source (A.7) imposes c(y)=P_amp*exp(y/10) and theta=1 on y<=0; hence I0,I1>=5 P_amp², and the independently audited G1 correction jet improves to
Pi1_X(0,0)=−12−(1/2+h)I0−I1 <=−12−(15/2+5h)P_amp².

## Constructive axis screening (B.2), conditional on the preceding exterior schedule

For 0<h<1/100, 0<j0<=1/20 and original exterior amplitude P_amp>=1, write A=1/2+h, D=1/2−h, U*=4eta+j0, H*=Deta+(1−eta²)U*, and use the original Z*:
Z*=−A(1−2eta U*)U*−H*U*'−(1−eta²)P_axis' +4Aeta P_axis.
The unique root H*(eta0)=0 obeys −j0/4<eta0<−j0/5; the pressure moments give Z*(eta0)>0.9 j0. Exact rational bounds yield sup_(eta in [-1,1])|Z*'|<=103+24 I0.

**Fully explicit source B.2 selector:**
r*=j0/[10(104+24I0)], delta*=j0/2, sigma*=r*/20=j0/[200(104+24I0)].

On the concrete interval [-101/100,101/100], |Z*|<=delta* implies |H*|>=r*, hence chi=H*²/(H*²+sigma*²)>=400/401>99/100. This verifies the specific source screening requirement B.2, not the full Proposition B.2 existence/continuation threshold.

## Common axis-only inherited multiplier bounds

The explicit axis tube width is delta_ax=min(1/10,sigma*²/880) and the inherited transverse weight radius is varrho=delta_ax/8. If axis-only F is analytic and bounded by M_F on that tube, Cauchy bounds imply ||F||_B<=M_F and ||partial_eta F||_B<=4 M_F/delta_ax. The exact elementary supremums are sup_(m>=0)(m+1)²/4^m=1 and sup_(m>=0)(m+1)³/4^m=2.

Source-specific supremum envelopes: L^(-1)<=100/97, |H*|<11, |zeta*|<=23/sigma*², |chi|<=3, |eta/L|<=2, |d/L|<=4, |P_axis|<=128I0/225, |phi*|<=exp(30Lambda/sigma*²). Thus C>=exp(30Lambda/sigma*²) suffices for source normalization (B.16), **not** for the independent unspecified contraction threshold C0(Lambda).

## Critical unsolved input schedule

The original ordered choices Md, Td=exp(Md+10), P_amp>exp(Td), lambda <<1, h<<min(lambda,exp(−Td)), then j0,sigma*,Lambda,C include non-numerical threshold phrases. Neither a numerical source-admissible exterior schedule nor I0,I1 has been interval-certified. No certified complex *radial leading profile*, finite startup hierarchy, noncircular startup threshold or zero physical PDE residual has been produced. The diagnostic h=1/200 is not a validated member of the original extremely-small-h schedule.

**Next:** fully authenticate one actual exterior schedule and integrals, resolve each implicit selection threshold, certify the radial leading solution and inherited multiplier constants on one fixed product domain, and then verify every finite startup coefficient and the differentiated unforced residual. The weighted H8 seven-ray inverse and nonlinear global correction remain open.

This claim boundary is intentional. The three-page full scholarly proof, cumulative 216-page PDF (preserving all prior 213 pages), exact checker and SHA-256 proof packet are conversation artifacts, not a Lean proof of the G1 existence theorem.
