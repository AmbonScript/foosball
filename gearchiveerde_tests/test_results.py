from __future__ import annotations
from position import Position
from team import Team
from player import Player
from competition import Competition
from round import Round
from result import Result
from matchslot import MatchSlot
from typing import List
import math
import random

# add_round_results
assert Result._Result__result_history is None
Result.add_round_results(10)
assert len(Result._Result__result_history[0]) == 10
assert isinstance(Result.get_result(1, 1).getWinningTeam(), Team)
assert isinstance(Result.get_result(1, 1).getGoalDifference(), int)
Result.add_round_results(10)
assert len(Result._Result__result_history[1]) == 10
assert isinstance(Result.get_result(2, 1).getWinningTeam(), Team)
assert isinstance(Result.get_result(2, 1).getGoalDifference(), int)