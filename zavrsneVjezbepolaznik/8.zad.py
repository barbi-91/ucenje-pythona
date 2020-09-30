lista = []
lista1 = []
while True:
    n = int(input("unesi neki broj"))
    if n > 2 and n < 21:
        print("unesite", n, "puta par brojava")
        suma=0
        for brojac in range (1,n+1):
            prvi=int(input("unesi broj prvog para:"))
            drugi=int(input("unesi broj drugog para:"))
            suma=prvi+drugi
            lista1.append([prvi, drugi])
            lista.append(suma)
            
            

    else:
        print("broj nije u intervalu, pokusajte ponovno")
        continue
    
    print ("parovi",lista1)
    print("suma parova",lista)
    lista.sort()
    print("najveca suma brojava je:", lista[-1])
    najveci=0
    for e in lista1:
        if e[0]+e[1] == lista[-1]:
            print(e, "je par sa najvecom sumom")