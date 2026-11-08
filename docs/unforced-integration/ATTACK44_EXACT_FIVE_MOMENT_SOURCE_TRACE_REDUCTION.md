# Source-exact five-moment trace reduction and cone response — 8 November 2026

**Result:** Exact reduction of the actual original B.8 five-moment discrepancy to six analytic input traces and rigorous coefficients for one source-compatible cutoff. **No actual numerical radial continuation, matching coefficients, corrected cone, G1 convergence or global unforced singularity is certified.** The original OpenAI (2026) paper is a **forced** Navier–Stokes result: https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf

## Source and normalization

Use original source (B.34)–(B.39), with x=X/X_R, E0=P_*f(eta)x^(1/10), U0=4eta and f=(1+eta²)^−1. The original azimuthal transition finishes at x_s=X_sep/X_R=exp(T_sh)/(CP_*)^10<exp(−8). For x>=x_s until the 5-bump patch, E is **exactly** E0, while U=G_i(eta) until it is smoothly restored to 4eta on exp(−8)<x<exp(−7). Fix an explicit source-permitted restoration alpha(x):
- alpha=1 for x_s<=x<=exp(−8);
- alpha=1−sigma(log x+8) on exp(−8)<x<exp(−7);
- alpha=0 for x>=exp(−7).

The source smooth step sigma is monotone, flat at endpoints, symmetric sigma(t)+sigma(1−t)=1, and has explicit formula sigma(t)=[1+exp(t^(-2)−(1−t)^(-2))]^(-1). Set g(eta)=G_i(eta)−4eta and U=U0+alpha*g. This is a choice of the source's allowed restoration cutoff, not a claim that its published construction uniquely fixed that cutoff.

## EXACT five-component discrepancy at the source's correction entrance x=exp(−6)

Define five accumulated trace mismatches B=(B_M,B_I,B_J,B_S,B_C) at x_s relative to the ideal reference, using the source's row basis (Mhat,Ihat,Jhat−4eta Ihat,Shat−8eta Mhat,Cp). The source source-native normalized moment definitions are:
Mhat=integral U dx, Ihat=integral sqrt(2x)E dx, Jhat=integral sqrt(2x)U E dx, Shat=integral (U²−E²/2)dx, Cp=integral E²/(2x) dx.

The **exact original pre-correction** joining vector, at x=exp(−6), is

 d5=( B_M+R1*g, B_I, B_J+sqrt(2)P_*f*R35*g, B_S+R2*g², B_C )

with
R1=exp(−8)[1+I1]−x_s,
R2=exp(−8)[1+I1sq]−x_s,
R35=exp(−64/5)[5/8+I8/5]−(5/8)x_s^(8/5),

I1=∫_0^1 exp(t)[1−sigma(t)]dt,
I1sq=∫_0^1 exp(t)[1−sigma(t)]²dt,
I8/5=∫_0^1 exp(8t/5)[1−sigma(t)]dt.

**Exact cancellations:** E=E0 after x_s implies I and Cp acquire no later discrepancy. J−4eta I integrates sqrt(2x)(U−U0)E, and S−8eta M integrates (U−U0)² because U0=4eta. No linear g term is permitted in the fourth row. The mismatch vanishes on exp(−7)<x<exp(−6) before the five bumps.

## Fully exact rational cutoff certificates

Monotone interval sums at N=8192 cells with pure Fraction, exact Taylor envelopes of exp and outward rounding denominator 2^40 verify:
0.650848<I1<0.651130,
0.602312<I1sq<0.602583,
0.770655<I8/5<0.771080.

Therefore
5.5379e−4<R1+x_s<5.5390e−4,
5.3751e−4<R2+x_s<5.3761e−4,
3.853e−6<R35+(5/8)x_s^(8/5)<3.855e−6.

For eps_g=||g||_(C1) and eps_B=max_j||B_j||_(C1), since ||f||_(C1)<=5/3 and ||g²||_(C1)<=eps_g²:
||d5||_(C1,infinity) <= eps_B+
 max{5.5390e−4 eps_g, 9.1e−6 P_* eps_g, 5.3761e−4 eps_g²}.
This is a **fully numerical coefficient bound**, but actual eps_g and eps_B **have not been supplied/derived numerically** from the original source continuation. It is therefore NOT a genuine unconditional numeric enclosure of the original d5.

## Exact nonlinear five-bump and stress-response identities

For two U bumps delta U=Σ_(j=1,2)c_j u_j and three E bumps delta E=Σ_(k=1,3)c_(k+2)e_k in exp(−6)<x<exp(−5), after the source's row operations, the quadratic terms are

Q_M=Q_I=0,
Q_(J−4eta I)=∫sqrt(2x) delta U delta E dx,
Q_(S−8eta M)=∫[(delta U)²−(delta E)²/2]dx,
Q_(Cp)=(1/2)∫(delta E)²/x dx.

The overlap cross term delta U delta E is ESSENTIAL. The source's finite correction equation is B5*c+Q5(c,c)=−d5, with inverse bounds from Attack43 but NO numeric input d5.

For a fully corrected state let delta m=(delta M,delta I,delta J,delta S,delta Pi) and delta H=sqrt(2x)delta E, all relative to the same ideal reference. From the source's **exact (B.35)**, write T0=x H0(Q0+W0), delta T=(1−h)delta I−Deta delta I_eta−(1−eta²)delta J_eta+2(h−D)eta delta J. Then

delta W=−[2Deta delta M+(1−eta²)delta M_eta]/x,
delta Qs=−delta W+[delta T−x(Q0+W0)delta H]/[x(H0+delta H)],
delta Ns=−W0 delta U−delta W U0−delta W delta U
 +[D(delta M−eta delta M_eta)+4h eta delta S−(1−eta²)delta S_eta]/x
 +4Aeta delta Pi−(1−eta²)delta Pi_eta.

These were independently verified algebraically. Numerical pointwise interval testing of original source (B.36), especially corrected Ns/(E Qs), is STILL REQUIRED. If (B.36) has been certified and Qmin>87/50, an explicit sufficient last scale is X_R>=9000 for Pc>2 everywhere on exp(−8)<=x<=exp(−5). This DOES NOT establish the (B.36) premises.

## Input bottleneck and evidence

The source Proposition B.8 continues a parameter-dependent analytic profile and chooses C,j0,Lambda etc by successive existence criteria. It does not publish one numerical interval enclosure for the six required C² traces (g and B_M,B_I,B_J,B_S,B_C), nor a fully numerical source-admissible parameter tuple. Thus the five nonlinear coefficients and corrected strict cone minima cannot truthfully be computed as numeric values from the available source alone.

A 3-page polished mathematical PDF/TeX note is appended to the earlier 232-page cumulative research PDF, giving **235 pages** with all earlier 232 page text streams exactly preserved. Pure Fraction N=8192 intervals, Sympy exact row and stress identities, and independent arbitrary-profile 60-digit direct integral replay (<1e−48 agreement) passed. The diagnostic profile is NOT the original Gi. Complete LaTeX/proof/verifier ZIP and SHA-256 checks were created. This note is a new *reduction and authenticated interface*, **not completion of Proposition B.8's numeric run, local G1 or the global unforced problem**.
