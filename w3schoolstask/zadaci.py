

# 2
# word="mamabaka"
# characters={}
# for character in word:
#     if character in characters:
#         characters[character] += 1
#     else:
#         characters[character] =  1
# print(characters)

# 2 
# rijec="mama"
# slova={}
# for slovo in rijec:
#     if slovo in slova:
#         slova[slovo]+=1
#     else:
#         slova[slovo]=1
# print(slova)

#3
# b=input("unesi rijec")
# a=len(b)
# if a==2:
#     print(b+b)
# elif a==1:
#     print("empty string")
# else:
#     print(b[0:2]+b[-2:])

#4 moja verzija ako se slova pojavljuju ona se zmijenjuju sa dolarznakom
# rijec="restart"
# isti=[]
# for slovo in rijec:
#     if slovo in isti:
#         isti.append("$")
#     else:
#         isti.append(slovo)
# print(isti)

# #4 MOJE-sva slova unutar rijeci koja su ista prvom slovu promijeniti u dolar
# rijec="restart"
# brojac=0
# slovo1=rijec[0]
# for slovo in rijec:
#     if slovo==slovo1:
#         brojac=brojac+1
#         if brojac<2:
#             print(slovo, end="")
#         if brojac>=2:
#             print("$",end="")       
#     else:
#         print(slovo,end="")

# print("****************")

# #4 NJIHOVO
# def change_char(str1):
#   char = str1[0]
#   str1 = str1.replace(char, '$')
#   str1 = char + str1[1:]

#   return str1

# print(change_char('restart'))    



# #5 MOJE
# a=input("prvi string")
# b=input("drugi string")

# c= a[:2]+b[2:]+b[:2]+a[2:]
# print(c)

#6
# a="ing"
# b=input("unesi string")
# c="ly"

# if b[-3:]=="ing":
#     d=b+c
#     print(d)
# else:
#     d=b+a
#     print(d)

#7



#8
# def pronadi_rijec(lista_rijeci):
#     rijec_duljina=[]
#     for n in lista_rijeci:
#         rijec_duljina.append((len(n),n))
#     rijec_duljina.sort()
#     print(rijec_duljina[-1][1])
#     return rijec_duljina[-1][1]

# print(pronadi_rijec(["mama","tattinko","cigan"]))

#9
# def remove_char(str, n):
#       first_part = str[:n] 
#       last_part = str[n+1:]
#       return first_part + last_part
# print(remove_char('Python', 2))
# print(remove_char('Python', 3))
# print(remove_char('Python', 5))

#10
# a=input("unesi rijec")
# ap=a[0]
# az=a[-1]
# ai=a[1:-1]
# c=az+ai+ap
# print(c)

# #ili funkcija
# def change_string(string):
#     return(string[-1]+string[1:-1]+string[0])

# print(change_string("abcd"))

#11
# lista=[]
# def neparan(rijec):
#     duljina=len(rijec)
#     for slovo in range(0,duljina,2):
#         lista.append(rijec[slovo])
#     return lista

# print(neparan("abcdef")

#12  upisati- vadenje rijeci iz recenice splitajem i brojacem u dictionaryu
# brojac=0
# def duple_rijeci(recenica):
#     brojac=dict()
#     rijeci=recenica.split()

#     for rijec in rijeci:
#         if rijec in brojac:
#             brojac[rijec]+=1
#         else:
#             brojac[rijec]=1
#     return brojac
        
# print(duple_rijeci("ova recenica se ponavlja ako se ponavlja"))


# #13
# a=input("unesi recenicu")
# print(a.lower())
# print(a.upper())

#14 upisati
# rijeci=input("unesizarezom odvojenu recenicu rijeci")
# rijeci=[rijeci for rijec in rijeci.split(",")]
# print(",".join(sorted(list(set(rijeci)))))

# #15
# def add_tags(tag, word):
#     return "<%s><%s></%s>" % (tag, word,tag)

# print(add_tags("b","Barby_stranica"))

#16 MOJE
# def polovljenje(recenica):
#     rijeci=recenica.split()
#     print(rijeci)
#     polovica=len(rijeci)//2
#     print(polovica)
    
#     prva=rijeci[:polovica]
#     print(prva)
    
