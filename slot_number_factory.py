from __future__ import annotations
from slot import Slot
from player import Player
from team import Team
from position import Position
from result import Result
from typing import List
import math
import random
import copy

class SlotNumberFactory:
    __slot: Slot = None

    def get_next_slot_number(slot: Slot) -> int:
        SlotNumberFactory.__slot = None
        SlotNumberFactory.__slot = slot
        base_nr: int = SlotNumberFactory.__get_base_nr()
        occupied_slots: List[Slot] = SlotNumberFactory.__get_occupied_slots()
        open_slot_nrs: List[int] = SlotNumberFactory.__get_open_slot_nrs(base_nr, occupied_slots)
        lowest_placeable_ranks: List[int] = SlotNumberFactory.__get_lowest_placeable_ranks(open_slot_nrs)
        next_slot_nr: int = SlotNumberFactory.__choose_slot_nr(open_slot_nrs, lowest_placeable_ranks)
        return next_slot_nr
    
    def __get_base_nr() -> int:
        return (SlotNumberFactory.__slot.match - 1) * 4
    
    def __get_occupied_slots() -> List[Slot]:
        return SlotNumberFactory.__slot.determine_occupied_slots_in_match()

    def __get_open_slot_nrs(base_nr: int, occupied_slots: List[Slot]) -> List[int]:
        if len(occupied_slots) < 4:
            open_slot_nrs: List[int] = [num + base_nr for num in [1, 2, 3, 4]]
            for slot in occupied_slots:
                open_slot_nrs.remove(slot.number)
        else:
            base_nr += 4
            open_slot_nrs: List[int] = [num + base_nr for num in [1, 2, 3, 4]]
        return open_slot_nrs
    
    def __get_lowest_placeable_ranks(open_slot_nrs: List[int]) -> List[int]:
        lowest_placeable_ranks: List[int] = []
        for slot_nr in open_slot_nrs:
            lowest_placeable_ranks.append(SlotNumberFactory.__find_lowest_placeable_rank(slot_nr))
        return lowest_placeable_ranks

    def __find_lowest_placeable_rank(slot_nr: int) -> int:
        initial_next_slot: Slot = copy.copy(SlotNumberFactory.__slot.next_slot)
        SlotNumberFactory.__slot.next_slot = Slot(slot_nr, SlotNumberFactory.__slot.next_slot)
        lowest_placeable_rank: int = SlotNumberFactory.__try_ranks(SlotNumberFactory.__slot.next_slot)
        SlotNumberFactory.__slot.next_slot = initial_next_slot
        return lowest_placeable_rank
    
    def __try_ranks(slot: Slot) -> int:
        slot.player = None
        for rank in range((Player.get_number_of_players_in_round() + 1)):
            if not slot.can_place(rank): continue
            else: return rank
        return 1000
    
    def __choose_slot_nr(open_slot_nrs: List[int], lowest_placeable_ranks: List[int]) -> int:
        min_value = min(lowest_placeable_ranks)
        min_indices = [i for i, value in enumerate(lowest_placeable_ranks) if value == min_value]
        min_index = random.choice(min_indices)
        return open_slot_nrs[min_index]
