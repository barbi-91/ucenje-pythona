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
# print(lista)

lista=[]
brojac=0

while True:
    a=int(input("unesi brojeve u listu od 6 elemenata"))    
    
    if a!=5:  
        lista.append(a)
        brojac+=1
    else:
        break

while brojac<6:
    lista.append(0)
    brojac+=1
print(lista)
        
#poanta je u brojacu, treba svaku petlju while zavrsiti sa brojacem kako bi on zapmtio za slijedecu petlju gdje je stao racunati
#while petlje se okrecu po zadanom brojacu...nastavljaju u slj petlji po brojacu...nemoze se kombinirati range i while...isprobano je..
        
