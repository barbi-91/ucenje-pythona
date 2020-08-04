slova= "ABCDEFGHIJK"
br_slova = len(slova)
n=2
if br_slova > n:
    index=0
    print("n je manji od slova")
    for neko_slovo in slova:
        
        if index%n==0:
            print(neko_slovo, end="")
        index=index+1
else:
    print ("GRESKA")

