from monnaie import Dollar,CHF


def test_multiplication():
    cinq = Dollar(5)
    dix = 2 * cinq

    assert 10 == dix.montant


def test_eq():
    assert Dollar(5) == Dollar(5) and Dollar(5) != Dollar(6)

def test_multiplication_Franc():
    cinq = CHF(5)
    dix = 2 * cinq

    assert 10 == dix.montant


def test_multiplication_Franc():
    assert CHF(5) == CHF(5) and CHF(5) != CHF(6)

def test_eq_inter_monnaie() :
    assert Dollar(5) == CHF(25)




#def test_addition_InterMonnaie():
 #   dollarcinq = Dollar(5)
  #  francvingcinq = CHF(25)
    #dollardix = Dollar(10)
    #assert dollarcinq + francvingcinq == dollardix

