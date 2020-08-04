n=5
m=10

def fakt(x):
    umnozak=1

    while x>1:
        umnozak *=x
        x-=1

    return umnozak
if 0<=n and n<=m:
    print(fakt(m)/fakt(n)*fakt(m-n))
else:
    print ("uvijet nije zadovoljen")
