# ukol 7 + 8
import sys

# a)
#rodne_cislo = "000000/0011"
rodne_cislo = str(input("Zadej rodne_cislo: "))
##sesticisli = rodne_cislo[:6]
##lomitko = rodne_cislo[6]
##ctyrcisli = rodne_cislo[7:]

# pomocne funkce
def je_cislo(retezec):
    try:
        float(retezec)
        return True
    except ValueError:
        return False

def je_lomitko(retezec):
    if retezec == "/":
        return True
    else:
        return False   

def ukol7_a(rodne_cislo):
    if len(rodne_cislo) == 11:
        sesticisli = rodne_cislo[:6]
        lomitko = rodne_cislo[6]
        ctyrcisli = rodne_cislo[7:]
        je_cislo(sesticisli)
        je_cislo(ctyrcisli)
        je_lomitko(lomitko)
        if je_cislo (sesticisli) and je_lomitko(lomitko) and je_cislo(ctyrcisli):
            return True
        else:
            return False
    else:
        return False

# b)
def ukol7_b(rodne_cislo):
    rc_cisla = rodne_cislo[:6] + rodne_cislo[7:]
    if float(rc_cisla)//11 == float(rc_cisla)/11:
        return True
    else:
        return False

# c)
def ukol7_c(rodne_cislo):
    den = rodne_cislo[4:6]
    mesic = rodne_cislo[2:4]
    if float(mesic) > 12:
        mesic = str(int(float(mesic) - 50))
    rok = "19" + rodne_cislo[:2]
    return den, mesic, rok

# d)
def ukol7_d(rodne_cislo):
    mesic = rodne_cislo[2:4]
    if float(mesic) > 12:
        return "žena"
    else:
        return "muž"
    
# volani funkci
print ("kontrola spravnosti formatu:")
print (ukol7_a(rodne_cislo))
if ukol7_a(rodne_cislo) == False:
    print ("\nŠpatně zadaný formát rodného čísla!!!")
    sys.exit() 
print ("\ndělitelnost 11:")
print (ukol7_b(rodne_cislo))
print ("\ndatum narození (den, mesic, rok):")
print (ukol7_c(rodne_cislo))
print ("\npohlaví:")
print (ukol7_d(rodne_cislo))
