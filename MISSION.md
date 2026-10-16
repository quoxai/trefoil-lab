# Trefoil Lab — research charter

**Principal investigator:** ChatGPT GPT-6 (interactive sessions)
**Infrastructure:** independent low-cost Linux VM, potentially provisioned through Hyperion/QuoxMCP
**Model usage:** zero LLM calls within the experiment runner.
**Publication:** private until results merit wider scrutiny.

## Hypothesis

A Trefoil is an adaptive computational lifecycle of **pursue, prove, evolve** with governed crossings. Investigate whether explicit proof-gated commits, independent verifier authority, adaptation boundaries and composability offer advantages over conventional feedback loops and finite-state machines.

## Definitions under test

- Pursue creates a candidate state, without mutating committed state.
- Prove evaluates that candidate against externally protected invariants.
- Evolve changes the strategy for subsequent pursuit, not the acceptance standard.
- Crossing enforces admissible transitions and records observations.
- Commit requires approval from the verifier; failure leaves the committed state unchanged.
- Termination includes success, exhaustion, failure, suspension and cancellation.

These semantics are provisional, not a claim that a knot topology has computational novelty.

## Experimental standards

1. Write hypotheses and expected results before execution.
2. Version test definitions and source commitments separately.
3. Compare against a fair baseline performing equivalent work with equivalent resources.
4. Treat failed hypotheses as valid findings.
5. Label empirical evidence separately from inferred and formal properties.
6. Include deterministic seeds, runtime versions and exact commit SHA.
7. Require independent approval for acceptance criteria changes.
8. Disallow self-modifying tests or unreviewed evaluation-policy changes.

## Milestones

- T000: GitHub → VM → GitHub execution and failure-feedback loop.
- T001: minimal synchronous Trefoil.
- T002: verification cannot be bypassed to commit.
- T003: fair comparison against feedback loop/state machine.
- T004: adversarial verifier and evaluator protection.
- T005+: nested/concurrent Trefoils, fault injection, proof semantics and language experiment.

## Boundaries

LabBridge is a transport / instrumentation component, not Trefoil. Proof components must not be able to rewrite protected success conditions. Quox integrations are optional and explicitly deferred.

The laboratory may not be able to awaken the ChatGPT investigator merely because results were pushed; requests in chat (or a later supported scheduled mechanism) prompt new analysis.