#     druga=rijeci[polovica:]
#     print(druga)
#     lista=[]
#     rijec=("pepeljaste")
#     lista.append(rijec)
#     print(lista)

#     a=prva,rijec,druga
#     return a

# print(polovljenje("maca je bijele boje zelenih ociju"))
# print("====")
# print(polovljenje("danas je preletjela sova boje koje se prelijevaju"))


#16 njohovo UZ PREBRAJANJE SLOVA A MOOJE RADI AUTOMATSKI
# def insert_string_middle(str, word):
#     return str [:15]+ word+" "+  str[15:]

# print(insert_string_middle("MACA JE BIJELE BOJE I ZELENIH OCIJU","PEPELJASTE"))

#17
# def coppy_last_char(string):
#     a=string[-2:]
#     return (a)*4

# print(coppy_last_char("python"))

#18
# def first_char(string):
#     a=string[:3]
#     return (a) if len(string) > 3 else string
# print(first_char("Python"))
# print(first_char("mama"))
# print(first_char("sonjaibik"))
# print(first_char("Py"))

#19
# string="https://www.w3resource.com/python-exercises/string"
# print(string.rsplit("/",1)[0])

# string="barbara erdec"
# print(string.rsplit("a",1)[1])
# print(string.rsplit("e",2)[0])

#20
# def reverse_string(str1):
#     if len(str1)>2:
#         return " ".join(reversed(str1))
#     return str1


# print(reverse_string("barbara"))

#20
# def obrnuta(recenica):
#     if len(recenica)>2:
#         return " ".join (reversed(recenica))

# print(obrnuta("ja sam recenica sa razmacimai obrnuta sam"))

# #21 ispisati
# def velika(recenica):
#     num_upper=0
#     for slovo in recenica[:4]:
#         if slovo.upper()==slovo:
#             num_upper +=1
#     if num_upper >=2:
#         return recenica.upper()
#     return recenica

# print(velika("PytHon"))

# #22 ispisati
# string="w3resbouaArAcBe"
# a=sorted(string.upper())
# #svi postaj lower ili upper a ispod metdom zadrzavaju mijesani oblik
# print(a)

# def slovarica(string):
#     temp = sorted(string)
#     #return(temp)
#     return sorted(sorted(temp=, key=str.upper)
  
# test = "w3resbouaArAcBe"
# print(slovarica(test))

# #23 micanje praznog reda ispisati
# rijec='Python Exercises\n'
# print(rijec)
# print(rijec.rstrip())

# #24 ispis
# slova="m4skejdaj"
# print(slova.startswith("jk3l4"))
# print(slova.startswith("m4s"))


#25 caesar enkripcija ispis

# def caesar_enkripcija(kod,korak):
#   output=[]
#   kod1=[]
#   velika = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#   mala = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#   for slovo in kod:
#     if slovo in velika:
#       index=velika.index(slovo)
#       kodiranje=(index + korak)%26
#       kod1.append(kodiranje)
#       slovo1=velika[kodiranje]
#       output.append(slovo1)

#     elif slovo in mala:
#       index=mala.index(slovo)
#       kodiranje=(index + korak) %26
#       kod1.append(kodiranje)
#       slovo1=mala[kodiranje]
#       output.append(slovo1)
#   return output

# print(caesar_enkripcija("„Na svijetu uvijek postoji jedna osoba koja čeka onu drugu, bilo da je nasred pustinje ili usred velikog grada. A kad se te osobe sretnu i njihovi se pogledi ukrste, prošlost i budućnost gube svako značenje. Postoji taj trenutak i nevjerojatna sigurnost da je sve stvari pod suncem ispisala jedna ista ruka, ruka koja je stvorila po jednu dušu, blizanku za svaku osobu.-P.C.", 28))


#26 #27 #28 #29
# import textwrap
# sample_text=("""„Na svijetu uvijek postoji jedna osoba koja čeka onu drugu, bilo da je nasred pustinje ili usred velikog grada. A kad se te osobe sretnu i njihovi se pogledi ukrste, prošlost i budućnost gube svako značenje. Postoji taj trenutak i nevjerojatna sigurnost da je sve stvari pod suncem ispisala jedna ista ruka, ruka koja je stvorila po jednu dušu, blizanku za svaku osobu.""")
# print()
# b=textwrap.wrap(sample_text, width=20)
# a=textwrap.fill(sample_text, width=20)
# c=textwrap.indent(sample_text, "ivan mic ")
# d=textwrap.dedent(c)
# print(b)
# print(a)
# print(c)
# print(d)
# print()

