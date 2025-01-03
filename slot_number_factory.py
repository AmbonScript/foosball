from __future__ import annotations
from slot import Slot
from player import Player
from team import Team
from position import Position
from result import Result
from typing import List
import math
import random

class SlotNumberFactory:
    __slot: Slot = None

    @staticmethod
    def get_next_slot_number(slot: Slot) -> int:
        SlotNumberFactory.__slot = slot
        base_nr: int = SlotNumberFactory.__get_base_nr()
        occupied_slots: List[Slot] = SlotNumberFactory.__get_occupied_slots()
        open_slot_nrs: List[int] = SlotNumberFactory.__get_open_slot_nrs(base_nr, occupied_slots)
        return SlotNumberFactory.__choose_slot_nr(open_slot_nrs)
    
    @staticmethod
    def __get_base_nr() -> int:
        return (SlotNumberFactory.__slot.match - 1) * 4
    
    @staticmethod
    def __get_occupied_slots() -> List[Slot]:
        return SlotNumberFactory.__slot.determine_occupied_slots_in_match()

    @staticmethod
    def __get_open_slot_nrs(base_nr: int, occupied_slots: List[Slot]) -> List[int]:
        if len(occupied_slots) < 4:
            open_slot_nrs: List[int] = [num + base_nr for num in [1, 2, 3, 4]]
            for slot in occupied_slots:
                open_slot_nrs.remove(slot.number)
        else:
            base_nr += 4
            open_slot_nrs: List[int] = [num + base_nr for num in [1, 2, 3, 4]]
        return open_slot_nrs
    
    @staticmethod
    def __choose_slot_nr(open_slot_nrs: List[int]):
        return random.choice(open_slot_nrs)