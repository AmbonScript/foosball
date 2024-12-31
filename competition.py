from player import Player
from round import Round
from typing import List

class Competition:
    def __init__(self, number_of_players: int):
        Player.set_players(number_of_players)
        self.__rounds: List[Round] = None
    
    def play_round(self) -> None:
        self.__createNewRound()
        self.__rounds[(len(self.__rounds) - 1)].play()

    def __createNewRound(self) -> None:
        if self.__rounds is None:
            self.__rounds = []
            self.__rounds.append(Round(1))
        else:
            self.__rounds.append(Round((len(self.__rounds) + 1)))
