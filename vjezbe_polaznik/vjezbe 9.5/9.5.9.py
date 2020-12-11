# x^2+ y^2= z
from math import pow
lista=[]
for x in range (41):
    # print("*")
    for y in range (41):
        # print("+")
        for z in range (41):
            # print("!")
            if (pow(x,2)+pow(y,2))==z:   #ZAKAJ IF
                izlaz=[x,y,z]           #da napravimo uvjet za punjenje varijeble liste
                lista.append(izlaz)
                
#ispisivanje liste         
for element in lista:   
    print(element)      