# VM provisioning handoff — minimal external assistance

Goal: provision a low-cost clean Linux VM that runs code from `quoxai/trefoil-lab` and reports errors/results back to GitHub. Once this is operational, ChatGPT authors code and experiments through GitHub. **No Claude agents or LLM API calls in the runtime.**

Requirements:
- Ubuntu LTS or equivalent, Python 3.10+ and Git.
- Dedicated unprivileged supervisor service account.
- Independent supervisor outside the experiment checkout; systemd-managed and auto-restart.
- Pull pinned commits from an approved research branch; never auto-run results branch commits.
- Sandbox experimental code: no secrets, minimal privileges, bounded time/CPU/RAM/storage, preferably network disabled.
- Per-repository credentials only; short-lived GitHub App token or narrowly scoped token if available.
- GitHub writes publish to `lab-results`, with attempt IDs and immutable run directories.
- Persist failed uploads locally and retry; supervisor publishes its own heartbeat / error status.
- Run `python3 -m unittest discover -s tests -v` and `python3 -m lab.run --out report.json` against the pinned checkout.
- Before handing over, demonstrate success, failure, repair and reboot recovery.
- Do not grant root, rack-wide access or any production credentials to the experiment runner.

No QuoxMCP/Hyperion dependency for normal tests. They can later assist provisioning/recovery if separately permitted.

**Important:** this document is an operational specification, not evidence that any VM has been provisioned.
