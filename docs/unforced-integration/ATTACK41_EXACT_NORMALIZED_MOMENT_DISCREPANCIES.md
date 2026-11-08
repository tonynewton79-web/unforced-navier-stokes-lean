# Exact source-normalized two-moment discrepancy — 8 November 2026

**Research boundary:** This closes the **prescribed angular two-moment correction** in Appendix A.3 of the original OpenAI **forced** Navier–Stokes construction, assuming its prescribed earlier-stage conditions. It does not authenticate the full 3×3, 5×5, heat or stress-cone exterior; the G1 exact local unforced core and global unforced singularity remain OPEN.

The source is https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf, especially (4.15), (A.5)–(A.11), Lemma A.2, and the radial angular moment equation in Appendix A.3.

## 1. Actual angular vector, without an anonymous C_pre

Let \(\lambda\in(0,1/16]\), \(c=1-\lambda\), \(H=\sqrt{2X}E\), \(I(X,\eta)=\int_0^XH\), \(r_I=I/(XH)\), and \(y=\log X\). For the prescribed logarithmic slope \(l=\partial_y\log H\),
\[
\partial_y r_I=1-(1+l)r_I.
\]
The reference \(y\le0\) has \(l=3/5\), hence \(r_I=5/8\). All subsequent stages prior to angular interpolation (the first transition, axial transition, intermediate segment, and full axial pulse) have \(l\ge-\lambda\). They change \(U\), not \(E\), so \(0\le r_I\le1/c\) at the interpolation start. This also applies after axis attachment **provided its five source moments have been matched**, as prescribed separately in Appendix B.

On the source's actual interpolation of length \(T_f=256\),
\[
l=-\lambda-\Delta(\eta)q(y),\quad
\Delta(\eta)=\log2-\log(1+\eta^2),\quad
q(y)=\sigma'(y/256)/256.
\]
Let \(r_f(\eta)\) be the value of the unique ODE solution at the end of interpolation. The source then holds \(l=-\lambda\) for \(30\log(1/\lambda)\). The two angular bumps are centered 3 and 1 units before its end, so the first-center local distance is \(Y=30\log(1/\lambda)-3\).

The exact source-normalized *uncorrected* moment discrepancy for the two conditions in (A.11) is
\[
\boxed{d_{\rm ang}(\eta)=(-(r_f-c^{-1})e^{-cY},\ 0).}
\]
The second component is exactly ZERO: that source condition preserves the pressure moment of the **unedited** profile. The first component has the sign needed to cancel \(I-XH/(1-\lambda)\) at the endpoint.

**Exact uniform C1 theorem.** With source step derivative bound \(0\le\sigma'\le36\), \(\Delta\in[0,7/10]\), \(|\Delta'|\le1\), put \(q_{\max}=9/64\). The multiplier \(k=c-\Delta q\) satisfies \(k\ge4/5\) for all \(\lambda\le1/16\). The actual r equation and upstream comparison imply \(0\le r\le5/4\). For \(e=r-c^{-1}\),
\[
 e'=-ke+\Delta q/c,\quad e_\eta'=-ke_\eta+\Delta'qr,\quad e_\eta(0)=0.
\]
Thus \(|e(256)|<1/7\), \(|e_\eta(256)|\le225/1024<1/4\), whence \(\|e(256)\|_{C^1}<1/2\). Since \(e^{3c}\le e^3<21\), \(30c\ge225/8>28\),
\[
\boxed{\|d_{\rm ang}\|_{C^1([-1,1])}<11\lambda^{28}.}
\]
This directly implies \(\|d\|_{C^1}<1/1500\) and \(\|d\|_{C^0}<\lambda/10^6\) for every \(\lambda\le1/16\). Applying the **previously verified** source-specific nonlinear two-bump inverse estimates from Attack 40,
\[
\boxed{\|c_{\rm ang}\|_{C^1}<33\lambda^{28},}
\]
and the correction preserves \(E>0\) and the strict slope \(l<-\lambda/2\). **This particular angular 2×2 stage is closed at the mathematical level without knowing C_pre or fixing a numerical M_d,P_*.** It is NOT the complete exterior.

