from __future__ import annotations
from position import Position
from typing import List
import random


class Player:
    __players: List[Player] = None
    __current_attacker_bye: int = None
    __current_defender_bye: int = None

    @staticmethod
    def set_players(number_of_players: int) -> None:
        if (Player.__players == None):
            Player.__initialize_players(number_of_players)
    
    @staticmethod
    def __initialize_players(number_of_players: int) -> None:
        Player.__players = []
        for i in range(number_of_players):
            Player.__players.append(Player(i))
        Player.__rank_players_randomly()

    @staticmethod
    def __rank_players_randomly() -> None:
        attackerRanks: List[int] = list(range(1, len(Player.__players) + 1))
        random.shuffle(attackerRanks)
        defenderRanks: List[int] = list(range(1, len(Player.__players) + 1))
        random.shuffle(defenderRanks)

        for i in range(len(Player.__players)):
            Player.__players[i].set_rank(Position.ATTACKER, attackerRanks[i])
            Player.__players[i].set_rank(Position.DEFENDER, defenderRanks[i])
    
    @staticmethod
    def get_player_with_rank(rank: int, position: Position) -> Player:
        return next((player for player in Player.get_players() if player.get_rank(position) == rank), None)
    
    @staticmethod
    def get_players() -> List[Player]:
        return Player.__players
    
    @staticmethod
    def get_number_of_players_in_round():
        if Player.is_bye_necessary(): return len(Player.__players) - 1
        else: return len(Player.__players)

    @staticmethod
    def is_bye_necessary():
        if len(Player.__players) % 2 == 1: return True
        else: return False

    @staticmethod
    def get_bye_for(position: Position):
        if position == Position.ATTACKER: return Player.__current_attacker_bye
        else: return Player.__current_defender_bye
    
    @staticmethod
    def provide_byes() -> None:
        print("In Player.provide_byes()")
        if len(Player.__players) % 2 == 1:
            Player.__provide_byes_for(Position.ATTACKER)
            Player.__provide_byes_for(Position.DEFENDER)
    
    @staticmethod
    def __provide_byes_for(position: Position) -> None:
        if position == Position.ATTACKER: unbyed_players = [player for player in Player.__players if player.__attackerByeReceived == False]
        else: unbyed_players = [player for player in Player.__players if player.__defenderByeReceived == False]
        lowest_ranked_player = max(unbyed_players, key=lambda player: player.get_rank(position))
        if position == Position.ATTACKER: lowest_ranked_player.__attackerByeReceived = True; Player.__current_attacker_bye = lowest_ranked_player.get_rank(Position.ATTACKER)
        else: lowest_ranked_player.__defenderByeReceived = True; Player.__current_defender_bye = lowest_ranked_player.get_rank(Position.DEFENDER)      

    def __init__(self, number: int):
        self.__number: int = number
        self.__attackerRank: int = None
        self.__defenderRank: int = None
        self.__attackerByeReceived: bool = False
        self.__defenderByeReceived: bool = False
        self.__attackerGamesWon: int = 0
        self.__defenderGamesWon: int = 0
    
    def get_number(self) -> int:
        return self.__number

    def set_rank(self, position: Position, rank: int) -> None:
        if position == Position.ATTACKER:
            self.__attackerRank = rank
        else:
            self.__defenderRank = rank
    
    def get_rank(self, position: Position) -> int:
        if position == Position.ATTACKER:
            return self.__attackerRank
        else:
            return self.__defenderRank
    
    def receive_bye(self, position: Position) -> bool:
        if position == Position.ATTACKER:
            if self.__attackerByeReceived == False:
                self.__attackerGamesWon = self.__attackerGamesWon + 1;
                self.__attackerByeReceived = True
                return True
        else:
            if self.__defenderByeReceived == False:
                self.__defenderGamesWon = self.__defenderGamesWon + 1;
                self.__defenderByeReceived = True
                return True
        return False
    
    def bye_received(self, position: Position) -> bool:
        if position == Position.ATTACKER:
            return self.__attackerByeReceived
        else:
            return self.__defenderByeReceived