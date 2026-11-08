# Attack 36 — a triangular mixed strong-velocity / weak-pressure G1 ledger

8 November 2026. **Conditional functional-analytic result; the actual local terminal-core G1 theorem and global unforced 3D Navier–Stokes problem remain OPEN.**

The formal source is the exact implicit-q hierarchy transcribed in \`Exact_Local_Unforced_Terminal_Core_Dynamics_JFM_FINAL.tex\`: physical q satisfies tau=q(1−eta²), z=q^(1/2−h) eta, X=r²/(2q). The source coefficient equations for phi_n,U_n,V_n,Pi_n and Omega_{n−1} are not replaced by a surrogate.

## Exact strong–weak pair

Use inherited doubled analytic weights
w_(a,beta)=R^(−a) varrho^(−beta)(2a+beta)!/[(2a)!(a+1)²(beta+1)²]
and weak pressure weights b_(a,beta)=w_(a,beta+1), with radial ideals I_n of order at least n.

The weight ratio w_(a,beta)/b_(a,beta)=varrho(beta+2)²/[(beta+1)²(2a+beta+1)] proves:
- ||partial_eta F||_(B−) <= ||F||_B exactly;
- ||D_X F||_(B−) <= 4 varrho ||F||_B;
- ||F||_(B−) <= 4 varrho ||F||_B;
- and n F is strong→weak uniformly when F has valuation >=n−1.

A strong analytic multiplier times a weak pressure field is weak, with the same positive convolution-algebra constant: the order-beta weak Leibniz terms form a subset of the strong order-(beta+1) Leibniz terms.

For nu=1,2, the regular-singular inverse J_nu on input degree a has multiplier 1/[(a+1)(a+nu)] and adds one radial degree. The inequalities
w_(a,beta+1)/[(a+1)w_(a+1,beta)] <= 8R/varrho and
w_(a,beta+2)/[(a+1)²w_(a+1,beta)] <= 16R/varrho²
give J_nu : I_m(B−) -> I_(m+1)(B) with O((m+1)^−1), and the **complete** J1 Z_(−2A,n) : I_(n−1)(B−) -> I_n(B) uniformly for n<=a+1.

## Exact nonlinear transport divergence form

The **true incompressibility** identity V_(i,X)=−Z_(−A,i)U_i implies, for every positive pair i,j and H_j=phi_j or U_j,
V_i H_(j,X) = partial_X(V_i H_j) + (Z_(−A,i)U_i) H_j.

Here V_i is strong with one radial lift, J_nu partial_X is bounded on its strong product with H_j, and ZU_i is weak so its product with H_j is weak before J_nu returns to strong. No naked unbounded radial derivative is assumed bounded. Similarly V_i H_j/X uses (V_i/X) in B− and H_j in B, while J_nu(U_i Z_(c,j)H_j) uses B×B− ->B− and J_nu smoothing. J_nu Z^[2]_(c,n−1) H_(n−1) is handled by the previously established two-derivative regular-singular estimate.

## Exact complete weak pressure ledger

For E_n=||phi_n||_(I_n(B))+||U_n||_(I_n(B)), the source-normalized Pi_n contains:
- the order-n pressure products C^(−2)int_0^X sum_(i+j=n) phi_i phi_j, with current i=0/j=0 treated by the current block;
- temporal, index-zero endpoint and viscous primitives from the exact Omega_(n−1) source;
- the twice-shifted source +(1/2)Z^[2]_(0,n−2) C_X V_(n−2);
- positive-index quadratic −(1/4X)sum_(i+j=n−1) V_i V_j −(1/2)C_X sum_(i+j=n−1) U_i Z_(0,j)V_j.

The useful pressure pairs are:
||V_i||_(I_(i+1)(B))<=C||U_i||_(I_i(B)),
||V_i/X||_(I_i(B−))<=C||U_i||_(I_i(B)),
||Z_(0,j)V_j||_(B−)<=C||U_j||_B.
Thus the complete positive-index quadratic terms are weak-bounded by the mixed product and C_X radial primitive; the dangerous bare XV_XX is NEVER separately bounded because its exact pressure primitive is V_X=−Z U.

**Conditional pressure proposition:** under fixed common analytic multiplier membership and the separately derived source-native double-shift weak-pressure estimate,
||Pi_n||_(I_(n−1)(B−)) <= C [E_n+E_(n−1)+E_(n−2)+Σ_(i+j=n, positive)E_iE_j+Σ_(i+j=n−1, positive)E_iE_j].
The constant is uniform in n. The true pressure remains weaker than velocity; no invalid strong-pressure bound is assumed.

## Conditional complete G1 majorant and reconstruction

Assume (a) the authentic leading profiles and their finitely many derivatives share one B domain; (b) the original finite-order coefficient hierarchy admits axis-regular analytic startup solutions for all n<N in this domain; (c) the complete exact four-block current operator has ||K_n||<=C_K/(n+1); (d) the full twice-shifted weak-pressure coefficient estimate holds for those actual leading multipliers. Then K_n is invertible for large n and the full *velocity* sequence satisfies the two-convolution recurrence
E_n <= p_n+a(E_(n−1)+E_(n−2))+c Σ_(i+j=n,pos)E_iE_j+d Σ_(i+j=n−1,pos)E_iE_j.
The analytic majorant Y=P+a(z+z²)Y+(c+dz)Y² gives E_n<=C B^n. The complete weak pressure ledger then gives ||Pi_n||_(B−)<=C' (B')^n. Strict radial subcore shrink and polynomial n/degree growth of a fixed number of physical derivatives give termwise reconstruction on compact t<T and sufficiently small q with the **true** implicit-q chain rules. This is CONDITIONAL: no authentic finite startup domain or all-source kernel certificate was released.

## Independently verified startup jet

From the original n=1 equations, using the axis operator 𝒵_c f=(2c eta f + (1−eta²)f')/(1−2h eta²), and source axis trace U0(0,eta)=4eta+j0:
- U1_X(0,0)=(1/2+h)j0 exactly.
- If phi0(0,eta)=f0+f1 eta+(f2/2)eta²+..., then phi1_X(0,0)=(1+h)f0/2−f2/4.
- If U0(X,eta)=4eta+j0+u1(eta)X+..., Pi1_X(0,0)=−2−(1/2+h)j0²−u1'(0).
These are source-specific necessary **first radial jets**, not validation of all startup profiles.

Independent local replay passed: startup identities in SymPy, 9 nonconstant exact transport identities, 450 exact rational strong/weak and J1 Z weights, 2,178 mixed strong×weak Leibniz bounds, and 24 corrected-majorant coefficients.

A 4-page scholarly PDF/LaTeX supplement and 209-page cumulative research edition preserving the previous 205 extracted-text page streams were created and visually inspected in the chat; a SHA-256 verified proof packet contains the editable files and checker.

**Remaining release-critical work:** source-fixed numerical/analytic profile constants and common domain; actual full finite startup including pressure; independent verification of exact K_n and twice-shifted pressure maps for those profiles; an exact physical cylindrical/Cartesian differentiated residual replay with one pressure gauge; then global periodic H8 weighted seven-ray stress and nonlinear correction. None of these or a global unforced finite-time blowup is certified by the abstract theorem. Keep PR draft.
