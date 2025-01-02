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
        print("----------------")
        slot_numbers: List[int] = [1, 2, 3, 4]
        occupied_slots: List[Slot] = self.__determine_occupied_slots()
        for slot in occupied_slots:
            # print(self.__determine_slot_position_in_match(slot))
            slot_numbers.remove(self.__determine_slot_position_in_match(slot))
        # print(f"Huidige slotnummer is: {self.__slot.number} met positie {self.__determine_slot_position_in_match(slot)} in wedstrijd")
        # print(f"Kiesbare posities in wedstrijd zijn: {slot_numbers}")
        ophoger: int = 0
        if len(slot_numbers) == 0:
            slot_numbers = [1, 2, 3, 4]
            ophoger = 4
            ## En hier ook het volgende slot in de volgende WEDSTRIJD stoppen. Niet dezelfde!
            ## En ook nog inbouwen
        picked_slot: Slot = random.choice(slot_numbers)
        # print(f"Verkozen positie in wedstrijd is: {picked_slot}")
        next_slot_number: int = ((self.__slot.match - 1)*4) + picked_slot + ophoger
        # print(f"Wat overeen komt met slotnummer: {next_slot_number}")
        return next_slot_number
    
    def __determine_slot_position_in_match(self, slot: Slot) -> int:
        position: int = slot.number % 4
        if position == 0: position = 4
        return position


    def __empty_slots_in_match(self) -> int:
        return 4 - self.__slot.number % 4
    
    def __determine_occupied_slots(self) -> List[Slot]:
        return self.__slot.determine_occupied_slots_in_match()        