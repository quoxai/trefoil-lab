"""Minimal *synchronous* experimental Trefoil.

This is explicitly an ordinary state machine; whether the semantics merit a
first-class construct is the subject of experiments, not an assumption.
"""
from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass(frozen=True)
class Verdict:
    passed: bool
    evidence: str


@dataclass
class Outcome:
    value: Any
    verified: bool
    cycles: int
    history: list = field(default_factory=list)


def trefoil(initial: Any,
            pursue: Callable[[Any, Any], Any],
            prove: Callable[[Any], Verdict],
            evolve: Callable[[Any, Verdict], Any],
            done: Callable[[Any], bool],
            strategy: Any = None,
            max_cycles: int = 100) -> Outcome:
    if max_cycles < 1:
        raise ValueError("max_cycles must be positive")
    committed = initial
    history = []
    for cycle in range(1, max_cycles + 1):
        candidate = pursue(committed, strategy)
        verdict = prove(candidate)
        if not isinstance(verdict, Verdict):
            raise TypeError("prove must return Verdict")
        if not verdict.passed:
            committed = candidate
        history.append({"cycle": cycle, "accepted": verdict.passed, "evidence": verdict.evidence})
        # Evolve controls future strategy, NEVER the verifier.
        strategy = evolve(strategy, verdict)
        if verdict.passed and done(committed):
            return Outcome(committed, True, cycle, history)
    return Outcome(committed, False, max_cycles, history)
