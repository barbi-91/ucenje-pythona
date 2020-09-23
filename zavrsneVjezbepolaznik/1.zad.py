# suma=0
# prvi=0
# brojac=1
# drugi=int(input("unesi neki broj"))

# while drugi>0 and drugi > prvi:
#         suma=prvi+drugi
        
#         prvi=drugi
#         print(prvi, "prvi")
#         drugi=suma
#         print(drugi,"drugi")

#         suma=suma+drugi
        
        

#         if prvi==5:
#                 print("program se prekida")
#                 break
        
# brojac+=1

# print (suma, "suma")
#************************************************
# suma=0
# a=int(input("unesi neki broj"))
# suma=suma+a
# print( "unijeli ste a:",a)
# print("suma je sada:", suma)
# while True:
#         b=a
#         a=int(input("unesi broj:"))
#         if a<=b:
#                 break
#         suma=suma+a
#         b=a
#         print(suma, "suma trenutna")
# print("suma svih vrijednosti je:",suma, 
#  "uneseni broj se ne racuna jel je ponovljen i program je stao s radom")
#**************************************************

lista=[]
trenutni=0
suma=0
while True:
        n=int(input("unesi broj"))
        if n==5 and trenutni>n:
                print("upisani broj je prekidni ili je manji od prethodnog i program se prekida")
                break
        
        else:
                print("broj je veci od prethodnog i broj nije jednak prekidnom")
                lista.append(n)
                suma=suma+n
                trenutni=n
print("lista trenutno upisanih brojeva", lista)
print( "suma trenutno upisanih brojeva je", suma)
