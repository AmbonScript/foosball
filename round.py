from player import Player
from position import Position
from matchslot import MatchSlot
from typing import List
import copy

class Round:
    def __init__(self, number: int):
        self.__number: int = number
        self.__match_slot: MatchSlot = MatchSlot()
    
    def get_round_number(self) -> int:
        return self.__number

    def play_round(self) -> None:
        Player.provide_byes()
        self.__set_up_matches()
        self.__match_slot.play_matches()
    
    def __set_up_matches(self):
        self.__match_slot.set_up_match_slots(self.get_round_number())
        self.__match_slot.closeLoop()
        self.__match_slot.place_players()
