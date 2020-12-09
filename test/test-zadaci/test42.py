# # #Animal is-a object
# # class Animal(object):
# #     pass
# # #class Dog is-a Animal
# # class Dog(Animal):
# #     def _init_(self, name):
# #     #class Dog(is-a Animal) has-a _init_that takes self and name parameters
# #         self.name = name
# #     #from self get name varibale and set it to name
# # #clas Cat is-a Animal
# # class Cat(Animal):
# #     def _init_(self, name):
# #     #class Cas(is-a Animal) has-a init that takes self and name parameter
# #         self.name = name
# # class Person(object):
# #     def _init_(self, name):
# #         self.name = name
# #         self.pet = None
# #
# # class Employe(Person):
# #     def _init_(self, name,salary):
# #         super(emplye, self)._init_(name)
# #         self.salary = salary
# #
# # class Fish(object):
# #     pass
# # class Salamon(object):
# #     pass
# # class Halibut(Fish):
# #     pass
# #
# #
# # rover = Dog ("Rover");
# # satan = Cat ("Satan");
# # mary = Person ("Mary");
# # mary.pet = satan
# # frank = Employe("Frank", 120000)
# # frank.pet = rover
# # flipper = Fish()
# # crouse = Salamon()
# # harry = Halibut()
#
#
# #
# # class Animal(object):
# #     def __init__(self, atribut):  #ucestal greska...iit ima dva underscora i ispicuje,.... class take no argoment
# #         self.atribut = atribut
# #
# #     def plivati(self):
# #         for tekst in self.atribut:#pravilne gramticke rijeci
# #             print(tekst)
# #
# # varijabla1 = Animal(["ovo je klasa animal"])
# #
# # varijabla2 = Animal(["ovo je isto"])
# #
# # varijabla1.plivati()
# # varijabla2.plivati()
#
#
# class Animal():
#     def __init__(self, tekst):
#         self.tekst = tekst
#     def plivati(self):
#         print(self.tekst.title(), "u funkciji")
# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name.title() + ' is now sitting.')
#
#     def roll_over(self):
#         print(self.name.title() + ' is now rolling over.')
#
# my_cat = Animal("Maca")
# my_dog = Dog('Willie', 6)
# print("my dog's name is " + my_dog.name.title() + ".")
# print('my dog is ' + str(my_dog.age) + '.')
# print("my cat", my_cat.plivati())
# varijabla1 = Animal (["plivati svaki dan u jezeru"])
# varijabla2 = Animal (["ili u kadi"])
#
#
# my_dog = Dog('Max', 12)
# print("My dogs name is", my_dog.name.title())
# print("My dog is...", str(my_dog.age), ".")
# print("My dog", my_dog.name.title(), "can", my_cat.plivati())

# class Covijek:
#     oci = "smede"
#     visina = 1.80
#     tezina = "75 kg"
#
# string1 = "nesto unutar ovog"
# string2 = "nesto drugo"
# josip = Covijek()
# marko = Covijek()
# print(marko.oci)
# print(josip.tezina)
#
# class Covjek:
#     def __init__(self, boja_ociju, tezina, visina):
#         self.boja_ociju = boja_ociju
#         self.tezina = tezina
#         self.visina = visina
#
# Marko = Covjek("plava", "80 kg", 188)
# Josip = Covjek("zelena", "70 kg", 175)
# print(Marko.tezina)
# print(Josip.tezina)
# print(Josip.boja_ociju)

# class Vojnik:
#     tezina = "90 kg"
#     visina = "1.90m"
#     def __init__(self, boja_ociju, brada):
#         self.boja_ociju = boja_ociju
#         self.brada = brada
# Ivan = Vojnik("smeda", "ne")
# Dejan = Vojnik("crna", "da")
#
# print(Ivan.boja_ociju)
# print(Dejan.brada)
# print(Ivan.tezina)
# print(Dejan.tezina)


# class Covjek:
#     def spavanje(self):
#         print("ja sada spavam")
#     def zbroji(self, a,b):
#         rezultat = a + b
#         print("rezultat je", rezultat)
#
# Barbara = Covjek()
# print(Barbara.spavanje())
#
# print(Barbara.zbroji(29,8))

############Nasljedivanje
# class Zivotinja:
#     tezina = 150
#     broj_nogu = 4
#     def spavanje(self):
#         print("zivince spava")
#
# class Lav (Zivotinja):
#     def rikanje(self):
#         print("Ja sam lavvvv i ricem")
#
# lav = Lav()
# print(lav.rikanje())
# print(lav.tezina)
# print(lav.spavanje())
# print(lav.broj_nogu)
#
# #overridanje i polimorfizam
#
# class Lav(Zivotinja):
#     def rikanje(self):
#         print("ja sam Lav i ricem")
#     def spavanje(self):
#         print("ja sam Lav i spavam")
# lav = Lav()
# print(lav.rikanje())
# print(lav.spavanje())
#
#
# class Lavic(Lav, Zivotinja):
#     pass
# lavic = Lavic()
# print(lavic.rikanje())
# print(lavic.spavanje())
# print(lavic.tezina)
