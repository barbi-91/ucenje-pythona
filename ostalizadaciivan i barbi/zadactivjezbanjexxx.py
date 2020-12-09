# temperatura = [17, 23, 12, 15, 19, 21, 25]
# minimalna=min(temperatura)
# print(minimalna)
# maksimalna=max(temperatura)
# print(maksimalna)
# razlika=maksimalna-minimalna
# print(razlika)


# visine_djevojcica = [165, 153, 155, 155, 157]
# visine_djecaka = [170, 168, 173, 156, 172]


# visina= visine_djevojcica + visine_djecaka
# print(len(visina))
# print (sum(visina)/len(visina))


# cijene=[1420,1799,1569]
# print(cijene, "nesortirano")
# cijene.sort()
# print(cijene, "sortirano")
# cijene[0]=1   #zamjena prve najnize sa 1kunom
# print(cijene, "sa 1com")
# print(sum(cijene),"suma sa 1com")


# cijene = [58.00, 104.95, 117.50, 11.95, 10.4, 37.95, 85.5]
# suma1=sum(cijene)
# print(suma1)
# cijene.sort()
# print(cijene)
# suma2=sum(cijene[:3])
# print(suma2)
# suma3=sum(cijene[-3:])
# print(suma3)

# a=input("unesi ime")
# if a.endswith("a"):
#     print("zensko ime")
# else:
#     print("musko ime")

# #ili

# a=input("unesi ime")
# if a[-1]=="a":
#     print("zensko")
# else:
#     print("musko")

# a=input("unesi prvu rijec")
# b=input("unesi drugu rijec")
# c=len(a)
# d=len(b)
# print(c,d)
# if c>d:
#     print("prva rijec je duza")
# elif d>c:
#     print("druga rijec je duza")
# else:
#     print("obje su jednako duge")

# a=input("upisi rijec:")
# b=a.replace("a", "o")
# print(b)

# a=input("upisi recenicu")
# b=a.replace("is","was")
# print(b)

# a=input("unesi rijec")
# if a.endswith("ka"):
#     print("Kaladont")
# else:
#     print("dalje:")

# a=input("unesi rijec")
# if a.endswith("o"):
#     print("srednji rod")
# elif a.endswith("a"):
#     print("zenski rod")
# else:
#     print("muski rod")



# i=input("unesi lozinku")
# a=len(i)
# if a<8:
#     print("slaba lozinka")
# else:
#     print("jaka lozinka")

# u=input("unesi Korisnicko ime")
# l=len(u)
# if l<1:
#     print("niste upisali korisnicko ime")
# else:
#    print("Pozdrav", u)


# u= input("unesi svoju nadrazu rijec")
# l=len(u)
# print("tvoja rijec ima", l, "slova")
# if l >=7:
#     print("rijec je duga")
# else:
#     print("rijec je kratka")

# lista = [2,27,35,17]
# a = int(input("Unesi jedan broj")) 
# if a in lista:
#     print("Uneseni broj se nalazi u listi") 
# else:
#     print("Uneseni broj se ne nalazi u listi")

# ljubimci = ["pas", "mačka", "papagaj", "zec", "kornjača"]
# for i in [1,3]:
#     print(ljubimci[i])

# ljubimci = ["pas", "macka", "papagaj", "zec", "kornjaca"]
# for i in range(3):
#     print(ljubimci[i])

# lista = [-3, 5, 16, 5, -2]
# s = 0
# for x in lista:
#     s = s + x
#     print(s)

# ista = [22, 20, 21, 24, 15, 19]
# s = 0
# for x in lista: 
#     if x % 2 == 0: 
#         s = s + x 
#         print(s)


# r = []
# slova = "abcdefghijklmnoprstuvz"
# for x in slova:
#     r[x] = 0



# niz=[0]*5
# for i in range (0,5):
#     niz[i] = int(input("unesi broj"))
# for i in range (0,5):
#     print(niz[i])

# zbroj=0
# lista=[0]*10
# for i in range(0,10):
#     lista[i]=lista[i]+1
# for i in range(1,10,2):
#     zbroj= zbroj + lista[i]
# for i in range(0,10):
#     print(lista[i])
# print("zbroj parnih brojeva", zbroj)

# popis = [87, 74, 25, 26, 46]

# print(min(popis))
# lista=[4, 1, 3, -5]
# print( sum( lista ) / len( lista ) )

# lista = ['Marko Marković', 'Ivan Ivić', 'Petar Petić', 'Ivan Tot', 'Mario Car', 'Ivan Nađ']
# print (lista.index("Ivan Tot"))

# l= ['Marko Marković', 'Ivan Ivić', 'Petar Petić', 'Ivan Tot', 'Mario Car', 'Ivan Nađ']
# k = l.index( "Mario Car" ) 
# print( l[ k-1 ] )

# l = [13, 11, 18]
# k = [13, 16, 15]
# n = l + k 
# print( n )

# def unos():
#     a = int(input("unesi neki broj"))

# print("poziv funkcije")
# for i in range(1,5):
#     unos()

# def zbroj():
#     a=int(input("unesi broj a"))
#     b=int(input("unesi broj b"))
#     c=(a+b)
#     print("zbroj dva broja je:",c)

# for i in range(1,4):
#     zbroj()

# def paran(a):
#     if a % 2 == 0:
#         print("paran broj")
#     else: 
#         print("broj je neparan")

# def negativan(a):
#     if a<0:
#         print("broj je negativan")
#     else:
#         print("broj je pozitivan")

# for i in range(1,4):
#     unos= int(input("unesi neki broj"))
#     paran(unos)
#     negativan(unos)

