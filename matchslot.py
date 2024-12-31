from __future__ import annotations
from player import Player
from team import Team
from position import Position
from result import Result
from typing import List
import math

class MatchSlot:
    __historical_match_slots: List[MatchSlot] = []
    
    @staticmethod
    def get_slots_from_round(round: int) -> MatchSlot:
        item = round - 1
        return MatchSlot.__historical_match_slots[item]

    def __init__(self):
        self.__match: int = None
        self.__team: Team = None
        self.__position: Position = None
        self.__next_slot: MatchSlot = None
        self.__player: Player = None
        self.__number: int = None
    
    def set_up_match_slots(self, slot_number: int = 1) -> None:
        self.__number = slot_number
        self.__set_match(slot_number)
        self.__set_team(slot_number)
        self.__set_position(slot_number)
        self.__set_next_match_slot(slot_number)
    
    def closeLoop(self, first_match_slot: MatchSlot = None) -> None:
        if first_match_slot is None:
            first_match_slot = self
        if self.__next_slot == None:
            self.__next_slot = first_match_slot
        else:
            self.__next_slot.closeLoop(first_match_slot)
        
    def place_players(self) -> bool:
        first_batch_placed: bool = self.__do_placements()
        return first_batch_placed
    
    def store(self) -> None:
        # print(f"Before appending len(MatchSlot.__historical_match_slots) is: {len(MatchSlot.__historical_match_slots)}")
        MatchSlot.__historical_match_slots.append(self)
        # print(f"After appending len(MatchSlot.__historical_match_slots) is: {len(MatchSlot.__historical_match_slots)}")
    
    def process_results(self, round: int, first_match_slot: MatchSlot = None) -> None:
        if first_match_slot is None:
            first_match_slot = self
        # print(f"In MatchSlot#process_results() van slot#{self.__slot_number}")
        winning_team: Team = Result.get_result(round, self.__match).get_winning_team()
        goal_difference: int = Result.get_result(round, self.__match).get_goal_difference()
        attacker_opponent: Player = self.__get_opponent(Position.ATTACKER, self)
        defender_opponent: Player = self.__get_opponent(Position.DEFENDER, self)
        self.__player.process_results(self.__position, self.__team, winning_team, goal_difference, attacker_opponent, defender_opponent)
        if self.__next_slot != first_match_slot:
            self.__next_slot.process_results(round, first_match_slot)

    def __get_opponent(self, position: Position, start_slot: MatchSlot) -> Player:
        match_same: bool = self.__next_slot.__match == start_slot.__match
        team_different: bool = self.__next_slot.__team != start_slot.__team
        position_correct: bool = self.__next_slot.__position == position
        if match_same and team_different and position_correct:
            return self.__next_slot.__player
        else:
            return self.__next_slot.__get_opponent(position, start_slot)

    def __do_placements(self) -> bool:
        for rank in range((Player.get_number_of_players_in_round() + 1)):
            # print(f"Bezig speler met {self.__position}-rank {rank} te plaatsen in match slot {self.__slot_number}")
            if rank == 0: continue
            if rank == Player.has_bye_for(self.__position): continue
            if self.__already_in_same_postion_or_match(Player.get_player_with_rank(rank, self.__position)): continue
            if self.__repeating_configuration(Player.get_player_with_rank(rank, self.__position)): continue
            self.__player = Player.get_player_with_rank(rank, self.__position)
            if self.__done_placing(): return True
            else:
                if self.__next_slot.__do_placements(): return True
        self.__player = None
        return False
        
    def __already_in_same_postion_or_match(self, player:Player, start_slot: MatchSlot = None) -> bool:
        if start_slot == None:
            start_slot = self
        next_player_same: bool = self.__player_next_slot_same(player)
        next_position_same: bool = self.__position_next_slot_same(start_slot)
        next_match_same: bool = self.__match_next_slot_same(start_slot)
        next_match_slot_same: bool = self.__next_slot == start_slot
        if next_player_same and (next_position_same or next_match_same):
            return True
        else:
            if next_match_slot_same:
                return False
            else:
                return self.__next_slot.__already_in_same_postion_or_match(player, start_slot)

    def __repeating_configuration(self, player: Player) -> bool:
        opponent_slots_in_match: List[MatchSlot] = self.__find_opponent_slots_in_match()
        if len(opponent_slots_in_match) == 0: return False
        previous_match_slots: List[MatchSlot] = self.__find_previous_slots_with_player_in_same_position(player)
        # print(f"previous_match_slots of player#{player.get_number()}: {previous_match_slots}")
        previous_opponent_slots: List[List[MatchSlot]] = self.__find_previous_opponent_slots(previous_match_slots)
        # print(f"len(previous_opponent_slots) = {len(previous_opponent_slots)}")
        for opponent_slot in opponent_slots_in_match:
            for i in range(len(previous_match_slots)):
                # print(f"i = {i}")
                previous_slot: MatchSlot = previous_match_slots[i]
                previous_opponent_set: List[MatchSlot] = previous_opponent_slots[i]
                for previous_opponent_slot in previous_opponent_set:
                    if self.__configuration_same(opponent_slot, previous_slot, previous_opponent_slot): return True
        return False
    
    def __configuration_same(self, opponent_slot: MatchSlot, previous_slot: MatchSlot, previous_opponent_slot: MatchSlot) -> bool:
        if opponent_slot.__player == previous_opponent_slot.__player:
            if self.__team == opponent_slot.__team:
                if  previous_slot.__team == previous_opponent_slot.__team:
                    return True
            else:
                if self.__position == opponent_slot.__position:
                    if previous_slot.__position == previous_opponent_slot.__position:
                        return True
                else:
                    if previous_slot.__position != previous_opponent_slot.__position:
                        return True
        return False

    def __find_opponent_slots_in_match(self, other_occupied_slots_in_match: List[MatchSlot] = None, start_slot: MatchSlot = None) -> List[MatchSlot]:
        if other_occupied_slots_in_match is None:
            other_occupied_slots_in_match = []
        if start_slot is None:
            start_slot = self
        if self.__next_slot == start_slot:
            return other_occupied_slots_in_match
        if (self.__next_slot.__match == start_slot.__match) and (self.__next_slot.__player is not None):
            other_occupied_slots_in_match.append(self.__next_slot)
        return self.__next_slot.__find_opponent_slots_in_match(other_occupied_slots_in_match, start_slot)
    
    def __find_previous_slots_with_player_in_same_position(self, player: Player) -> List[MatchSlot]:
        previous_match_nrs_with_player_in_same_position: List[MatchSlot] = []
        for match_slot in MatchSlot.__historical_match_slots:
            match_nr: MatchSlot = match_slot.__find_same_position_match(self.__position, player)
            previous_match_nrs_with_player_in_same_position.append(match_nr)
        return previous_match_nrs_with_player_in_same_position
    
    def __find_same_position_match(self, position: Position, player: Player, start_slot: MatchSlot = None) -> MatchSlot:
        if start_slot is None:
            start_slot = self
        if self.__next_slot == start_slot:
            return None
        if ((position == self.__position) and (player == self.__player)):
            return self
        else:
            return self.__next_slot.__find_same_position_match(position, player, start_slot)

    def __find_previous_opponent_slots(self, previous_match_slots: List[MatchSlot]) -> List[List[MatchSlot]]:
        previous_opponent_slots: List[List[MatchSlot]] = []
        # Zoek in alle vorige rondes
        # Vindt daar de 3 matchslots waarvan:
            # - Het matchnummer overeenkomt met die uit previous_match_slots
            # - Het slot zelf juist niet die ene was waar de speler in stond
            # Doe dit in een aparte-recursieve methode
        for i in range(len(MatchSlot.__historical_match_slots)):
            # print(f"Finding previous opponent slots for slot#{self.__number}")
            player_slot: MatchSlot = previous_match_slots[i]
            if player_slot is None:
                previous_opponent_slots.append(None)
            else:
                round_slots: MatchSlot = MatchSlot.__historical_match_slots[i]
                opponent_slots: List[MatchSlot] = []
                opponent_slots = round_slots.__find_opponent_slots_in_round(player_slot)
                print(f"len(opponent_slots) is: {len(opponent_slots)}")
                previous_opponent_slots.append(opponent_slots)
        # print(f"len()")
        return previous_opponent_slots
    
    def __find_opponent_slots_in_round(self, player_slot: MatchSlot, opponent_slots: List[MatchSlot] = None, start_slot: MatchSlot = None) -> List[MatchSlot]:
        if opponent_slots is None:
            opponent_slots = []
        # print(f"len(opponent_slots) is: {len(opponent_slots)}")
        if start_slot is None:
            start_slot = self
        if ((self.__match == player_slot.__match) and (self != player_slot)):
            opponent_slots.append(self)
        if self.__next_slot == start_slot:
            return opponent_slots
        else:
            return self.__next_slot.__find_opponent_slots_in_round(player_slot, opponent_slots, start_slot)

    def __player_next_slot_same(self, player: Player) -> bool:
        if self.__next_slot.__player is None:
            return False
        else:
            return self.__next_slot.__player == player
    
    def __position_next_slot_same(self, start_slot: MatchSlot) -> bool:
        position = start_slot.__position
        # print(f"    In __position_next_match_slot_same_as_first and position is: {position}")
        return self.__next_slot.__position == position

    def __match_next_slot_same(self, start_slot: MatchSlot) -> bool:
        match = start_slot.__match
        # print(f"    In __match_next_match_slot_same_as_first and match is: {match}")
        return self.__next_slot.__match == match
        
    def __done_placing(self) -> bool:
        end_slot: int = self.__determine_end_slot()
        if self.__number == end_slot:
            is_done: bool =  True
        else:
            is_done: bool =  False
        # print(f"    done_placing is: {is_done}")
        return is_done
    
    def __determine_end_slot(self) -> int:
        return (Player.get_number_of_players_in_round() * 2)

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
        if slot_number < self.__determine_end_slot():
            self.__next_slot = MatchSlot()
            self.__next_slot.set_up_match_slots(slot_number + 1)
        
    def print_slots(self, start_slot: MatchSlot = None) -> None:
        if start_slot is None:
            start_slot = self
        print(f"In slot#{self.__number}. Match = {self.__match}. Team = {self.__team}. Position = {self.__position}. Player = {self.__player.get_number()}")
        if self.__next_slot != start_slot:
            self.__next_slot.print_slots(start_slot)