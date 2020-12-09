import turtle
turtle.home()

# from turtle import *
# home()

# dot(10); fd(200); lt(90)
# dot(10); fd(200); lt(90)
# dot(10); fd(200); lt(90)
# dot(10); fd(200); lt(90)

from turtle import *
home()
pensize(5)
pencolor('red')
a = int(input('Duljina stranice kvadrata: '))
b = int(input('Povećanje stranice kvadrata: '))

for i in range(4):
 for j in range(4):
 fd (a); lt(90)
 pu(); fd(a);pd()
 a = a + b
