import random
from util import tah

def tah_pocitace(pole, znak_pocitace):
    print("Tah počítače")
    if len (pole) == 0:
        return "Zadáno pole s nulovou délkou, počítač nemá kam umístit tah"
    if "-" not in pole:
        return "Plné hrací pole, počítač nemá kam umístit tah"
    while True:
        cislo_policka = random.randrange(len(pole))
        if pole[cislo_policka] == "-":
            return tah(pole, cislo_policka, znak_pocitace)

