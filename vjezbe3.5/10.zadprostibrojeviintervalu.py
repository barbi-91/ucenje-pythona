#unesi neka dva proizvoljna broja
#ispisi sve prste brojeve izmedu njih
brojac=0
a=int(input("unesi neki proizvoljni broj:"))
b=int(input("unesi jos neki proizvoljni broj:"))

for n in range (a, b+1):
    prim = True
    for x in range (a, n):
        if n % x == 0:
            prim= False
            break
    if prim==True:
        brojac+=1
print (brojac)