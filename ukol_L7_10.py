# ukol 10

def ukol_10(seznam_dvojic):
    seznam = []
    radek = []
    for i in range (0,10):
        radek.extend(["."])
    for i in range (0,10):
        radek_n = list(radek)
        seznam.extend([radek_n])

    dvojice = []
    for i in seznam_dvojic:
        dvojice_i = list(i)
        dvojice.extend([dvojice_i])
               
    for i in dvojice:
        seznam[i[1]][i[0]] = "X"

    for i in seznam:
        for j in i:
            print (j, end = " ")
        print ("")

# volani
seznam_dvojic = [(0, 0), (1, 0), (2, 2), (4, 3), (8, 9)]
ukol_10(seznam_dvojic)
