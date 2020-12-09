#variable directly
def checklist(fruit,vegetables):
    print(f"fruit {fruit} is in a basket, but vegetables {vegetables} also!")
    print("We can go to pay it")
    print(f"for {fruit} 10 euro, for {vegetables} 8 euro","\n")

checklist("APPLE", "CARROT")

#varibales
voce = "banana"
povrce = "green_salat"
checklist(voce, povrce)

#math---kokatenacija
checklist("banana" + "APPLE", "green_salat" + "CARROT")

#math and variable cocatenation
checklist(voce + "APPLE", "CARROT" + povrce)

#input
input1 = input("Unesi voce")
input2 = input("unesi povrce")
checklist(input1,input2)
