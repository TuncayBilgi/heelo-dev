from tapis_vert import Tapis_vert
from stat_dice import StatDice

tapis=Tapis_vert()

statee=StatDice()

for i in range(1,100):
    statee.roll()

print(statee.stat)
