# lista=[]
# i=0 #i je brojac

# while True:
#     a=int(input("unesi broj:"))
#     a=int(a)
    

#     if a!=5:
#         i+=1
#         lista.append(a)
#     else:
#         break

# while i<6: #sve dok je brojac manji od 6
#     lista.append(0)
#     i+=1

# i=0
# for element in lista:
#     print("[",i,"]=",element)
#     i+=1
    
lista=[]
brojac=0

while True:
    a=int(input("unesi brojeve u listu od 6 elemenata"))    
    
    if a!=5:  
        lista.append(a)
        brojac+=1
        print(lista)
    else:
        print("unijeli ste broj 5, lista se prekinula, preostali brojevi bit ce 0")
        break
        

while brojac<6:
    lista.append(0)
    brojac+=1

i=0
for element in lista:
    print([i], element)
    i+=1

print("ovo je lista brojeva sa njihovim indexima")        
