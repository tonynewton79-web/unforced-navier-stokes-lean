# Edition XXVIII — exact sharp universal source-dependent H8 ray inverse

**24 October 2026. Exact rational finite-dimensional/annular theorem established. Unforced 3D Navier–Stokes and complete Lean proof OPEN.**

## Core advance relative to Edition XXVII

Edition XXVII fixed the splitting parameter h across every signed stress Q and obtained radial pressure-equivalent carrier b=(85/8)mu+(471/4)M and entrywise stress <=122M+11mu.

Edition XXVIII permits a *smooth stress-dependent choice* of the seven-ray coefficient kernel and a position-dependent isotropic scalar pressure gauge, while keeping one fixed radial-only pressure-neutral carrier. For symmetric co-rotating annular Q with all independent entries |Qij|<=M and a radial cutoff chi=1 on a neighborhood of supp Q, the rigorous sharp universal result is

[
b=rac{85}{8}mu+rac{343}{4}M,quad
S=sum_{j=1}^7 d_j v_jotimes v_j
  =Q+a(r,z)I+bchi(r)e_rotimes e_r,quad
d_jgemuchi.
]

The isotropic a(r,z) is allowed to vary with Q because div(a I)=grad a, while the radial carrier also has exact gradient divergence. Consequently P div S=P div Q on R²×S¹_z or an embedded annular disk of T³. The entrywise stress size improves further:

[
|S|_{infty,	ext{entry}}le90M+11mu.
]

The M-slope improvement is from 471/4=117.75 to 343/4=85.75 (about 27.2%). The exact universal bound is sharp for the full signed symmetric-entry box, not necessarily for the smaller PSD/Reynolds class.

## Frozen finite certificate and constructive smooth selection

The frozen table XXVIII_64_CORNER_EXACT_CERTIFICATES.txt provides 64 rational solutions, one for each sign vertex of Q's six components, all with a common carrier 343/4 and nonnegative seven ray weights. The verifier tests all 384 component equalities, all 448 coefficient nonnegativities, and a further 750 independent exact Fraction interpolated/collar cases.

Define W_s(q/M)=2^-6 product_i(1+s_i q_i/M). The smooth global choice for M>0 is

[
a=chi[3mu/8 +Msum_sW_s a_s],quad
d_j=chi[mu (1,1,3,2,2,1,1)_j+Msum_sW_s d_{s,j}].
]

Because Q=0 on the cutoff collar and chi=1 wherever Q is nonzero, these polynomial choices are globally smooth and reproduce Q exactly. For M=0 use the source-free coefficient vector.

The independent sharp dual L(H)=-Hrr-15 Htheta-theta+16 Hzz-(31/4)Hrtheta-46 Htheta-z evaluates on the seven rays as (-1,-31/8,0,0,0,-23/4,0). Since L(I)=0 and L(er er)=-1, the positive ray floor forces b>=L(Q)+85mu/8. At stress sign corner (-M,-M,+M,-M,-M,-M), L(Q)=343M/4, matching the construction.

## Independent second-pass derivative audit

An exact 48-edge table check supplies full componentwise Lipschitz factors for the isotropic gauge and ray coefficients. In terms of any scalar spatial or time derivative D and G_D=max_i|D Q_i|, for fixed mu,M,

[
|D a|le(11/4)G_D+(3mu/8+13M/4)|Dchi|,
]
[
max_j|Dd_j|le(225/4)G_D+(3mu+99M/2)|Dchi|.
]

This is only the derivative of co-rotating *scalar coefficients*. Cartesian derivative bounds must additionally include differentiation of the cylindrical frame and rays. Time-dependent source normalization should freeze mu and M over its slab before using the estimate. The source derivative cost can be much larger than the pointwise 90M+11mu norm.

## Verification and rigorous boundaries

- Exact-rational 64/64 corner certificates: pass.
- Exact 750/750 multilinear interpolation/collar cases: pass.
- Independent signed dual and optimal worst corner: pass.
- Exact 48 edge derivative constants: pass.
- Finite Lean scalar dual theorems committed. GitHub Actions may remain queued and are NOT called kernel verified.
- The true physical source profile, A.11/A.19 parameters, pressure and collar derivatives, H8 q^(1/2) source budget, compact R³ virtual work, and all nonlinear harmonics remain unverified.
- The repository's FULL_UNFORCED_SOURCE_CERTIFICATE_REQUIRED_20261022.json remains FAIL_CLOSED_MISSING_SOURCE_DATA. Exact physical zero-force residual, blowup persistence, and end-to-end Lean PDE theorem remain OPEN.
- The openai/NavierStokesAndEuler upstream proves Navier–Stokes breakdown **with** forcing and separately **unforced Euler**; the formalized Navier–Stokes theorem is not unforced.

**Next decisive scientific target:** obtain an actual source-backed stress Q and upper bounds for its size and derivatives over every source interval, then test the 90M+11mu stress bound *and* 225/4 source derivative cost against the real H8 seven-ray cone and other PDE control norms. Abstract pressure-quotient algebra does not remove the physical residual.