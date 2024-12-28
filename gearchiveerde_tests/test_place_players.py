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

# Player Get Players
# Check of players initieel [] is
assert Player._Player__players is None
# Check of de 2e keer get_players aanroepen zelfde resultaat geeft als 1e keer
Player.set_players(30)
players1: List[Player] = Player.get_players()
Player.set_players(30)
players2: List[Player] = Player.get_players()
assert players1 == players2
assert Player.get_player_with_rank(7, Position.ATTACKER).get_rank(Position.ATTACKER) == 7

# Place attackers nieuw
Player.set_players(30)
players: List[Player] = Player.get_players()
match_slot: MatchSlot = MatchSlot()
match_slot.set_up_match_slots(1)
match_slot.closeLoop()
for i in range(len(players)*2):
    print(f"Match slot {match_slot._MatchSlot__slot_number} heeft position {match_slot._MatchSlot__position}")
    match_slot = match_slot._MatchSlot__next_match_slot
assert match_slot.place_players()
for i in range(len(players)*2):
    assert isinstance(match_slot._MatchSlot__player, Player)
    # print(f"Match slot {match_slot._MatchSlot__slot_number} is speler geplaatst met {match_slot._MatchSlot__position} rank {match_slot._MatchSlot__player.get_rank(match_slot._MatchSlot__position)}")
    match_slot = match_slot._MatchSlot__next_match_slot

# __set_match
match_slot: MatchSlot = MatchSlot()
match_slot._MatchSlot__set_match(1); assert match_slot._MatchSlot__match == 1
match_slot._MatchSlot__set_match(2); assert match_slot._MatchSlot__match == 1
match_slot._MatchSlot__set_match(3); assert match_slot._MatchSlot__match == 1
match_slot._MatchSlot__set_match(4); assert match_slot._MatchSlot__match == 1
match_slot._MatchSlot__set_match(5); assert match_slot._MatchSlot__match == 2
match_slot._MatchSlot__set_match(6); assert match_slot._MatchSlot__match == 2
match_slot._MatchSlot__set_match(7); assert match_slot._MatchSlot__match == 2
match_slot._MatchSlot__set_match(8); assert match_slot._MatchSlot__match == 2
match_slot._MatchSlot__set_match(15); assert match_slot._MatchSlot__match == 4
match_slot._MatchSlot__set_match(21); assert match_slot._MatchSlot__match == 6
match_slot._MatchSlot__set_match(35); assert match_slot._MatchSlot__match == 9
match_slot._MatchSlot__set_match(40); assert match_slot._MatchSlot__match == 10

# __set_team
match_slot: MatchSlot = MatchSlot()
match_slot._MatchSlot__set_team(1); assert match_slot._MatchSlot__team == Team.A
match_slot._MatchSlot__set_team(2); assert match_slot._MatchSlot__team == Team.A
match_slot._MatchSlot__set_team(3); assert match_slot._MatchSlot__team == Team.B
match_slot._MatchSlot__set_team(4); assert match_slot._MatchSlot__team == Team.B
match_slot._MatchSlot__set_team(5); assert match_slot._MatchSlot__team == Team.A
match_slot._MatchSlot__set_team(6); assert match_slot._MatchSlot__team == Team.A
match_slot._MatchSlot__set_team(7); assert match_slot._MatchSlot__team == Team.B
match_slot._MatchSlot__set_team(8); assert match_slot._MatchSlot__team == Team.B
match_slot._MatchSlot__set_team(15); assert match_slot._MatchSlot__team == Team.B
match_slot._MatchSlot__set_team(21); assert match_slot._MatchSlot__team == Team.A
match_slot._MatchSlot__set_team(35); assert match_slot._MatchSlot__team == Team.B
match_slot._MatchSlot__set_team(40); assert match_slot._MatchSlot__team == Team.B

# __set_position
match_slot: MatchSlot = MatchSlot()
match_slot._MatchSlot__set_position(1); assert match_slot._MatchSlot__position == Position.ATTACKER
match_slot._MatchSlot__set_position(2); assert match_slot._MatchSlot__position == Position.DEFENDER
match_slot._MatchSlot__set_position(3); assert match_slot._MatchSlot__position == Position.ATTACKER
match_slot._MatchSlot__set_position(4); assert match_slot._MatchSlot__position == Position.DEFENDER
match_slot._MatchSlot__set_position(5); assert match_slot._MatchSlot__position == Position.ATTACKER
match_slot._MatchSlot__set_position(6); assert match_slot._MatchSlot__position == Position.DEFENDER
match_slot._MatchSlot__set_position(7); assert match_slot._MatchSlot__position == Position.ATTACKER
match_slot._MatchSlot__set_position(8); assert match_slot._MatchSlot__position == Position.DEFENDER
match_slot._MatchSlot__set_position(15); assert match_slot._MatchSlot__position == Position.ATTACKER
match_slot._MatchSlot__set_position(21); assert match_slot._MatchSlot__position == Position.ATTACKER
match_slot._MatchSlot__set_position(35); assert match_slot._MatchSlot__position == Position.ATTACKER
match_slot._MatchSlot__set_position(40); assert match_slot._MatchSlot__position == Position.DEFENDER

