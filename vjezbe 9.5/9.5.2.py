lista=[]#kreiranje prazne liste
while True:#kad je zadovoljen uvrijet
    a=input("unesi neku vrijednost")#unos s tipkovnice
    a=int(a)#naznacit da je int

    if a!=5:#uvijet
        lista.append(a)#pod idejom da on puni listu
        print(lista)#provjera puni li se lista zaista
    else:#u suprotonom 
        print("UNESENA VRIJEDNOST JE 5, PROGRAM SE PREKIDA")
        break#dolazi do poruke i program se prekida
    