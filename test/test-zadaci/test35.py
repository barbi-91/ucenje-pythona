from sys import exit
def gold_room():
    print("This room is full of gold. How much do you take? ")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice) #brojacana varijabla pretvorana iz stringa radi usporedbe brojeva
        #variable how much is assisgment to set value at input variable choice
        if how_much < 50:
            print("Nice, you are not greedy, you win!")
            exit(0)
        else:
            dead("You greedy bastard.")
    else:
        print("Man, learn to type a number, number is not valid.\n")
        print("hint* = number have to contain 0 or 1 in, good luck")
        gold_room()
        #else in case no 0 no 1..any other number is brake y dead function




def bear_room():
    print ("There is a bear here.")
    print ("The bear has a bunch of honey.")
    print ("The fat bear is in front of another door.")
    print ("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go trouht it knoow")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed odd and chew your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
def cthulhu_room():
    print ("Here you see the great evil Cthulhu.")
    print ("He, it, whatever stares at you and you go insane.")
    print ("Do you flee for your life or eat your head?")

    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
def dead(why):
    print(why,"good job!")
    exit(0)

def start():
    print ("You are in a dark room.")
    print ("There is a door to your right and left.")
    print ("Which one do you take?")

    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble arounf the room until you starve")

start()
