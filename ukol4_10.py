# --- domaci projekty 4 - ukol 10 ---

pocet_radku = int(input("Zadej pocet radku (a zaroven sloupcu): "))

for radek in range(pocet_radku): 
    for sloupec in range(pocet_radku):
        print (radek * sloupec, end = " ") 
    print (" ")     
