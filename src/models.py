

from dataclasses import dataclass
from enum import Enum


class Move(str, Enum):
    COOPERATE = "C"
    DEFECT = "D"


@dataclass(frozen=True)
class PayoffMatrix:
    reward: int = 3
    sucker: int = 0
    temptation: int = 5
    punishment: int = 2

    def score(self, own: Move, other: Move) -> int:
        if own == Move.COOPERATE and other == Move.COOPERATE:
            return self.reward
        if own == Move.COOPERATE and other == Move.DEFECT:
            return self.sucker
        if own == Move.DEFECT and other == Move.COOPERATE:
            return self.temptation
        return self.punishment

