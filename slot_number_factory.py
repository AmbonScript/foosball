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
    def __choose_slot_nr(open_slot_nrs: List[int]) -> int:
        lowest_placeable_ranks: List[int] = []
        for slot_nr in open_slot_nrs:
            lowest_placeable_ranks.append(SlotNumberFactory.__find_lowest_placeable_rank(slot_nr))
        return random.choice(open_slot_nrs)
    
    @staticmethod
    def __find_lowest_placeable_rank(slot_nr: int) -> int:
        SlotNumberFactory.__slot.next_slot = Slot(slot_nr, SlotNumberFactory.__slot.next_slot)
        lowest_placeable_rank: int = SlotNumberFactory.__try_ranks(SlotNumberFactory.__slot.next_slot)
        return 1
    
    @staticmethod
    def __try_ranks(slot: Slot) -> int:
        slot.player = None
        for rank in range((Player.get_number_of_players_in_round() + 1)):
            if not slot.can_place(rank): continue
            else: return rank
        return 1000
