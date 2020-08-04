a=5
b=55
c=207
d=308
e=76
f=203
brojac=0
if a or b or c or d or e or f > 100:
    print("some variable are greater than 100")

my_first_array = [a, b, c, d, e, f]
for number in my_first_array:
    if number > 100:
        brojac=brojac+1
        print(str(number) + " is greater than 100")

if brojac >=3:
    print("zadovoljava")
else:
    print("nezadovoljava")    
       