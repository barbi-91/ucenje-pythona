# #taj je opasan ;)

while True:
    n=int(input("unesi broj"))
    if n>=3 and n<=10:
        print(n, "je ispravna vrijednost, radimo tablicu sa:",n,"*",n, "redaka i stupaca")
        break
    else:
        print("vrijednost",n," je neispravna")
    

b=1
for indexRetka in range(0, n): #odreduje redak
    for idnexStupca in range (0, indexRetka): #prazan stupac je širine 3 space-a, može imati: "   ", " xx", "  x"
        print("   ", end="")
    for indexStupca in range (0, n - indexRetka): #ISPISUJE BROJ
        if b >= 0 and b <= 9: #provjerava da li je brojač jednoznamenkasti - ako je ostavi 2 space-a, 1 mjesto = jedna znamenka
            print("  ", end="")
            print(b, end="")
        else:   #ovo se izvrši ako je brojač dvoznamenkasti - ako je ostavi 1 space-a, 2 mjesta = 2 znamenke
            print(" ",end="")
            print(b, end="")
        b+=1 # povećava brojač, svaki slijedeći je za jedan veći
    print()



# #####sican ali ispisuje opet od jedinice, sama izmislila

# n=5
# b=1
# for i in range(0, n): #odreduje redak
#     for j in range (0, i): #prazan stupac je širine 3 space-a, može imati: "   ", " xx", "  x"
#         print("***", end=" ")
#     b=1
#     for j in range (0, n - i): #ISPISUJE BROJ
#         if b >= 0 and b <= 9: #provjerava da li je brojač jednoznamenkasti - ako je ostavi 2 space-a, 1 mjesto = jedna znamenka
#             print("##", end="")
#             print(b, end=" ")
#         else:   #ovo se izvrši ako je brojač dvoznamenkasti - ako je ostavi 1 space-a, 2 mjesta = 2 znamenke
#             print("#",end="")
#             print(b, end=" ")
#         b+=1 # povećava brojač, svaki slijedeći je za jedan veći
#     print()

#####sican ali ispisuje  obrnuto

# n=5

# for i in range(0, n): #odreduje redak
#     b=1
#     for j in range (0, n - i): #ISPISUJE BROJ
#         if b >= 0 and b <= 9: #provjerava da li je brojač jednoznamenkasti - ako je ostavi 2 space-a, 1 mjesto = jedna znamenka
#             print("##", end="")
#             print(b, end=" ")
#         else:   #ovo se izvrši ako je brojač dvoznamenkasti - ako je ostavi 1 space-a, 2 mjesta = 2 znamenke
#             print("#",end="")
#             print(b, end=" ")
#         b+=1 # povećava brojač, svaki slijedeći je za jedan veći
#     for j in range (i): #prazan stupac je širine 3 space-a, može imati: "   ", " xx", "  x"
#         print("***", end=" ")
#     print()

# n=5
# b=1
# for i in range(1, n): #odreduje redak
#     for j in range (0, i): #ISPISUJE BROJ
#         if b >= 0 and b <= 9: #provjerava da li je brojač jednoznamenkasti - ako je ostavi 2 space-a, 1 mjesto = jedna znamenka
#             print("##", end="")
#             print(b, end=" ")
#         else:   #ovo se izvrši ako je brojač dvoznamenkasti - ako je ostavi 1 space-a, 2 mjesta = 2 znamenke
#             print("#",end="")
#             print(b, end=" ")
#         b+=1 # povećava brojač, svaki slijedeći je za jedan veći
    
#     for j in range (n-i): #prazan stupac je širine 3 space-a, može imati: "   ", " xx", "  x"
#         print("***", end=" ")
#     print()

# n=5

# for i in range(1, n): #odreduje redak
#     b=1
#     for j in range (0, i): #ISPISUJE BROJ
#         if b >= 0 and b <= 9: #provjerava da li je brojač jednoznamenkasti - ako je ostavi 2 space-a, 1 mjesto = jedna znamenka
#             print("##", end="")
#             print(b, end=" ")
#         else:   #ovo se izvrši ako je brojač dvoznamenkasti - ako je ostavi 1 space-a, 2 mjesta = 2 znamenke
#             print("#",end="")
#             print(b, end=" ")
#         b+=1 # povećava brojač, svaki slijedeći je za jedan veći
    
#     for j in range (n-i): #prazan stupac je širine 3 space-a, može imati: "   ", " xx", "  x"
#         print("***", end=" ")
#     print()
