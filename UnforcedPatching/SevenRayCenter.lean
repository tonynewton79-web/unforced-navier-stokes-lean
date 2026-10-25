import UnforcedPatching.ConeBudget

/-!
# Exact quarter-aperture seven-ray covariance

Independent rational verification of the explicit centre in the
carrier-independent H8 source. This is coordinate algebra in the frozen
orthonormal frame `(e₁,e₂,e₃)` and does not establish compact H8 attachment.
No square roots or approximate eigensolvers enter the certificate.
-/

namespace UnforcedPatching

/-- Coordinates of the seven rays at aperture `t = 1/4`, in source order.
Indices `0,...,6` represent the source's rays `1,...,7`. -/
def quarterRay (i : Fin 7) (a : Fin 3) : ℚ :=
  if a.val = 0 then 1
  else if a.val = 1 then
    match i.val with
    | 1 => 1 / 4
    | 2 => -1 / 4
    | 5 => 1 / 4
    | 6 => 1 / 4
    | _ => 0
  else
    match i.val with
    | 3 => 1 / 4
    | 4 => -1 / 4
    | 5 => 1 / 4
    | 6 => -1 / 4
    | _ => 0

/-- Raw positive coefficients `(1,1,59/43,1,1,1,1)` from the source. -/
def quarterRawWeight (i : Fin 7) : ℚ :=
  if i.val = 2 then 59 / 43 else 1

/-- Exact covariance `∑ᵢ cᵢ vᵢ ⊗ vᵢ`, not a stipulated matrix. -/
def rawQuarterCovariance (a b : Fin 3) : ℚ :=
  ∑ i : Fin 7, quarterRawWeight i * quarterRay i a * quarterRay i b

/-- The exact symmetric matrix in the original H8 source (no numeric fit). -/
def quarterSourceCovariance (a b : Fin 3) : ℚ :=
  if a.val = 0 then
    if b.val = 0 then 317 / 43 else if b.val = 1 then 35 / 86 else 0
  else if a.val = 1 then
    if b.val = 0 then 35 / 86 else if b.val = 1 then 47 / 172 else 0
  else if b.val = 2 then 1 / 4 else 0

/-- All nine entries of the paper's raw covariance are independently
reconstructed from its seven rays and rational raw weights. -/
theorem quarter_source_covariance_exact (a b : Fin 3) :
    rawQuarterCovariance a b = quarterSourceCovariance a b := by
  fin_cases a <;> fin_cases b <;>
    norm_num [rawQuarterCovariance, quarterSourceCovariance,
      quarterRawWeight, quarterRay, Fin.sum_univ_succ]

/-- The trace used for removing the isotropic gauge is itself computed
from the seven outer products, rather than assumed. -/
theorem quarter_raw_trace :
    (∑ i : Fin 3, rawQuarterCovariance i i) = 679 / 86 := by
  simp_rw [quarter_source_covariance_exact]
  norm_num [quarterSourceCovariance, Fin.sum_univ_succ]

/-- The normalized ray coefficients `172/1229` (six rays) and `236/1229`
(third ray) follow from rescaling the original raw coefficients. -/
theorem quarter_raw_coefficients_scale_to_margin (i : Fin 7) :
    (172 / 1229 : ℚ) * quarterRawWeight i =
      (if i.val = 2 then 236 / 1229 else 172 / 1229) := by
  by_cases h : i.val = 2
  · simp [quarterRawWeight, h]
    norm_num
  · simp [quarterRawWeight, h]

/-- The source's rational rank-one direction `(35,2,0)`.
Its squared norm is exactly `1229`. -/
def rationalQuarterAxis (a : Fin 3) : ℚ :=
  if a.val = 0 then 35 else if a.val = 1 then 2 else 0

/-- Normalized trace-free covariance. The trace of the raw Q₀ is `679/86`,
so one third of its isotropic trace is `679/258`. -/
def normalizedQuarterTraceFree (a b : Fin 3) : ℚ :=
  (172 / 1229) *
    (rawQuarterCovariance a b - (if a = b then 679 / 258 else 0))

/-- Rational version of `b ⊗ b - I/3` with
`b = (35,2,0)/√1229`. -/
def rationalQuarterProjector (a b : Fin 3) : ℚ :=
  (rationalQuarterAxis a * rationalQuarterAxis b) / 1229 -
    (if a = b then 1 / 3 else 0)

/-- The claimed seven-ray normalized trace-free covariance is *exactly*
the rank-one projector in every one of its nine matrix entries. -/
theorem quarter_tracefree_rankOne (a b : Fin 3) :
    normalizedQuarterTraceFree a b = rationalQuarterProjector a b := by
  fin_cases a <;> fin_cases b <;>
    norm_num [normalizedQuarterTraceFree, rationalQuarterProjector,
      rationalQuarterAxis, rawQuarterCovariance,
      quarterRawWeight, quarterRay, Fin.sum_univ_succ]

/-- The source's transformed rank-one direction has exact physical
radial–axial product `-4443/9832`. The radicals cancel algebraically;
the sign corresponds to the fixed orientation in the source frame. -/
theorem quarter_physical_axial_efficiency :
    ((35 * Real.sqrt (91 / 200 : ℝ) + 2 * Real.sqrt (1 / 2 : ℝ)) *
      (-35 * Real.sqrt (91 / 200 : ℝ) + 2 * Real.sqrt (1 / 2 : ℝ))) / 1229 =
      -(4443 / 9832 : ℝ) := by
  have hs : (Real.sqrt (91 / 200 : ℝ)) ^ 2 = 91 / 200 :=
    Real.sq_sqrt (by norm_num)
  have hq : (Real.sqrt (1 / 2 : ℝ)) ^ 2 = 1 / 2 :=
    Real.sq_sqrt (by norm_num)
  calc
    ((35 * Real.sqrt (91 / 200 : ℝ) + 2 * Real.sqrt (1 / 2 : ℝ)) *
      (-35 * Real.sqrt (91 / 200 : ℝ) + 2 * Real.sqrt (1 / 2 : ℝ))) / 1229 =
      (4 * (Real.sqrt (1 / 2 : ℝ)) ^ 2 -
        1225 * (Real.sqrt (91 / 200 : ℝ)) ^ 2) / 1229 := by ring
    _ = -(4443 / 9832 : ℝ) := by rw [hq, hs]; norm_num

/-- The resulting moment efficiency strictly exceeds the source's
required strong-Rayleigh companion threshold. -/
theorem quarter_axial_efficiency_exceeds_companion :
    (9 / 20 : ℚ) < 4443 / 9832 := by
  norm_num

end UnforcedPatching
