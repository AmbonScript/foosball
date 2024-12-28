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
        self.__match_slot.place_players()
    
    def __set_up_matches(self):
        self.__match_slot.set_up_match_slots(self.get_round_number())
        self.__match_slot.closeLoop()

    def __provideByes(self):
        self.__provide_byes_for(Position.ATTACKER)
        self.__provide_byes_for(Position.DEFENDER)
    
    def __provide_byes_for(self, position: Position) -> List[Player]:
        un_byed_players: List[Player] = self.__filter_previously_byed_players(Player.get_players(), position)
        to_bye_player: Player = self.__find_lowest_ranked_player(un_byed_players, position)
        to_bye_player.receive_bye(position)
        active_players = [player for player in Player.get_players() if player != to_bye_player]
        return active_players
    
    def __filter_previously_byed_players(self, players: List[Player], position: Position) -> List[Player]:
        un_byed_players = [player for player in players if player.bye_received(position) == False]
        return un_byed_players # minus de spelers die al eerder een bye hebben gekregen
    
    def __find_lowest_ranked_player(self, players: List[Player], position: Position) -> Player:
        lowest_ranked_player: Player = players[0]
        lowest_rank: int = lowest_ranked_player.get_rank(position)
        for player in players:
            rank: int = player.get_rank(position)
            if rank >= lowest_rank:
                lowest_ranked_player = player
                lowest_rank = rank
        return lowest_ranked_player