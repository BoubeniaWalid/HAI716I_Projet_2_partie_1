

import random
from dataclasses import dataclass

from .models import Move, PayoffMatrix
from .strategies import Strategy


@dataclass
class MatchResult:
    first_name: str
    second_name: str
    first_score: int
    second_score: int
    first_history: list[Move]
    second_history: list[Move]


def play_match(
    first: Strategy,
    second: Strategy,
    rounds: int = 200,
    payoff: PayoffMatrix | None = None,
    noise: float = 0.0,
    rng: random.Random | None = None,
) -> MatchResult:
    if rounds <= 0:
        raise ValueError("rounds must be positive")
    if not 0 <= noise <= 1:
        raise ValueError("noise must be between 0 and 1")

    payoff = payoff or PayoffMatrix()
    rng = rng or random.Random()
    first.reset()
    second.reset()
    first_history: list[Move] = []
    second_history: list[Move] = []
    first_score = second_score = 0

    for _ in range(rounds):
        first_move = first.choose(first_history, second_history)
        second_move = second.choose(second_history, first_history)
        if rng.random() < noise:
            first_move = _invert(first_move)
        if rng.random() < noise:
            second_move = _invert(second_move)
        first_history.append(first_move)
        second_history.append(second_move)
        first_score += payoff.score(first_move, second_move)
        second_score += payoff.score(second_move, first_move)

    return MatchResult(
        first.name,
        second.name,
        first_score,
        second_score,
        first_history,
        second_history,
    )


def _invert(move: Move) -> Move:
    return Move.DEFECT if move == Move.COOPERATE else Move.COOPERATE

