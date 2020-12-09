from sys import argv
#importanje modula system za argument varijablu
script, filename = argv
#ASSIGMENT to variable value to new arrgument value

print(f"We are going to erase al {filename} text file!")
#PRINTING out a  text what we plan to do helping with curly parenthases format text... retrievel a initial variable in arguments
print("for excape go hit: ctrl plus c")
print("If you do want that hit any keybord button")

input("vasa odluka je:...(upisite odgovoro*)")

print("opening file...")
#first we open
#variable text open (variable  in argument , w reading way)
text =  open (filename, 'w')
print (f"file is erase, goodbye to text in {filename}!")
#second we do something
#variable text ___akcion after opening: erase all
#text.truncate()

#prepare variable for input....mk variable...and set it to input mode
print("now we will fill a text file with thre sentence:")
l1 = input("l1: ")
l2 = input("l2: ")
l3 = input("l3: ")
print("I am going to write these to the file")
#variable text. write, ono sto smo naznacili sa w da  ce biti sad t dajemo naredbu
#znaci tekst varijabla tocka akcija je write (gdje ili u sto- pa u line 1)
#slicno appendanju niza lista.append(a)..znaci lista(varijabla koje je niz),,,,writea upisuje koga ili sto ...pa vrijablu a
text.write(f"{l1},{l2},{l3}")
#one comand instead of 6 write  text variable
print("And finally we close it")
text.close()

text_again = open(filename)
print(text_again.read())
