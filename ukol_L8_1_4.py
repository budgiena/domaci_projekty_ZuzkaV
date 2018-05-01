# ukol 0
def ukol_0(n):   
    seznam = []
    for i in range (1,n+1):
        hodnota_i = i**2
        seznam.extend([(i, hodnota_i)])
    slovnik = dict(seznam)
    return slovnik

#volani    
##print(ukol_0(4))


# ukol_1
slovnik=ukol_0(4)
def ukol_1(slovnik):
    #slovnik = ukol_1(4)
    #print (slovnik)
    klice = slovnik.keys()
    hodnoty = slovnik.values()
    suma_klicu = sum(klice)
    suma_hodnot = sum(hodnoty)
    return suma_klicu, suma_hodnot

#volani    
##print(ukol_1(slovnik))

# ukol_2
"""
Napiš funkci, která jako argument dostane řetězec a vrátí slovník, ve kterém budou jako klíče jednotlivé
znaky ze zadaného řetězce a jako hodnoty počty výskytů těchto znaků v řetězci.
"""

def ukol_2(retezec):
    # tvorba noveho reteze s odstranenim duplicit a tvorba listu z retezce
    retezec_unikat = ""
    retezec_list = []
    for znak in retezec:
        if znak not in retezec_unikat:
            retezec_unikat = retezec_unikat + znak
            retezec_list.extend([znak])

    # tvorba retezce poctu klicu
    pro_pocty = []
    for znak in retezec_unikat:
        pro_pocty_i = retezec.count(znak)
        pro_pocty.extend([pro_pocty_i])

    # tvorba slovniku ze seznamu
    seznam = []
    for i in range (0,len(retezec_list)):
        seznam_i = [(retezec_list[i],pro_pocty[i])]
        seznam.extend((seznam_i))
    slovnik = dict(seznam)
    return slovnik

# volani
##retezec = "kočička"
##print (ukol_2(retezec))


# ukol 3
"""
Napiš funkci, která vypíše obsah slovníku (klíče a k nim náležící hodnoty) na jednotlivé řádky.
Funkci, která něco vypisuje, je vhodné pojmenovat speciálně, zde třeba vypis_slovnik, aby bylo jasné, že jen
vypisuje a nic nevrací.

"""
def vypis_slovnik(slovnik):
    for klic, hodnota in slovnik.items():
        print('{}: {}'.format(klic, hodnota))

# volani
##vypis_slovnik(slovnik)


# ukol 4
import random
"""
Úkolem je vytvořit známou skautskou hru „Kdo? S kým? Co dělali?“. Hra se hráče zeptá postupně na
různé otázky, například „Kdo?“, „S kým?“, „Co dělali?“, „Kde?“, „Kdy?“, a nakonec „Proč?“, s tím, že
mu umožní na jednu otázku odpovědět vícekrát a všechny odpovědi si uloží. Na závěr pak hra z každé
sady odpovědí vybere náhodně jednu odpověď a z takto vybraných odpovědí složí větu, kterou vypíše
uživateli. Seznam otázek by mělo být možné změnit na jednom místě bez zásahu do logiky programu.
"""

otazky = ["Kdo?", "S kým?", "Co dělali?", "Kde?", "Kdy?", "Proč?"]
odpovedi = []

for i in range (0,len(otazky)):
    nova_otazka = "a"
    odpovedi_i = []
    print ('\n')
    while (nova_otazka == "a"):
        odpoved_i_i = str(input(otazky[i]+ ": "))
        odpovedi_i.extend([odpoved_i_i])
        nova_otazka = str(input("pokud chcete znovu odpovědět, zmáčkněte a, pokud ne, zmáčkněte enter: "))
    odpovedi.extend([odpovedi_i])

# prevod na slovnik
seznam = []
for i in range (0,len(otazky)):
    seznam_i = [(otazky[i], odpovedi[i])]
    seznam.extend(seznam_i)
slovnik = dict(seznam)    
print ('\n\n')
### vypis seznamu s nahodnymi hodnotami
##for klic, hodnota in slovnik.items():
##    print('{}: {}'.format(klic, random.choice(hodnota)))
  
print ('\n')
for hodnota in slovnik.values():
    print(random.choice(hodnota), end = " ")
