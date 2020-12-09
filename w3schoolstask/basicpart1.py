#6
# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)

#7
# values=input("input some char with dot")
# ekst=values.split(".")
# print("ekstenzija:"+ repr(ekst[-1]))

#9
# exam_st_date = (1,12,2020)
# print( "The examination will start from : %i / %i / %i" % exam_st_date)

#10
# n=int(input("unei neki n:"))
# n1=int("%i" % n)
# print (n1)
# n2=int("%i%i" % (n,n))
# print(n2)
# n3=int("%i%i%i" % (n,n,n))
# print(n3)
# r=n1+n2+n3
# print(r)

# s=input("unesi recenice")
# c="mama"
# d="tata"
# a1=str("%s" % s)
# a2=str("%s%s" % (s,c))
# a3=str("%s%s%s" % (s,c,d))
# f=a1+a2+a3
# print(a1, " te ", a2 ," te " ,a3)

# s="srce veliko"
# c="svima blizu"
# d="tebi daleko"
# a1=str("%s" % s)
# a2=str("%s%s" % (s,c))
# a3=str("%s%s%s" % (s,c,d))
# f=a1+a2+a3
# print(a1,",", a2 ," to " ,a3)

#11
# print(abs.__doc__)

#12
# import calendar
# y=int(input("unesi godinu:"))
# m=int(input("unesi mjesec:"))
# print(calendar.month(y,m))

#14 igra datumima izracunavanje
# from datetime import date
# upoznali= date(2020,1,20)
# danasnji=date(2020,10,21)
# skupa=danasnji-upoznali
# print(skupa.days, "ukupno od upoznavanja do danas")
# uselili=date(2020,7,1)
# zajedno=danasnji-uselili
# print(zajedno.days,"odvojeno samo zajendo kod pocrnica")

#17
# def near_thousand(n):
#       return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))   
# print(near_thousand(2200))

#19
# def new_one(recenica):
#     if len(recenica) >=2 and recenica[:2]=="Is":
#         return recenica
#     return "Is" + recenica

# print(new_one("array"))
# print(new_one("IsEmpty"))

#20
# a=int(input("unesite broj ponavaljanja"))
# b=input("unesite rijec")
# for ponavljanje in range (a):
#     print(b,end="")

# def veci_string(rijec,n):
#     result=""
#     for brojac  in range(n):
#         result=result + rijec
#     return result
# print(veci_string(".mama",5))

#22
# array=["1","2","4","23","4","3","1"]
# a="4"
# n=0
# for brojac in array:
#     if a==brojac:
#         n+=1
#         print(brojac)
# print("u nizu se nalaze ukupno:",n)


# def usporedba(brojevi):
#     brojac=0
#     for broj in brojevi:
#         if broj==4:
#             brojac+=1
#     return (brojac)
# print(usporedba([1,4,6,7,4]))

#23

# def kopiranje(n,rijec):
#     a=rijec[0:2]
#     return (a*n)
# print(kopiranje(3,"mata"))
# print(kopiranje(2,'abcdef'))
# print(kopiranje(3,'p'))

#24
# def samoglasnik(slovo):
#     samoglasnici="aeiou"
#     if slovo in samoglasnici:
#         return slovo
# print(samoglasnik("e"))
# print(samoglasnik("b"))

#25
# def provjera(n,niz):
#     brojac=0
#     for broj in niz:
#         if n== broj:
#             brojac+=1
#     return brojac
# print (provjera(3,[1,5,3,8,3]))
# print(provjera(3,[3,1, 5,3, 8, 3]))
# print(provjera(-1,[5, 8, 3,-2,-1]))

#26
# def histogram (niz):
#     znak="@"
#     for broj in niz:
#         print (znak*broj)

# #print(histogram ([2,3,6,5]))
# print(histogram ([1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1]))

#27 stavljanje " " i str
# def kokate(niz):
#     lista= ""
#     for element in niz:
#         lista+=str(element)
#     return lista
# print (kokate([3,5,7,9]))

#28
# def parni(numbers):
#     a=237
#     for broj in numbers:
#         if broj == 237:
#             print(a)
#             break
#         if broj%2==0:
#             print(broj)


# print(parni(numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]))

#29
# a=set(["white","black","red"])
# b=set(["red", "green"])
# print(a.difference(b))
# print(a-b)

#30

# b=int(input("unesi bazu"))
# h=int(input("unesi visinu"))
# a=(1/2)*b*h
# print("opseg",a)

#31????????????????????????????????
# def sumica(x,y):
#     sumica=1

#     if x%y==0:
#         return y
#     for k in range(int(y/2),0,-1):
#         if x%k==0 and y%k==0:
#             sumica=k
#             break
#     return sumica
# print(sumica(12, 17))
# print(sumica(4, 6))

#32
#33
a=int(input("unesi 3znamenkasti broj"))
lista=[]
for a in range (3):
    if a in lista:
        brojac+=1
        break 
    else:
        lista.append(a)
        brojac=1





