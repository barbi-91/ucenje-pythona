with open  ("datoteka.txt", "w") as f:
    for i in range (1,11):
        f.write(str(i) + "\n")

suma=0
with open ("datoteka.txt", "r") as f:
    for i in f.readlines():
        suma+=int(i)

print (suam)