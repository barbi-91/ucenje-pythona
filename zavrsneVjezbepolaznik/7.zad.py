#odlicno usjepjela sama :D
početnaLista = []
lista = []
word = input("unesi proizvoljni niz znakova:")
početnaLista.append(word)
print(početnaLista)
parni=0
neparni=0

for letter in range(len(word)):
    if letter %2 == 0:
        parni = (word[letter].upper())
        lista.append(parni)
    else:
        neparni = (word[letter].lower())
        lista.append(neparni)
print(lista)

#dodatno: prva opcija petlje kako ispisati slova kao brojeve iz rijeci
#xdruga opcija kako ispisati slova iz rijeci 
# n=input("unesi neku rijec")
# i=0
# for i in range(len(n)):
#     print(i, end=" ")
# for element in n:
#     for slovo in element:
#         print(slovo, end=" ")