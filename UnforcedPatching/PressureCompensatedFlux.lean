import UnforcedPatching.MeridionalInverse
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Tactic

/-!
# Pressure-compensated axial flux on a cylindrical annulus

We formalize the one-dimensional radial FTC bridge following azimuthal
and axial averaging of a cylindrical axial-divergence identity:

  F(r) = S'(r) + S(r)/r + q(r).

Here `S` is the axially integrated meridional shear, `F` the axially
integrated axial source, and `q` the **full axial boundary trace** of
`K_zz + p`. The theorem does not silently set `q = 0`.

The prior Cartesian-to-cylindrical, angular-average and axial-integration
steps are not proved here. Nor is an H8 source, frame, cutoff or compact
positive coefficient correction constructed.
-/

noncomputable section

open MeasureTheory
open scoped Interval

namespace UnforcedPatching

/-- The normalized radial primitive of the true axial source marginal. -/
def axialSourcePrimitive (F : ℝ → ℝ) (a r : ℝ) : ℝ :=
  (∫ s in a..r, s * F s) / r

/-- The normalized radial primitive of the pressure/tensor axial trace. -/
def axialBoundaryPrimitive (q : ℝ → ℝ) (a r : ℝ) : ℝ :=
  (∫ s in a..r, s * q s) / r

/-- The cylindrical axial balance in differential form implies the
conservative derivative `(r*S)' = r*(F-q)` at any nonzero radius. -/
theorem pressureCompensatedFluxConservativeDerivative
    (S F q : ℝ → ℝ) (x : ℝ) (hx : x ≠ 0)
    (hS : HasDerivAt S (F x - q x - S x / x) x) :
    HasDerivAt (fun s : ℝ => s * S s) (x * (F x - q x)) x := by
  have h : HasDerivAt (fun s : ℝ => s * S s)
      (S x + x * (F x - q x - S x / x)) x := by
    have hRaw := (hasDerivAt_id x).mul hS
    have hFun : (id * S) = (fun s : ℝ => s * S s) := by
      funext s
      simp
    rw [hFun] at hRaw
    simpa only [id_eq, one_mul] using hRaw
  have hval : S x + x * (F x - q x - S x / x) =
      x * (F x - q x) := by
    field_simp [hx]
    ring
  simpa [hval] using h

/-- The complete pressure-compensated axial source primitive equals
the shear slice minus its inner trace plus the full axial boundary
primitive. The radial interval integral and FTC are certified here,
while the construction of physical `S,F,q` is an explicit upstream gate. -/
theorem pressureCompensatedFluxIdentity
    (S F q : ℝ → ℝ) (a r : ℝ)
    (ha : 0 < a) (har : a ≤ r)
    (hS : ∀ x ∈ Set.Icc a r,
      HasDerivAt S (F x - q x - S x / x) x)
    (hF : IntervalIntegrable (fun s : ℝ => s * F s) volume a r)
    (hq : IntervalIntegrable (fun s : ℝ => s * q s) volume a r) :
    axialSourcePrimitive F a r =
      S r - (a / r) * S a + axialBoundaryPrimitive q a r := by
  have hrne : r ≠ 0 := ne_of_gt (lt_of_lt_of_le ha har)
  have hderiv (x : ℝ) (hx : x ∈ Set.uIcc a r) :
      HasDerivAt (fun s : ℝ => s * S s) (x * (F x - q x)) x := by
    have hxI : x ∈ Set.Icc a r := by
      simpa [Set.uIcc_of_le har] using hx
    have hxne : x ≠ 0 := ne_of_gt (lt_of_lt_of_le ha hxI.1)
    exact pressureCompensatedFluxConservativeDerivative S F q x hxne (hS x hxI)
  have hInt : IntervalIntegrable (fun s : ℝ => s * (F s - q s)) volume a r := by
    have hfun : (fun s : ℝ => s * (F s - q s)) =
        (fun s : ℝ => s * F s - s * q s) := by
      funext s
      ring
    rw [hfun]
    exact hF.sub hq
  have hFTC : (∫ s in a..r, s * (F s - q s)) =
      r * S r - a * S a :=
    intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hInt
  have hsplit : (∫ s in a..r, s * (F s - q s)) =
      (∫ s in a..r, s * F s) - (∫ s in a..r, s * q s) := by
    have hfun : (fun s : ℝ => s * (F s - q s)) =
        (fun s : ℝ => s * F s - s * q s) := by
      funext s
      ring
    rw [hfun, intervalIntegral.integral_sub hF hq]
  rw [hsplit] at hFTC
  have hFlux : (∫ s in a..r, s * F s) =
      r * S r - a * S a + (∫ s in a..r, s * q s) := by
    linarith
  unfold axialSourcePrimitive axialBoundaryPrimitive
  rw [hFlux]
  field_simp [hrne]

