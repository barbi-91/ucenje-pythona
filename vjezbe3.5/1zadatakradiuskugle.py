import math
r=int(input("molimo unesite radius:"))
print("radius kugle je:",r)
if r > 0:
    V=((4/3)*(r**3))*math.pi
    print("volumen kugle proizlazi", V)

else:
     print("radijus u varijabli r je neispravan")

