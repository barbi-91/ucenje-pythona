# #import modul system to input argument trough varijable keybord
# from sys import argv
# #set how many variable have argument
# script, filename = argv
# #varibale txt has value that in initial variable sekend argument
# txt = open(filename)
# #print format text with uble quotes and arentheses curly one inside of format put sekund variable argument
# print(f"Here's your file {filename}:")
# #print varibale txt and read what has point to varibale in argumet set by keybord
# print(txt.read())
# #test string
print("Type the filename again:")
#set a variable true the keybord to repet the txt doc
file_again = input("> ")
#text in tt doc open with new variable
txt_again = open(file_again)
#thid new variable read with comand print
print(txt_again.read())



# from sys import argv
# script, filename = argv
#
# print(f"now we can open a file {filename}:")
# text = open(filename)
# print(text.read())
#
# print("we can now print file agin")
# filename_ponovljeno= input(">>> ")
# textponovljeno = open(filename_ponovljeno)
#
# print(textponovljeno.read())
