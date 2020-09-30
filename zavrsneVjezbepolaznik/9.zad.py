# listaPocetka = []
# listaKraja = []   #obrnuta
# n=input("upisi proizvoljni niz znakova")
# if len(n)%2==1:
#     print("niz je neparan, ulazi u kategoriju provjere palindroma")
#     for element in n:
#         for slovo in element:
#             listaPocetka.append(slovo)
#             listaKraja=listaPocetka[::-1]
# else: 
#     print("niz nije neparan, ne ulazi u kategoriju provjere palindroma")
# print(listaPocetka)
# print(listaKraja)
#fali dio usporedbe dva niza







# # ako je rijec do pola od pocetka do kraja isti rijeci od kraja do pola 
# # ako je parno prepoloviti po pola
# # ako je neparno rijec prepoloviti po pola i pretvorit u intiger -1 znak u rangu
# # mozda pospremit svaki od elementa u listu i usporediti dali se indexi pasu
# # lista = []

# # n=input("upisi proizvoljni niz znakova")
# # if len(n)%2==1:
# #     print("niz je neparan, ulazi u kategoriju provjere palindroma")
# #     for element in n:
# #         for slovo in element:
# #             listaPocetka.append(slovo)
# #             listaKraja.append(slovo)
        
# # else: 
# #     print("niz nije neparan, ne ulazi u kategoriju provjere palindroma")
# # print(listaPocetka)
# # print(listaKraja)
# # duljina = len(n)
# # rang=(duljina/2)
# # rang=int(rang)

# rijec = "anavolimilovana"
# duljina = len(rijec)
# brojac1 = 0
# brojac2 = duljina - 1 
# polovica = int(duljina / 2)
# while brojac1 < polovica:
#     if rijec[brojac1] != rijec[brojac2]:
#         print("Nije Palindrom")
#         break
#     else:
#         brojac1 += 1  
#         brojac2 -= 1
#         if brojac1 == polovica:
#             print( "Palindrom je")

niz=input("unesi rijec")
rijec=niz.lower()
duljina=len(rijec)
i=0
e=duljina

if duljina<=1:
    print("rijec je prekratka")


while i < int(duljina/2):
    print(rijec[i])
    print(rijec[e-1])
    
    if rijec[i] != rijec[e-1]:
        print("nije polindrom")
        break
    else:
        i+=1
        e-=1
        if i==e:
            print("palindrom je" )

# # duljina = len(n)
# # rang=(duljina/2)
# # rang=int(rang)
# # for znak in range(rang):
# #     if slovo[i]in listaPocetka == slovo[-e] in listaKraja:
# #     # i=i+1
# #     # e=e+(-1)
# #         print("rijec je polindrom")