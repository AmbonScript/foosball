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
    
    def choose_next_slot(self) -> int:
        return self.__empty_slots_in_match()
    
    def __empty_slots_in_match(self) -> int:
        return self.__slot.number
