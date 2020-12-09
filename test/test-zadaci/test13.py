from sys import argv
#read the Wyss section for how to run this
script, first, second, third = argv
prompt = "***"
prompt1 = "> "

print("The script is called:", script)
print("Xour first variable is:", first)
print("Your second variable is:", second)
print("Your third variabe is:", third)


#dodatno trazeno u zadatku
print("unesi proizvoljno neke inpute pod ***")
a = input(prompt)
print("ja sam proizvoljni input 1:", a)
b = input()
print("ja sam proizvoljni input 2:", b)
c= input(prompt1)
print("ja sam proizvoljni input 2:", c)
