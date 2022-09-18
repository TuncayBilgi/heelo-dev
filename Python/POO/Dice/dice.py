from random import randint


class Dice:
    compteur = 0
    def __init__(self,position=1) :
        self.position=position
        self._couleur="noir"
        Dice.compteur += 1

    @staticmethod
    def get_compteur1() :
        return Dice.compteur
    
    @classmethod
    def get_compteur2(cls) :
        return cls.compteur

    @property
    def couleur(self) :
        return self._couleur

    def __str__(self):
        return str(self.position)

    def get_position(self):
        return self.position
    
    def set_position(self,position):
        assert isinstance(position,int)
        self.position=position
    
    def roll(self) :
        self.set_position(randint(1,6))
        return self

