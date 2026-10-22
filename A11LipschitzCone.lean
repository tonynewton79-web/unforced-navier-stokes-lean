import A11BernsteinCone

/-! Abstract A.11 non-polynomial Lipschitz net certificate.
Not a proof of the actual A.11 derivative bounds or Navier--Stokes theorem. -/
namespace A11LipschitzCone

theorem net_lower_bound (f : ℝ → ℝ) (S V : Set ℝ)
    (r L δ : ℝ) (hL : 0 ≤ L)
    (hcover : ∀ x ∈ S, ∃ y ∈ V, |x-y| ≤ r)
    (hLip : ∀ x ∈ S, ∀ y ∈ V, |f x-f y| ≤ L*|x-y|)
    (hnodes : ∀ y ∈ V, δ + L*r ≤ f y) :
    ∀ x ∈ S, δ ≤ f x := by
  intro x hx
  obtain ⟨y,hy,hxy⟩ := hcover x hx
  have hdiff := hLip x hx y hy
  have hreserve : L*|x-y| ≤ L*r := mul_le_mul_of_nonneg_left hxy hL
  have hnode := hnodes y hy
  have hlower : -( |f x-f y| ) ≤ f x - f y := neg_abs_le _
  linarith

theorem uniform_two_sign_from_nets
    (E N : ℝ → ℝ) (S V : Set ℝ)
    (λ r LE LP LM δ : ℝ)
    (hδ : 0 < δ)
    (hcover : ∀ x ∈ S, ∃ y ∈ V, |x-y| ≤ r)
    (hLE : 0 ≤ LE) (hLP : 0 ≤ LP) (hLM : 0 ≤ LM)
    (hLipE : ∀ x ∈ S, ∀ y ∈ V, |E x-E y| ≤ LE*|x-y|)
    (hLipP : ∀ x ∈ S, ∀ y ∈ V,
      |(λ*E x+2*N x)-(λ*E y+2*N y)| ≤ LP*|x-y|)
    (hLipM : ∀ x ∈ S, ∀ y ∈ V,
      |(λ*E x-2*N x)-(λ*E y-2*N y)| ≤ LM*|x-y|)
    (hENodes : ∀ y ∈ V, δ+LE*r ≤ E y)
    (hPNodes : ∀ y ∈ V, LP*r ≤ λ*E y+2*N y)
    (hMNodes : ∀ y ∈ V, LM*r ≤ λ*E y-2*N y) :
    ∀ x ∈ S, |N x|/E x ≤ λ/2 := by
  intro x hx
  have ebound := net_lower_bound E S V r LE δ hLE hcover hLipE hENodes x hx
  have pbound := net_lower_bound
    (fun z => λ*E z+2*N z) S V r LP 0 hLP hcover hLipP hPNodes x hx
  have mbound := net_lower_bound
    (fun z => λ*E z-2*N z) S V r LM 0 hLM hcover hLipM hMNodes x hx
  exact A11BernsteinCone.two_sign_cone λ (E x) (N x)
    (lt_of_lt_of_le hδ ebound) pbound mbound

#print axioms net_lower_bound
#print axioms uniform_two_sign_from_nets
end A11LipschitzCone
