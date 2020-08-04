n=10
y=8 #y=red
x=7 #x=stupac
#[2,5] kordinate
for red in range (1, n+1):
    for stupac in range (1, n+1):
        if red==y and stupac==x:
            print("X", end="")
        else:
            print("-", end="")
    print ()