

import random
from abc import ABC, abstractmethod

from .models import Move


class Strategy(ABC):
    name = "strategy"

    def reset(self) -> None:
        """Réinitialise l'état entre deux parties."""

    @abstractmethod
    def choose(self, own_history: list[Move], opponent_history: list[Move]) -> Move:
        """Choisit C ou D à partir de l'historique connu."""


class AllD(Strategy):
    name = "ALL-D"

    def choose(self, own_history, opponent_history):
        return Move.DEFECT


class RandomStrategy(Strategy):
    name = "RANDOM"

    def __init__(self, rng: random.Random, cooperation_probability: float = 0.5):
        self.rng = rng
        self.cooperation_probability = cooperation_probability

    def choose(self, own_history, opponent_history):
        return (
            Move.COOPERATE
            if self.rng.random() < self.cooperation_probability
            else Move.DEFECT
        )


class TitForTat(Strategy):
    name = "TIT-FOR-TAT"

    def choose(self, own_history, opponent_history):
        return Move.COOPERATE if not opponent_history else opponent_history[-1]


class Tester(Strategy):
    name = "TESTER"

    def reset(self):
        self._round = 0

    def choose(self, own_history, opponent_history):
        # TODO: remplacer par la définition exacte du cours.
        self._round = len(own_history)
        return Move.DEFECT if self._round == 0 else Move.COOPERATE


class Joss(Strategy):
    name = "JOSS"

    def __init__(self, rng: random.Random, defection_probability: float = 0.1):
        self.rng = rng
        self.defection_probability = defection_probability

    def choose(self, own_history, opponent_history):
        if self.rng.random() < self.defection_probability:
            return Move.DEFECT
        return Move.COOPERATE if not opponent_history else opponent_history[-1]


class Pavlov(Strategy):
    """Nouvelle stratégie candidate : win-stay, lose-shift."""

    name = "PAVLOV"

    def choose(self, own_history, opponent_history):
        if not own_history:
            return Move.COOPERATE
        if own_history[-1] == opponent_history[-1]:
            return own_history[-1]
        return Move.DEFECT if own_history[-1] == Move.COOPERATE else Move.COOPERATE


class AlwaysCooperate(Strategy):
    """Nouvelle stratégie candidate à comparer aux autres."""

    name = "ALL-C"

    def choose(self, own_history, opponent_history):
        return Move.COOPERATE

