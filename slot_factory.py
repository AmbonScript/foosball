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
        slot_numbers: List[int] = [1, 2, 3, 4]
        occupied_slots: List[Slot] = self.__determine_occupied_slots()
        for slot in occupied_slots:
            slot_numbers.remove(self.__determine_slot_position_in_match(slot))
        next_match_increaser: int = 0
        if len(slot_numbers) == 0:
            slot_numbers = [1, 2, 3, 4]
            next_match_increaser = 4
        picked_slot: Slot = random.choice(slot_numbers)
        return ((self.__slot.match - 1)*4) + picked_slot + next_match_increaser
    
    def __determine_slot_position_in_match(self, slot: Slot) -> int:
        position: int = slot.number % 4
        if position == 0: position = 4
        return position
    
    def __determine_occupied_slots(self) -> List[Slot]:
        return self.__slot.determine_occupied_slots_in_match()        