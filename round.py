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
        # Loop over alle MatchSlots -> in methode van MatchSlot-klasse
            # Per MatchSlot, geef aan de Speler uit het MatchSlot door:
                # Op welke positie hij/zij speelde
                # In welke team hij/zij speelde
                # Welke spelers tegenstanders waren -> bewaar dit in een List[Player] instance variabele
                # Welk team gewonnen heeft -> als gewonnen, ken een gewonnen wedstrijd toe 
                # Wat het doelverschil was -> en pas het totaal aan
        # In Player -> Bepaal het aantal resistance points
        # In Player -> Bepaal de ranking opnieuw
