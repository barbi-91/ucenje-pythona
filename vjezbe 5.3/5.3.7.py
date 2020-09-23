
while True:
    n=int(input("unesi broj"))
    if n>=3 and n<=10:
        print(n, "je ispravna vrijednost")
        break
    else:
        print("vrijednost",n," je neispravna")
    

b=1
for brojRetka in range(0, n): #odreduje redak
    for brojStupca in range (0, brojRetka): #prazan stupac je širine 3 space-a, može imati: "   ", " xx", "  x"
        print("   ", end="")
    for brojStupca in range (0, n - brojRetka): #ISPISUJE BROJ
        if b >= 0 and b <= 9: #provjerava da li je brojač jednoznamenkasti - ako je ostavi 2 space-a, 1 mjesto = jedna znamenka
            print("  ", end="")
            print(b, end="")
        else:   #ovo se izvrši ako je brojač dvoznamenkasti - ako je ostavi 1 space-a, 2 mjesta = 2 znamenke
            print(" ",end="")
            print(b, end="")
        b+=1 # povećava brojač, svaki slijedeći je za jedan veći
    print()