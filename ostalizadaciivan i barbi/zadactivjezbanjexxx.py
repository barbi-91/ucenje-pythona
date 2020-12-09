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

# def zbroj(n):
#     s=0
#     for i in range (1, n+1):
#         s=s+i
#     return s

# def unos():
#     n=int(input("unesi neki broj"))
#     print(zbroj(n))
# unos()


# def zbroj_slova(s):
#     d=len(s)
#     br=0
#     for i in range(d):
#         if s[i]=="A" or s[i]== "a":
#             br=br+1
#     return br
# tekst=input("unesi tekst:")
# print ("broj pojavljivnja slova a", zbroj_slova(tekst))


# def unos(niz):
#     for i in range(0,5):
#         niz[i]=int(input("unesi neki niz"))

# def ispis(niz):
#     for i in range (0,5):
#         print(niz[i])

# niz=[0]*5
# unos(niz)
# ispis(niz)

# def f(a):
#     return - 3 * a

# print(f(0) - f(-1))

# def f(a):
#     return 2 * a + 3

# print(f(-2) - f(f(2)))

# def f(a):
#     if a % 5 == 0:
#         return 2 * a
#     else:
#         return a + 1

# m = int(input("unesi cijeli broj"))
# print(f(m))

# def vrijeme(a): 
#     s = a // 60 
#     m = a % 60
#     return s,m


# x = int(input("Unesi koliko minuta je Edita čitala knjigu")) 
# vrijeme(x)
# # m = int(input("unesi cijeli broj"))
# print(vrijeme(x))

# def f(l,n):
#     return l + n

# print(f(11,22)," ",f("11","22")) 

# def f(l,n):
#     return l * n

# print(f(2,"3"))

# def f(a):
#     return a*a

# print([f(x) for x in range (4,11)])

# def dvocifren(a):
#     d = a // 10
#     j = a % 10	
#     return j + d

# c=34
# print(dvocifren(c))

# taj me orginal zbunio# # # def opseg(o):
# # #     return o[0] + o[1] + o[2]

# # # trokuti= [(3,4,5),(5,12,13),(7,24,25)]
# # # for trokut in trokuti:
# # #     print(opseg(trokut))


# def povrsina(a):
#     return a[0]*a[1]
# pravokutnik=[(3,9),(4,9),(5,10)]
# for p in pravokutnik:
#     print(povrsina(p))

# def formirajlistu(n):
#     lista = []
#     for i in range(2,n,2):
#         lista.append(i)
#     return lista

# print(formirajlistu(8))


# def formirajListu():
#     b = []
#     a=int(input("unesi broj"))
#     for i in range (a, a+11):
#         b.append(i)
#       print(b())

# formirajListu()

#ili

# ?????

# a=4
# b=5
# print("{:5}{:10}{:5.2f}".format(a,b,a+b))
# # a=5
# # b=4
# # c=a+b
# # print("{:11}".format(a))
# # print("{}{:10}".format("+",b))
# # print("{:20}".format("________________"))
# # print("{:11.1f}".format(c))

# strijelci = {"Mesi", "Ronaldo", "Mesi", "Ibrahimović", "Ibrahimović", "Nejmar", "Nejmar"}
# print(strijelci)
# golovi = ["Mesi", "Ronaldo", "Mesi", "Ibrahimović", "Ibrahimović", "Nejmar", "Nejmar"]
# strijelci = set(golovi) 
# print(strijelci)

# ritmicka = {"Ana", "Marica", "Ivana", "Gordana"}
# odbojka = {"Tara", "Nada", "Marica", "Ivana", "Aleksandra"} 
# dva_sporta = ritmicka & odbojka
# bar_jedan_sport = ritmicka | odbojka 
# samo_odbojka = odbojka - ritmicka 

# print(dva_sporta) 
# print(bar_jedan_sport) 
# print(samo_odbojka)

# vocarna={1001:"Jabuka",1002:"Kruška",1003:"jagoda",1004:"Banana",1005:"kivi"}
# for kljuc,vrijednost in vocarna.items(): 
#     print(kljuc," - ",vrijednost)


# cijeneAuta={"golf":234,"mazda":145,"seat":456, "citroen":345}
# auto= input("unesi model automobila")
# cijena=()
# print(cijeneAuta[auto])


# gradovi= {"Zagreb":(44,20),
#     "Budimpesta":(47, 19),
#     "Beč": (48.2082, 16.3738),
#    
#  "Bratislava": (48.1486, 17.1077)}

# grad= input("unesi ime grada:")
# kordinate=()
# print(gradovi[grad])

# gradovi= {"hrv": "zagreb, split, osijek",
# "njem":"berlin, munchen,karlsluhe", 
# "slo":"maribor, ljubljana, ptuj" }

# zemlja = input("unesi ime zemlje")
# if zemlja in gradovi:
#     print(gradovi[zemlja])
# else:
#     print("nepoznata zemlja")

# brojDana= {"sijecanj":31, "veljaca":28, "ozujak":31, "travanj":30, "svibanj":31, "lipanj":30}
# mjesec= input("unesi ime mjeseca za koji trazis broj dana:")
# if mjesec in brojDana:
#     print(brojDana[mjesec])
# else:
#     print("nepoznat mjesec", mjesec)

# a= {32, 1, 41, 12, 46, 19, 27, 30}
# b = {33, 1, 41, 43, 48, 22, 28, 29}
# c = a & b 
# d = c - {1}
# print( len(d) )

# p = (177,75)
# print(p[1])

# s = {'a8': 12.0}
# lista = [] 
# for x in s:
#     lista.append(s[x]) 
#     print(lista)


# for red in range(0,4):
#     for stupac in range(0,5):
#         print(end="*")
#     # print("\n") 
        
#     print("")

# for red in range(0,4):
#     for stupac in range(red):
#         print(end="?")
#     # print("\n") 
        
#     print("")

# for red in range(1,11):                       :=)
#     for stupac in range(1,11):
#         c=red * stupac
#         if c<10:
#             print ("   ",c, end=" ")
#         elif c>=10:
#             print ("  ",c, end=" ")
#         elif c>=100:
#             print (" ",c,end=" ")
#     print("")
# **********************************************
# niz = [2, 7, 1, 0, 6]
# for broj in niz:
#     print(broj, end="")

# duljina=len(niz)
# for elementNiza in range(0,duljina-1):  #o do 4 jer su 4 usporedbe
#     for sljedeciElement in range (elementNiza+1,duljina): #ukupno 0+1 do 4
#         print("\n")
#         print (niz[elementNiza])
#         print(niz[sljedeciElement])
#         if (niz[elementNiza]>niz[sljedeciElement]):
            
            
            
#             b=niz[elementNiza]
#             print(b ,"je b")
#             niz[elementNiza]=niz[sljedeciElement]
#             print(niz[elementNiza], "je prvi")
#             niz[sljedeciElement]=b
#             print(niz[sljedeciElement], "je drugi")
#             print(niz, end="")
#     print("")

# for k in niz:
#     print("****",k,end="*")
# ************************************************

# lista=[]
# broj= int(input("unesite broj elemenata koliko zelite unijeti"))
# print("unesite elemente u listu")
# for k in range (broj):
#     lista.append(int(input()))
# print("nesortirana lista", lista)

# for i in range(0,len(lista)):
#     for j in range(i+1, len(lista)):
#         if lista[i]>lista[j]:
#             b=lista[i]
#             lista[j]=lista[i]
#             lista[i]=b
# print(lista,"nova lista")

#************************************************

def bubleSort(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                b=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=b


lista=[6,2,3,7,0,1]
bubleSort(lista)
print(lista)