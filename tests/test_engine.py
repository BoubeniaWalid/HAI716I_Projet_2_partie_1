import unittest

from src.engine import play_match
from src.models import Move
from src.strategies import AllD, AlwaysCooperate


class EngineTests(unittest.TestCase):
    def test_all_d_against_all_cooperate(self):
        result = play_match(AllD(), AlwaysCooperate(), rounds=2)
        self.assertEqual(result.first_score, 10)
        self.assertEqual(result.second_score, 0)
        self.assertEqual(result.first_history, [Move.DEFECT, Move.DEFECT])

    def test_invalid_noise_is_rejected(self):
        with self.assertRaises(ValueError):
            play_match(AllD(), AlwaysCooperate(), noise=1.1)


if __name__ == "__main__":
    unittest.main()