/-- A genuinely zero axial boundary trace gives the simpler formula.
This specialization cannot be used when the trace is unknown. -/
theorem pressureCompensatedFluxZeroTrace
    (S F : ℝ → ℝ) (a r : ℝ)
    (ha : 0 < a) (har : a ≤ r)
    (hS : ∀ x ∈ Set.Icc a r,
      HasDerivAt S (F x - S x / x) x)
    (hF : IntervalIntegrable (fun s : ℝ => s * F s) volume a r) :
    axialSourcePrimitive F a r = S r - (a / r) * S a := by
  have hS' : ∀ x ∈ Set.Icc a r,
      HasDerivAt S (F x - (fun _ : ℝ => (0 : ℝ)) x - S x / x) x := by
    intro x hx
    simpa using hS x hx
  have hq : IntervalIntegrable
      (fun s : ℝ => s * (fun _ : ℝ => (0 : ℝ)) s) volume a r := by
    simp
  have h := pressureCompensatedFluxIdentity S F (fun _ => 0)
    a r ha har hS' hF hq
  simpa [axialBoundaryPrimitive] using h

/-- The exact source primitive inherits any independently authenticated
upper and lower bounds for the shear slice, *after* subtracting the
full boundary trace and adding the inner shear trace. The `B±` may be
the source-frame or rotating-frame cone supports, once those are proved
for the authentic spatial stress. -/
theorem pressureCompensatedFluxSupportGate
    (S F q : ℝ → ℝ) (a r Bminus Bplus : ℝ)
    (ha : 0 < a) (har : a ≤ r)
    (hS : ∀ x ∈ Set.Icc a r,
      HasDerivAt S (F x - q x - S x / x) x)
    (hF : IntervalIntegrable (fun s : ℝ => s * F s) volume a r)
    (hq : IntervalIntegrable (fun s : ℝ => s * q s) volume a r)
    (hSupport : -Bminus ≤ S r ∧ S r ≤ Bplus) :
    -Bminus ≤ axialSourcePrimitive F a r + (a / r) * S a -
        axialBoundaryPrimitive q a r ∧
      axialSourcePrimitive F a r + (a / r) * S a -
        axialBoundaryPrimitive q a r ≤ Bplus := by
  have heq : axialSourcePrimitive F a r + (a / r) * S a -
      axialBoundaryPrimitive q a r = S r := by
    rw [pressureCompensatedFluxIdentity S F q a r ha har hS hF hq]
    ring
  rw [heq]
  exact hSupport

/-- A genuine, nonzero axial boundary trace: `q(s)=2s` on `[1,2]`
has radial primitive `7/3`. In particular it cannot be discarded
as if the complete physical pressure/tensor boundary term vanished. -/
theorem pressureCompensatedFluxNonzeroTraceExample :
    axialBoundaryPrimitive (fun s : ℝ => 2 * s) 1 2 = (7 / 3 : ℝ) := by
  unfold axialBoundaryPrimitive
  have hfun : (fun s : ℝ => s * (2 * s)) = (fun s : ℝ => s ^ 2 * 2) := by
    funext s
    ring
  rw [hfun, intervalIntegral.integral_mul_const, integral_pow]
  norm_num

end UnforcedPatching
