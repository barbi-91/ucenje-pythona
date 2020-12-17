# Napisi metodu string solution(int N) koja vraća string 
# duljine N takav da je u njemu uvijek neparni broj znakova, 
# string smije sadržavati samo znakove [a, b, c, d], npr.:
#da se neparni broj puta ponavllja isto slovo uu jednoj rijeci!

# 		N = 1, string je "a" ili "b" ili "c"...
# 		N = 2, string je "ab" ili "bc"...
# 		N = 3, string je "abc" ili "bcd"...
# 		N = 4, string je "abcd"
# 		N = 5, string je "abccc" ili "aaabc" ili "abbbc" ili "bcddd"...
# 		N = 6, string je "aaabbb" ili "aaaaab"...

import random
N = int(input("unesi broj duljine stringa:"))  
def ispis_koda(N):
    lista = []
    
for element in range(1, N+1):
    x = random.randrange(1,5)

    if x == 1:
        x = a
    if x == 2:
        x = b
    if x == 3:
        x = c
    if x == 4:
        x = d
    lista.append(x)

    for slovo in lista:
        if slovo == a:
            tmp = a
            a = tmp + 1
        if slovo == b:
            tmp = b
            b = tmp + 1
        if slovo == c:
            tmp = c
            c = tmp + 1
        if slovo == d:
            tmp = d
            d = tmp + 1
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0 and d % 2 == 0:
        ispis_koda(N)
ispis_koda(N) 






