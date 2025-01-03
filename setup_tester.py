from slot import Slot
from player import Player
from team import Team
from position import Position

Player.set_players(29)
slot: Slot = Slot()
slot.place_players()
assert slot._Slot__match == 1
assert slot._Slot__team == Team.A
assert slot._Slot__position == Position.ATTACKER
# slot.print_slots()