#30
# x=3.14159267498257497589275897495278933792879857349857298
# y=12.99999

# print("\nOriginal Number: ", x)
# print("Formatted Number:","{:.2f}".format(x));
# print("Original Number: ", y)
# print("Formatted Number:", "{:.2f}".format(y));
# print("formatiranje broja:", "{:10f}".format(x));

#31
# x=3.14
# y=-3.99
# print("formatiranje:","{:+.2f}".format(x))
# print("formatiranje:","{:+.2f}".format(y))

#32
# x = 3.1415926
# y = -12.9999
# print("\nOriginal Number: ", x)
# print("Formatted Number with no decimal places: "+"{:+.0f}".format(x));
# print("Original Number: ", y)
# print("Formatted Number with no decimal places: "+"{:+.0f}".format(y));
# print()

#33
# x = 3
# y = 123
# print("\nOriginal Number: ", x)
# print("Formatted Number(left padding, width 2): "+"{:*>2d}".format(x));
# print("Original Number: ", y)
# print("Formatted Number(left padding, width 6): "+"{:*>6d}".format(y));
# print()

# #34
# x = 3
# y = 123
# print("\nOriginal Number: ", x)
# print("Formatted Number(right padding, width 2): "+"{:*< 3d}".format(x))
# print("Original Number: ", y)
# print("Formatted Number(right padding, width 6): "+"{:*< 7d}".format(y))
# print()

#35 , separator
# x = 3000000
# y = 30000000
# print("\nOriginal Number: ", x)
# print("Formatted Number with comma separator: "+"{:.}".format(x))
# print("Original Number: ", y)
# print("Formatted Number with comma separator: "+"{:,}".format(y))
# print()

#36
# x = 0.25
# y = -0.25
# print("\nOriginal Number: ", x)
# print("Formatted Number with percentage: "+"{:.2%}".format(x))
# print("Original Number: ", y)
# print("Formatted Number with percentage: "+"{:.2%}".format(y))
# print()

#37
# x = 22
# print("\nOriginal Number: ", x)
# print("Left aligned (width 10)   :"+"{:*<10d}".format(x));
# print("Right aligned (width 10)  :"+"{:*>10d}".format(x));
# print("Center aligned (width 10) :"+"{:*^10d}".format(x));
# print()

#38
# recenica = 'The quick brown fox jumps over the lazy dog.'
# print()
# print(recenica.count("fox"))
# print()

# def ponavljanje (recenica):
#     recenica.count()

# print(ponavljanje("The quick brown fox jumps over the lazy dog.'"))

#39
# def obrnutiniz (recenica):
#     glue="."
#     return glue.join(reversed(recenica))
    

# print(obrnutiniz("javascript"))

#40
# def obrnutiniz (text):
#     for rijec in text.split("\n"):
#         print(text.split())
#         a=rijec.split()
    
#         d=a[::-1]
#         return (d)
    
# def obrnutaslova(text):
#     glue=","
#     return glue.join(reversed(text.split()))

# print(obrnutiniz("ovo je obrnuta recenica"))
#print(obrnutaslova("ovo je obrnuta"))

#41
# def samoglasnici(recenica):
#     vowelList = ['a','e','i','o','u']
#     for slovo in recenica:
#         if slovo not in vowelList:
#             print(slovo, end=" ")

# print (samoglasnici("The quick brown fox"))

# def strip_chars(recenica, char):
#     return " ".join(letter for letter in recenica if letter not in char)
# print("\nOriginal String: ")
# print("The quick brown fox jumps over the lazy dog.")
# print("After stripping a,e,i,o,u")      
# print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))
# print()

#42
# def counter (recenica):
#     dict={}
#     for slovo in recenica:
#         keys=dict.keys()
#         if slovo in keys:
#             dict[slovo]+=1
#         else:
#             dict[slovo]=1
#     return dict

# print(counter("jasammalajabukamedena"))

import collections
str1 = 'aaabbcddddee'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted(d, key=d.get, reverse=True):
  if d[c] > 1:
      print('%s %d' % (c, d[c]))