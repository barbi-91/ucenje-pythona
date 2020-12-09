from test import class Zivotinje()
class ZecjaRupa(Scene):
    def enter(self):
        print(dedent("""
            Kako bi se maleni zeko probudio iz najljpseg ziskog sna i shvatio da je
            doslo proljece potrenbno je pogoditi pravilnu sifru na vratima.
            """))

        vrata = 2003
        print("Broj koji otvara vrata je cetveroznamen broj i predstavlja datum dolaska proljeca(dan i mjesec)")

        pogodak = input ("pogodi sifru >>> ")

        brojac = 1
        while int(pogodak) != vrata and brojac < 3:
            brojac += 1
            print("pokusaj ponovno")
            pogodak = input("pogodi: >>> ")

        if pogodak == vrata:
            print("Bili ste tik do pobjede sa budenjem zeke. Pojeo vas je ljuti:")
            ljuti= Zivotinje()
            ljuti.enter()
            return 'smrt'

        else:
            print("""Zeko je zato postao najpoznatiji i najslavniji zec
                            u cijeloj šumi na Zečevu.""")
            return 'kraj'
