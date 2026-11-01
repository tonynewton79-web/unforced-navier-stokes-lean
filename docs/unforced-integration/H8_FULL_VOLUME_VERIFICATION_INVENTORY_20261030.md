# Full H8 cumulative volume: GitHub source and independent verification record

**Date:** 2026-10-30. **Scoped GitHub branch:** `feature/case006-source-band-lean-20261027`. **Earlier checked head:** `ced3b7058e3ad9eac03da6c97f44fdebb8560d69` (later catalogue edits do not alter the recorded audit). **Full unforced existence target:** OPEN.

The full **129-page cumulative research PDF** preserves the existing 115-page master and adds 14 pages, Appendices AE–AI: logarithmic retention, affine-source periodic pressure, the GitHub module catalogue, **Reproducible finite-arithmetic verification** with the complete independent Python source, and the exact unforced correction equation. This cumulative PDF and editable appendix LaTeX are delivered as conversation files; GitHub provides the underlying editable research master and the verification ledgers.

## Crucial independent reviewer point: the formula was already correct in LaTeX

The 11-page journal-style LaTeX source has `\sum_{n\ge0}\frac{\tau_n^{1/2-h}}{\delta_{\tau_n}^{2}}<\infty` in its equation (1.8), and the same denominator in the proof immediately before `This proves (1.8)`. It is algebraically equivalent to multiplying by `\delta_{\tau_n}^{-2}`; this **is not the incorrect positive power**. `\sqrt{\log(1/\tau)}` is explicitly present in the LaTeX source; the displayed `p` noted by a reviewer came from plain-text PDF extraction. The expanded 129-page edition prints both equivalent forms and the correct logarithmic contradiction.

The user-uploaded independent checker `verify_h8_independent.py` was executed without modification and gave **17 PASS assertions**: exact rational minimum margin, exact enumeration of 8 4D cone vertices and 6 projected (A,C) hull vertices, sharp meridional cap, scale exponents, dyadic energy constant, correction Fourier polarization, constant-one Riesz/Frobenius multiplier inequality, and explicit divergence of the correct borderline sum versus convergence of the wrong product. On the corrected series its partial sums at N=1e3,1e5,1e7 were ~9.9938,16.6363,23.2802. The local AF/JAMS pytest suites added another **26 passing tests**. These are **finite checks**, not a certificate of PDE existence.

## Audited Lean theorem source modules (18)

### Exact seven-ray centre and coefficient cone

- `UnforcedPatching/SevenRayCenter.lean`
- `UnforcedPatching/ConeBudget.lean`
- `UnforcedPatching/ConeOperator.lean`
- `UnforcedPatching/FourFieldPhysical.lean`
- `UnforcedPatching/ExactCoefficientCone.lean`
- `UnforcedPatching/SharpCoefficientDual.lean`
- `UnforcedPatching/PositiveCoefficientCone.lean`
- `UnforcedPatching/AxialFluxCone.lean`
- `UnforcedPatching/JointFluxCone.lean`

### Moving frame and physical coordinate operators

- `UnforcedPatching/RotatingFrameDual.lean`
- `UnforcedPatching/FrameConnectionDerivative.lean`
- `UnforcedPatching/CartesianAxialBridge.lean`
- `UnforcedPatching/NonaxisymmetricAxialBridge.lean`
- `UnforcedPatching/PhysicalCircleAngular.lean`
- `UnforcedPatching/AngularMean.lean`

### Pressure and source compatibility

- `UnforcedPatching/MeridionalInverse.lean`
- `UnforcedPatching/PressureCompensatedFlux.lean`
- `UnforcedPatching/Case006SourceBand.lean`

These modules contain the exact rational centre, sharp factor 14, absolute vs one-sided support bounds, source-frame tensor map, joint axial--azimuthal cone, rotating-frame derivative connection, cylindrical/Cartesian bridges, angular means, and source-pressure boundary primitives. **Source present does not imply hosted compile PASS.** The repository README separately records a historical pinned GitHub run #12 (ID `35779131542`) for the abstract `UnforcedClosure.lean`; it is not physical H8 closure. At our latest check, all new PR #5 hosted jobs were **queued**. Check `#print axioms` for any future claim of kernel certification of a particular branch.

## Regression modules visible in the connected PR (34)

- `tests/test_h8_anisotropic_interface_20261029.py`
- `tests/test_h8_anisotropic_pressure_limit_20261030.py`
- `tests/test_h8_axial_flux_cone_cap.py`
- `tests/test_h8_axisymmetric_pressure_mode_20261030.py`
- `tests/test_h8_c4_signed_pressure_20261030.py`
- `tests/test_h8_complementary_strain_nogo_20261029.py`
- `tests/test_h8_correction_halo_nogo_20261030.py`
- `tests/test_h8_cylindrical_full_source.py`
- `tests/test_h8_dynamic_two_mode_gate_20261029.py`
- `tests/test_h8_energy_dissipation_retention_20261030.py`
- `tests/test_h8_equatorial_swirl_obstruction_20261029.py`
- `tests/test_h8_final_physical_pde_20261029.py`
- `tests/test_h8_fourth_multipole_20261030.py`
- `tests/test_h8_global_energy_gate_20261029.py`
- `tests/test_h8_joint_cone.py`
- `tests/test_h8_local_energy_influx_20261029.py`
- `tests/test_h8_logarithmic_dyadic_retention_20261030.py`
- `tests/test_h8_physical_rayleigh_gate_20261029.py`
- `tests/test_h8_physical_rayleigh_returnflow_20261029.py`
- `tests/test_h8_quadratic_stress_concentration_20261030.py`
- `tests/test_h8_return_flow_spectral_20261029.py`
- `tests/test_h8_signed_poisson_fft_20261030.py`
- `tests/test_h8_signed_poisson_pressure_20261029.py`
- `tests/test_h8_signed_pressure_coefficient_20261030.py`
- `tests/test_h8_source_gauge_projection_20261029.py`
- `tests/test_h8_split_cutoff_gate.py`
- `tests/test_h8_torque_flux_gate.py`
- `tests/test_h8_translation_energy_20261029.py`
- `tests/test_h8_translation_projection_20261029.py`
- `tests/test_h8_two_mode_physical_chart_20261029.py`
- `tests/test_h8_two_mode_projection_20261029.py`
- `tests/test_h8_vacuum_curl_gate.py`
- `tests/test_h8_weighted_terminal_matching_20261029.py`
- `tests/test_h8_affine_pressure_mismatch_20261030.py`

## Exact full correction and open gates

For smooth divergence-free U and w, let B(f,g)=P[(f·∇)g], G=U_t-ΔU+B(U,U), L_Uw=Δw-B(U,w)-B(w,U). An exact **unforced** solution requires G+w_t-L_Uw+B(w,w)=0 for every space-time point and the actual periodic pressure -Δπ=∂i∂j[(U_i+w_i)(U_j+w_j)]. Positive seven-ray engineering stress H is not automatically the velocity quadratic stress U⊗w+w⊗U+w⊗w.

**G0 OPEN; G1–G3 PAPER_CONDITIONAL; G4–G8 OPEN.** The authenticated physical (U,w,H,ρ,E) tuple, full four-patch overlap, mixed/exterior periodic pressure and signed remaining flux, compact positive one-sided stress inverse, nonlinear zero-residual solution, and terminal pointwise blow-up are not established. The historical 115-page work and the new appendices are validly scoped partial results; they do not establish a breakthrough on unforced Navier–Stokes regularity.
