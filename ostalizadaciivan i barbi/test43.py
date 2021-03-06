# from sys import exit
# from random import randint
# from textwrap import dedent

#
# class Scene(object):
#     def ulaz(self):
#         print("nije jos osmisljena")
#         print("Treba subbclassu")
#         exit(1)

class Program(object):
    def __init__(self, mapiranje):
        self.mapiranje = mapiranje
    def igraj(self):
        trenutna = self.mapiranje.opening_scene()
        last_scene = self.mapiranje.next_scene('kraj_igre')

        while trenutna != last_scene:
            next_ime_scene = trenutna.ulaz()
            trenutna = self.mapiranje.next_scene(next_ime_scene)
        trenutna.ulaz()

    #overridanje sa ulazom
# class Smrt(Scene):
#     citati = [
#         "You died.RIP",
#         "Died.End.",
#         "Such a light, youu dieeed!.",
#         "I have a small puppy that's better at this."
#     ]
#     def ulaz(self):
#         print(Smrt.citati[randint(0,len(self.citati)-1)])
#         exit(1)




# class SobaZelja(Scene):
#     def ulaz(self):
#         print(dedent("""
#             The Gothons of Planet Percal #25 have invaded your ship and destroyed
#             your entire crew.  You are the last surviving member and your last
#             mission is to get the neutron destruct bomb from the Weapons Armory,
#             put it in the bridge, and blow the ship up after getting into an
#             Drvo
#
#             You're running down the central corridor to the Weapons Armory when
#             a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
#             flowing around his hate filled body.  He's blocking the door to the
#             Armory and about to pull a weapon to blast you.
#             """))
#         action = input("> ")
#
#         if action == "shoot!":
#             print(dedent("""
#                 Quick on the draw you yank out your blaster and fire it at the Gothon.
#                 His clown costume is flowing and moving around his body, which throws
#                 off your aim.  Your laser hits his costume but misses him entirely.  This
#                 completely ruins his brand new costume his mother bought him, which
#                 makes him fly into an insane rage and blast you repeatedly in the face until
#                 you are dead.  Then he eats you.
#                 """))
#             return 'smrt'
#
#         elif action == "dodge!":
#             print(dedent("""
#                 Like a world class boxer you dodge, weave, slip and slide right
#                 as the Gothon's blaster cranks a laser past your head.
#                 In the middle of your artful dodge your foot slips and you
#                 ang your head on the metal wall and pass out.
#                 You wake up shortly after only to die as the Gothon stomps on
#                 your head and eats you.
#                 """))
#             return 'smrt'
#
#         elif action == "tell a joke":
#             print(dedent("""
#                 Lucky for you they made you learn Gothon insults in the academy.
#                 You tell the one Gothon joke you know:
#                 Lbhe zbgure vf fb sng, jura fur fvgf ebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.
#                 The Gothon stops, tries not to laugh, then busts out laughing and can't move.
#                 While he's laughing you run up and shoot him square in the head
#                 putting him down, then jump through the Weapon Armory door.
#                 """))
#             return 'oruzje'
#
#         else:
#             print ("Nevazeca rijec!")
#             return 'kuca'


