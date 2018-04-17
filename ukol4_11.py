# --- domaci projekty 4 - ukol 11 ---

pocet_radku = int(input("Zadej pocet radku (a zaroven sloupcu): "))

for cislo in range (pocet_radku + 1): # +1 tam je, protoze 1. radek je prazdny
    for cislo2 in range (cislo):
        print ("X ", end = "")
    print ("") 
