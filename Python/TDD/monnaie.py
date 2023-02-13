class Monnaie:
    def __init__(self, montant):
        self._montant = montant
        self.taux = 1

    @property
    def montant(self):
        return self._montant

    @montant.setter
    def montant(self, value):
        self._montant = value

    def __mul__(self, other):
        return type(self)(self.montant * other)

    __rmul__ = __mul__

    def __eq__(self, other):
        return self.montant*self.taux == other.montant*other.taux

class CHF(Monnaie):

    def __init__(self,montant):
        super().__init__(montant)
        self.taux=1/5

class Dollar(Monnaie):
    def __init__(self,montant):
        super().__init__(montant)
        self.taux=1
