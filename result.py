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
    def get_result(round: int, match: int) -> Result:
        round -= round
        wedstrijd = (match - 1)
        return Result.__result_history[round][wedstrijd]

    def __init__(self):
        self.__simulate_winning_team()
        self.__simulate_goal_difference()
    
    def get_winning_team(self) -> Team:
        return self.__winningTeam
    
    def get_goal_difference(self) -> int:         
        return self.__goal_difference
    
    def __simulate_winning_team(self) -> Team:
        coinflip: int = random.randint(0,1)
        if coinflip == 0:
            self.__winningTeam = Team.A
        else:
            self.__winningTeam = Team.B

    def __simulate_goal_difference(self) -> int:
        self.__goal_difference = random.randint(1,8)