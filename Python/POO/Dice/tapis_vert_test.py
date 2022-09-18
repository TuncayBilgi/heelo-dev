from tapis_vert import Tapis_vert
from dice import Dice

def test_init():
    tapis=Tapis_vert()
    assert tapis is not None and isinstance(tapis[1],Dice) and len(tapis.des)==5

def test_str():
    tapis=Tapis_vert()
    assert isinstance(str(tapis),str)

def test_copie():
    tapis=Tapis_vert()
    a=tapis[1]
    a.set_position(10)
    assert str(tapis[1])==str(10)

def test_roll():
    tapis=Tapis_vert()
    tapis.roll()
    assert tapis[1].position in range(1,7)

def test_main():
    tapis=Tapis_vert()
    tapis.des[4].position=2
    tapis.main()
    assert tapis.carre==1 and tapis.paire==0 and tapis.double_paire==0 and tapis.brelan==0 and tapis.full==0

    tapis.des[3].position=2
    tapis.main()
    assert tapis.carre==0 and tapis.paire==0 and tapis.double_paire==0 and tapis.brelan==0 and tapis.full==1

    tapis.des[2].position=5
    tapis.main()
    assert tapis.carre==0 and tapis.paire==0 and tapis.double_paire==1 and tapis.brelan==0 and tapis.full==0

    tapis.des[1].position=2
    tapis.main()
    assert tapis.carre==0 and tapis.paire==0 and tapis.double_paire==0 and tapis.brelan==1 and tapis.full==0

    tapis.des[1].position=4
    tapis.main()
    assert tapis.carre==0 and tapis.paire==1 and tapis.double_paire==0 and tapis.brelan==0 and tapis.full==0



