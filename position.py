from __future__ import annotations
from enum import Enum

class Position(Enum):
    ATTACKER = 1
    DEFENDER = 2

    def get_position(number_of_players: int, position_among_players: int) -> Position:
        if position_among_players < (number_of_players / 2):
            return Position.ATTACKER
        else:
            return Position.DEFENDER