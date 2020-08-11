gradovi=["Daruvar", "Koprivnica", "Karlovac", "Split", "Delnice"]
print(gradovi.index("Delnice"))
gradovi.pop()
print(gradovi)
gradovi.insert(0, "Delnice")
print(gradovi)



while "Delnice"in gradovi:
    gradovi.remove("Delnice")

print(gradovi)
#drugi nacin rjesavanja