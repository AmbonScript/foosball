from slot import Slot
from player import Player
from team import Team
from position import Position

#def __configuration_same(self, opponent_slot: Slot, previous_slot: Slot, previous_opponent_slot: Slot) -> bool:
# self slot
    # 
    # Player 1


# Wedstrijd 1
w1_A_Ta: Slot = Slot(1)
w1_A_Ta.player = Player(5)
assert w1_A_Ta._Slot__team == Team.A
assert w1_A_Ta._Slot__position == Position.ATTACKER
assert w1_A_Ta.player.get_number() == 5

w1_V_Ta: Slot = Slot(2)
w1_V_Ta.player = Player(3)
assert w1_V_Ta._Slot__team == Team.A
assert w1_V_Ta._Slot__position == Position.DEFENDER
assert w1_V_Ta.player.get_number() == 3

w1_A_Tb: Slot = Slot(3)
w1_A_Tb.player = Player(7)
assert w1_A_Tb._Slot__team == Team.B
assert w1_A_Tb._Slot__position == Position.ATTACKER
assert w1_A_Tb.player.get_number() == 7

w1_V_Tb: Slot = Slot(4)
w1_V_Tb.player = Player(6)
assert w1_V_Tb._Slot__team == Team.B
assert w1_V_Tb._Slot__position == Position.DEFENDER
assert w1_V_Tb.player.get_number() == 6

# Wedstrijd 2
w2_A_Ta: Slot = Slot(5)
w2_A_Ta.player = Player(3)
assert w2_A_Ta._Slot__team == Team.A
assert w2_A_Ta._Slot__position == Position.ATTACKER
assert w2_A_Ta.player.get_number() == 3

w2_V_Ta: Slot = Slot(6)
w2_V_Ta.player = Player(0)
assert w2_V_Ta._Slot__team == Team.A
assert w2_V_Ta._Slot__position == Position.DEFENDER
assert w2_V_Ta.player.get_number() == 0

w2_A_Tb: Slot = Slot(7)
w2_A_Tb.player = Player(6)
assert w2_A_Tb._Slot__team == Team.B
assert w2_A_Tb._Slot__position == Position.ATTACKER
assert w2_A_Tb.player.get_number() == 6

w2_V_Tb: Slot = Slot(8)
w2_V_Tb.player = Player(7)
assert w2_V_Tb._Slot__team == Team.B
assert w2_V_Tb._Slot__position == Position.DEFENDER
assert w2_V_Tb.player.get_number() == 7

# Wedstrijd 3
w3_A_Ta: Slot = Slot(5)
w3_A_Ta.player = Player(7)
assert w3_A_Ta._Slot__team == Team.A
assert w3_A_Ta._Slot__position == Position.ATTACKER
assert w3_A_Ta.player.get_number() == 7

w3_V_Ta: Slot = Slot(6)
w3_V_Ta.player = Player(0)
assert w3_V_Ta._Slot__team == Team.A
assert w3_V_Ta._Slot__position == Position.DEFENDER
assert w3_V_Ta.player.get_number() == 0

w3_A_Tb: Slot = Slot(7)
w3_A_Tb.player = Player(3)
assert w3_A_Tb._Slot__team == Team.B
assert w3_A_Tb._Slot__position == Position.ATTACKER
assert w3_A_Tb.player.get_number() == 3

## Checks
assert w3_A_Tb._Slot__configuration_same(w3_A_Ta, w1_V_Ta, w1_A_Tb) == False
assert w3_A_Tb._Slot__configuration_same(w3_A_Ta, w2_A_Ta, w2_V_Tb) == False
assert w3_A_Tb._Slot__configuration_same(w3_V_Ta, w2_A_Ta, w2_V_Ta) == False


