# odkladiste funkce, ktere pouzivame v ai.py a piskvorky.py
def tah(pole, cislo_policka, symbol): # symbol
    vystup_pocitace = pole[0:cislo_policka] + symbol + pole[cislo_policka + 1:]
    return vystup_pocitace
