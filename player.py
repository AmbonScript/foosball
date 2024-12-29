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
        return next((player for player in Player.__players if player.get_rank(position) == rank), None)
        
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
        # print("In Player.provide_byes()")
        if len(Player.__players) % 2 == 1:
            Player.__provide_byes_for(Position.ATTACKER)
            Player.__provide_byes_for(Position.DEFENDER)
    
    @staticmethod
    def __provide_byes_for(position: Position) -> None:
        if position == Position.ATTACKER: 
            unbyed_players = [player for player in Player.__players if player.__attacker_bye_received == False]
        else:
            unbyed_players = [player for player in Player.__players if player.__defender_bye_received == False]
        lowest_ranked_player = max(unbyed_players, key=lambda player: player.get_rank(position))
        lowest_ranked_player.__attacker_bye_received = True
        Player.__current_attacker_bye = lowest_ranked_player.get_rank(position)

    @staticmethod
    def process_round_results(round: int) -> None:
        print(f"In Player.process_round_results() voor ronde {round}")
        # Verkrijg het circkeltje van MatchSlot bijbehorend aan de ronde
            # Uit de MatchSlot.get_slots_from_round()
        # Loop over alle MatchSlots -> in methode van MatchSlot-klasse
            # Per MatchSlot, geef aan de Speler uit het MatchSlot door:
                # Op welke positie hij/zij speelde
                # In welke team hij/zij speelde
                # Welke spelers tegenstanders waren -> bewaar dit in een List[Player] instance variabele
                # Welk team gewonnen heeft -> als gewonnen, ken een gewonnen wedstrijd toe 
                # Wat het doelverschil was -> en pas het totaal aan
        # In Player -> Bepaal het aantal resistance points
        # In Player -> Bepaal de ranking opnieuw

    def __init__(self, number: int):
        self.__number: int = number
        self.__attacker_rank: int = None
        self.__defender_rank: int = None
        self.__attacker_games_won: int = 0
        self.__defender_games_won: int = 0
        self.__attacker_resistance_points: int = 0
        self.__defender_resistance_points: int = 0
        self.__attacker_goal_differene: int = 0
        self.__defender_goal_difference: int = 0
        self.__attacker_bye_received: bool = False
        self.__defender_bye_received: bool = False
        
    
    def get_number(self) -> int:
        return self.__number

    def set_rank(self, position: Position, rank: int) -> None:
        if position == Position.ATTACKER:
            self.__attacker_rank = rank
        else:
            self.__defender_rank = rank
    
    def get_rank(self, position: Position) -> int:
        if position == Position.ATTACKER:
            return self.__attacker_rank
        else:
            return self.__defender_rank
    
    def receive_bye(self, position: Position) -> bool:
        if position == Position.ATTACKER:
            if self.__attacker_bye_received == False:
                self.__attacker_games_won = self.__attacker_games_won + 1;
                self.__attacker_bye_received = True
                return True
        else:
            if self.__defender_bye_received == False:
                self.__defender_games_won = self.__defender_games_won + 1;
                self.__defender_bye_received = True
                return True
        return False
    
    def bye_received(self, position: Position) -> bool:
        if position == Position.ATTACKER:
            return self.__attacker_bye_received
        else:
            return self.__defender_bye_received