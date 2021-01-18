from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("Slika scene")
        exit(0)

class Smrt(Scene):

    citati = [
        " Ljudi vam nikada neće oprostiti uspjeh, čvrst hod nakon pada i širok osmijeh preko cijelog lica.\n",
        " Budi pametan… i pravi se lud… tako najbolje vidiš stvari.\n",
        " Toliko je u životu bilo stvari kojih smo se bojali. A nije trebalo, trebalo je živjeti…\n ",
        " Život je ono što se događa dok vi pravite planove za život.\n",
        " Tamo kamo se isplati ići ne vodi prečica!\n"
    ]
    def enter(self):
        print(Smrt.citati[randint(0,len(self.citati)-1)])
        print ("            **  **  **         ")
        print("""
        ....i onako si izgubio, mozda shvatis da nije uvijek najbolje
        biti najpametniji, najhrabriji ili najaci... ali mozda naucis
        nesto iz ove mudre izreke!  END!
        """)
        exit(0)


class Vrt(Scene):
    def enter(self):
        print(dedent("""
            ***************************************************************
            ***************************************************************

            Iznad malog sela Radosne Livadice uzdize se lagani brezuljak Zecevo,
            obrastao niskom, pretezno crnogoricnom sumom u kojoj zivi
            mnogo zeceva. Zato je ovaj brezuljak i dobio ime po zecevima,
            njegovim stanovnicima, lijepim, hitrim i nadasve ljupkim bicima.
                                *  *  *
            U Zecevu zivi Zeko koji se uvijek dosjeti neceg pametnog, a usto
            je i iznimno oprezan. Cim bi netko nepoznat ili sumnjiv dosao u
            njihovu sumu, Zeko bi uzdignuo usi, rasirio oci i podignuo se na
            zadnje noge, te brzim pokretima lupkao nogom u pod, kao zurni znak
            za uzbunu!
                                *  *  *
            Svi se zecevi na to poplase se i odmah zakljucaju u svoje zecje
            kucice (jazbine). Zeko vodi dosta brige o sigurnosti svojih rođaka.
            Iako je na Zecevu tijekom godine bilo dovoljno hrane za sve zečeve,
            dolaskom zime bilo je sve manje i manje. Zečevi tada žive veoma
            skromno, kopaju snijeg, tražeći suhu travu, glodaju koru drveća te
            grmlje u šumi. Tada zečevi pretežno žive u svojim toplim kućicama,
            pogotovo kada padne snijeg. Stoga Zeko mora u Opskrbu po zelje i
            mrkvu do vrta u selu i to oprezno kako ga ne bi uhvatila lisica,
            lovac ili ljuti seljanin.
                                *  *  *
            Zeko je Krenuo hrabro po mrkvu, medutim naisao je na gladnu lisicu
            putem koja ga je uocila! Pomozi Zeki odluciti, hoce li se nas Zeko:
                a) sakriti ?
                b) boriti ?
                c) pobjeci ?

            """))

        radnja = input("> ")

        if radnja == "sakriti":
            print(dedent("""
                Ako nemaš brod, plivaj!
                Ako ne znaš plivati, izgradi brod!
                Uspjeh je stvar stava!

                Sugerirati jednom Zeki da se sakrije nije hrabro a niti mudro.
                Zbog krive odluke, a vrlo dobrog njuha te velike lukavosti i
                spretnosti, Zeko je pao u sape lisice.
                """))

            return 'smrt'


        elif radnja == "boriti":
            print(dedent("""
                U tebi su tri covjeka: Jedan, kakav bi zelio biti. Drugi, kakav mislis da jesi.
                I treci, kakav si zaista. Tog jedino ne poznajes. Naposljetku, sustina saznavanja
                nije u tome gubimo li igru, vec kako gubimo, sto s time spoznajemo, cemu nas je
                poraz naucio i kako nas to mijenja. Gubiti na odredeni nacin znaci – dobivati.

                Vrlina zeca nije u snazi vec u brzini, odlucnosti i inteligenciji.

                Zeko je bio nepazljiv, a lisica je omastila brk.
                """))

            return 'smrt'


        elif radnja == "pobjeci":
            print(dedent("""
             ************************************Zeko odluci pobjeci***********************
             ******************************************************************************

                                                *  *  *
                Zeko je obisao cijelo selo i vidio pune vrtove zasadene prekrasnim kupusom.
                                                *  *  *
                Od silne radosti su rasle zazubice. Pazio da ga nitko ne vidi i pazljivo
                se suljao uz plotove vrtova. I na kraju trud se isplatio. U zadnjem vrtu na
                kraju sela, malo udaljen od kuća, Zeko je ispod plota iskopao jednu rupu,
                tek toliku da se mogao provuci, kroz koju je usao u vrt. Rupu je mogao kopati
                na miru, jer tuda nije nitko prolazio. Napokon njegovoj gladi dosao je kraj.

                I tako je Zeko svako jutro dok su seljaci jos spavali, odlazio u njihov
                vrt s kupusom i mrkvom. Medutim jednog dana na povratku kuci, prolazeci
                summom ugledao je lovca.
                """))

            return 'lovac'

        else:
            print("Nepravilno unesena rijec!")
            return 'vrt'


class Zagonetke(Scene):
    odgonetke = [
        """
        Kraj potoka ili rijeke
        On prepreke pravi neke.
        Drvosječa to je hrabar,
        to bi bio mudri ___?___.
        """,
                    #dabar
        """
        Duge uši, kratke noge,
        one pamte staze mnoge:
        mene jure redom svi -
        sove, lije, lovci, psi.
        I kad spavam, tj. ležim,
        ja sve mislim kud da bježim.
        Eci, peci, pec,
        ja sam mali___?___.
        """,
                    #zec
        """
        Po krošnjama šećem
        i veselo skakućem.
        Volim šumski mir.
        Da zimi ne prosim
        u kućicu nosim
        lešnike i žir, da
        mi bude fina vecerica,
        ja sam slatka ___?___.
        """
                #vjeverica
    ]

    def enter(self):
        print(Zagonetke.odgonetke[randint(0,len(self.odgonetke)-1)])


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

