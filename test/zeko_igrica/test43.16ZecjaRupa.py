from test43.15Zivotinje import Zivotinje

class ZecjaRupa(Scene):
    def enter(self):
        print(dedent("""
            Kako bi se maleni zeko probudio iz najljpseg ziskog sna i shvatio da je
            doslo proljece potrenbno je pogoditi pravilnu sifru na vratima.
            Zeko je znao da ce usnuti te je zatvorio vrata kako mu ne bi dosla k
            akva ljut zivotinja dok je on u najljepsem snu, no Zeko nije razmisljao
            da je vec prije njega netko dr posao na san te je sada on u opasnosti.
            Potrebno ga je probuditi prije no sto se probudi druga zivtinja koja ce
            ga pojesti za dorucak!
            """))

        vrata = 2003
        print("""Broj koji otvara vrata je cetveroznamen broj i predstavlja
        datum dolaska proljeca(dan i mjesec)""")

        pogodak = input ("pogodi sifru >>> ")

        brojac = 1
        while int(pogodak) != vrata and brojac < 3:
            brojac += 1
            print("pokusaj ponovno")
            pogodak = input("pogodi: >>> ")

        if pogodak == vrata:
            print("""Bili ste tik do pobjede. Na zalost Zeko je izvukao deblji kraj 
            te ga je pojeo ljuti:""")
            ljuti= Zivotinje()
            ljuti.enter()
            return 'smrt'

        else:
            print("""Zeko je zato postao najpoznatiji i najslavniji zec
                            u cijeloj šumi na Zečevu.""")
            return 'kraj'
