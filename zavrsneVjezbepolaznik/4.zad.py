# lista=[]

# cijeliBroj=int(input("unesi cijeli broj:"))
# i=0

# for i in lista:
#     if cijeliBroj>0:
#         lista.append(cijeliBroj)
#         print(lista)
#         i+=1
#     else:
#         print("broj je manji od 0")

a=int(input("unesi neki broj a"))
for i in range(a,0,-1):
    print(i, end=" ")

print("\n")

b=int(input("unesi neki broj b"))
while b>0:
    print (b, end=" ")
    b-=1