class Potok(Scene):

    def enter(self):
        print(dedent("""
            ********************smrznuo se potocic******************************
            A onda su dosli jos hladniji dani, zekina braca i sestre su sve cesce
            ostajali kod tople kuce umjesto igre u potocicu… Ali mali Zeko svaki
            bi dan dosao, skakao i sljapkao po svom potocicu.
            No, jedne zimske noci, u Zecevu smrznuo se potocic i pokrio ga snijeg.
            I tuzan mislio je Zeko ta gdje je potok taj, uskoro ce i prvi maj.
                                *  *  *
            I tako je zeko tumarao sumom sve dok nije sreo dobru sumsku jezicu.
            Na njegovo pitanje jezica je odgovorila: “Mali Zeko nemoj biti tuzan.
            Tvoj potocic nije nestao! Samo se zaledio! Cim dođe ljepse vrijeme i
            snijeg malo okopni, on ce poceti veselo zuboriti.
                                *  *  *
            No Zeko nije zelio cekati... i nisu mu se svidali odgovori...
            Razmisljao je kako si moze pomoci i dosao na ideju. Moze odmrznuti
            potok ako nalozi vatru, tako da sakupi puno granja te paziti da
            vatra ne ugansne dok se ne otopi sav led, a sto je opasno za malog
            zeca ili odluciti te usnuti i tako docekati proljece u svom toplom
            kreveticu.

            Hmmmm, sto je pametnije:
            a) odmrznuti ?
            b) usnuti ?
            """))

        radnja = input("> upisi odgovor (glagol) >>> ")

        if radnja == 'odmrznuti':
            print(dedent("""
                Zeko nije naucen na vatru, sve je poslo po zlu. Niti je zapalio vatru niti
                otpoio led. Niti dosao do vode a jos se dobro i prehladio.
                """))
            return 'smrt'

        elif radnja == 'usnuti':
            print(dedent("""
                *******************************SAN******************************
                Ispravna odluka!
                Zeko je radosno pomislio na san te da je to najblja odluka kako
                bi docekao proljece sto prije i kako bi mogao uzivati sa svojim
                prijateljima pored potocica koji ih je tako smijelo mamio svojim
                plavim ljeskanjem i suncem te cvijecm savrseno uklapljenim u idilu
                male, razigrane doline.

                Tako je Zeko utonuo u misli i radosno odskakuto u svoj krevetic.
                ********************************************************************
                """))
            return 'zecja_rupa'

        else:
            print("krivo upisan tekst")
            return 'potok'

class Zivotinja(Scene):
    bice = [
            "MEDVJED",
            "VUK",
            "LISAC",
            "CAGALJ",
        ]
    def enter(self):
        print(Zivotinja.bice[randint(0,len(self.bice)-1)])

# OVDJE SAM STALA POGLEDATI DALI OVO RADI!
class ZecjaRupa(Scene):
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
                return zecja_rupa

            else:
                brojac = 0
                print(dedent("""
                * * * * * * * * * * * *
                imate jos tri pokusaja!
                * * * * * * * * * * * *
                """))
                while int(pogodak) != vrata  and brojac < 3:
                    brojac += 1
                    print("pokusaj ponovno")
                    pogodak = int(input("pogodi: >>> "))

                if pogodak != vrata:

                    print("""Bili ste tik do pobjede. Na zalost Zeko je izvukao
                    gorak kraj te ga je pojeo ljuti:""")
                    ljuti = Zivotinja()
                    ljuti.enter()
                    return 'smrt'
                else:
                    return 'kraj'

        else:
            print("""Zeko je zato postao najpoznatiji i najslavniji zec
                            u cijeloj šumi na Zečevu.""")
            return 'kraj'


class Kraj(Scene):

    def enter(self):
        print(dedent("""
        ************************************************************************
        ****************************** * *  <3 * <3 * <3  * * ******************
        ************************************************************************
                                Pobjedili ste zimu, Bravo!
        * * *  <3 * <3 * <3  * * *
        Ako podijelimo barem malu iskricu topline s onima koje sretnemo na putu,
                        zima će postati mnogo toplija, za sve!
        ************************************************************************
        ******************************* * *  <3 * <3 * <3  * * *****************

        """))

        return 'kraj'

##########################################
class Organizacija(object):

    def __init__(self, plan):
        self.plan = plan

    def igra(self):
        trenutna_scena = self.plan.scena_otvaranja()
        zadnja_scena = self.plan.sljedeca_scena('kraj')

        while trenutna_scena != zadnja_scena:
            sljedeca_scena_ime = trenutna_scena.enter()
            trenutna_scena = self.plan.sljedeca_scena(sljedeca_scena_ime)
        trenutna_scena.enter()
#########################################

class Mapa(object):

    scene = {
        'vrt': Vrt(),
        'lovac': LovSuma(),
        'potok': Potok(),
        'zecja_rupa': ZecjaRupa(),
        'smrt': Smrt(),
        'kraj': Kraj()
        }

    def __init__(self, startna_scena):
        self.startna_scena = startna_scena

    def sljedeca_scena(self, ime_scene):
        ime = Mapa.scene.get(ime_scene)
        return ime

    def scena_otvaranja(self):
        return self.sljedeca_scena(self.startna_scena)


zeko_mapa = Mapa('vrt')
zeko_igra = Organizacija(zeko_mapa)
zeko_igra.igra()
