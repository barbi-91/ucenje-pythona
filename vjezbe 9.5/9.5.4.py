lista=[]
i=0 #i je brojac

while True:
    a=int(input("unesi broj:"))
    a=int(a)
    

    if a!=5:
        i+=1
        lista.append(a)
    else:
        break

while i<6: #sve dok je brojac manji od 6
    lista.append(0)
    i+=1

i=0
for element in lista:
    print("[",i,"]=",element)
    i+=1
    
