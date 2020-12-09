niz = [2, 7, 1, 0, 6]
for broj in niz:
    print(broj, end="")

duljina=len(niz)
for elementNiza in range(0,duljina-1):  #o do 4 jer su 4 usporedbe
    for sljedeciElement in range (elementNiza+1,duljina): #ukupno 0+1 do 4
        print("\n")
        print (niz[elementNiza])
        print(niz[sljedeciElement])
        if (niz[elementNiza]>niz[sljedeciElement]):
            
            
            
            b=niz[elementNiza]
            print(b ,"je b")
            niz[elementNiza]=niz[sljedeciElement]
            print(niz[elementNiza], "je prvi")
            niz[sljedeciElement]=b
            print(niz[sljedeciElement], "je drugi")
            print(niz, end="")
    print("")

for k in niz:
    print("****",k,end="*")



# lista=[]
# broj= int(input("unesite broj elemenata koliko zelite unijeti"))
# print("unesite elemente u listu")
# for k in range (broj):
#     lista.append(int(input()))
# print("nesortirana lista", lista)

# for i in range(0,len(lista)):
#     for j in range(i+1, len(lista)):
#         if lista[i]>lista[j]:
#             b=lista[i]
#             lista[j]=lista[i]
#             lista[i]=b
# print(lista,"nova lista")