from dice import Dice
from random import randint

class StatDice(Dice):
    compteur = 0
    def __init__(self,position = 1):
        super().__init__(position)
        self.stat = { x:0 for x in range(1,7) }
        StatDice.compteur += 1

    def set_position(self, position):
        super().set_position(position)
        self.stat[position] = self.stat[position] + 1

