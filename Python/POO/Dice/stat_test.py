from stat_dice import StatDice

def test_stat_dice():
    dice = StatDice()
    assert dice.stat=={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

def test_set():
    dice = StatDice()
    dice.set_position(5)
    assert dice.stat=={1:0, 2:0, 3:0, 4:0, 5:1, 6:0}

def test_roll():
    dice = StatDice()
    a=dice.stat
    dice.roll()
    b=dice.stat
    assert  a == b