from nbappel import Nbappel
from tapis_vert import Tapis_vert
from dice import Dice
from stat_dice import StatDice

@Nbappel
def roll_de(dé) :
    dé.roll()
    return dé

dé=Dice()
statdé=StatDice()

print(Dice.get_compteur1())
print(StatDice.get_compteur1())
print(Dice.get_compteur2())
print(StatDice.get_compteur2())

roll_de(roll_de(roll_de(dé)))

dé.roll()

roll_de(dé)
