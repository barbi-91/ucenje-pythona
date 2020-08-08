#kreiranje prazne tekstualne datoteke
 
with open("datoteka.txt", "w") as f:    #koristimo with, open kao otvaranje i unutar zagrada naziv datoteke koju otvaramo
    for i in range (0,20): #funkcija za izvrsavanje ispisavanja parnih brojeva od jedan do dvadeset
        if i%2==0:
            f.write(str(i)+ " ") #naredba za uspiavanje stringa tj. naredbe funckije koje ce se ispisati u novu datoteku