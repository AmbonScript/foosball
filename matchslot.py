from __future__ import annotations
from player import Player
from team import Team
from position import Position
from result import Result
from typing import List
import math
import random

class MatchSlot:
    __historical_match_slots: List[MatchSlot] = []

    def __init__(self):
        self.__round: int = None
        self.__match: int = None
        self.__team: Team = None
        self.__position: Position = None
        self.__next_match_slot: MatchSlot = None
        self.__player: Player = None
        self.__result: Result = None
        self.__slot_number: int = None
    
    def set_up_match_slots(self, round: int, slot_number: int = 1) -> None:
        self.__slot_number = slot_number
        self.__round = round
        self.__set_match(slot_number)
        self.__set_team(slot_number)
        self.__set_position(slot_number)
        self.__set_next_match_slot(slot_number)
    
    def closeLoop(self, first_match_slot: MatchSlot = None) -> None:
        if first_match_slot is None:
            first_match_slot = self
        if self.__next_match_slot == None:
            self.__next_match_slot = first_match_slot
        else:
            self.__next_match_slot.closeLoop(first_match_slot)
        
    def place_players(self) -> bool:
        first_batch_placed: bool = self.__do_placements()
        return first_batch_placed

    def __do_placements(self, rank: int = None) -> bool:
        if self.__player is not None: return self.__next_match_slot.__do_placements()
        if rank is None: rank = 1
        # print(f"Bezig speler met {self.__position}-rank {rank} te plaatsen in match slot {self.__slot_number}")
        if rank > len(Player.get_players()): return False
        player: Player = Player.get_player_with_rank(rank, self.__position)
        if self.__can_place(player): self.__player = player
        else: self.__player = None; return self.__do_placements(rank + 1)
        if self.__done_placing(): return True
        else:
            if self.__next_match_slot.__do_placements(): return True
            else: self.__player = None; self.__do_placements(rank + 1)
        
    def __can_place(self, player:Player, beginning_slot: MatchSlot = None):
        if beginning_slot == None:
            beginning_slot = self
        next_player_same: bool = self.__player_next_slot_same(player)
        next_position_same: bool = self.__position_next_slot_same(beginning_slot)
        next_match_same: bool = self.__match_next_slot_same(beginning_slot)
        next_match_slot_same: bool = self.__next_match_slot == beginning_slot
        if next_player_same and (next_position_same or next_match_same):
            return False
        else:
            if next_match_slot_same:
                return True
            else:
                return self.__next_match_slot.__can_place(player, beginning_slot)

    def __player_next_slot_same(self, player: Player):
        if self.__next_match_slot.__player is None:
            return False
        else:
            return self.__next_match_slot.__player == player
    
    def __position_next_slot_same(self, beginning_slot: MatchSlot):
        position = beginning_slot.__position
        # print(f"    In __position_next_match_slot_same_as_first and position is: {position}")
        return self.__next_match_slot.__position == position

    def __match_next_slot_same(self, beginning_slot: MatchSlot):
        match = beginning_slot.__match
        # print(f"    In __match_next_match_slot_same_as_first and match is: {match}")
        return self.__next_match_slot.__match == match
        
    def __done_placing(self):
        end_slot: int = self.__determine_end_slot()
        if self.__slot_number == end_slot:
            is_done: bool =  True
        else:
            is_done: bool =  False
        # print(f"    done_placing is: {is_done}")
        return is_done
    
    def __determine_end_slot(self) -> int:
        return len(Player.get_players()) * 2

    def __set_match(self, slot_number: int) -> None:
        self.__match = math.ceil(slot_number / 4)
    
    def __set_team(self, slot_number: int) -> None:
        if (slot_number+1) % 4 > 1:
            self.__team = Team.A
        else:
            self.__team = Team.B
    
    def __set_position(self, slot_number: int) -> None:
        if slot_number % 2 == 1:
            self.__position = Position.ATTACKER
        else:
            self.__position = Position.DEFENDER
    
    def __set_next_match_slot(self, slot_number: int) -> None:
        number_of_players: int = len(Player.get_players())
        print(f"{(len(Player.get_players()) % 2)}")
        if slot_number < number_of_players * 2:
            self.__next_match_slot = MatchSlot()
            self.__next_match_slot.set_up_match_slots(self.__round, slot_number + 1)