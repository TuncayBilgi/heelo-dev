class Panier:
    def __init__(self):
        self.stock = tuple()

    def ajoute(self, fruit):
        temp = []
        temp.extend(self.stock)
        temp.append(fruit)
        self.stock = tuple(temp)

    def montre_panier(self):
        return self.stock

    def supprime(self, fruit):
        temp = []
        temp.extend(self.stock)
        temp.remove(fruit)
        self.stock = tuple(temp)