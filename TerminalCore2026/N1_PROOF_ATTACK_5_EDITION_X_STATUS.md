# Proof Attack 5 / Edition X: coupled first-order meridional-swirl equations

**Scope:** linearized cylindrical axisymmetric incompressible NS around a pure-swirl leading field U0 e_theta. The exact leading background residual R0 is displayed rather than presumed to vanish.

- Exact difference equations: radial forcing (2U0 W+W^2)/r, axial momentum and angular convection coupling, with full nonlinear perturbation convection retained.
- If R0 vanishes at the relevant order, linear meridional angular vorticity satisfies (d_t - nu Ltheta) omega_theta = (2/r) d_z(U0 W).
- Pressure Poisson: L pi = (2/r) d_r(U0 W). Meridional streamfunction gives omega_theta = -(psi_rr-psi_r/r+psi_zz)/r.
- Under homogeneous linearized equations and valid decay/periodic/no-flux conditions, E' + nu D = int W[Vr(U0/r-U0_r)-Vz U0_z] dx <= M(t) E. Hence zero initial perturbation is unique. This does NOT exclude an inhomogeneous correction needed to cancel an existing source residual.
- Independent SymPy exact source-independent verification passes divergence, curl/viscous commutator, pressure-Poisson, streamfunction, energy algebra, and a manufactured smooth Gaussian with nonzero (U0 W)_z on z=0. 10,000 exact rational checks of Young's inequality passed.
- New Lean source N1CoupledVorticityScalar.lean proves only finite scalar implications if CI succeeds. Neither Lean nor Lake is installed in the current local container, so no local Lean kernel compilation was performed. Do not mark kernel pass on a queued GitHub Action.
- The mathematical identities are classical local linearization/energy consequences, not a solution to unforced Navier--Stokes finite-time blowup.

**HOLD:** true source-specific order-one annular corrector and leading residual R0; inhomogeneous matched Oseen/Stokes solve; pressure/matching/axis conditions; complete nonlinear correction, nonzero initial datum, convergent higher-order hierarchy, full physical zero-force PDE, end-to-end formalized theorem.

**Files:** N1_Coupled_Vorticity_Edition_X_20261022_Insert.tex; N1CoupledVorticityScalar.lean; verify_n1_coupled_vorticity.py; generated Edition X cumulative proof addendum PDF and reproducibility ZIP.

**Next attack:** physical annulus source extraction, explicit boundary/data compatibility and invertibility/energy estimates for the inhomogeneous first-order coupled operator.