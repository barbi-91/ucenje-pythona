a=int(input("unesite neki broj:"))
b=int(input("unesite jos neki broj:"))
if a and b < 100:
    print(" obje unesene vrijednosti varijable su manje od 100")
elif a < 100 or b < 100:
    print("jedna unesena vrijednost je manja a druga je veca od 100")
else:
    print("unesene vrijdnosti varijable su vece od 100")

