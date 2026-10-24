# Edition XXIII — nonaxisymmetric Fourier-mode pressure and torque gate

**24 October 2026 | Exact source-independent mode results. Full unforced Navier–Stokes and Lean proof OPEN.**

This is a cumulative successor to Editions XIX–XXII. It tests an m=±1 angular correction against the axisymmetric circulation gate, source residual, pressure compatibility and the existing H8 slice-torque obstruction. It is not an exact source correction.

## Coupled cylindrical m-mode system

For an axisymmetric pure-swirl background U(r,z,t)e_theta (not assumed force-free), let the perturbation be e^(imθ)(a e_r+b e_theta+c e_z), set D_m=∂rr+r^-1∂r-m²r^-2+∂zz and L_m=∂t-νD_m. Its exact linearized system with imposed modewise force H is

\[
\begin{aligned}
L_m a+\nu(a+2im b)/r^2+(imU/r)a-2Ub/r+\pi_r&=H_r,\\
L_m b+\nu(b-2im a)/r^2+(imU/r)b+(U_r+U/r)a+U_zc+(im/r)\pi&=H_\theta,\\
L_m c+(imU/r)c+\pi_z&=H_z,\\
a_r+a/r+imb/r+c_z&=0.
\end{aligned}
\]
The necessary, not sufficient, pressure compatibility condition is
\[
D_m\pi=\operatorname{div}_mH-2im(U_ra+U_zc)/r+2\partial_r(Ub)/r.
\]
The off-diagonal viscous terms are essential vector-Laplacian effects. No actual compatible Poisson inverse with regularity and source matching has been constructed.

## A smooth exact m=±1 positive control

On R² × S¹ with axial period 2π, set f=exp(-r²), a=f cos z, b=i a+λ r² f cos z, c=-f' sin z-iλrf sin z. The real velocity formed from plus and minus Fourier conjugates has exact Cartesian representation

\[
v=(2f\cos z(1-\lambda xy),\ 2\lambda x^2f\cos z,\ (4x+2\lambda y)f\sin z).
\]
It is smooth, finite-energy, divergence-free, and has precisely cylindrical m=±1 content. Its angular-mean Reynolds stress Q is pointwise PSD of rank at most two. Exactly,

\[
Q_{r\theta}=2\lambda r^2e^{-2r^2}\cos^2z,\qquad
Q_{z\theta}=\lambda r(2r^2-1)e^{-2r^2}\sin2z,
\]
\[
\boxed{g_\theta=r^{-2}\partial_r(r^2Q_{r\theta})+\partial_zQ_{z\theta}
=2\lambda r e^{-2r^2}(2-2r^2+\cos2z)},
\]
\[
\boxed{m(z)=\int_0^\infty r^2g_\theta(r,z)\,dr
=\lambda\cos2z/4.}
\]

The total axial torque is zero but the radial-slice torque is generally nonzero. This is an exact positive control for the kind of torque accounting needed by the separate H8 slender-shell inversion; it is not the actual H8 physical shell, so no unverified norm transfer is assumed.

## Exact non-gradient m=2 leakage

Quadratic self-convection of the positive unit mode creates an m=2 coefficient N. Its cylindrical components are

\[
N_r=aa_r+iba/r+ca_z-b^2/r,\quad
N_\theta=ab_r+ib^2/r+cb_z+ab/r,\quad
N_z=ac_r+ibc/r+cc_z.
\]
At λ=1,r=1,z=0, its axial curl is exactly

\[
\boxed{(\operatorname{curl}N)_z^{(2)}=2(-2+5i)e^{-2}\ne0}.
\]
Therefore this particular first-harmonic model cannot be closed exactly at modes 0,±1 by adjusting pressure alone. This does not rule out special null structures or other Fourier constructions.

## Verification and the remaining complete Lean gate

Independent SymPy differentiation of the modal pressure identity passes. Both independent complex-mode multiplication and real-angle trigonometric integration reproduce the same Reynolds components. Cartesian solenoidality, full Gaussian radial integration, the m=2 nonzero-curl witness and the Gram identity pass. Exactly 12,000/12,000 seeded rational cancellation examples pass. The scalar Lean file N1NonaxisFourierScalar.lean and its isolated kernel workflow are committed; a green run has not yet been reported.

The source's axisymmetric m=0 residual cannot be canceled *linearly* by pure m=±1 modes; their impact on m=0 begins quadratically and also generally creates m=±2. The next indispensable work is to freeze the authentic source's full A.11/A.19-corrected residual and mean pressure, test the stress-cone and H8 slice-torque margin, construct a coupled all-mode inverse and control infinite-harmonic nonlinear tails in a singularity-preserving norm. Only after an exact zero-force PDE solution with smooth finite-energy initial data and proven blowup exists can its theorem be formally integrated into the pinned OpenAI Lean library. The existing upstream formalization proves *forced Navier–Stokes* and *unforced Euler*, not the present unforced Navier–Stokes goal.

**RESEARCH STATUS: PARTIAL SOURCE-INDEPENDENT EXACT RESULT; FULL UNFORCED PDE AND END-TO-END LEAN PROOF OPEN.**
