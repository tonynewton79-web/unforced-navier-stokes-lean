# Pulse-end source theorem and Lean dependency ledger — 21 October 2026

STATUS: Exact structural result, not a completed unforced Navier–Stokes theorem.

The source Appendix A.9 translated positive bump matrix has entries
[[k_alpha, exp(2 alpha) k_alpha], [k_beta, exp(2 beta) k_beta]],
where alpha=1/2-lambda and beta=1/2-2lambda.
Its determinant equals
-k_alpha*k_beta*exp(2 beta)*(exp(2 lambda)-1)<0.
The unique correction coefficients therefore cancel the two terminal
M,J moments exactly; their true eta derivatives cancel both first jets.
When U=0 on later stages these four normalized variables remain zero
even through the different Appendix A.11 azimuthal corrections.
Hence only i,s,i_eta,s_eta remain as forward moment states;
p,p_eta retain their separate radial-infinity backward gauge.

For a source-authenticated entrance bound |i(0)|,|i_eta(0)|<=100,
0<lambda<=1/20 and 0<h<=lambda/100, the paper proves
|Q_s(Y)-q0| <= (775680000/3722098081)*lambda^4 < lambda/1000,
so Q_s(Y)>lambda/2. This is a PULSE-EXIT implication, not a
uniform pulse or A.11 support certificate.

Independent exact tests:
- pulse_end_moment_cancellation_exact.py, generic 2x2 inverse,
  two moments, both eta jets, post-pulse stresses;
  negative control catches omitted coefficient derivatives.
- pulse_end_Q_positive_exact.py, exact rational fourth-order bound.
- PulseEndMomentCancel.lean, scalar candidates WITHOUT sorry or new
  axioms; kernel correctness still requires successful CI.

OPEN STEP 1: Freeze a genuinely source-admissible Appendix A tuple,
including the actual axial A.9 and distinct azimuthal A.11 correction
coefficients and their eta sensitivities.
OPEN STEP 2: Certify the real pulse-entrance i and i_eta values.
OPEN STEP 3: Certify the full pulse xi in [0,13] with rigorous
integrating-factor kernels and correlated source interval data,
including A.29-A.30 residual bounds and Q_s positivity everywhere.
OPEN STEP 4: Check full exterior stress cone, A.11 support ratio
|N_s|/E<=lambda/2, joining stages and terminal matching.
OPEN STEP 5: Certify the nonlinear Appendix B common analytic profile,
actual unforced n=1,2 startup solutions, complete recurrence,
differentiated convergence and zero physical no-force PDE residual.
OPEN STEP 6: Formalize all integrals, certified intervals, analytic
estimates and PDE reconstruction in Lean and obtain independent review.

No full Lean proof of the proposed unforced Theorem 1.1 exists.
The originating OpenAI whole-space theorem has compactly supported
smooth forcing and is not an unforced singularity theorem.
