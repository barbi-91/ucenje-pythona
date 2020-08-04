brojac = 0
clanEnMinus2 = 0
print(clanEnMinus2)

clanEnMinus1 = 1
print(clanEnMinus1)

clanIzracunatUTrenutnojIteraciji = 0
while brojac < 98:
    clanIzracunatUTrenutnojIteraciji = clanEnMinus2 + clanEnMinus1
    print(clanIzracunatUTrenutnojIteraciji)
    clanEnMinus2 = clanEnMinus1
    clanEnMinus1 = clanIzracunatUTrenutnojIteraciji
    brojac = brojac + 1
    