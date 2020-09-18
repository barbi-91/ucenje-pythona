# listaA=[]
# listaB=[]
# niz1=input("unesite niz znakova u listu A:")
# niz2=input("unesi niz znakova u listu B:")
# a.islower()
# b.islower()
# listaA.append(a)
# listaB.append(b)
# print(listaA)
# print(listaB)

niz1=input("unesite niz znakova u listu A:")
niz2=input("unesi niz znakova u listu B:")

duljinaNiza1=len(niz1)
duljinaNiza2=len(niz2)
#naredbom zadajemo prebrajenje duzine

if duljinaNiza1<duljinaNiza2:
    duljina = duljinaNiza1
else:
    duljina = duljinaNiza2
# duljine 1 i 2 trpamo u jedan red...pod idojom koja je kraca njoj se pridruzeje ostatak

i=0 #radimo brojac za iste znakove
while i < duljina: #brojac iterira kroz duljinu a ne beskonacno na nacin dok je on manji od duljine radnja se ponavalja
    if niz1[i].lower() == niz2[i].lower():
        #preokrecemo ako ima koje veliko slovo... u malo
            print(i, niz1[i].lower())
    i+=1

