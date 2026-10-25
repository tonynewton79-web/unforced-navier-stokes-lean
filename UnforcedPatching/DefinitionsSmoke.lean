import UnforcedPatching.Definitions

/-!
This compile-only test checks the new *unforced* proposition against the
upstream physical field types. It will fail if the candidate silently
reverts to the forced, zero-initial-data CandidateProperties interface.
-/

#check UnforcedPatching.InitialNonzero
#check UnforcedPatching.UnforcedPeriodicCandidate
#check UnforcedPatching.unforcedTargetStatement

example {u : NavierStokes.ProblemStatement.VelocityField}
    {p : NavierStokes.ProblemStatement.PressureField}
    (h : UnforcedPatching.UnforcedPeriodicCandidate u p) :
    ∃ x : NavierStokes.ProblemStatement.Space, u (0, x) ≠ 0 :=
  h.initial_nonzero

example {u : NavierStokes.ProblemStatement.VelocityField}
    {p : NavierStokes.ProblemStatement.PressureField}
    (h : UnforcedPatching.UnforcedPeriodicCandidate u p)
    (t : ℝ) (ht : t ∈ Set.Ioo (0 : ℝ) 1)
    (x : NavierStokes.ProblemStatement.Space) :
    NavierStokes.ProblemStatement.navierStokesResidual u p t x = 0 :=
  h.navier_stokes_zero t ht x

#print axioms UnforcedPatching.candidate_initial_not_zero
