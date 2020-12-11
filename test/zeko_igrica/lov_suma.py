from Zagonetke import *

class LovSuma(Scene):
    def enter(self):
        print(dedent("""
            **************************ZEKO SRECE LOVACA*************************
            Polako, ali pazljivo da ga ne vidi, sa punom vrecom kupusa
            uz brdo penjao se Zeko. Vreca je bila teska pa se Zeko morao
            odmarati nekoliko puta.

            Prilikom odmora nije ni znao da gubi vrijeme, lovac je slijedio njegov
            trag te uhvatio zeca. Kako je Zeko bio vrlo inteligentan, pokusao je
            pregovarati s lovcem ne bi li ga pustio. Ponudi je lovcu da mu uz rijesenu
            zagonetku uslisi molitve te ga pusti u sumu. Lovac nije znao da je Zeko
            najmudrije bice u sumi te misleci da zec nema nikakve sanse te pristane na
            okladu kako bi se jos malo zabavio na racun zeke.

            Lovac se zamisli... a potom rece:
            """))

        tko_je = Zagonetke()
        tko_je.enter()

        pogodak = input("pogodi: >>> ")
        pokusaji = 0

        while pogodak != "dabar" and pogodak != "zec" and pogodak != "vjeverica" and pokusaji < 10:
            pokusaji += 1
            print("pokusaj ponovno")
            pogodak = input("pogodi: >>> ")

        if pogodak == 'dabar' or pogodak == 'zec' or pogodak =='vjeverica':
            print(dedent(f"""
                **************************{pogodak}****************************
                I tako je mali intelignetni sivi Zeko jos jednom dokazao svoju mudrost.
                Slatko se nasmijao i u tren oka umakao lovcu iz narucja, a potom i iz
                vida, dok se lovac jos zaprepasteno cudio.

                Zvonilo je podne kad je stigao na brezuljak Zecevo sa kupusom i mrkvom.
                Pozvao je na rucak sve zeceve iz cijele sume. Svi su mu zecevi bili
                zahvalni što ih je nahranio usred zime.
                Na njihova lica vratila se radost, a iz ociju zablistao je vedar sjaj.
                Od tada Zeko je među svojim rođacima uživao veliki ugled i povjerenje.

                ***************************************************************
                """))

            return 'potok'


        else:
            print(dedent("""
                Lovac je uhvatio mladog nadobudnog zeca.
                Jedina prava mudrost je u spoznaji -da ništa ne znaš.
                """))

            return 'smrt'
