from __future__ import annotations
from position import Position
from team import Team
from player import Player
from competition import Competition
from round import Round
from result import Result
from matchslot import MatchSlot
from typing import List


# Position -----------------------------------------------------------------------
# Get Position
attacker: Position = Position.get_position(10, 2)
assert(attacker == Position.ATTACKER)

defender: Position = Position.get_position(10, 7)
assert(defender == Position.DEFENDER)

# Team ---------------------------------------------------------------------------
# Get Team
teamA: Team = Team.get_team(0)
assert teamA == Team.A

teamB: Team = Team.get_team(1)
assert teamB == Team.B

# Result -------------------------------------------------------------------------
#Constructor
result: Result = Result()
assert result._Result__winningTeam is None
assert result._Result__goalDifference is None

# Get Winning team
assert isinstance(result.getWinningTeam(), Team)
assert result.getWinningTeam == result.getWinningTeam

# Get Goal Difference
assert isinstance(result.getGoalDifference(), int)
assert result.getGoalDifference == result.getGoalDifference

# Player -------------------------------------------------------------------------
# Constructor
player: Player = Player(1)
assert player._Player__number == 1
assert player._Player__attackerRank is None
assert player._Player__defenderRank is None
assert player._Player__attackerByeReceived == False
assert player._Player__defenderByeReceived == False
assert player._Player__attackerGamesWon == 0
assert player._Player__defenderGamesWon == 0

# Receive Attacker Bye
player: Player = Player(100)
assert player.bye_received(Position.ATTACKER) == False
byeReceived: bool = player.receive_bye(Position.ATTACKER)
assert byeReceived == True
assert player._Player__attackerGamesWon == 1
assert player._Player__defenderGamesWon == 0
assert player._Player__attackerByeReceived == True
assert player._Player__defenderByeReceived == False
byeReceived: bool = player.receive_bye(Position.ATTACKER)
assert byeReceived == False
assert player._Player__attackerGamesWon == 1
assert player.bye_received(Position.ATTACKER) == True

# Receive Defender Bye
player: Player = Player(57)
assert player.bye_received(Position.DEFENDER) == False
byeReceived: bool = player.receive_bye(Position.DEFENDER)
assert byeReceived == True
assert player._Player__attackerGamesWon == 0
assert player._Player__defenderGamesWon == 1
assert player._Player__attackerByeReceived == False
assert player._Player__defenderByeReceived == True
byeReceived: bool = player.receive_bye(Position.DEFENDER)
assert byeReceived == False
assert player._Player__defenderGamesWon == 1
assert player.bye_received(Position.DEFENDER) == True

# Get Players
players: List[Player] = Player.set_players(3)
assert len(players) == 3

players: List[Player] = Player.set_players(12)
assert len(players) == 12

players: List[Player] = Player.set_players(1500)
assert len(players) == 1500

# Competition --------------------------------------------------------------------
# Players initialized in constructor
competition: Competition = Competition(3)
assert len(competition._Competition__players) == 3

competition: Competition = Competition(12)
assert len(competition._Competition__players) == 12

competition: Competition = Competition(15)
assert len(competition._Competition__players) == 15

# First round declared - but not intialized - in constructor competition
competition: Competition = Competition(12)
assert competition._Competition__round is None

# Second round created when Competion.play_round() is called for the 2nd time
competition: Competition = Competition(12)
competition.play_round()
competition.play_round()
assert competition._Competition__round.get_round_number() == 2

# Players ranked after playing first round
competition: Competition = Competition(12)
competition.play_round()
player: Player = competition._Competition__players[6]
assert player._Player__defenderRank is not None
assert player._Player__attackerRank is not None
player7: Player = competition._Competition__players[7]
assert player._Player__defenderRank is not player7._Player__defenderRank
assert player._Player__attackerRank is not player7._Player__attackerRank

# Players list intact after playing first round
competition: Competition = Competition(12)
assert len(competition._Competition__players) == 12
competition.play_round()
assert len(competition._Competition__players) == 12

# Round --------------------------------------------------------------------
# Round number set in constructor
players: List[Player] = Player.set_players(10)
round: Round = Round(1, players)
assert round._Round__number == 1

players: List[Player] = Player.set_players(10)
round: Round = Round(12, players)
assert round._Round__number == 12

players: List[Player] = Player.set_players(10)
round: Round = Round(1500, players)
assert round._Round__number == 1500

# MatchSlot --------------------------------------------------------------------
# Set Match
players: List[Player] = Player.set_players(20)
match_slot: MatchSlot = MatchSlot(players)
match_slot._MatchSlot__set_match(1)
assert match_slot._MatchSlot__match == 1
match_slot._MatchSlot__set_match(14)
assert match_slot._MatchSlot__match == 2
match_slot._MatchSlot__set_match(15)
assert match_slot._MatchSlot__match == 3
match_slot._MatchSlot__set_match(7)
assert match_slot._MatchSlot__match == 4
match_slot._MatchSlot__set_match(20)
assert match_slot._MatchSlot__match == 5

#Set Team
players: List[Player] = Player.set_players(20)
match_slot: MatchSlot = MatchSlot(players)
match_slot._MatchSlot__set_team(1)
assert match_slot._MatchSlot__team == Team.A
match_slot._MatchSlot__set_team(14)
assert match_slot._MatchSlot__team == Team.B
match_slot._MatchSlot__set_team(6)
assert match_slot._MatchSlot__team == Team.B
match_slot._MatchSlot__set_team(19)
assert match_slot._MatchSlot__team == Team.A

#Set Position
players: List[Player] = Player.set_players(20)
match_slot: MatchSlot = MatchSlot(players)
match_slot._MatchSlot__set_position(1)
assert match_slot._MatchSlot__position == Position.ATTACKER
match_slot._MatchSlot__set_position(9)
assert match_slot._MatchSlot__position == Position.ATTACKER
match_slot._MatchSlot__set_position(11)
assert match_slot._MatchSlot__position == Position.DEFENDER
match_slot._MatchSlot__set_position(17)
assert match_slot._MatchSlot__position == Position.DEFENDER

#Set Next Match Slot
players: List[Player] = Player.set_players(20)
match_slot: MatchSlot = MatchSlot(players)
players: List[Player] = Player.set_players(20)
assert len(players) == 20
match_slot._MatchSlot__set_next_match_slot(1)
for i in range(1, 20):
    match_slot = match_slot._MatchSlot__next_match_slot
    assert isinstance(match_slot, MatchSlot)
assert match_slot._MatchSlot__next_match_slot is None

# Set Up Match Slots
players: List[Player] = Player.set_players(20)
match_slot: MatchSlot = MatchSlot(players)
players: List[Player] = Player.set_players(20)
match_slot.set_up_match_slots(1)
for i in range(1, 20):
    match_slot = match_slot._MatchSlot__next_match_slot
    assert isinstance(match_slot, MatchSlot)
assert match_slot._MatchSlot__next_match_slot is None

#Close Loop of Match Slots
players: List[Player] = Player.set_players(20)
match_slot: MatchSlot = MatchSlot(players)
first_slot: MatchSlot = match_slot
players_close: List[Player] = Player.set_players(10)
match_slot.set_up_match_slots(1)
first_slot.closeLoop()
for i in range(1, 30):
    match_slot = match_slot._MatchSlot__next_match_slot
    assert isinstance(match_slot, MatchSlot)

#Place players