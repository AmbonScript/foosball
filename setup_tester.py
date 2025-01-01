from matchslot import MatchSlot
from player import Player
from team import Team
from position import Position

Player.set_players(8)
slot: MatchSlot = MatchSlot()
assert slot._MatchSlot__match == 1
assert slot._MatchSlot__team == Team.A
assert slot._MatchSlot__position == Position.ATTACKER
slot.print_slots()
