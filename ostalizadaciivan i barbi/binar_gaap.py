#testni brojevi su: 9, 59,20,15,16

N = int(input("unesi neki cijeli broj:"))
V = (bin(N)[2:].zfill(8))

print(f"""
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Binaran prikaz cijelog broja: {N} je: {V} 
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''""")
# lista_a = []              #lista zapoceta sa nulama---nevazceca
# lista_b = []              #lista gapova --- vazeca
lista_c = []                #zbroj nula u gapovima
brojac_nula = 0
brojac_jedinica = 0

for broj in str(V):

    if broj != "1":
        # nula = broj
        # print(nula, end="")
        brojac_nula += 1

        if brojac_jedinica == 0: 
            # lista_a.append(broj)
            brojac_nula = 0

        # elif brojac_jedinica == 1:
        #     # lista_b.append(broj)
         
        

    else: #broj == 1:
        # jedan = broj
        # print(jedan, end="")
        brojac_jedinica += 1
        if brojac_jedinica == 2:
            lista_c.append(brojac_nula)
            brojac_nula = 0
            brojac_jedinica = 1

            
if brojac_jedinica == 1 and brojac_nula > 1:
            brojac_nula = 0
            lista_c.append(brojac_nula)   
najveci = (sorted(lista_c)[-1])
if najveci == 0:
    najveci = ("Nema binarnih praznina!!!")
    
print(f"""
****************************************************************************************
Za neki binarni broj {V} njegov najveci binarni gap je: {najveci}!
****************************************************************************************
""")