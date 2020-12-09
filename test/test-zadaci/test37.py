# def remove_duplicates(lista):
#     lista2 = []
#     for item in lista:
#         if item not in lista2:
#             lista2.append(item)
#     return lista2
# print (remove_duplicates ([1,2,3,3]))



import sys
import random

odg = True

while odg:
    pitanje = input("Pitaj carobnu kuglu vase tajno pitanje: (pritisni enter ako si ispucao sva pitanja) ")

    odgovor = random.randint(1,8)

    if pitanje == "":
        sys.exit(0)

    elif odgovor == 1:
        print ("to je zasigurno")

    elif odgovor == 2:
        print ("vrlo moguce")

    elif odgovor == 3:
        print ("apsolutno sigurno")

    elif odgovor == 4:
        print ("pitaj kasnije")

    elif odgovor == 5:
        print ("koncentriraj se i pitaj ponovno")

    elif odgovor == 6:
        print ("odgovor je nmaglovit, pitaj ponovno")

    elif odgovor == 7:
        print ("odgovor je negativan")

    elif odgovor == 8:
        print ("Ne nadajte se")
