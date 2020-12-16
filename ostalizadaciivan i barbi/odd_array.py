#A = [9,3,9,3,9,7,9]
#A = [3,2,3,2,2,3,1,3]
#A = [3,2,3,2,3,2,3,4,3,2,3,2,3,2,3,2,3,5]
#A = [3,5,3,5,1,2,1,2,3]
A = [3,5,3,6,1,2,1,2,4,2,4]




if len(A) % 2 != 0: #dobijemo paran broj liste
    if len(A) == 1:
        print(A[0])
    else:
        if len (A) % 4 == 1:
            print(A[-1], "taj broj ispisujemo jer je on neparan clan bez para")
            A.pop(-1)

        if  len (A) % 4 == 2  or len (A) % 4 == 3:
            print(A[-2], "taj broj ispisujemo jer je on neparan clan bez para")
            A.append(A[-2])

if len(A) % 2 == 0: #dobijemo neparan broj liste
    if len(A) != 2:
        if len(A) % 4 != 0:
            print(A[-2],",",A[-1], "ispisujemo clanove parne, ali bez njihovog para")
            A.pop(-1)
            A.pop(-1)
            

        if len(A) % 4 == 0:
            for index in range(1, (len(A)-1), 4):
                a = A[index]
                A[index] = A[index+1]
                A[index + 1] = a
            
            
            for index in range(0, len(A), 2):
                if A[index] != A[index+1]:
                    print(A[index])

    else:
        if A[index] != A[index+1]:
                print(A[index])            
        
            

        # for element in range (1, len(A), 2):
        #     B = A.pop(element)
        #     print(A)
        #     print(B)
            

        # for index in range(0, len(A), 2):

        #     if index + 1 > len(A): 
        #         print(A[index])

        #     if A[index] != A[index+2]:
        #         print(A[index])

        


# for element in A:
#     c = A.index(element)
#    # print (A.index(element), end="")
#    # print (element, end="")
#    a=0
#    b=1
#     if A.index(element) != a and A.index(element) != b:
#         print(element)



#njegovo rijesenje sa interneta
#A = [9,3,9,3,9,7,9]

# def solution(A):     
#     if len(A) == 1:                 #ako je duljina niza jednaka 1 vrati nulti clan indeksa
#          return A[0]
#     A = sorted(A)                    #sortiraj listu
#     for i in range(0 , len (A), 2): #za index u rangu od nula do duljina, preskaci 2 mjesta
#          if i+1 == len(A):           #ako je drugi indeks jednak duljina vrati prvi clan
#              return A[i]
#          if A[i] != A[i+1]:          #ako je prvi clan razlicit od drugog vrati prvi
#              return (A[i])
#                                         #problem je zaustavljanje na prvom paru.... potrebno je ispisati taj par i nastaviti dalje sto se postize sa print a ne return!
# print(solution(A))

