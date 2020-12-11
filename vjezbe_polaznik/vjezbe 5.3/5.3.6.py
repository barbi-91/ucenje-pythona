while True:
    a=input("unesite broj bodova:")
    a=float(a)
    
    if a>=0 and a<50:
        print("nedovoljan")
    elif a>=50 and a<62.5:
        print("dovoljan")
    elif a>= 62.5 and a<75:
        print("dobar")
    elif a>=75 and a<87.5:
        print("vrlo dobar")
    elif a>=87.5 and a<=100:
        print("odlican")

    else:
        print("pogreska unosa!")
