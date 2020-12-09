print("""You enter a dark room with two  doorss.
Do you go trought door #1 or door #2 or even a #3?""")

door = input("> ")
if door == "1":
    print ("There's a giant bear here eating a cheese cake.  What do you do?")
    print ("1. Take the cake.")
    print ("2. Scream at the bear.")

    bear = input("> ")
    if bear == "1":
        print("The bar eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
elif door == "2":
    print ("You stare into the endless abyss at Cthulhu's retina.")
    print ("1. Blueberries.")
    print ("2. Yellow jacket clothespins.")
    print ("3. Understanding revolvers yelling melodies.")
    print ("4. meet a J.Lo.")

    insanity = input("> ")
    if insanity == "1" or insanity == "2" or insanity == "4":
        print("You body survives powered by a mind of jello.")
        print("Good job")
    else:
        print("The insanity rots your eyes  into a pool of muck")
        print("Good job!")
elif door == "3":
    print("Yuo are standing in livingroom")
    print("There is a sofa, and behind is sa large plate with fruit")
    print("Woud you like to 1: eat a fruit")
    print("sit in a sofa, number 2")
    insanity = input("> ")

    if insanity == "1":
        print("you are eating a good fruit, enyoing with fireplace and looking around a old room")
    if insanity == "2":
        print("Siting on sofa and thinking about a past?")
        print("take samo alkohol, people enyoj to do that if past is really bad!")
    else:
        print("You are supose to go out off room")
else:
    print("You stumle arond and fall on a knife and die. Good job!")




# 
# print("""Nalazite se u rajskom vrtu...
# Pred vama su tri ulaza koja ulaze u labirint.
# Koji ulaz zelite odabrati?
# #1
# #2
# ?""")
# ulaz = input("> ")
#
# if ulaz == "1":
#     print("""U slucaju da ste odabrali prvi ulaz to je pravi ula za vas....
#     usli ste u prostoriju punu vatre koju trebate gasiti""")
#     print("pored vas je vodica bozja upotrijebiti je :)")
# elif ulaz == "2":
#     print("ovo je pogresan ulaz usli ste u sobu iskupljenja do kraj vijecnosti molit cete se mariji")
# else:
#     print("vas odogovor je vise nego logican, mozete se okrenuti i vratiti u realnost")
