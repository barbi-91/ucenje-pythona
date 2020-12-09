type_of_people = 10
#a assigment value of variable is set to 10
x = f"There are {type_of_people} types of people."
#assigment value of variable is format of dubel qoutes which represent a string sentence and aded qurly parentheses with a variable inside, and continuing with sentens , duble qouots
binary = "binary"
#binary variable is set to string (string is writed with tho duble qouots)
do_not = "don't"
#same sa binary variable ....assigment variable to string
y= f"Those who know {binary} and those who {do_not}."
#assigment variable with format strin, inside od duble quote set 2 curly parenthses
#print variable x and y
print(x)
print(y)
print(f"i said: {x}")
#print formated string againt assigment in string format to variable x
print(f"i also said: '{y}'")

hilarius = True
#variable hil set to False (this si true argumet for statement hilarius)
joke_evaluation = "isn't that joke so funny?! {}"
#this variable is assigment to string but this is second tipe of formated text...
#in this case we put string with duble qoutose, and the end of the sentenc before close dugle quotes we pt curly open and close parentheses
#how we printing that tipe of formating text?
#well normaly put print and opet parenthses, inside set variable dot format and again parenthses in which we put variable name we want to add to sentence
print (joke_evaluation.format(hilarius))

w = "this is the  left side of " ""
e = "a string with a right side."
#two sentens we merge in one with a simple plus
print (w + e)
