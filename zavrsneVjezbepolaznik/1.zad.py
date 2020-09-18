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

suma=0
a=int(input("unesi neki broj"))
suma=suma+a
print( "unijeli ste a:",a)
print("suma je sada:", suma)
while True:
        b=a
        a=int(input("unesi broj:"))
        if a<=b:
                break
        suma=suma+a
        b=a
        print(suma, "suma trenutna")
print("suma svih vrijednosti je:",suma,  "uneseni broj se ne racuna jel je ponovljen i program je stao s radom")