## 2. Exact axial-pulse vector including all upstream contributions

Let \(P_*>0\), \(f(\eta)=(1+\eta^2)^{-1}\), \(X_R\) original reference radius, \(H_0=\sqrt{2X_R}P_*f\), \(T_d=e^{M_d+10}\), \(T_w=60\log(1/\lambda)\), and
\[
k(t)=4[1-\sigma(\log(1+t)/M_d)],\quad
K_d=\int_0^{T_d}e^t k(t)\,dt,\quad
J_d=\int_0^1\exp(8y/5-3\int_0^y\sigma(v)dv/5)\,dy.
\]
The EXACT full pre-pulse moments are
\[
M_p=X_R\eta(4e+eK_d),\qquad
J_p=X_RH_0\eta(5/2+4J_d+e^{13/10}K_d).
\]
This includes \(y\le0\), first-unit transition and entire axial transition. The intermediate stage has \(U=0\), so its M,J do not change. At pulse start \(X_p=X_Re^{2+T_d+T_w}\), and
\[
X_pE_p=X_RP_*f\,e^{D_M},\quad X_pH_pE_p=X_RH_0P_*f\,e^{D_J},\quad
D_M=13/10-\lambda/2+T_d/2+(1/2-\lambda)T_w,\quad
D_J=8/5-\lambda+T_d/2+(1/2-2\lambda)T_w.
\]
Set \(s_1=1/2-\lambda,s_2=1/2-2\lambda,Y_p=13/\lambda-3\). For the source trial amplitude \(\mathsf A(\eta)\) and prescribed pulse shape \(R_0\), define
\[
L_i(\lambda)=\int_0^{11/\lambda}e^{-s_i(Y_p-v)}R_0(\lambda v)\,dv,\quad i=1,2.
\]
The exact source-normalized axial discrepancy, before the two relative U bumps, is
\[
\boxed{d_{\rm ax}(\eta)=-\left(e^{-s_1Y_p}\frac{M_p}{X_pE_p}+\mathsf A L_1,\quad e^{-s_2Y_p}\frac{J_p}{X_pH_pE_p}+\mathsf A L_2\right).}
\]
Nothing is concealed inside a C_pre term. If \(M_d\ge0\), \(P_*\ge1\), \(0<\lambda\le1/64\), and a trial \(\mathsf A\in[0.9,1.2]\), then source \(k(t)\) is supported before \(e^{M_d}-1\), \(K_d\le4(e^{e^{M_d}-1}-1)\), \(J_d<5\). Since \(T_d>1000e^{M_d}\), the upstream normalized terms are bounded by \(8e^{-499}\), \(58e^{-499}\). Since \(R_0\le11\) and vanishes after \(\xi=11\),
\[
L_i\le(88/3)e^{-375/8}<(88/3)10^{-20}.
\]
Therefore \(\|d_{\rm ax}\|_{C^0}<10^{-18}\). Its **C1** norm still depends on the *actual corrected amplitude derivative* \(\mathsf A'(\eta)\), which is not numerically certified because the source (A.19) remainder constant was not fixed. No final pulse coefficient or five-moment heat correction is claimed.

## 3. Independent verification / next gate

The scholarly 3-page PDF/LaTeX and 225-page cumulative research PDF preserving the previous 222 page text streams have been created. Exact rational/SymPy replay checks the difference equation, factorial-free rational margins, amplitude C0 tail, and upstream normalization. An independent scipy ODE integration tested \(\eta\in\{-1,-1/2,0,1/2,1\}\), \(\lambda\in\{1/16,1/32,1/64\}\), several extremal initial values and agreed with the very conservative exact bound. The theorem depends on the exact inequalities, not finite simulations.

**Next missing source data:** certify \(C^1\) of corrected \(\mathsf A(\eta)\) from its scalar S moment (A.19), then the axial C1 correction and the additional nonlinear three-/five-moment and heat exterior systems, including the complete strict seven-ray stress cone. The original 2026 OpenAI construction proves a **forced** singular-flow theorem; local and global unforced Navier–Stokes results remain OPEN.
