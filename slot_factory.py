from __future__ import annotations
from slot import Slot
from player import Player
from team import Team
from position import Position
from result import Result
from typing import List
import math

class SlotFactory:

    def __init__(self, slot: Slot):
        self.__slot = slot