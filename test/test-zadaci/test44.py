# # # class Parent(object):
# # #     def implicit(self):
# # #         print("roditelj implicit()")
# # # class Child(Parent):
# # #     pass
# # #
# # # tata = Parent()
# # # sin = Child()
# # #
# # # tata.implicit()
# # # sin.implicit()
# #
# # class Parent(object):
# #     def override(slef):
# #         print("PARENT override()")
# #
# # class Child(Parent):
# #     def override(self):
# #         print("CHILD override()")
# #
# # dad = Parent()
# # son = Child()
# #
# # dad.override()
# # son.override()
#
# #
# # class Mama(object):
# #     def impliciranje(self):
# #         print("mamin citat")
# #
# # class Kcer(Mama):
# #     pass
# #
# # Ana = Mama()
# # Lea = Kcer()
# #
# #
# # Ana.impliciranje()
# # Lea.impliciranje()
#
# class Mama(object):
#     def __init__(self, citat):
#         self.citat = citat
#         print(citat)
#     def overidanje(self, abc):
#         print(abc)
#
# class Kcer(Mama):
#     def overidanje(self,txte):
#         print(txte)
#
# Ana = Mama("mamin citat")
# Lea = Kcer("kcerin citat")
#
# Ana.overidanje("tko se maca laca")
# Lea.overidanje("od maca i pogiba")



# class Parent(object):
#     def implicit(self):
#         print("ja sam implicit Parenta")
#
# class Child(Parent):
#     pass
#
# mam = Parent()
# son = Child()
#
# mam.implicit()
# son.implicit()
#

#::::::::::
# class Parent(object):
#     def override(self):
#         print("ja sam override Parenta")
#
# class Child(Parent):
#     def override(self):
#         print("ja sam override Chielda")
#
# mam = Parent()
# son = Child()
#
# mam.override()
# son.override()
#
# class Parent(object):
#     def altered(self):
#         print("parent altered")
# class Child(Parent):
#     def altered(self):
#         print("child before")
#         super(Child,self).altered()
#         print("CHILD, after")
# dad = Parent()
# son = Child()
#
# dad.altered()
# son.altered()


# class Parent(object):
#     def override(self):
#         print("PARENT override")
#     def implicit(self):
#         print("PARENT implicit")
#     def altered(self):
#         print("PARENT altered")
#
# class Child(Parent):
#     def override(self):
#         print("CHILD override")
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered")
#         super(Child.self).altered()
#         print("CHILD, AFTER PARENT altered")
#
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()
#
# dad.override()
# son.override()
#
# dad.altered()
# son.altered()
#

class Dog:
    def __init__(self, name):
        self.name = name
        print(self.name, "atribut")
        print(name, "varijabla")
ovcar = Dog("Boni")
