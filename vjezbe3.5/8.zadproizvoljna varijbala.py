niz= "ovo je moj proizvoljni niz znakova, Koje Pisem mAlim i Velikim slovima"
count=0
foundA=0

for x in niz:
    
    print(x)

    # if x > "A" and x <= "Z":
    if str.isupper(x) and x != "A":
        count = count + 1 
        print("Nađeno veliko slovo " + x)
    
    if x == "A":
        foundA = 1
        print("letter A is found, and count number is:", count )
    
    if foundA == 1:
        break

print(count)