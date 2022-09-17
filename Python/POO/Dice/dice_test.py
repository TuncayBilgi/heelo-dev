from dice import Dice

def test_init():
    dice=Dice()
    assert dice is not None and dice.position==1

def test_str():
    dice=Dice()
    assert print(dice)==print(1)

def test_get():
    dice=Dice()
    assert isinstance(dice.get_position(), int)

def test_set():
    dice=Dice()
    dice.set_position(4)
    assert dice.position==4

def test_roll():
    dice=Dice()
    dice.roll().roll()
    assert dice.position in range(1,7)