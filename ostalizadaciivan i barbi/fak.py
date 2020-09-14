#fAK 4!= 4x3x2x1

# petlja koja je se vrti faktorijel puta.. brojac je mnozitelj

brojac=1
rezultat=1
n=int(input("unesite neki broj"))
while brojac<=n:
    rezultat=rezultat*brojac
    
    brojac=brojac+1
print(rezultat)