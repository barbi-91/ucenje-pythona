from sys import argv
script, filename = argv

print(f"We are going to erase {filename}.")
print("IF you dont want that,hit : Ctrl C")
print("If you do want that hit any keybord button")

input(">>>?>>>")

print("opening the file")
target = open (filename, 'w')
print ("truncating the file. goodbye")
target.truncate()
print("Now i am going to ask you for three lines")

l1 = input("l1: ")
l2 = input("l2: ")
l3 = input("l3: ")

print("I am going to write these to the file")

target.write(l1)
target.write("\n")
target.write(l2)
target.write("\n")
target.write(l3)
target.write("\n")

print("And finally we close it")
target.close()
