# Trefoil Lab

Private experimental research into **verified adaptive computation**.

Three independent lines of research:
1. **Trefoil** — can pursue / prove / evolve constitute a useful reusable computational primitive?
2. **Proof** — can evidence and acceptance gates be independently inspected and reproduced?
3. **LabBridge** — can ChatGPT propose experiments through GitHub and a separate VM execute and report them without LLM calls?

This repository is **experimental and private**. The objective is to *test* whether Trefoil adds meaningful value over ordinary loops and state machines, not assume it does.

## Start locally

Python 3.10+; no third-party dependencies.

```bash
python3 -m unittest discover -s tests -v
python3 -m lab.run --out /tmp/trefoil-lab-report.json
```

## Status

M0 bootstrap: reference experiment and structured JSON report prepared; VM supervisor **not provisioned or validated yet**. No claim of autonomous execution.

## Safety and research integrity

- Keep the VM supervisor separate from untrusted experiment code.
- Pin source commits; isolate execution; limit time, CPU, memory, disk and network.
- Do not grant the experimental process GitHub write credentials.
- Do not change acceptance criteria merely to get a passing result.
- Changes to evaluator or baseline must be separately approved and versioned.
- Publishing results must not trigger new runs.
- Never claim formal proof from passing tests.
- GitHub report and source commits must be traceably connected.

See [MISSION.md](MISSION.md), [docs/protocol.md](docs/protocol.md) and [docs/vm-handoff.md](docs/vm-handoff.md).

## First milestone

T000: execute the reference experiment on the VM, push its report to a results branch, deliberately fail an implementation, capture the error, fix it, and demonstrate recovery after reboot. GitHub results are the feedback channel; the researcher is invoked via chat or a separately configured scheduled controller.