# # Place attackers nieuw
# players: List[Player] = Player.get_players(40)
# match_slot: MatchSlot = MatchSlot(players)
# match_slot.set_up_match_slots(1)
# match_slot.closeLoop()
# # assert match_slot.place_players()
# assert match_slot._MatchSlot__place_players_at_position(Position.ATTACKER)
# for i in range(len(players)):
#     assert isinstance(match_slot._MatchSlot__player, Player)
#     print(f"Match slot {match_slot._MatchSlot__slot_number} is speler geplaatst met attacker rank {match_slot._MatchSlot__player.get_rank(Position.ATTACKER)} en defender rank {match_slot._MatchSlot__player.get_rank(Position.DEFENDER)}")
#     match_slot = match_slot._MatchSlot__next_match_slot
# assert match_slot._MatchSlot__place_players_at_position(Position.DEFENDER)
# for i in range(len(players), len(players)*2):
#     assert isinstance(match_slot._MatchSlot__player, Player)
#     print(f"Match slot {match_slot._MatchSlot__slot_number} is speler geplaatst met defender rank {match_slot._MatchSlot__player.get_rank(Position.DEFENDER)} en attacker rank {match_slot._MatchSlot__player.get_rank(Position.ATTACKER)}")
#     match_slot = match_slot._MatchSlot__next_match_slot


# # # Position correct after seting_up_match_slots
# # players: List[Player] = Player.get_players(10)
# # match_slot: MatchSlot = MatchSlot(players)
# # match_slot.set_up_match_slots(1)
# # match_slot.closeLoop()
# # for i in range(len(players) * 2):
# #     expected_position: Position = Position.DEFENDER
# #     if (i < len(players)):
# #         expected_position = Position.ATTACKER
# #     assert match_slot._MatchSlot__position == expected_position
# #     match_slot = match_slot._MatchSlot__next_match_slot

# # # Team correct after seting_up_match_slots
# # players: List[Player] = Player.get_players(10)
# # match_slot: MatchSlot = MatchSlot(players)
# # match_slot.set_up_match_slots(1)
# # match_slot.closeLoop()
# # for i in range(len(players) * 2):
# #     if i % 2 == 0:
# #         assert match_slot._MatchSlot__team == Team.A
# #     else:
# #         assert match_slot._MatchSlot__team == Team.B
# #     match_slot = match_slot._MatchSlot__next_match_slot

# # # Match correct after seting_up_match_slots
# # players: List[Player] = Player.get_players(10)
# # match_slot: MatchSlot = MatchSlot(players)
# # match_slot.set_up_match_slots(1)
# # match_slot.closeLoop()
# # for i in range(len(players) * 2):
# #     assert (match_slot._MatchSlot__match == math.ceil((i + 1)/2)) or (match_slot._MatchSlot__match == math.ceil((i + 1)/2) - (len(players) / 2))
# #     match_slot = match_slot._MatchSlot__next_match_slot
    

# # # player_not_none
# # players: List[Player] = Player.get_players(8)
# # match_slot: MatchSlot = MatchSlot(players)
# # match_slot.set_up_match_slots(1)
# # match_slot.closeLoop()
# # assert not match_slot._MatchSlot__player_not_none(match_slot)
# # match_slot._MatchSlot__player = players[0]
# # assert match_slot._MatchSlot__player_not_none(match_slot)
# # assert not match_slot._MatchSlot__player_not_none(match_slot._MatchSlot__next_match_slot)
# # match_slot._MatchSlot__next_match_slot._MatchSlot__player = match_slot._MatchSlot__player = players[1]
# # assert match_slot._MatchSlot__player_not_none(match_slot._MatchSlot__next_match_slot)


# # # __player_next_match_slot_same_as_first
# # players: List[Player] = Player.get_players(8)
# # match_slot: MatchSlot = MatchSlot(players)
# # match_slot.set_up_match_slots(1)
# # match_slot.closeLoop()
# # assert not match_slot._MatchSlot__player_next_match_slot_same_as_first(match_slot)
# # match_slot._MatchSlot__player = players[0]
# # match_slot._MatchSlot__next_match_slot._MatchSlot__player = players[0]
# # assert match_slot._MatchSlot__player_next_match_slot_same_as_first(match_slot)
# # assert not match_slot._MatchSlot__next_match_slot._MatchSlot__player_next_match_slot_same_as_first(match_slot)
# # match_slot._MatchSlot__next_match_slot._MatchSlot__next_match_slot._MatchSlot__player = players[0]
# # assert match_slot._MatchSlot__next_match_slot._MatchSlot__player_next_match_slot_same_as_first(match_slot)

