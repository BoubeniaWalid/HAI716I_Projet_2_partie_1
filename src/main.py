"""Point d'entrée des tournois."""

import argparse
import random

from .engine import play_match
from .strategies import (
    AllD,
    AlwaysCooperate,
    Joss,
    Pavlov,
    RandomStrategy,
    Tester,
    TitForTat,
)
from .models import ALTERNATIVE_PAYOFF
from .tournaments import round_robin


def build_strategies(tournament: str, seed: int):
    rng = random.Random(seed)
    strategies = [
        AllD(),
        RandomStrategy(rng),
        TitForTat(),
        Tester(),
        Joss(rng),
    ]
    if tournament in {"extended", "noise", "payoff"}:
        strategies.extend([Pavlov(), AlwaysCooperate()])
    return strategies


def build_strategy(name: str, seed: int):
    rng = random.Random(seed)
    strategies = {
        "all-d": AllD(),
        "random": RandomStrategy(rng),
        "tit-for-tat": TitForTat(),
        "tester": Tester(),
        "joss": Joss(rng),
        "pavlov": Pavlov(),
        "all-c": AlwaysCooperate(),
    }
    return strategies[name]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--match",
        nargs=2,
        metavar=("FIRST", "SECOND"),
        choices=[
            "all-d",
            "random",
            "tit-for-tat",
            "tester",
            "joss",
            "pavlov",
            "all-c",
        ],
        help="Joue une partie entre deux stratégies.",
    )
    parser.add_argument("--rounds", type=int, default=200)
    parser.add_argument("--match-noise", type=float, default=0.0)
    parser.add_argument(
        "--tournament",
        choices=["baseline", "extended", "noise", "payoff"],
        default="baseline",
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--noise", type=float, default=0.05)
    args = parser.parse_args()

    if args.match:
        first = build_strategy(args.match[0], args.seed)
        second = build_strategy(args.match[1], args.seed + 1)
        result = play_match(
            first,
            second,
            rounds=args.rounds,
            noise=args.match_noise,
            rng=random.Random(args.seed),
        )
        print(f"{result.first_name}: {result.first_score}")
        print(f"{result.second_name}: {result.second_score}")
        return

    strategies = build_strategies(args.tournament, args.seed)
    scores = round_robin(
        strategies,
        seed=args.seed,
        payoff=ALTERNATIVE_PAYOFF if args.tournament == "payoff" else None,
        noise=args.noise if args.tournament == "noise" else 0.0,
    )
    for position, (name, score) in enumerate(scores.items(), start=1):
        print(f"{position:>2}. {name:<16} {score}")


if __name__ == "__main__":
    main()

