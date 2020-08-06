#MOZE OVAKO:NAJVALJIVANJE
# import math
# a=int(input("unesi a:"))
# b=int(input("unesi b:"))
# print("kvadrat zbroja od",a, "i",b, "je:")
# rezulutat=(math.pow(a,2)+(2*a*b)+math.pow(b,2))
# print(rezulutat)

#A MOZE I OVAKO:UKLJUCIVANJE
from math import pow
a=int(input("unesi a:"))
b=int(input("unesi b:"))
rezultat=pow(a,2)+2*a*b+pow(b,2)
print(rezultat)