
class Potok(Scene):

    def enter(self):
        print(dedent("""
            ********************smrznuo se potocic******************************
            A onda su dosli jos hladniji dani, zekina braca i sestre su sve cesce
            ostajali kod tople kuce umjesto igre u potocicu… Ali mali Zeko svaki bi
            dan dosao, skakao i sljapkao po svom potocicu.
            No, jedne zimske noci, u Zecevu smrznuo se potocic i pokrio ga snijeg.
            I tuzan mislio je Zeko ta gdje je potok taj, uskoro ce i prvi maj.
                                *  *  *
            I tako je zeko tumarao sumom sve dok nije sreo dobru sumsku jezicu.
            Na njegovo pitanje jezica je odgovorila: “Mali Zeko nemoj biti tuzan.
            Tvoj potocic nije nestao! Samo se zaledio! Cim dođe ljepse vrijeme i
            snijeg malo okopni, on ce poceti veselo zuboriti.
                                *  *  *
            No Zeko nije zelio cekati... i nisu mu se svidali odgovori...
            Razmisljao je kako si moze pomoci i dosao na ideju. Moze odmrznuti potok
            vatrom tako da sakupi puno granja i paziti da vatra ne ugansne, sto je
            naporno za malog zeca ili usnuti te docekati proljece u svom toplom kreveticu.

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
                Zeko je radosno pomislio kako ce spavati da bi proljece sto prije
                doslo i kako bi mogao uzivati sa svojim prijateljima pored potocica koji
                ih je tako smijelo mamio svojim plavim ljeskanjem i suncem te cvijecm koje
                se savrseno uklapalo u idilu te male razigrane doline.

                Tako je Zeko utonuo u misli i radosno odskakuto u svoj krevetic.
                ***************************************************************
                """))
            return 'zecja_rupa'

        else:
            print("krivo upisan tekst")
            return 'potok'
