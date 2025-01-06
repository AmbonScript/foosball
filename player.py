from __future__ import annotations
from position import Position
from team import Team
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
    def has_bye_for(position: Position) -> int:
        if position == Position.ATTACKER: return Player.__current_attacker_bye
        else: return Player.__current_defender_bye
    
    @staticmethod
    def provide_byes() -> None:
        if len(Player.__players) % 2 == 1:
            Player.__provide_byes_for(Position.ATTACKER)
            Player.__provide_byes_for(Position.DEFENDER)
    
    @staticmethod
    def __provide_byes_for(position: Position) -> None:
        if position == Position.ATTACKER: 
            unbyed_players: List[Player] = [player for player in Player.__players if player.__attacker_bye_received == False]
            lowest_ranked_player: Player = max(unbyed_players, key=lambda player: player.get_rank(position))
        else:
            unbyed_players: List[Player] = [player for player in Player.__players if player.__defender_bye_received == False]
            lowest_ranked_player: Player = max(unbyed_players, key=lambda player: player.get_rank(position))
        lowest_ranked_player.receive_bye(position)
    
    @staticmethod
    def rank_players():
        for player in Player.__players:
            player.__determine_resistance_points()
        ranked_attackers: List[Player] = sorted(Player.__players, key=lambda player: (-player.__attacker_wins, -player.__attacker_resistance_points, -player.__attacker_goal_difference, random.random()))
        ranked_defenders: List[Player] = sorted(Player.__players, key=lambda player: (-player.__defender_wins, -player.__defender_resistance_points, -player.__defender_goal_difference, random.random()))
        for i in range(len(ranked_attackers)):
            ranked_attackers[i].__attacker_rank = (i + 1)
        for i in range(len(ranked_defenders)):
            ranked_defenders[i].__defender_rank = (i + 1)

    def __init__(self, number: int):
        self.__number: int = number
        self.__name = Player.__names[number]
        self.__attacker_rank: int = None
        self.__defender_rank: int = None
        self.__attacker_wins: int = 0
        self.__defender_wins: int = 0
        self.__attacker_resistance_points: int = 0
        self.__defender_resistance_points: int = 0
        self.__attacker_goal_difference: int = 0
        self.__defender_goal_difference: int = 0
        self.__attacker_bye_received: bool = False
        self.__defender_bye_received: bool = False
        self.__attacker_attacker_opponents: List[Player] = []
        self.__attacker_defender_opponents: List[Player] = []
        self.__defender_attacker_opponents: List[Player] = []
        self.__defender_defender_opponents: List[Player] = []
        
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
                self.__attacker_wins += 1;
                self.__attacker_bye_received = True
                return True
        else:
            if self.__defender_bye_received == False:
                self.__defender_wins += 1;
                self.__defender_bye_received = True
                return True
        return False
    
    def bye_received(self, position: Position) -> bool:
        if position == Position.ATTACKER:
            return self.__attacker_bye_received
        else:
            return self.__defender_bye_received
    
    def process_results(self, position: Position, team: Team, winning_team: Team, goal_difference: int, attacker_opponent: Player, defender_opponent: Player) -> None:
        win: bool = self.__win(team, winning_team)
        self.__register_wins(win, position)
        self.__register_goal_difference(win, position, goal_difference)
        self.__register_opponents(position, attacker_opponent, defender_opponent)
    
    def __win(self, team: Team, winning_team: Team) -> bool:
        if team == winning_team:
            return True
        else:
            return False

    def __register_wins(self, win: bool, position: Position) -> None:
        if win:
            if position == Position.ATTACKER:
                self.__attacker_wins += 1
            else:
                self.__defender_wins += 1
    
    def __register_goal_difference(self, win: bool, position: Position, goal_diffence: int):
        if not win:
            goal_diffence = - goal_diffence
        if position == Position.ATTACKER:
            self.__attacker_goal_difference += goal_diffence
        else:
            self.__defender_goal_difference += goal_diffence
    
    def __register_opponents(self, position: Position, attacker_opponent: Player, defender_opponent: Player):
        if position == Position.ATTACKER:
            self.__attacker_attacker_opponents.append(attacker_opponent)
            self.__attacker_defender_opponents.append(defender_opponent)
        else:
            self.__defender_attacker_opponents.append(attacker_opponent)
            self.__defender_defender_opponents.append(defender_opponent)

    def __determine_resistance_points(self) -> None:
        for player in self.__attacker_attacker_opponents:
            self.__attacker_resistance_points += player.__attacker_wins
        for player in self.__attacker_defender_opponents:
            self.__attacker_resistance_points += player.__defender_wins
        for player in self.__defender_attacker_opponents:
            self.__defender_resistance_points += player.__attacker_wins
        for player in self.__defender_defender_opponents:
            self.__defender_resistance_points += player.__defender_wins
    

    @staticmethod
    def get_names() -> List[str]:
        return Player.__names
    
    @staticmethod
    def set_name(name: str, item: int) -> None:
        Player.__names[item] = name
    
    __names: List[str] = [
        "Ome Henk",
        "Eppie",
        "Asterix",
        "Obelix",
        "Hachi",
        "Simba",
        "Wouter",
        "Demcon",
        "De Blinde",
        "De Lamme",
        "Mette Bus",
        "Bennie Weijs",
        "Lieve Lingen",
        "Co de Kraker",
        "Be Thalen",
        "Nies Slim",
        "Dino Saris",
        "Rocky Dool",
        "Elke Gram - Raak",
        "Ik Raas - Kal",
        "Connie Boere",
        "Mat Ras",
        "Adriaan Bassie",
        "Kenneth Wilhelmus",
        "Nikky Maus",
        "Elke Kant",
        "Ben Vierkant",
        "Anne Bol",
        "Eddy Schekman",
        "Jack Pot",
        "Klaar Wakker",
        "Hilbrand Baar",
        "Riet Suiker",
        "Sjef Kock",
        "Joska Bouter",
        "Dies Goorman",
        "Willie Wortel",
        "Chris Mus",
        "Iet Sanders",
        "Mario Netten",
        "Candy Man",
        "Loek Out",
        "Ferry Kuhlman",
        "Ben Dral",
        "Per Ooijevaar",
        "Vogel Kooi",
        "Wil Helmes",
        "Kitty Miao",
        "Indy Haan",
        "Fried Kaanen",
        "Max",
        "Fc Volendam",
        "Keukentafel",
        "Jacques",
        "Lampie",
        "Eelco",
        "Jesse",
        "Victoria",
        "Deborah",
        "Lihi"
    ]