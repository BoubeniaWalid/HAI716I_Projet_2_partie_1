import unittest
import random

from src.engine import play_match
from src.models import Move
from src.strategies import AllD, AlwaysCooperate, Joss, Tester, TitForTat


class EngineTests(unittest.TestCase):
    def test_all_d_against_all_cooperate(self):
        result = play_match(AllD(), AlwaysCooperate(), rounds=2)
        self.assertEqual(result.first_score, 10)
        self.assertEqual(result.second_score, 0)
        self.assertEqual(result.first_history, [Move.DEFECT, Move.DEFECT])

    def test_invalid_noise_is_rejected(self):
        with self.assertRaises(ValueError):
            play_match(AllD(), AlwaysCooperate(), noise=1.1)

    def test_tit_for_tat_starts_with_cooperation_then_copies(self):
        result = play_match(TitForTat(), AllD(), rounds=3)
        self.assertEqual(
            result.first_history,
            [Move.COOPERATE, Move.DEFECT, Move.DEFECT],
        )

    def test_tester_uses_tit_for_tat_after_retaliation(self):
        result = play_match(Tester(), AllD(), rounds=3)
        self.assertEqual(
            result.first_history,
            [Move.DEFECT, Move.DEFECT, Move.DEFECT],
        )

    def test_tester_repeats_cooperate_cooperate_defect_without_retaliation(self):
        result = play_match(Tester(), AlwaysCooperate(), rounds=7)
        self.assertEqual(
            result.first_history,
            [
                Move.DEFECT,
                Move.COOPERATE,
                Move.COOPERATE,
                Move.DEFECT,
                Move.COOPERATE,
                Move.COOPERATE,
                Move.DEFECT,
            ],
        )

    def test_joss_follows_tit_for_tat_against_all_d(self):
        result = play_match(Joss(random.Random(42)), AllD(), rounds=3)
        self.assertEqual(
            result.first_history,
            [Move.COOPERATE, Move.DEFECT, Move.DEFECT],
        )


if __name__ == "__main__":
    unittest.main()
