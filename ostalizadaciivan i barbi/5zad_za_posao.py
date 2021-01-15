# # Napisi metodu string solution(int N) koja vraća string
# # duljine N takav da je u njemu uvijek neparni broj znakova,
# # string smije sadržavati samo znakove [a, b, c, d], npr.:
# #da se neparni broj puta ponavllja isto slovo uu jednoj rijeci!

# # 		N = 1, string je "a" ili "b" ili "c"...
# # 		N = 2, string je "ab" ili "bc"...
# # 		N = 3, string je "abc" ili "bcd" ili "aaa"...
# # 		N = 4, string je "abcd" ili "ss
# # 		N = 5, string je "abccc" ili "aaabc" ili "abbbc" ili "bcddd"...
# # 		N = 6, string je "aaabbb" ili "aaaaab"...


#kod s rekurzijom
# import random
# N = int(input("unesi broj duljine stringa:"))
# def ispis_koda(N):
#     lista = []
#     brojac1 = 0
#     brojac2 = 0
#     brojac3 = 0 
#     brojac4 = 0

#     for element in range(0,N,1):
#         x = random.randrange(1,5)
#         if x == 1:
#             x = "a"
#             brojac1 += 1
#         if x == 2:
#             x = "b"
#             brojac2 += 1
#         if x == 3:
#             x = "c"
#             brojac3 += 1
#         if x == 4:
#             x = "d"
#             brojac4 += 1
#         lista.append(x)
#     if brojac1 % 2 == 0 or brojac2 % 2 == 0 or brojac3 % 2 == 0 or brojac4 % 2 == 0:
#         ispis_koda(N)
#     else:
#         print(lista)
# ispis_koda(N) 

N = int(input("unesi broj duljine stringa"))
lista = ["a","b","c","d"]

if N % 2 == 0:
    print((N-1)*lista[0]+lista[1])
else:
    print(N*lista[0])