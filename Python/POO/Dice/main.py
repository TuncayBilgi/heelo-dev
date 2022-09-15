from dice import Dice

dice=Dice()
n=0
goal=input("wanted value between 1 and 6 : ")
while dice.get_position() != int(goal) and int(goal) in range(1,7) :
    dice.roll()
    print (dice.get_position())
    n=n+1

print("you needed : "+ str(n) + " roll")
