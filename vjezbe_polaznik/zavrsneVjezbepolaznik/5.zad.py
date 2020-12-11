# def izracun():
#     suma=0
#     tmp=x

#     if tmp<0:
#         tmp *= -1
#     while tmp >0:
#         suma += tmp
#         tmp-=1
    
#     if x<0:
#         suma *=-1

#     return suma

# x=int(input ("unesi neki broj"))
# suma=izracun()
# print(suma)

def izracun():
    suma = 0
    n = unos
    if n == 0:
        return 0
    else:
        if n < 0:
            pocetniIndeks = n
            zavrsniIndeks = 0
        else:
            pocetniIndeks = 1
            zavrsniIndeks = n + 1

    for i in range(pocetniIndeks, zavrsniIndeks):
        suma = suma + i
    
    return suma #return predaje rezltat motodi...u pozivu metode ispisuje se rezultat otuputa kojeg baca return

i = 0
unos = int(input("upisi cijeli broj"))
izracun()
print(izracun(), "je rezutlat")

#glloblnu varijablu predajemo lokalnoj global n ako je nazovemo opet n
#ili nvi naziv varijable u samoj metodi...n=unos