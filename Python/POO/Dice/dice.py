from random import randint


class Dice:
    compteur = 0
    def __init__(self,position=1) :
        self.position=position
        Dice.compteur += 1

    @staticmethod
    def get_compteur1() :
        return Dice.compteur
    
    @classmethod
    def get_compteur2(cls) :
        return cls.compteur

    def __str__(self):
        return str(self.position)

    def get_position(self):
        return self.position
    
    def set_position(self,position):
        self.position=position
    
    def roll(self) :
        self.set_position(randint(1,6))
        return self

