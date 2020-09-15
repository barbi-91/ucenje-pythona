lista=[]
brojac=0
n=0

while True:
    n=int(input("upisi element u listu:"))
    if n != 5:
        
        lista.append(n)
        brojac+=1   
    

    else:

        print("nevazeci broj")
        break
print(lista, "orginalna lista")

lista.reverse()    #obrnuta lista
print(lista, "obrnuta lista")

    
   S
