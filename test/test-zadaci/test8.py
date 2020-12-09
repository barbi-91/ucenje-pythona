# inicializaction a variable with string which contains 4 placeholders separated with blanc space
formatter = "{} {} {} {}"
#printing  assigment value od format char to inicialization variable
print(formatter.format(1,2,3,4))
#printing formated variable with arguments in parentheses in this case it is numbers
print(formatter.format("one", "two","tree","four"))
#printing formated varible with arguments in parenthese, for place holder there is a string variable set
print(formatter.format(True, False, False, True))
#bolean in formated text which is assigment to value of formatter
print(formatter.format(formatter, formatter, formatter, formatter))
#forat of inicializaction variable with her one set
print(formatter.format(
    "Try your",
    "own text here",
    "Maybe a poem",
    "or a song about fear"
))
#an assigment ov value which contains string in each new line formating a inicial variable formatter
