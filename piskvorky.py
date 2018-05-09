# -*- coding: cp1250 -*-
# ukol9
# 1D piskvorky
import random
from ai import tah_pocitace
from util import tah

znak_hrace = "x"
znak_pocitace = "o"

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


def tah_hrace(pole,cislo_policka):
    while True:
        if cislo_policka not in range (0,len(pole)):
            hlaska = "Zad�no �patn� ��slo! Zadejte, pros�m, cel� ��slo v rozmez� 0 - 19."
            return (hlaska)
        elif pole[cislo_policka] != "-":
            hlaska =  "Pol��ko u� je obsazen�, zkuste jin�"
            return (hlaska)
        else:
            return tah(pole, cislo_policka, znak_hrace) 

def piskvorky1d(pole, hraje):
    while True:
        print (pole)
        if (hraje == znak_hrace):
            cislo_policka = int(input("Jste na tahu! Zadejte ��slo pol��ka v rozmez� 0 - 19: "))
            ok = tah_hrace(pole,cislo_policka)
            #while True:
            if ok in ["Zad�no �patn� ��slo! Zadejte, pros�m, cel� ��slo v rozmez� 0 - 19.", "Pol��ko u� je obsazen�, zkuste jin�"]:
                print (ok)
                cislo_policka = int(input("Jste na tahu! Zadejte ��slo pol��ka v rozmez� 0 - 19: "))   
            pole = tah_hrace(pole,cislo_policka)    
            """jeste potrebuji zabudovat while (?) cyklus na osetreni toho, kdyz uzivatel zada cislo spatne 2 a vic krat po sobe"""
            hraje = znak_pocitace
        elif hraje == znak_pocitace:
            pole = tah_pocitace(pole, znak_pocitace)
            hraje = znak_hrace
        vysledek = vyhodnot(pole)
        if vysledek != "-":
            print(str(pole))
            if vysledek == "!":
                return ("Rem�za! {}".format(pole))
            elif vysledek == znak_hrace:
                return("Gratuluji k v�t�zstv�!")
            elif vysledek == znak_pocitace:
                return ("Vyhr�l po��ta� :-(")


