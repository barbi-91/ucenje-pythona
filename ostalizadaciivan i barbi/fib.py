
#formula   fn=fn-1 + fn-2
#fn-1= prvi clan
#fn-2=drugi clan
brojac=0
rezultat=0

prviClan=0
print(prviClan)
drugiClan=1
print(drugiClan)


rezultat= prviClan + drugiClan
# 0 + 1= 1, 1+1=2, 1+2=3
while rezultat>=1 and rezultat<100:
    rezultat= prviClan + drugiClan
    print(rezultat)
    prviClan=drugiClan
    drugiClan=rezultat
    brojac+=1


    #Ivan micasti mic :D fibi je rijesen :D