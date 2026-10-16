"""Run deterministic T000 reference exercise and publish JSON locally."""
import argparse
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from .trefoil import Verdict, trefoil


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def execute():
    start = utc_now()
    def pursue(value, strategy):
        return value + 1
    def prove(value):
        return Verdict(value <= 3, "candidate <= 3")
    def evolve(strategy, verdict):
        return strategy
    outcome = trefoil(0, pursue, prove, evolve, lambda x: x == 3, max_cycles=5)
    passed = outcome.verified and outcome.value == 3 and outcome.cycles == 3
    return {
        "schema": "trefoil-lab-report/v0.1",
        "experiment": "T000",
        "source_commit": None,
        "tests_commit": None,
        "run_id": None,
        "status": "passed" if passed else "failed",
        "exit_code": 0 if passed else 1,
        "started_at": start,
        "finished_at": utc_now(),
        "environment": {"python": platform.python_version(), "platform": platform.system()},
        "measurements": {"cycles": outcome.cycles, "final_value": outcome.value},
        "failures": [] if passed else ["unexpected outcome"],
        "artifacts": []
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    report = execute()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "report": str(args.out)}))
    return report["exit_code"]


if __name__ == "__main__":
    sys.exit(main())
