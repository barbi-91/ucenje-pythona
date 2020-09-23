#lagan ...rijesila samostalno i drugacije od rijesenja
while True:  
    troznamenkasti=str(input("unesi troznamenkasti broj:"))
    duljina=len(troznamenkasti)
    i=1
    troznamenkasti=int(troznamenkasti)
    troznamenkasti1 = troznamenkasti + 1
    if duljina==3:
        print("unijeli ste broj:", troznamenkasti, "prvi slijedeci polindrom je:", troznamenkasti1 )
    else:
        print("prekida se izvodenje programa, niste unijeli troznamenkast broj")
        break


