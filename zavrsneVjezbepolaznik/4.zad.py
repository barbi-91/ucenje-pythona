lista=[]
while True:
    x= input("unesi neki broj")
    if x<="0":
        break
    else:
        lista.append(x)
        print(lista)
print(lista)

sumaelemenata=[]
for element in lista:
    suma=0
    for brojElementa in element:
        brojElementa=int(brojElementa)
        suma=suma+brojElementa
    sumaelemenata.append(suma)
lista.sort()
print(lista[0], "ovo je najmanji broj unesen")
print(sumaelemenata, "ovo je suma upisanih pojedinacnih brojeva")
sumaelemenata.sort()
print(sumaelemenata, "ovo je suma sortiranih pojedinacnih brojeva")
print(sumaelemenata[0], "ovo je najmanja suma")



# #pokusaj resenja
# #  # # # lista=[]

# # # # cijeliBroj=int(input("unesi cijeli broj:"))
# # # # i=0

# # # # for i in lista:
# # # #     i+=1
# # # #     if cijeliBroj>0:
# # # #         lista.append(cijeliBroj)
# # # #         print(lista)
    
# # # #     else:
# # # #         print("broj je manji od 0")

# # # # #koji od ucitanih brojeva ima najmanju sumu znamenki
# # # # #  te ispisite taj broj i sumu!


# #********************************************************************rijesenje skripta
# # def sumaZnamenki(x):
# #     suma=0

# #     while x >0:
# #         suma += x%10

# #         x/=10
# #         x=int(x)
        

# #     return suma

# # najmanji =0
# # najmanjaSuma=-1

# # while True:
# #     x=int(input("unesite broj: "))
    

# #     if x <=0:
# #         break

# #     s = sumaZnamenki(x)

# #     if najmanjaSuma==-1 or najmanjaSuma > s:
# #         najmanjaSuma= s
# #         najmanji=x
# # print("Broj:", najmanji)
# # print("Najmanja suma znamenki:", int(najmanjaSuma))
# #*******************************************************

# lista=[]
# while True:
#     broj = input("Unesite broj: ")
#     if broj == '0':
#         break
#     else:
#         lista.append(broj)

# # '12', '554', '67'
# # 1+2, 5+5+4, 6+7
# # 3, 14, 13 - sortirati i uzeti prvog (najmanjeg)

# listOfElementSums = []
# for element in lista:
#     elementSum = 0
#     for letter in element:
#         elementSum = elementSum + int(letter)
#     listOfElementSums.append(elementSum)

# listOfElementSums.sort()

# print(listOfElementSums[0])


# #**************************************************
# # number = 335
# # letters = []
# # while number > 0:
# #     letter = number % 10
# #     number /= 10
# #     number = int(number)
# #     letters.append(letter)

