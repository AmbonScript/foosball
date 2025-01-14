from __future__ import annotations
from enum import Enum

class Team(Enum):
    A = 1
    B = 2

    def get_team(position_among_players: int) -> Team:
        if position_among_players % 2 == 0:
            return Team.A
        else:
            return Team.B