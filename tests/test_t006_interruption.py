"""T006: deliberate long-running run for supervisor interruption recovery.

This test is intentionally slow and is only present on the dedicated
research/T006-interrupt branch. It does not alter Trefoil behaviour.
T006 approval must separately authorise the addition to tests/:
the SSH-signed approval tag message must include 'tests-change: approved'.
"""
import sys
import time
import unittest


class InterruptionRecoveryProbe(unittest.TestCase):
    def test_long_running_interruptible_execution(self):
        duration_seconds = 180
        started = time.monotonic()
        sys.stderr.write("T006_BEGIN long-running interruption window\n")
        sys.stderr.flush()
        while True:
            elapsed = time.monotonic() - started
            if elapsed >= duration_seconds:
                break
            time.sleep(min(1.0, duration_seconds - elapsed))
        sys.stderr.write("T006_COMPLETE uninterrupted execution\n")
        sys.stderr.flush()
        self.assertGreaterEqual(time.monotonic() - started, duration_seconds)


if __name__ == "__main__":
    unittest.main()
