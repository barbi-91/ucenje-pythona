
osoba={"ime":"Barbara", "prezime":"Erdec", "godine":29}
osoba.update({"adresa":"Ivana Berute"})
print(osoba)

del osoba["godine"]
print(osoba)



for vrijednost in osoba.keys():
    print(vrijednost)

#brisanje vrijednosti iz rijecnika pomocu DEL ž
#takoder pomocu for petlje ispisavanje samo vrijednosti a ne i kljuceva iz rijecnika