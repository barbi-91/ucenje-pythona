#this one s like xput scripts with argv
def print_two (*args):
    arg1, arg2, = args
    print(f"arg1:{arg1}, arg2: {arg2}")
#ok that *ARGS IS ACTUALLY POINTLESS  we can just do this
def print_two_again(arg1,arg2):
    print(f"arg1:{arg1}, arg2: {arg2}")

#this just takes one arg
def print_one(arg1):
    print(f"arg1:{arg1}")

#this one takes no arguments
def print_none():
    print("i got nothing")

print_two("Barbara","Erdec")
print_two_again("Barbara","Erdec")
print_one("Barbara")
print_none()
