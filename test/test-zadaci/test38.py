ten_things = "Appes Oranges Crow Telephone Light Sugar"
print("Whait there are not 10 things")
stuff = ten_things.split(' ')
print(stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn","Banana", "Girl", "Boy"]
print (more_stuff)
a = len(stuff)
print(a)
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding:", next_one)
    stuff.append(next_one)
print(f"There are {len(stuff)} items now.")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
