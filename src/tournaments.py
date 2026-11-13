

import random
from collections import defaultdict

from .engine import play_match
from .models import PayoffMatrix
from .strategies import Strategy


def round_robin(
    strategies: list[Strategy],
    rounds: int = 200,
    matches_per_pair: int = 5,
    seed: int = 42,
    payoff: PayoffMatrix | None = None,
    noise: float = 0.0,
) -> dict[str, int]:
    if matches_per_pair <= 0:
        raise ValueError("matches_per_pair must be positive")

    rng = random.Random(seed)
    scores = defaultdict(int)
    for index, first in enumerate(strategies):
        for second in strategies[index + 1 :]:
            for _ in range(matches_per_pair):
                result = play_match(
                    first, second, rounds, payoff, noise=noise, rng=rng
                )
                scores[result.first_name] += result.first_score
                scores[result.second_name] += result.second_score
    return dict(sorted(scores.items(), key=lambda item: (-item[1], item[0])))

