# --- domaci projekty 4 - ukol 13 ---

pocet_radku = int(input("Zadej pocet radku (a zaroven sloupcu): "))

"""
# puvodni varianta 
##for cislo_radku in range(pocet_radku):
##    if cislo_radku in (0,pocet_radku-1):
##        for prvni_posledni in range(pocet_radku):
##            print ("X", end = " ")
##        print ("")
##    else:    
##        for cislo_sloupce in range (pocet_radku):
##            if cislo_sloupce in (0,pocet_radku-1):
##                print ("X", end = " ")
##            else:
##                print (" ", end = " ")
##        print ("")
##     
"""
for cislo_radku in range(pocet_radku):
    for cislo_sloupce in range(pocet_radku):
        if (cislo_radku in (0, pocet_radku-1)) or (cislo_sloupce in (0, pocet_radku-1)):
            print ("X", end = " ")
        else:
            print (" ", end = " ")
    print ("")
