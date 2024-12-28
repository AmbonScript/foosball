from __future__ import annotations
from position import Position
from team import Team
from player import Player
from competition import Competition
from round import Round
from result import Result
from matchslot import MatchSlot
from typing import List
import math
import random

Player.set_players(13)
players: List[Player] = Player.get_players()
lowest_attacker: Player = max(players, key=lambda player: player.get_rank(Position.ATTACKER))
assert lowest_attacker.get_rank(Position.ATTACKER) == 13
assert lowest_attacker._Player__attackerByeReceived == False
lowest_attacker._Player__attackerByeReceived = True
assert lowest_attacker._Player__attackerByeReceived == True
Player._Player__provide_byes_for(Position.ATTACKER)
assert Player._Player__current_attacker_bye == 12
Player._Player__provide_byes_for(Position.ATTACKER)
assert Player._Player__current_attacker_bye == 11