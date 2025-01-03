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
        if len(occupied_slots) < 4:
            open_slot_nrs: List[int] = [num + base_nr for num in [1, 2, 3, 4]]
            for slot in occupied_slots:
                open_slot_nrs.remove(slot.number)
        else:
            base_nr += 4
            open_slot_nrs: List[int] = [num + base_nr for num in [1, 2, 3, 4]]
        return open_slot_nrs