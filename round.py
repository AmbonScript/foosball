from player import Player
from result import Result
from matchslot import MatchSlot

class Round:
    def __init__(self, number: int):
        self.__number: int = number
        self.__match_slot: MatchSlot = MatchSlot()
    
    def get_round_number(self) -> int:
        return self.__number

    def play(self) -> None:
        Player.provide_byes()
        self.__set_up_matches()
        self.__play_matches()
        self.__process_results()
    
    def __set_up_matches(self):
        self.__match_slot.set_up_match_slots(self.get_round_number())
        self.__match_slot.closeLoop()
        self.__match_slot.place_players()
    
    def __play_matches(self) -> None:
        Result.add_round_results(int(Player.get_number_of_players_in_round() / 2))
        self.__match_slot.store()
        # Player.process_round_results(self.get_round_number())
    
    def __process_results(self) -> None:
        print(f"In Round#process_results() voor ronde {self.__number}")
        self.__match_slot.process_results(self.get_round_number())
        Player.rank_players()
