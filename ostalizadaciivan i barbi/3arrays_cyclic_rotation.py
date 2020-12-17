A = [3, 8, 9, 7, 6]
#A = [1,2,3,4]
#A = [0,0,0]

######prva verzija#########
# print(A, "pocetna lista")
# korak = 4
# print("vrtimo", korak, "puta")
# B = []

# for element in range (0,korak):
#     B.append(A.pop(-1))
#     print(" >>> izbacujemo zadnji broj", B)
#     A.insert(0,B.pop(0))
#     print(A, "sada je zadnji prvi", "\n")


#######druga verzija#############
korak = 4
print(A, "pocetna lista")
for i in range (len(A)-1,((len(A)-1)-korak),-1):
    a = A.pop(-1)
    A.insert(0,a)
    print(A, "lista nakon promjene broja",a, "sa zadnjeg na prvo mjesto")


