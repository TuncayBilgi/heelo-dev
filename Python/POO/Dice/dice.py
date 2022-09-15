from random import randint


class Dice:
    def __init__(self,position=1) :
        self.position=position

    def get_position(self):
        return self.position
    
    def set_position(self,position):
        self.position=position
    
    def roll(self) :
        self.position=randint(1,6)

