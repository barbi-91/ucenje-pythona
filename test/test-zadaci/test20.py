from sys import argv
script, input_file = argv
#importanje moduala argv is system, set  a incremental variable to  2 values

def print_all(f):
    print(f.read())
    #create funtion, give over parametaar f, printing parametar f like read file
def rewind(f):
    f.seek(0)
    #rewind ???
def print_a_line(line_count,f):
    print(line_count,f.readline())
    #printing ich line in file out, counter with parametar f


current_file = open(input_file)
#temporary variable which open a file


print("First lets print the whole file;\n")
print_all(current_file)# prining all

print("now lets rewind, kind of like a tape")
rewind(current_file)#????

print("lets print 3 lines:")
current_LINE = 1
print_a_line(current_LINE,current_file)
#printing line  by line
#counter seet value at 1
#call function and set argument in parentheses

current_LINE = current_LINE + 1
print_a_line(current_LINE,current_file)

current_LINE = current_LINE + 1
print_a_line(current_LINE, current_file)
