# Edition XXXVIII: sustained torque scaling and packet smoothness obstruction
24 October 2026 — Tony Newton, Newton Astro Labs.

## Real mathematical results
1. **Exact compensated angular-momentum transport.** For the Edition XXXVII global smooth, unforced nonaxisymmetric Gaussian datum, the initial radial angular-momentum covariance J(r,z)=eps²r³exp(-2(r²+z²)) implies T=-r^-1 d_r(rJ)=4eps²r²(r²-1) exp(-2(r²+z²)). For every cylinder radius R, integral_0^R T(r,z)rdr=-eps²R⁴ exp(-2(R²+z²)); the total radial integral is exactly zero. For well-decaying exact unforced flow, total Lz is conserved. Negative core torque is compensated by positive exterior torque. The creation in Edition XXXVII is local mean angular momentum, not global net angular momentum.
2. **Parabolic-scale illusion.** Every rescaled u_lambda(x,t)=lambda u(lambda x,lambda²t) is global smooth exact zero-force NS. Gamma_lambda(x,t)=Gamma(lambda x,lambda²t), T_lambda=lambda²T(lambda x,lambda²t). At initial sample r=1/(2lambda),z=0, T_lambda=-3eps²lambda² exp(-1/2)/4. Its critical Fourier X^-1 norm is invariant and L2 kinetic energy falls like lambda^-1. Arbitrarily large torque in a family of smooth solutions is not terminal blowup of any single solution.
3. **A direct multiscale stack smoothness obstruction.** Choose a compact smooth divergence-free cutoff phi of the same vortex, plateau around sample (r,z)=(1/2,0); centers c_n=(0,0,4^-n), scales lambda_n=16^n, and U_n=a_n lambda_n phi(lambda_n(x-c_n)). Supports are pairwise disjoint and accumulate at zero. The sum extends C-infinity across zero **iff** a_n lambda_n^(k+1) -> 0 for every integer k>=0. At the nth sample its exact initial torque is -3 a_n² lambda_n²exp(-1/2)/4 = o(lambda_n^-2). Fixed-amplitude or fixed-algebraic-amplitude stacked copies cannot serve as smooth initial data for this direct construction.
4. **Smooth-axis Taylor parity.** For a smooth Cartesian velocity with uniform C4 bounds near the z axis, the radial mean covariance J=O(r³), the axial covariance H=O(r²), and the mean Reynolds torque T=O(r²). Constants may diverge as an actual singular time approaches.

## Independent double checks
- Exact SymPy Gaussian covariance, signed interior/exterior radial balance, full cancellation, parabolic scaling, arbitrary quadratic planar-jet angular covariance order three.
- 20,000 exact-rational scale-energy tests.
- Independently authored packet disjointness/smooth-jet verifier, 20,000 exact-rational tests. A minor algebraic test typo was corrected before final verification.
- Standalone three-page LaTeX/PDF compiled twice, rendered and visually inspected. SHA256 verified release ZIP includes PDF/TEX, both exact Python verifiers, the source ledger and reproducibility instructions.
- Finite Lean scalar identities committed with isolated no-sorry workflow. It does not formalize conservation or the unforced PDE; kernel success requires a completed GitHub CI run.

## Source and research gates
The published OpenAI Navier--Stokes result allows smooth **external forcing**; its unforced blowup result is for Euler: https://github.com/openai/NavierStokesAndEuler .
The actual Section 10 source numerical parameters/cutoffs and projected-force residual remain unfrozen.
The source-specific terminal theta swirl is proportional to tau^(-1/2-h), requiring torque/oscillation growth at least order tau^-h in our prior necessary dichotomy.
The present exact unforced solutions are globally regular. No smooth-data unforced NS singularity, source-matched correction, terminal Reynolds-torque cascade or complete Lean PDE proof has been obtained. **FAIL CLOSED.**

## Next decisive analytic step
Replace instant-time scale amplification by a **single-flow space-time dyadic energy/torque transfer mechanism**, quantitative enough to prove a lower bound for the angular momentum transport across a shrinking cylinder under the exact unforced equation while retaining source-compatible pointwise swirl. An exact transport identity is necessary; a positive nonlinear cascade with all viscosity, pressure and frequency leakage estimates remains unproved.
