from player import Player
from round import Round

class Competition:
    def __init__(self, number_of_players: int):
        Player.set_players(number_of_players)
        self.__round: Round = None
    
    def play_round(self) -> None:
        self.__createNewRound()
        self.__round.play()

    def __createNewRound(self) -> None:
        if self.__round is None:
            self.__round = Round(1)
        else:
            self.__round = Round(self.__round.get_round_number() + 1)