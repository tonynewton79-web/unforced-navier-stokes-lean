# Edition XXXII: source numerical freeze gate and a nonzero-data spectral-retention obstruction

**24 October 2026 | Tony Newton | Newton Astro Labs**

## Source provenance and audit
Primary source: OpenAI (2026), *Finite Time Blowup for Navier--Stokes*, 166-page paper at https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf. Inspected actual pages 117–118, 124 and Appendix B pages 144–147 (PDF zero-based indices 116,117,123,143,145,146), including equations (10.3)–(10.5), (10.20)–(10.21), and Proposition B.2.

Section 10 does **not** supply a uniquely specified numerical profile and cutoff set. In particular, the constants qstar and C0, h and the earlier nonlinear-profile thresholds, and the cutoff functions are not all frozen numerically. The condition C0(tau0+z0^(1/(1/2-h)))<qstar/2 controls *admissible* choices; it does not identify one. The script/JSON intentionally leave true source values null and return HOLD.

## Mathematical results established
1. **Conditional rational shell certificate.** With independently certified outward bounds 0<m_-<=||u_B(t*)||_2, R²<=R2+, V<=V+, ||grad u_B||_2/||u_B||_2<=Q+, if rational L>0 and integer N>=1 satisfy R2+ V+ L^5<=45/4 and 2^N L>=4 Q+, then one of the N dyadic shells obeys b_K(t*)²>=13 m_-²/(16N). This requires no floating-point quadrature. The synthetic smoke test N=5, b_K²>=13/80 is NOT an original OpenAI numerical result.
2. **Rigorous small-nonzero-initial-data no-retention theorem.** For every fixed source shell b_K(t*)>0 and every 0<=kappa<1, arbitrarily small NONZERO compactly supported divergence-free initial data admit a globally smooth UNFORCED Navier--Stokes solution v_epsilon (standard global small-data theory). The exact correction w=v_epsilon-u_B obeys delta_K>=b_K-epsilon>kappa b_K if 0<epsilon<(1-kappa)b_K. Thus nonzero initial data alone never forces a uniform shell-retention fraction.
3. **Retention alone is not singularity persistence.** A globally smooth exactly unforced periodic heat shear can retain half of a forced ramp shear's Fourier shell at t*=1/2. This is an exact counterexample to the logical step from one-time retained shell energy to eventual blowup.
4. **Actual sufficient singularity-retention target.** Along x_tau=(sqrt(2 X_in tau),0,0), the source has u_{B,theta}=tau^(-1/2-h)(e0+O(tau^(2h))). If a zero-force corrector has |w_theta(x_tau,1-tau)|<=e0 tau^(-1/2-h)/4 for all sufficiently small tau, the completed velocity must blow up. NO corrected zero-force field satisfying this inequality is presently constructed.

## Tests and artifacts
- 15,000 exact rational conditional shell certificates passed; real source input refused.
- 25,000 exact rational non-retention margins passed; globally smooth periodic shear checked symbolically.
- A two-page research PDF and complete ZIP with verified SHA-256 manifest were created in this session.
- Finite Lean scalar lemmas and a path-scoped CI workflow are committed; no kernel success is claimed until GitHub reports it. None of these Lean scalars proves the PDE theorem.

## Remaining unclosed conditions
Full source profile and all cutoffs with actual numeric validation; interval-certified m,G,R,V at a named source time; entire Section 10 projected residual; a specific smooth nonzero initial condition; an unforced correction preserving pointwise growth along x_tau; all-harmonic convergence, pressure and boundary conditions; complete kernel-checked Lean PDE proof.

**Release status: HOLD_SOURCE_NUMERIC_PROFILE_AND_SINGULARITY_RETENTION_UNPROVED.** This programme has not proved the unforced 3D Navier--Stokes blowup theorem.