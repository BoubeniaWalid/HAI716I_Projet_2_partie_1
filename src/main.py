"""Point d'entrée des tournois."""

import argparse
import random

from .strategies import (
    AllD,
    AlwaysCooperate,
    Joss,
    Pavlov,
    RandomStrategy,
    Tester,
    TitForTat,
)
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
    if tournament == "extended":
        strategies.extend([Pavlov(), AlwaysCooperate()])
    return strategies


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tournament", choices=["baseline", "extended", "noise"], default="baseline")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--noise", type=float, default=0.05)
    args = parser.parse_args()

    strategies = build_strategies(args.tournament, args.seed)
    scores = round_robin(
        strategies,
        seed=args.seed,
        noise=args.noise if args.tournament == "noise" else 0.0,
    )
    for position, (name, score) in enumerate(scores.items(), start=1):
        print(f"{position:>2}. {name:<16} {score}")


if __name__ == "__main__":
    main()

