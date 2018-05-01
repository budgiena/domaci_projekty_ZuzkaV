# --- domaci ulohy z lekce 7 - ukol 0 ---
import sys
domaci_zvirata = ["pes", "kočka", "králík", "had"]

# ukol 1
def ukol_1 (domaci_zvirata):
    vybrana_zvirata = []
    for zvire in domaci_zvirata:
        if len(zvire)<5:
            vybrana_zvirata.extend([zvire])
    return vybrana_zvirata

# volani
##ukol_1 (domaci_zvirata)

# ukol 2
def ukol_2 (domaci_zvirata):
    vybrana_zvirata = []
    for zvire in domaci_zvirata:
        if zvire[0]=="k":
            vybrana_zvirata.extend([zvire])
    return vybrana_zvirata

# volani
##ukol_2 (domaci_zvirata)

# ukol 3
def ukol_3 (domaci_zvirata):
    zadane_zvire = str(input("Zadej název zvířete: "))
    if zadane_zvire in domaci_zvirata:
        return True
    else:
        return False

# volani
##ukol_3 (domaci_zvirata)


# ukol 4
zvirata_1 = ["potkan", "myš", "pavouk", "ještěrka", "brouk"]
zvirata_2 = ["pes", "myš", "brouk", "kráva", "žížala"]

def ukol_4(zvirata_1, zvirata_2):
    a = [] # zvirata, co jsou v obou seznamech
    for zvire in zvirata_1:
        if zvire in zvirata_2:
            a.extend([zvire])
    b = [] # zvirata jen v 2. seznamu
    for zvire in zvirata_1: 
        if zvire not in zvirata_2:
            b.extend([zvire])
            
    c = [] # zvirata jen v 3. seznamu
    for zvire in zvirata_2:
        if zvire not in zvirata_1:
            c.extend([zvire])
    return a, b, c

# volani
##ukol_4(zvirata_1, zvirata_2)

# ukol 5
def ukol_5 (domaci_zvirata):
    domaci_zvirata.sort()
    return domaci_zvirata

# volani
##ukol_5 (domaci_zvirata)
    
# ukol 6
def ukol_6(domaci_zvirata):
    domaci_zvirata.extend(["andulka"]) # prilet andulky
    domaci_zvirata_b = []
    for i in domaci_zvirata:
        j = i[1:]
        domaci_zvirata_b.extend([j])

    domaci_zvirata_a_b = list(zip(domaci_zvirata_b,domaci_zvirata))
    domaci_zvirata_a_b.sort()

    serazeny_list = []
    for i in domaci_zvirata_a_b:
        serazeny_list_i = i[1]
        serazeny_list.extend([serazeny_list_i])
    return serazeny_list

# volani
ukol_6(domaci_zvirata)

