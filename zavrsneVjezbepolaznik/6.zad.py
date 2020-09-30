def zbrajanje(b,c):
    a=b+c
    return a
def oduzimanje(b,c):
    a=b-c
    return a
def mnozenje(b,c):
    a=b*c
    return a
def djeljenje(b,c):
    a=b/c
    return a

print("unesite zeljenu vrijednsoti: 1 za zbrajanje, 2 za oduzimanje, 3 za mnozenje i 4 za dijeljenje" ,"\n", "ili 0 za izlazak iz programa")

while True:
    n=int(input("unesite broj zeljenje operacije:"))

    if n<=-1 or n>=5: 
        print("unijeli ste pogresan broj, pokusajte ponovno")
        continue
    if n==0:
            print("izlazak iz programa")
            break
    rezultat=0
    if n >= 0 or n <=4:
        b=int(input("unesi neki broj"))
        c=int(input("unesi neki broj"))
        if n==1:
            rezultat=zbrajanje(b,c)
        elif n==2:
            rezultat=oduzimanje(b,c)
        elif n==3:
            rezultat=mnozenje(b,c)
        elif n==4:
            rezultat=djeljenje(b,c)
        
        print(rezultat)
        
    





