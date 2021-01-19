from textwrap import dedent
from zivotinje import *

class ZecjaRupa():
    def enter(self):
        print(dedent("""
            ******************************* DOSLO JE PROLJECE **************************
            Kako bi se maleni zeko probudio iz najljepseg ziskog sna i shvatio da je
            doslo proljece potrebno je pogoditi pravilnu sifru za otvaranje vrata.
                                                *  *  *
            Zeko je znao da ce usnuti te je zatvorio vrata kako mu ne bi dosla
            kakva gladna zivotinja dok je on u bezbriznom snu! No, Zeko nije razmisljao
            da je vec prije njega netko drugi odlucio poci u san te je sada on u opasnosti!
            Potrebno ga je probuditi prije no sto se probudi gladna zvijer koja ce
            ga pojesti za dorucak!
            """))

        vrata = 2003
        print("""
        Broj koji otvara vrata je cetveroznamen broj i predstavlja
                datum dolaska proljeca! (dan i mjesec)
            """)

        pogodak = int(input ("pogodi sifru >>> "))

        if pogodak != vrata:

            if len(str(pogodak)) < 4 or len(str(pogodak)) > 4:
                print("sifra mora sadrzavati 4 znamenke!")
                return 'zecja_rupa'

            else:
                brojac = 0
                print(dedent("""
                * * * * * * * * * * * *
                imate jos tri pokusaja!
                * * * * * * * * * * * *
                """))
                while int(pogodak) != vrata  and brojac < 3:
                    brojac += 1                    
                    pogodak = int(input("pogodi sifru: >>> "))

                if pogodak != vrata:

                    print("""Bili ste tik do pobjede. Na zalost Zeko je izvukao gorak
                    kraj te ga je pojeo ljuti:""")
                    ljuti = Zivotinja()
                    ljuti.enter()

                    return 'smrt'

                else:
                    return 'kraj'

        else:
            print("""Zeko je zato postao najpoznatiji i najslavniji zec
                            u cijeloj šumi na Zečevu.""")
            return 'kraj'

