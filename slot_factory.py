from __future__ import annotations
from slot import Slot
from player import Player
from team import Team
from position import Position
from result import Result
from typing import List
import math

class SlotFactory:
    
    def __init__(self, slot: Slot):
        self.__slot = slot
        self.__occupied_slots: List[Slot] = []
    
    def choose_next_slot(self) -> int:
        self.__determine_occupied_slots()
        return self.__empty_slots_in_match()
    
    def __empty_slots_in_match(self) -> int:
        return 4 - self.__slot.number % 4
    
    def __determine_occupied_slots(self):
        self.__occupied_slots = self.__slot.determine_occupied_slots_in_match()
        print(len(self.__occupied_slots))
        