from __future__ import annotations
from slot import Slot
from player import Player
from team import Team
from position import Position
from result import Result
from typing import List
import math
import random

class SlotFactory:
    
    def __init__(self, slot: Slot):
        self.__slot = slot
    
    def choose_next_slot_number(self) -> int:
        base_nr: int = self.__get_base_nr()
        occupied_slots: List[Slot] = self.__get_occupied_slots()
        open_slot_nrs: List[int] = self.__get_open_slot_nrs(base_nr, occupied_slots)
        return random.choice(open_slot_nrs)
    
    def __get_base_nr(self) -> int:
        return (self.__slot.match - 1) * 4
    
    def __get_occupied_slots(self) -> List[Slot]:
        return self.__slot.determine_occupied_slots_in_match()

    def __get_open_slot_nrs(self, base_nr: int, occupied_slots: List[Slot]) -> List[int]:
        if len(occupied_slots) == 0:
            base_nr += 4
        open_slot_nrs: List[int] = [num + base_nr for num in [1, 2, 3, 4]]
        for slot in occupied_slots:
            open_slot_nrs.remove(slot.number)
        return open_slot_nrs
        

    ## -------------------------------------------- ##
    ## -------------------------------------------- ##
    
            # base_nr
        # occupied_slots
        # open_slots
        # random choice

        # determine occupied slots (method_1)
            # if 1, 2, or 3
                # -> determine all slot-numbers in same match as self (method_2)
                # -> determine open slots in same match (also method_2)
            # if 4
                # -> determine all slot-numbers in 1-higher match as self (method_3)
        # -> pick a random one  (method_4)

        # Daarna -> echt slot teruggeven!

    ## -------------------------------------------- ##
    ## -------------------------------------------- ##

    # def choose_next_slot_number_oud(self) -> int:
    #     self.__determine_open_slots_numbers()
    #     slot_numbers: List[int] = [1, 2, 3, 4]
    #     occupied_slots: List[Slot] = self.__determine_occupied_slots()
    #     for slot in occupied_slots:
    #         slot_numbers.remove(self.__determine_slot_position_in_match(slot))
    #     next_match_increaser: int = 0
    #     if len(slot_numbers) == 0:
    #         slot_numbers = [1, 2, 3, 4]
    #         next_match_increaser = 4
    #     picked_slot: Slot = random.choice(slot_numbers)
    #     return ((self.__slot.match - 1)*4) + picked_slot + next_match_increaser
    
    # def choose_next_slot_number2(self) -> int:
    #     open_slot_numbers: List[int] = self.__determine_open_slots_numbers
    #     next_slot: int = self.__choose_slot_number(open_slot_numbers)
    
    # def __determine_slot_position_in_match(self, slot: Slot) -> int:
    #     position: int = slot.number % 4
    #     if position == 0: position = 4
    #     return position
    
    # def __determine_occupied_slots(self) -> List[Slot]:
    #     return self.__slot.determine_occupied_slots_in_match()

    # def __determine_open_slots_numbers(self) -> List[int]:
    #     open_slot_numbers: List[int] = [num + self.__determine_base_nr() for num in [1, 2, 3, 4]]
    #     occupied_slots: List[Slot] = self.__slot.determine_occupied_slots_in_match()
    #     for slot in occupied_slots:
    #         open_slot_numbers.remove(self.__determine_slot_position_in_match(slot))
    #     return open_slot_numbers

    # def __choose_slot_number(self, open_slot_numbers: List[int]) -> int:
    #     base_nr: int = self.__determine_base_nr()
    #     if len(open_slot_numbers) == 0:
    #         base_nr += 4


        # determine occupied slots (method_1)
            # if 1, 2, or 3
                # -> determine all slot-numbers in same match as self (method_2)
                # -> determine open slots in same match (also method_2)
            # if 4
                # -> determine all slot-numbers in 1-higher match as self 
        # -> pick a random one  (method_4)
            


        # Determine the possible slot numbers in the match
            # Base number + [1, 2, 3, 4]
        # Remove the ones that are already occupied