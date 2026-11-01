# Physical moving-frame connection: checked Lean scope

27 October 2026. The source modules are
`UnforcedPatching/FrameConnectionDerivative.lean` and its smoke test.
They use the `FrameMatrix` representation of `RotatingFrameDual`,
interpreted as genuine 3-by-3 matrix multiplication.

For scalar-coordinate differentiable matrix functions `E(t),H(t)`,
the derivative at each physical tensor entry is **derived** by the
finite-sum product rule, not postulated:

`(E H Eᵀ)' = E' H Eᵀ + E H' Eᵀ + E H (E')ᵀ`.

If `E Eᵀ=I` at the evaluation point and its derivative obeys
`(E')ᵀ E+Eᵀ E'=0`, with `Ω=Eᵀ E'`, Lean checks both `Ωᵀ=-Ω`
and `E'=EΩ`, hence

`(E H Eᵀ)' = E (H'+ΩH-HΩ) Eᵀ`.

The differentiated orthogonality relation is explicitly supplied,
not silently deduced from a merely pointwise orthogonality equation;
it is the correct analytic consequence when E is orthogonal on a
neighbourhood and differentiable there. The Lean proof does not yet
formalise that neighbourhood-to-tangent differentiability lemma.

Two independent exact examples establish a nonzero connection for
`H=diag(1,2,0)`. With planar rotation generator
`Ω=[[0,-1,0],[1,0,0],[0,0,0]]`, the `(0,1)` commutator entry is
`-1`, not zero. Direct differentiation of the actual trigonometric
frame `E(t)=diag(R(t),1)` proves the same physical tensor entry has
`HasDerivAt` derivative `-1` at `t=0`.

This theorem removes the *abstract frame differentiation* gap.
It does **not** authenticate the original H8 frame E(r,theta,z),
the Case 006 core and shaper profiles, their pressure representative,
source-to-shear identity, spatial/temporal weighted cone, axial
integration, derivative interchange, global compact support,
or an unforced Navier--Stokes singularity. All these obligations
remain independent gates.

## Terminal Core relationship

The uploaded 22 October Terminal Core continuity handoff concerns a
different Appendix A.11 source-corrected terminal-core construction.
It explicitly records missing same-profile moment roots, eta jets,
pressure/terminal gauges and whole-patch stress certificates.
Those conditional bounds cannot be substituted for the Case 006 H8
frame, core/shaper cutoff or its source-to-shear data. They are useful
as a model of fail-closed source authentication and interval proof
receipts, but are not an additional hypothesis-free source match.
