from __future__ import annotations
from team import Team
from typing import List
import random

class Result:
    __result_history: List[List[Result]] = None

    @staticmethod
    def add_round_results(matches: int) -> None:
        if Result.__result_history is None:
            Result.__result_history = []
        round: int = len(Result.__result_history)
        round_results: List[Result] = []
        Result.__result_history.append(round_results)
        for match in range(matches):
            Result.__result_history[round].append(Result())
    
    @staticmethod
    def add_match_result(match_nr: int, winning_team: Team, goal_difference: int) -> None:
        print(f"match_nr is: {match_nr}")
        if Result.__result_history is None:
            Result.__result_history = []
        if match_nr == 0:
            round_results: List[Result] = []
            Result.__result_history.append(round_results)
        round: int = (len(Result.__result_history) - 1)
        print(f"round is: {round}")
        result: Result = Result()
        result.__set_winning_team(winning_team)
        result.__set_goal_difference(goal_difference)
        print(f"Length of result_history is {len(Result.__result_history)}")
        Result.__result_history[round].append(result)
        
        
    @staticmethod
    def get_result(round: int, match: int) -> Result:
        round -= round
        wedstrijd = (match - 1)
        return Result.__result_history[round][wedstrijd]

    def __init__(self):
        self.__simulate_winning_team()
        self.__simulate_goal_difference()
    
    def get_winning_team(self) -> Team:
        return self.__winning_team

    def __set_winning_team(self, winning_team: Team) -> None:
        self.__winning_team = winning_team
    
    def get_goal_difference(self) -> int:         
        return self.__goal_difference
    
    def __set_goal_difference(self, goal_difference: int) -> None:
        self.__goal_difference = goal_difference
    
    def __simulate_winning_team(self) -> Team:
        coinflip: int = random.randint(0,1)
        if coinflip == 0:
            self.__winning_team = Team.A
        else:
            self.__winning_team = Team.B

    def __simulate_goal_difference(self) -> int:
        self.__goal_difference = random.randint(1,8)