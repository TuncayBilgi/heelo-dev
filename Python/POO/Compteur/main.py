from compteur import Compteur
    
c1 = Compteur(2,1)
c2 = Compteur(4)
c1.ajoute()
c2.ajoute()
c1.ajoute()

print("c1 = " + str(c1.donne_valeur()),type(c2))
print(c2)
print("c1 > c2 : " + str(c1>c2))