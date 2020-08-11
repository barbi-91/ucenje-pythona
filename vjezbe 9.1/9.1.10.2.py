radniDani=["ponedjeljak","utorak","srijeda","cetvrtak","petak"]
dani=['ponedjeljak', 'utorak', 'srijeda', 'cetvrtak', 'petak', 'subota', 'nedjelja']
print(dani)
print(radniDani)

vikend=[]
#####vazan dio
#petlju for koristimo laske pristupanje elementima u listama


for dan in dani:
    if dan not in radniDani:
        vikend.append(dan)

print(vikend)