# # #__position_next_match_slot_same_as_first
# # players: List[Player] = Player.get_players(4)
# # match_slot: MatchSlot = MatchSlot(players)
# # match_slot.set_up_match_slots(1)
# # match_slot.closeLoop()
# # first_match_slot: MatchSlot = match_slot

# # # __find_player_at_rank(self, rank: int) -> Player:
# # players: List[Player] = Player.get_players(4)
# # match_slot: MatchSlot = MatchSlot(players)
# # match_slot.set_up_match_slots(1)
# # match_slot.closeLoop()
# # attackerRanks: List[int] = list(range(1, len(players) + 1))
# # random.shuffle(attackerRanks)
# # defenderRanks: List[int] = list(range(1, len(players) + 1))
# # random.shuffle(defenderRanks)
# # for i in range(len(players)):
# #     players[i].set_rank(Position.ATTACKER, attackerRanks[i])
# #     players[i].set_rank(Position.DEFENDER, defenderRanks[i])
# # for i in range(len(players)):
# #     verdediger: Player = match_slot._MatchSlot__find_player_at_rank(i, Position.DEFENDER)
# #     assert isinstance(verdediger, Player)
# #     assert verdediger.get_rank(Position.DEFENDER) == i+1
# #     aanvaller: Player = match_slot._MatchSlot__find_player_at_rank(i, Position.ATTACKER)
# #     assert isinstance(aanvaller, Player)
# #     assert aanvaller.get_rank(Position.ATTACKER) == i+1

# # Place Attackers
# players: List[Player] = Player.get_players(40)
# match_slot: MatchSlot = MatchSlot(players)
# first_match_slot: MatchSlot = match_slot
# match_slot.set_up_match_slots(1)
# match_slot.closeLoop()
# for i in range(len(players)):
#     assert match_slot._MatchSlot__player is None
#     match_slot = match_slot._MatchSlot__next_match_slot
# match_slot = first_match_slot
# assert match_slot.place_players()
# for i in range(len(players)):
#     assert isinstance(match_slot._MatchSlot__player, Player)
#     print(f"Match slot {match_slot._MatchSlot__slot_number} is speler geplaatst met attacker rank {match_slot._MatchSlot__player.get_rank(Position.ATTACKER)} en defender rank {match_slot._MatchSlot__player.get_rank(Position.DEFENDER)}")
#     match_slot = match_slot._MatchSlot__next_match_slot
# # for i in range(len(players), len(players)*2):
# #     assert isinstance(match_slot._MatchSlot__player, Player)
# #     print(f"Match slot {match_slot._MatchSlot__slot_number} is speler geplaatst met defender rank {match_slot._MatchSlot__player.get_rank(Position.DEFENDER)} en attacker rank {match_slot._MatchSlot__player.get_rank(Position.ATTACKER)}")
# #     match_slot = match_slot._MatchSlot__next_match_slot

# # Place attackers nieuw
# players: List[Player] = Player.get_players(40)
# match_slot: MatchSlot = MatchSlot(players)
# assert match_slot._MatchSlot__place_attackers()
# # assert match_slot._MatchSlot__place_attackers(1)
# # assert match_slot._MatchSlot__place_attackers(40)
# # assert not match_slot._MatchSlot__place_attackers(41)
# # assert not match_slot._MatchSlot__place_attackers(3000)


# # determine end slot
# players: List[Player] = Player.get_players(40)
# match_slot: MatchSlot = MatchSlot(players)
# match_slot._MatchSlot__position = Position.ATTACKER
# assert match_slot._MatchSlot__determine_end_slot() == 40
# match_slot._MatchSlot__position = Position.DEFENDER
# assert match_slot._MatchSlot__determine_end_slot() == 80

# # done placing
# players: List[Player] = Player.get_players(40)
# match_slot: MatchSlot = MatchSlot(players)
# match_slot._MatchSlot__position = Position.ATTACKER
# match_slot._MatchSlot__slot_number = 1
# assert not match_slot._MatchSlot__done_placing()
# match_slot._MatchSlot__slot_number = 39
# assert not match_slot._MatchSlot__done_placing()
# match_slot._MatchSlot__slot_number = 40
# assert match_slot._MatchSlot__done_placing()

