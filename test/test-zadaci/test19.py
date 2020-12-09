def cheese_and_crackers(cheese_count, boxes_of_creckers):
    #WE put in function a parametre
    print(f"You have {cheese_count},cheeses!")
    #printing a formating string tekst with variable in def function taket like pparameter

    print(f"You have {boxes_of_creckers} boxes_of_creckers")
    print("Man that's enough for a party!!!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly")
cheese_and_crackers(20,30)
#call a function repeat just a nema of def with parentheses and variable we give to deffunction separatet with coma

print("Or, we can use varibales from our script")
#crate 2 variable diferent name

amount_of_cheese = 10
amount_of_creckers = 50
#call def function and give over to function a variables with diferent name ...function will recognaze as parameter with that name of funtion
cheese_and_crackers(amount_of_cheese,amount_of_creckers)

print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)
#function name and variable as math task separate with coma

print("And we can combine the two, variable and math")
cheese_and_crackers(amount_of_cheese + 180, amount_of_creckers+1000)
#combine mth and variables and give over to funcation like variable just call a name of function with parentheses
