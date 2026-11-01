# H8 hosted Lean gate audit — 1 November 2026

The five-field unforced existence target remains **OPEN**. This note describes exactly what the connected GitHub Actions build errors show, and records a mathematically checked source repair. Syntax, tactic, and theorem-domain errors are kept distinct.

## Latest observed PR #5 workflow outcomes before patch

At head `0b379cba74c91aed2dbc5f34f06672bdac001125`, six workflow runs reported success, three failure, and the abstract Lean closure run was in progress. The successful nonaxisymmetric Fourier run confirms the earlier nested-comment parser fix.

The three failing jobs and their first actionable diagnostics were:

- Physical Lean: `UnforcedPatching/JointFluxCone.lean:43-44`, `abs_le.mpr` expected `-bound <= B`, but the supplied hypothesis was `-B <= bound`. These are equivalent inequalities but not definitionally identical. The repair uses `by linarith [hBlo]` and `by linarith [hXlo]` explicitly before applying `abs_le.mpr`. No cone coefficient or theorem statement was changed.
- Seven-ray scalar cone: `TerminalCore2026/N1SevenRayConeScalar.lean:17-18`, Real-valued definitions with division required `noncomputable def`. This is a Lean execution/declaration issue, not a rational identity change.
- Scalar cone theorem `xxv_zz`: under its original *unrestricted* four real variables, the claimed equality was false. Exact SymPy expansion of left minus right is `2*(s^2+c^2-1)`. The revised theorem explicitly requires `hsc : s^2+c^2=1`; at `s=c=0` the old conclusion fails by `-2`.
- Scalar cone theorem `xxv_ray_floor_gap`: the original unrestricted floor `mu` was invalid. With all seven `d_i=mu`, the right-hand side is `(27/4)*mu` while the claimed bound was `(105/16)*mu`. Their difference is `(3/16)*mu`, requiring `mu>=0`. At `mu=-1` the theorem is false. The revised declaration adds `hmu : 0 <= mu`, preserving the target numerical constant.
- Local terminal-core Lean: `TerminalCore2026/A11ConeMargin.lean:31`, `field_simp` had already discharged the goal, so the following unconditional `ring` failed with “No goals to be solved.” Changed to `field_simp <;> ring`.

## Independent verification

The companion local SymPy script reproduces seven exact tensor-component identities. Six vanish identically for unrestricted real inputs. The seventh reduces to `2*(s^2+c^2-1)`, so it vanishes precisely on the physically intended unit circle. It also verifies the sharp seven-ray floor value at the equal-floor vertex and exhibits an exact negative-floor counterexample.

The fixes were committed directly to PR #5 on the source branch. They are **not described as hosted kernel-passing** until fresh GitHub Action runs actually complete. No new PDE solution, positive compact stress inverse, full periodic pressure, or retained five-field construction has been produced.

## Remaining mathematical gate

An authenticated source must give the same complete four-patch `U,H,rho,E` and nonlinear retained correction `w`, including the signed axial fourfold channel, all twelve C4 overlaps, true periodic Poisson pressure, positive stress and exact zero residual on the full time interval. A collection of individually correct algebraic source gates is not this construction.
