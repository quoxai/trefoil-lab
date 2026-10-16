import unittest
from lab.trefoil import Verdict, trefoil


class MinimalTrefoilTests(unittest.TestCase):
    def test_verified_progress(self):
        result = trefoil(0, lambda x, s: x + 1,
                         lambda x: Verdict(x <= 3, "bounded"),
                         lambda s, v: s, lambda x: x == 3, max_cycles=5)
        self.assertTrue(result.verified)
        self.assertEqual(result.value, 3)
        self.assertEqual(result.cycles, 3)

    def test_rejected_candidate_cannot_commit(self):
        result = trefoil(0, lambda x, s: x + 2,
                         lambda x: Verdict(x <= 1, "never accept >1"),
                         lambda s, v: s, lambda x: x == 2, max_cycles=2)
        self.assertFalse(result.verified)
        self.assertEqual(result.value, 0)
        self.assertEqual(len(result.history), 2)
        self.assertTrue(all(not item["accepted"] for item in result.history))

    def test_verifier_contract(self):
        with self.assertRaises(TypeError):
            trefoil(0, lambda x, s: x + 1,
                    lambda x: True,
                    lambda s, v: s, lambda x: x == 1)


if __name__ == "__main__":
    unittest.main()
