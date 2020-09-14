# # lista=["Ivan", "Marko", "Ante", "Slavko", "Jura"]

# # i=0
# # for element in lista:
# #     if i % 2 == 0:
# #         print(element)
# #     i+=1     

# listaImena=["Matej", "Marko", "Luka", "Ivan", "Noel"]

# i=0
# for element in lista:
#     if i % 2 == 0:
#         print(element)
#     i+=1  

listaZivotinja=["1.macka","2.pas","3.riba", "4.ptica","5.gmaz"]
index=brojac=0
for zivotinja in listaZivotinja:
    if brojac%2==0:
        print(zivotinja, "nije na parnom mjestu")
    else:
        print(zivotinja, "se nalazi na parnom mjestu")
    brojac+=1