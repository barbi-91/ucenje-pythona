def analiza (lista):
    for provjera in lista:
        if provjera %2==1:
            return False
    return True
lista= [2,3,5,6,7,8]
if analiza (lista)== True:
    print("elemnti su parni")
else:
    print("element je neparan barem jedan")