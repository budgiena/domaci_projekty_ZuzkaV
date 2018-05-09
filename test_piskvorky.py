# ukol z lekce 9 (testovani) - ukol 

import pytest
from piskvorky import vyhodnot, tah_hrace
from util import tah
from ai import tah_pocitace

def test_tah_o(): 
    assert tah(20*"-", 1, "o") == '-o------------------'

def test_tah_x(): 
    assert tah("o--", 2, "x") == 'o-x'    


def test_vyhodnot_pomlcka():
    assert vyhodnot("-o-") == "-"
def test_vyhodnot_x():
    assert vyhodnot("oo-xxx---") == "x"

# fce tah_hrace a piskvorky1d nejde otestovat - je v nich zde funkce input

def test_tah_pocitace_1():
    assert tah_pocitace("---", "o") in ("o--", "-o-", "--o")
def test_tah_pocitace_2():    
    assert tah_pocitace("-", "o") == ("o")

# dalsi testy po uprave
def test_tah_hrace():
    tah_hrace("-----",2) == "--x--"
def test_tah_hrace_spatny_tah():
    tah_hrace("-----",8) == "Zadáno špatné číslo! Zadejte, prosím, celé číslo v rozmezí 0 - 19."

# ukol 4
def test_tah_pocitace_3():    
    delka_pole = tah_pocitace(10*"-", "o")
    assert delka_pole != 20
    """ ale toto to asi neovereni, ne?"""
    
def test_tah_pocitace_plne():
    tah_pocitace("xxoxoo", "o") == "Plné hrací pole, počítač nemá kam umístit tah"

def test_tah_pocitace_nulove():
    tah_pocitace("", "o") == "Zadáno pole s nulovou délkou, počítač nemá kam umístit tah"

        

