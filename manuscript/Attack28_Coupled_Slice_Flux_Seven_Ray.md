# Attack 28 — nonlinear slice flux coupled to the one-sided seven-ray stress margin

**Scope:** exact source-specific necessary identities plus an independent nonsingular polynomial control. These are NOT a full weighted stress inverse or a 3D unforced Navier–Stokes singularity theorem. This branch extends Attack 25 without altering the earlier papers.

## General carrier source identity

Work in a compact injective cylindrical torus chart with a smooth solenoidal carrier U and its physical residual F = U_t − νΔU + (U·∇)U + ∇P. Define L(z,t)=∫r² U_θ dr dθ, J(z,t)=∫r² U_z U_θ dr dθ. Exact cylindrical angular momentum conservation gives m(z,t)=∫r²F_θ dr dθ = L_t−νL_zz+J_z.

If a compact symmetric stress S = S_* + E H Eᵀ matches P div(S)=P F, E=(e_r,e_θ,e_z), with H_{23}=B and the **one-sided** cone bound |B| ≤ γρ/8, γ=15971/122900, then

|∂_t ∫_{−∞}^z L(s,t) ds − νL_z(z,t) + J(z,t) − T_*(z,t)| ≤ γ M_ρ(z,t)/8,

T_*=∫r²(S_*)_{zθ} dr dθ, M_ρ=∫r²ρ dr dθ.

This is necessary, not sufficient. The cylindrical-frame qualification is essential; a different local frame requires the rotated coefficient.

## Affine gauge and positive integrating factor

For a genuine implicit-q local core with potential A_θ e_θ + A_z e_z, choose χ=χ₀+εχ₄cos4θ (χ₄=O(r⁴)), U=curl(χ(A_c+c(z,t)e_z)). Let u_j = r⁻¹ ∂_r(rχ_jA_θ), v_j = −∂_r[χ_j(A_z+c)], j∈{0,4}. Then

L=2π∫r²v₀ dr, J=2π∫r²u₀v₀ dr+πε²∫r²u₄v₄ dr.

There is NO term linear in ε in the slice-averaged nonlinear flux for this fixed cutoff and axisymmetric scalar gauge.

With L=L₀+Wc, J=J₀+Qc, W=4π∫rχ₀ dr, Q=−2π∫r²(u₀χ₀,r+ε²u₄χ₄,r/2)dr, set c₀=−L₀/W, Y=W(c−c₀), b=Q/W where W>0 and b remains bounded. Define μ(z,t)=exp(−ν⁻¹∫_a^z b(s,t)ds)>0. The joint necessary inequality becomes

|∫_a^b μ(z,t)[J(c₀)(z,t)+∂_t∫_a^z Y(s,t)ds−T_*(z,t)] dz| ≤ (γ/8)∫_a^b μM_ρ dz.

Consequently an undersized cone forces a quantitative temporal angular-momentum modulation; allowing c(t,z) does not automatically repair the deficit.

## Exact stationary C² polynomial control — NOT the authentic terminal core

u_c=ω r e_θ+V e_z, p_c=ω²r²/2, A_θ=Vr/2, A_z=−ωr²/2, with Vω≠0.
Let f(r)=(1−r²)³ on 0≤r<1, g(z)=(1−z²)³ on |z|<1 (zero outside), χ₀=fg, χ₄=r⁴fg.

For c₀=ω/10, exact integration gives
- L(c₀)=0, W=πg/2;
- J(c₀)=2πVω g²/175·(1+5ε²/264);
- b=−2Vg(1/35+ε²/924).

The flux is strictly one-signed in the interior for all real ε and Vω≠0, so the compact stationary zero-slice-torque equation νY'−bY=J(c₀) has NO solution with Y(−1)=Y(1)=0, by integrating factor μ>0. For a nonnegative cutoff restrict |ε|≤1; the polynomial identities themselves hold for all real ε.

If T_*=0, ρ_λ=λψ(r)g² and I_ψ=∫r²ψ dr>0, the same integrating-factor identity plus the cone bound imply, **for every stationary compact scalar gauge**:

λ ≥ [8|Vω|/(175 γ I_ψ)](1+5ε²/264).

With the C² diagnostic ψ=f, I_f=16/315, so λ ≥ (110610/15971)|Vω|(1+5ε²/264) ≈ 6.925677791 |Vω|(1+5ε²/264). This is sharp only for the 1D toroidal projection: c=c₀ attains the flux budget. Full tensor source matching and axis regularity are not established by this saturation. Smooth flat annular ψ yields a smooth toroidal tensor component, but other physical source components remain uncontrolled.

## Authentic-core scaling requirement

Under a genuinely verified bounded normalized inner profile with A=1/2+h, D=1/2−h, radial length q^{1/2}, axial length q^D, U~q^{−A}, and stress envelope ρ~q^{−1−h}, the natural fluxes J and ∂_t∫L scale q^{1/2−2h}; available toroidal stress flux scales q^{1/2−h}, and viscous integrated term scales q^{1/2}. The leading nonlinear/temporal flux must cancel by **relative q^h**, conditional on these stated profile bounds and an appropriately sized baseline T_*.

No actual frozen local profile, flat cutoff, baseline and stress envelope have been authenticated as one data tuple, so this criterion is not yet applied to the genuine singular core. The exact Fourier mode calculations and the fourfold solenoidal detector remain separate necessary gates.

**Verification:** standalone exact SymPy replay and independent Gauss–Legendre/Fourier quadrature, packaged with the 177-page cumulative PDF and a five-page supplementary paper in the conversation artifact. The new source-level equations, their algebraic checks and the user's previous 16-, 65-, 167- and 188-page manuscripts are the evidentiary basis. General angular momentum conservation and 1D integrating factors are established prior art, not claimed as new methods.
