from player import Player
from result import Result
from slot import Slot
from communicator import Communicator

class Round:
    def __init__(self, number: int):
        Communicator.start_round(number)
        self.__number: int = number
        self.__match_slot: Slot = Slot()
    
    def get_round_number(self) -> int:
        return self.__number

    def play(self) -> None:
        Player.provide_byes()
        self.__set_up_matches()
        self.__play_matches()
        self.__process_results()
    
    def __set_up_matches(self):
        self.__match_slot.zieke_recursieve_methode_waarin_spelers_op_onnavolgbare_en_wellicht_optimale_manier_geplaatst_worden()
    
    def __play_matches(self) -> None:
        if Communicator.choose_manual_results():
            self.__manual_input_results()
        else:
            Result.add_round_results(int(Player.get_number_of_players_in_round() / 2))
        self.__match_slot.store()
    
    def __manual_input_results(self) -> None:
        for match_nr in range(int(Player.get_number_of_players_in_round() / 2)):
            Communicator.display_matches_and_get_results(self.__match_slot, match_nr)
    
    def __process_results(self) -> None:
        self.__match_slot.process_results(self.get_round_number())
        Player.rank_players()
        Communicator.show_rankings(self.__number)
