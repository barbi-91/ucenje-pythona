import math
#zaokruzivanje na prvi visi broj: floor
#zaokruzivanje na prvi nizi broj: ceil
#math.modf 

a=float(input("unesite neki broj"))
print(math.floor(a),"zaokruzeno na manje")
print(math.ceil(a), "zaokruzeno na vise")
print(math.modf(a), "sto je ovo?")#rasclanjuje cijeli broj i decimalni
