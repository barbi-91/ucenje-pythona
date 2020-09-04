lista=[]
i=0

while True:
    a=int(input("unesi broj:"))
    a=int(a)

    if a!=5:
        i+=1
        lista.append(a)
    else:
        break

while i<6:
    lista.append(0)
    i+=1
print(lista)
