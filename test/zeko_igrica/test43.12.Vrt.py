
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
            Svi se zecevi na to poplase se i odmah zakljucaju u svoje zecje kucice
            (jazbine). Zeko vodi dosta brige o sigurnosti svojih rođaka. Iako je na
            Zečevu tijekom godine bilo dovoljno hrane za sve zečeve, dolaskom zime
            bilo je sve manje i manje. Zečevi tada žive veoma skromno, kopaju snijeg,
            tražeći suhu travu, glodaju koru drveća te grmlje u šumi. Tada zečevi
            pretežno žive u svojim toplim kućicama, pogotovo kada padne snijeg.
            Stoga Zeko mora u Opskrbu po zelje i mrkvu do vrta u selu i to
            oprezno kako ga ne bi uhvatila lisica, lovac ili ljuti seljanin.
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
             *********************************POCETAK IGRE*********************************
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
