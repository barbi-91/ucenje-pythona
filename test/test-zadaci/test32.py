the_count = [1,2,3,4,5]
fruits = ['apple', 'oranges', 'pears','apricot']
change = [1, 'pennies', 2, 'dimes', 3, 'guartes']
#this first kind of for loop goes trought a list

for number in the_count:
    print(f"This i s count {number}")

#some as above
for fruit in fruits:
    print(f"A fruit of type:{fruit}")
#also we can go trough mixed list too
#notice we have to use {} since we dont konw what is in it
for i in change:
    print(f"I got {i}")

#we can also buidld list, first start with  an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range (0,6):
    print(f"adding {i} to the list")
    #append is a fnction that lists Understanding
    elements.append(i)
#now we can print them out tooo
for i in elements:
    print(f"elements was: {i}")
