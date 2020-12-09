from sys import exit
#iz sistema importati stavku exit za kraj programa
def zlatna_soba():
    print("Dobro dosli u zlatnu sobu <3, korka ste blize srcu vase djeve")
    print("vas uspavana djeva lezi na krevetu")
    print("zelite li je poljubiti ?")

    izbor = input("> ")
    if "da" in izbor or "zelim" in izbor:
        print("Stojite nad krevetom  Vase usnule dijeve!")
        krevet()
    else:
        print("""Vi niste pravi momak za nasu djevu,
        i bolje je da ste iskreni prema sebi!!!, zatvorite vrata
        i ne uznemiravajte nasu dijevu""")
        kraj_igre("Poljubac nije otvorio srce i dusu...")
def krevet():
    print(""""Vasa djeva lezi na krevetu sva blijeda i usnula,
    priblizite se i poljubite vasu djevu, kako biste je probudili iz
    vijecnog sna""")
    print("No Vasu djevu nije tako lako probuditi, potreban je odreden broj poljubaca!")
    print("Koliko puta cete poljubiti vasu djevu ?")
    poljubac()


def poljubac():
    poljub = input("> ")
    broj = int(poljub)
    if broj < 2:
        print("jedan pravi dusu otvara ali ne i srce")
        kraj_igre("Vasa dama ostala je usnula")
    elif broj < 3:
        print("dva poljubca za dusu ali nisu za otvaranje srca djeve nikako dovoljna")
        kraj_igre("Bili ste vrlo brlizu")
    else:
        print("Vi ste pravi princ, poljubac nikad nije dovoljan ako se broja")
        print("Vasa djeva otvorila je oci, uzvratila poljubac i osmijeh")
        print("Srce Vase dijeve je spaseno!!!!!!!!")
        ime = input("Molimo unesite Vase ime!")
        print(""" <3,<3,<3,<3,<3,<3""", ime, """ i Barby dugo su i sretno zivjeli <3,<3,<3,<3,<3,
        <3,<3,<3,<3,<3,<3,<3,<3,<3,<3,<3,<3,<3,<3""")
        exit(0)

def kraj_igre(kraj):
    print(kraj, "Za vas je ova igra gotova")
    print("Niste osvojili srce nase dijeve, pronadite drugu...Bye")
    exit(0)

def predsoblje():
    print("u predsoblju se nalazi veliki grm sa ruzama koji je okovao vrata")
    print("taj grm ima velike trnove")
    print("kako ces rijesiti grm da bi usao u sobu?")
    print("hoces li posjeci grm ili ga zapaliti?")
    grm_maknut = False


    while True:
        izbor = input("> ")
        if izbor == "zapaliti":
            kraj_igre("zapalio se i grm i kuca i vasa princeza!")
        elif izbor == "posjeci" and not grm_maknut:
            print("grm je posjecen sa vrata")
            print("mozes ih sada otvoriti")
            grm_maknut = True
        elif izbor == "posijeci" and grm_maknut:
            kraj_igre("Posjekli ste sebi nogu i nemozete do princeze...")
        elif izbor == "otvoriti vrata" and grm_maknut:
            zlatna_soba()
        else:
            print("ne razummijem sto zelis, nastavi sjeci grm ili otvori vrata!")

def podrum():
    print("Nalazite se u podrumu prince")
    print(""" to nije mjesto gdje se nalazi princeza, vec mrak i zivotinja koja
    vreba iz mraka, kao i velika kolicina pekmeza koja ju je privukla""")
    print("hoces li pobjeci ili se hrabro boriti sa zivotinjom u mraku?")

    izbor = input("> ")
    if "pobjeci" in izbor:
        start()
    elif "boriti se" in izbor:
        kraj_igre("MMMM to je bilo ukusno, pojeo vas je Medonja!")
    else:
        podrum()
def start():
    print("Nalazite se u kuci")
    print("Trazite vasu usnulu princezastu djevu")
    print("Potrebno je poljubiti je da bi se probudila")
    print("pred vama su dvoja vrata: 1 i 2!!, napisite broj vrata u koja cete uci!?")

    izbor = input("> ")
    if izbor == "1":
        predsoblje()
    elif izbor == "2":
        podrum()
    else:
        kraj_igre("lutali ste okolo hodnikom u kojem je labirint do iznemoglosti...")
start()