# match_slot._MatchSlot__position = Position.DEFENDER
# match_slot._MatchSlot__slot_number = 1
# assert not match_slot._MatchSlot__done_placing()
# match_slot._MatchSlot__slot_number = 39
# assert not match_slot._MatchSlot__done_placing()
# match_slot._MatchSlot__slot_number = 40
# assert not match_slot._MatchSlot__done_placing()
# match_slot._MatchSlot__slot_number = 79
# assert not match_slot._MatchSlot__done_placing()
# match_slot._MatchSlot__slot_number = 80
# assert match_slot._MatchSlot__done_placing()


# # print(f"Checking MatchSlot: {match_slot._MatchSlot__slot_number}")
# # print(f"Position of current MatchSlot with number {match_slot._MatchSlot__slot_number} is: {match_slot._MatchSlot__position}")
# # print(f"Position of next MatchSlot with number {match_slot._MatchSlot__next_match_slot._MatchSlot__slot_number} is: {match_slot._MatchSlot__next_match_slot._MatchSlot__position}")
# # print(f"Position of first MatchSlot with number {first_match_slot._MatchSlot__slot_number} is: {first_match_slot._MatchSlot__position}")
# # print("")
# # assert match_slot._MatchSlot__position_next_match_slot_same_as_first(match_slot)

# # match_slot = match_slot._MatchSlot__next_match_slot
# # print(f"Checking MatchSlot: {match_slot._MatchSlot__slot_number}")
# # print(f"Position of current MatchSlot with number {match_slot._MatchSlot__slot_number} is: {match_slot._MatchSlot__position}")
# # print(f"Position of next MatchSlot with number {match_slot._MatchSlot__next_match_slot._MatchSlot__slot_number} is: {match_slot._MatchSlot__next_match_slot._MatchSlot__position}")
# # print(f"Position of first MatchSlot with number {first_match_slot._MatchSlot__slot_number} is: {first_match_slot._MatchSlot__position}")
# # print("")
# # assert not match_slot._MatchSlot__position_next_match_slot_same_as_first(first_match_slot)

# # match_slot = match_slot._MatchSlot__next_match_slot
# # print(f"Checking MatchSlot: {match_slot._MatchSlot__slot_number}")
# # print(f"Checking MatchSlot: {match_slot._MatchSlot__slot_number}")
# # print(f"Position of current MatchSlot with number {match_slot._MatchSlot__slot_number} is: {match_slot._MatchSlot__position}")
# # print(f"Position of next MatchSlot with number {match_slot._MatchSlot__next_match_slot._MatchSlot__slot_number} is: {match_slot._MatchSlot__next_match_slot._MatchSlot__position}")
# # print(f"Position of first MatchSlot with number {first_match_slot._MatchSlot__slot_number} is: {first_match_slot._MatchSlot__position}")
# # print("")
# # assert not match_slot._MatchSlot__position_next_match_slot_same_as_first(first_match_slot)

# # match_slot = match_slot._MatchSlot__next_match_slot
# # print(f"Checking MatchSlot: {match_slot._MatchSlot__slot_number}")
# # print(f"Checking MatchSlot: {match_slot._MatchSlot__slot_number}")
# # print(f"Position of current MatchSlot with number {match_slot._MatchSlot__slot_number} is: {match_slot._MatchSlot__position}")
# # print(f"Position of next MatchSlot with number {match_slot._MatchSlot__next_match_slot._MatchSlot__slot_number} is: {match_slot._MatchSlot__next_match_slot._MatchSlot__position}")
# # print(f"Position of first MatchSlot with number {first_match_slot._MatchSlot__slot_number} is: {first_match_slot._MatchSlot__position}")
# # print("")
# # assert match_slot._MatchSlot__position_next_match_slot_same_as_first(first_match_slot)

# # match_slot = match_slot._MatchSlot__next_match_slot
# # print(f"Checking MatchSlot: {match_slot._MatchSlot__slot_number}")
# # print(f"Position of current MatchSlot with number {match_slot._MatchSlot__slot_number} is: {match_slot._MatchSlot__position}")
# # print(f"Position of next MatchSlot with number {match_slot._MatchSlot__next_match_slot._MatchSlot__slot_number} is: {match_slot._MatchSlot__next_match_slot._MatchSlot__position}")
# # print(f"Position of first MatchSlot with number {first_match_slot._MatchSlot__slot_number} is: {first_match_slot._MatchSlot__position}")
# # assert match_slot._MatchSlot__position_next_match_slot_same_as_first(first_match_slot)

# # # Position correct after seting_up_match_slots
# # players: List[Player] = Player.get_players(20)
# # match_slot: MatchSlot = MatchSlot(players)
# # match_slot.set_up_match_slots(1)
# # match_slot.closeLoop()
# # assert match_slot._MatchSlot__position == Position.ATTACKER
# # for i in range(len(players)):
# #     print(match_slot._MatchSlot__position)
# #     match_slot = match_slot._MatchSlot__next_match_slot

# # # __attempt_placement