class SobaBorbe(Scene):
    def ulaz(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan the room
            for more Gothons that might be hiding.  It's dead quiet, too quiet.
            You stand up and run to the far side of the room and find the
            neutron bomb in its container.  There's a keypad lock on the box
            and you need the code to get the bomb out.  If you get the code
            wrong 10 times then the lock closes forever and you can't
            get the bomb.  The code is 3 digits.
            """))
        code = (f"{randint(1,9)}{randint(1,9)}{randint(1,9)}").replace(',','')
        #imamo bug trebamo utpikat odrednim redom sa zareom i razmakom, potrebno napravit da se tipka kao jedan kod
        ## BUG: stavili smo code u zagrade i na kraju smo dodali tocku ... replace zareze sa praznim mjestom...tocnije spoji brojeeve
        print(code)
        pokusaj = input("[keypad]> ")
        pokusajes = 0

        while pokusaj != code and pokusajes < 10:
            print ("BZZZZEDDD!")
            pokusajes += 1
            pokusaj = input("[keypad]> ")

        if pokusaj == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting gas out.
                You grab the neutron bomb and run as fast as you can to the
                bridge where you must place it in the right spot.
                """))
            return 'most''
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a sickening
                melting sound as the mechanism is fused together.
                You decide to sit there, and finally the Gothons blow up the
                ship from their ship and you die.
                """))
            return 'smrt'



# class MostVrtni(Scene):
#
#     def ulaz(self):
#         print(dedent("""
#             You burst onto the Bridge with the netron destruct bomb
#             under your arm and surprise 5 Gothons who are trying to
#             take control of the ship.  Each of them has an even uglier
#             clown costume than the last.  They haven't pulled thei
#             weapons out yet, as they see the active bomb under your
#             arm and don't want to set it off.
#             """))
#
#         action = input("> ")
#
#         if action == "throw the bomb":
#             print(dedent("""
#                 In a panic you throw the bomb at the group of Gothons
#                 and make a leap for the door.  Right as you drop it a
#                 Gothon shoots you right in the back killing you.
#                 As you die you see another Gothon frantically try to disarm
#                 the bomb. You die knowing they will probably blow up when
#                 it goes off.
#                 """))
#             return 'smrt'
#
#         elif action == "slowly place the bomb":
#             print(dedent("""
#                 You point your blaster at the bomb under your arm
#                 and the Gothons put their hands up and start to sweat.
#                 You inch backward to the door, open it, and then carefully
#                 place the bomb on the floor, pointing your blaster at it.
#                 You then jump back through the door, punch the close button
#                 and blast the lock so the Gothons can't get out.
#                 Now that the bomb is placed you run to the escape pod to
#                 get off this tin can.
#                 """))
#             return 'drvo_carolije'
#         else:
#             print("Nevazeca rijec!")
#             return 'most'


# class Drvo(Scene):
# 
#     def ulaz(self):
#         print(dedent("""
#             You rush through the ship desperately trying to make it to
#             the escape pod before the whole ship explodes.  It seems like
#             hardly any Gothons are on the ship, so your run is clear of
#             interference.  You get to the chamber with the escape pods, and
#             now need to pick one to take.  Some of them could be damaged
#             but you don't have time to look.  There's 5 pods, which one
#             do you take?
#             """))
# 
#         sifra = randint(1,5)
#         pokusaj = input("[pod #]> ")
# 
# 
#         if int(pokusaj) != sifra:
#             print(dedent(f"""
#                 You jump into pod and hit the eject button." {pokusaj}
#                 The pod escapes out into the void of space, then
#                 implodes as the hull ruptures, crushing your body
#                 into jam jelly.
#                 """))
#             return 'smrt'
#         else:
#             print(dedent(f"""
#                 You jump into pod {pokusaj} and hit the eject button.
#                 The pod easily slides out into space heading to
#                 the planet below.  As it flies to the planet, you look
#                 back and see your ship implode then explode like a
#                 bright star, taking out the Gothon ship at the same
#                 time.  You won!
#                 """))
# 
#             return 'kraj_igre'
#
# class Kraj(Scene):
#
#     def ulaz(self):
#         print ("You won! Good job.")
#         return 'kraj_igre'

class Map(object):

    mapa_scena = {
        'kuca': SobaZelja(),
        'oruzje': SobaBorbe(),
        'most'': MostVrtni(),
        'drvo_carolije': Drvo(),
        'smrt': Smrt(),
        'kraj_igre': Kraj(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, ime_scene):
        val = Map.mapa_scena.get(ime_scene)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('kuca')
a_game = Program(a_map)
a_game.igraj()
