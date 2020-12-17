import math

x_pozicija = 10
y_pozicija = 85
d_korak = 30

# x_pozicija = 10
# y_pozicija = 20
# d_korak = 30

# x_pozicija = 10
# y_pozicija = 30
# d_korak = 20

# x_pozicija = 0
# y_pozicija = 0
# d_korak = 30

a = y_pozicija-x_pozicija
izracun = a/d_korak
b = math.ceil(izracun)
print(f"zabica je napravila {b} koraka")
f = b*d_korak
duljina = f-a
duljina1 = d_korak - a


if f > a:
    print(f"zabica je skocila za {duljina} cm vise od ocekivane tocke")
elif a == d_korak:
    print("zabica je skocila jednom od tocke do tocke, bez suvisnih centimetara")
elif d_korak > a:
    print(f"zabici nije zadana duljina skoka ")