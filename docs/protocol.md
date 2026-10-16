# LabBridge protocol v0.1 (draft)

## Branch contract

- `main`: stable research source and pinned acceptance criteria.
- `research/bootstrap`: initial proposal branch.
- `lab-results`: machine-generated reports only, updated independently of experimental source.

The supervisor must **not** auto-execute code pushed to `lab-results`.

## Run identity

`run_id = <experiment-id>-<source-sha-prefix>-<attempt>`

Each result must record full source SHA and the SHA of test definitions. Retries increment attempt rather than rewriting past attempts.

## Required report envelope

```json
{
  "schema": "trefoil-lab-report/v0.1",
  "experiment": "T000",
  "source_commit": "<full 40-char SHA>",
  "tests_commit": "<full 40-char SHA>",
  "run_id": "T000-<sha>-1",
  "status": "passed",
  "exit_code": 0,
  "started_at": "<UTC ISO-8601>",
  "finished_at": "<UTC ISO-8601>",
  "environment": {"python": "3.x", "platform": "Linux"},
  "measurements": {},
  "failures": [],
  "artifacts": []
}
```

Valid statuses: `passed`, `failed`, `error`, `timeout`, `cancelled`, `inconclusive`.

The exit code is not the same as evidence validity. Include both independently.

## Transport and reliability

- Use short polling or webhooks to discover new candidate source commits; pin to a SHA.
- Execute in disposable, unprivileged context with bounded CPU, memory and time.
- Capture stdout, stderr, exception traceback, and a compact failure summary.
- Publish manifest and logs to separate `lab-results` branch, ideally via atomic commits.
- Persist queue/run state locally to survive reboot.
- Distinguish job failure from supervisor/infrastructure failure.
- Redact credentials from logs, with hard size caps on artifacts.
- Results publication should be retried with exponential backoff and a local spool.
- Deploy key/token with contents-write to *only this repo*; keep it outside experiment context.
- Protect the source branch and evaluator against automatic modifications.

## Acceptance

T000 is complete only when the VM automatically (1) detects source update, (2) runs it, (3) commits results, (4) exposes a deliberate failure, (5) runs a revised fix, and (6) recovers after restart. Until then, protocol is a proposal, not proven.
