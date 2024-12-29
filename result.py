from __future__ import annotations
from team import Team
from typing import List
import random

class Result:
    __result_history: List[List[Result]] = None

    @staticmethod
    def add_round_results(matches: int) -> None:
        # print("In Result#add_round_results()")
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
        match -= match
        return Result.__result_history[round][match]

    def __init__(self):
        self.__simulateWinningTeam()
        self.__simulateGoalDifference()
    
    def getWinningTeam(self) -> Team:
        return self.__winningTeam
    
    def getGoalDifference(self) -> int:         
        return self.__goalDifference
    
    def __simulateWinningTeam(self) -> Team:
        coinflip: int = random.randint(0,1)
        if coinflip == 0:
            self.__winningTeam = Team.A
        else:
            self.__winningTeam = Team.B

    def __simulateGoalDifference(self) -> int:
        self.__goalDifference = random.randint(1,8)