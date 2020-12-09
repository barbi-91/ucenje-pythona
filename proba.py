
# # # # class Mama(object):
# # # #     def __init__(self, citat):
# # # #         self.citat = citat
# # # #         print(citat)
# # # #     def overidanje(self, citat):
# # # #         print("mamin citat", citat)

# # # # class Kcer(Mama):
# # # #     def overidanje(self,citat):
# # # #         print("kcerin citat",citat)


# # # # Ana = Mama("ma")
# # # # Lea = Kcer("kc")

# # # # Ana.overidanje("tko se maca")
# # # # Lea.overidanje("laca")


# # # # # # pogodak = input("pogodi: >>> ")
# # # # # # pokusaji = 1

# # # # # # while pogodak != 'dabar'and pokusaji < 10:
# # # # # #         pokusaji += 1
# # # # # #         print("pokusaj ponovno")
# # # # # #         pogodak = input("pogodi: >>> ") 

# # # # # # if pogodak == 'dabar':
# # # # # #     print("""
# # # # # #         Još prije podne stigao je na brežuljak Zečevo sa kupusom i mrkvom. 
# # # # # #         Pozvao je na ručak sve zečeve iz cijele šume i spasio ih od gladi..
# # # # # #         Svi su mu zečevi bili zahvalni što ih je nahranio usred zime. 
# # # # # #         Na njihova lica vratila se radost, a iz očiju zablistao je vedar sjaj. 
# # # # # #         Od tada Zeko je među svojim rođacima uživao veliki ugled i povjerenje.
# # # # # #         """)
# # # # # #     print ('potok')       
# # # # # # else:
# # # # # #     print("""
# # # # # #         Lovac je uhvatio mladog nadobudnog zeca.
# # # # # #         """)
# # # # # #     print ('smrt')

# # # # from random import randint

# # # # pogodak = randint(1,4)
# # # #         #random broj 
# # # # print(pogodak)
# # # # guess = input ("[pogodi]> ")

# # # # if int(guess) != pogodak:
# # # #     print("uzas")
# # # # else:
# # # #     print("bravo")



# # # from sys import exit
# # # from random import randint
# # # from textwrap import dedent

# # # class Scene(object):
# # #     def enter(self):
# # #         print("Slika scene")
# # #         exit(0)
# # # ##########################################
# # # class Organizacija(object):

# # #     def __init__(self, plan):
# # #         self.plan = plan

# # #     def igra(self):
# # #         trenutna_scena = self.plan.scena_otvaranja()
# # #         zadnja_scena = self.plan.sljedeca_scena('kraj')

# # #         while trenutna_scena != zadnja_scena:
# # #             sljedeca_scena_ime = trenutna_scena.enter()
# # #             trenutna_scena = self.plan.sljedeca_scena(sljedeca_scena_ime)
# # #         trenutna_scena.enter()
# # # ##########################



# # # class Smrt(Scene):
# # #     citati = [
# # #         "End. Ljudi vam nikada neće oprostiti uspjeh, čvrst hod nakon pada i širok osmijeh preko cijelog lica."
# # #         "End. Budi pametan… i pravi se lud… tako najbolje vidiš stvari."
# # #         "End. ‘Toliko je u životu bilo stvari kojih smo se bojali. A nije trebalo, trebalo je živjeti… "
# # #         "End. Život je ono što se događa dok vi pravite planove za život. "
# # #         "End. Kada se penješ stepenicama uvijek pozdravi one koje usput srećeš; jer ćeš ih ponovno vidjeti kad budeš silazio."
# # #     ]
# # #     def enter(self):
# # #         print(Smrt.citati[randint(0,len(self.citati)-1)])
# # #         print("....i onako si izgubio, mozda shvatis da nije uvijek najbolje biti najpametniji, najhrabriji ili najaci...mozda naucis nesto iz ove mudre izreke!")
# # #         exit(0)

# # # class Vrt(Scene):
# # #     def enter(self):
# # #         print(dedent("""
# # #             Iznad malog sela Livadovo uzdiže se lagani brežuljak Zečevo,
# # #             obrastao niskom, pretežno crnogoričnom šumom u kojoj živi
# # #             mnogo zečeva. Zato je ovaj brežuljak i dobio ime po zečevima,
# # #             njegovim stanovnicima, lijepim i ljupkim životinjama.

# # #             U Zecevu zivi Zeko koji se uvijek dosjeti nečeg pametnog što
# # #             drugim zečevima ne pada ni na kraj pameti, a usto je i iznimno
# # #             oprezan. Čim bi netko nepoznat ili sumnjiv došao u njihovu šumu,
# # #             Zeko bi uzdignuo uši, raširio oči i podignuo se na zadnje noge,
# # #             te brzim pokretima lupnuo jednom nogom u pod, a to je znak za
# # #             uzbunu. Svi se zečevi na znak uzbune odmah sakriju i zaključaju
# # #             u svoje zečje kućice. Zeko vodi dosta brige o sigurnosti svojih
# # #             rođaka. Iako je na Zečevu tijekom godine bilo dovoljno hrane za
# # #             sve zečeve, dolaskom zime bilo je sve manje i manje. Zečevi tada
# # #             žive veoma skromno. Oni tada kopaju snijeg, tražeći suhu travu,
# # #             glodaju koru drveća te grmlje u šumi. Tada zečevi pretežno žive
# # #             u svojim toplim kućicama(jazbinama), pogotovo kada padne snijeg.
# # #             Stoga Zeko mora u Opskrbu po zelje i mrkvu do vrta u selu i to
# # #             oprezno kako ga ne bi uhvatila lisica, lovac ili ljuti seljanin.

# # #             Zeko je Krenuo hrabro po mrkvu, medutim naisao je na gladnu lisicu
# # #             putem koja ga je uocila! Pomozi Zeki odluciti, hoce li se nas Zeko:
# # #                 a) sakriti ?
# # #                 b) boriti ?
# # #                 c) pobjeci ?

# # #             """))

# # #         radnja = input("> ")

# # #         if radnja == "sakriti":
# # #             print(dedent("""
# # #                 Ako nemaš brod, plivaj!
# # #                 Ako ne znaš plivati, izgradi brod!
# # #                 Uspjeh je stvar stava!

# # #                 Sugerirati jednom Zeki da se sakrije nije hrabro a niti mudro.
# # #                 Zbog krive odluke, a vrlo dobrog njuha te velike lukavosti i
# # #                 spretnosti, Zeko je pao u sape lisice.
# # #                 """))

# # #             return 'smrt'


# # #         elif radnja == "boriti":
# # #             print(dedent("""
# # #                 U tebi su tri čovjeka: Jedan, kakav bi želio biti. Drugi, kakav misliš da jesi.
# # #                 I treći, kakav si zaista. Tog jedino ne poznaješ. Naposljetku, suština saznavanja
# # #                 nije u tome gubimo li igru, već kako gubimo, što s time spoznajemo, čemu nas je
# # #                 poraz naučio i kako nas to mijenja. Gubiti na određeni način znači – dobivati.

# # #                 Vrlina zeca nije u snazi vec u brzini, odlucnosti i inteligenciji.

# # #                 Lisica je omastila brk.
# # #                 """))

# # #             return 'smrt'


# # #         elif radnja == "pobjeci":
# # #             print(dedent("""
# # #                 Puno malih koraka mogu preokrenuti Zecji svijet.
# # #                 Ništa ne može zamijeniti upornost. Niti talent,
# # #                 niti genijalnost, niti obrazovanje. Upornost i odlučnost su  moć.
# # #                 Zeko je obišao cijelo selo i vidio pune vrtove zasađene prekrasnim kupusom.

# # #                 Od silne radosti su rasle zazubice. Ujedno je bio i tužan, jer kupus je mogao
# # #                 dohvatiti samo okom, jer su vrtovi bili ograđeni visokim i gustim plotom.
# # #                 Seljake se nije usudio pitati da mu daju glavicu kupusa, jer seljaci baš
# # #                 ne vole vidjeti zečeve u svom vrtu. Zato je pazio da ga nitko ne vidi i pažljivo
# # #                 se šuljao uz plotove vrtova. I na kraju trud se isplatio. U zadnjem vrtu na
# # #                 kraju sela, malo udaljen od kuća, Zeko je ispod plota iskopao jednu rupicu,
# # #                 tek toliku da se mogao provući, kroz koju je ušao u vrt. Rupu je mogao kopati
# # #                 na miru, jer tuda nije nitko prolazio. Napokon njegovoj gladi došao je kraj.

# # #                 I tako je Zeko svako jutro dok su seljaci još spavali, odlazio u njihov
# # #                 vrt s kupusom i mrkvom. Medutim jednog dana na povratku kuci, prolazeci
# # #                 summom ugledao je lovca.
# # #                 """))

# # #             return 'lovac'

# # #         else:
# # #             print("Nepravilno unesena rijec!")
# # #             return 'vrt'
# # # class Zagonetke(Scene):
# # #     odgonetke = [
# # #         """Kraj potoka ili rijeke
# # #             On prepreke pravi neke.
# # #             Drvosječa to je hrabar,
# # #             to bi bio mudri ___?___.""",
# # #                     #dabar

# # #         """Duge uši, kratke noge,
# # #             one pamte staze mnoge:
# # #             mene jure redom svi -
# # #             sove, lije, lovci, psi.
# # #             I kad spavam, tj. ležim,
# # #             ja sve mislim kud da bježim.
# # #             Eci, peci, pec,
# # #             ja sam mali___?___.""",
# # #                     #zec

# # #         """Po krošnjama šećem
# # #             i veselo skakućem.
# # #             Volim šumski mir.
# # #             Da zimi ne prosim
# # #             u kućicu nosim
# # #             lešnike i žir, da
# # #             mi bude fina vecerica,
# # #             ja sam slatka ___?___."""
# # #                 #vjeverica
# # #     ]

# # #     def enter(self):
# # #         print(Zagonetke.odgonetke[randint(0,len(self.odgonetke)-1)])



# # # class LovSuma(Scene):
# # #     def enter(self):
# # #         print(dedent("""
# # #             Polako, ali pažljivo da ga ne vidi, sa punom vrećom kupusa
# # #             uz brdo penjao se Zeko. Vreća je bila teška pa se Zeko morao
# # #             odmarati nekoliko puta.

# # #             Prilikom odmora nije ni znao da gubi vrijeme, lovac je slijedio njegov
# # #             trag te uhvatio zeca. Kako je Zeko bio vrlo inteligentan, pokusao je
# # #             pregovarati s lovcem ne bi li ga pustio. Ponudi je lovcu da mu uz rijesenu
# # #             zagonetku uslisi molitve te ga pusti u sumu. Lovac nije znao da je Zeko najmudrije
# # #             bice u sumi te misleci da zec nema nikakve sanse pristane na okladu.

# # #             Lovac se zamisli... a potom rece:
# # #             """))

# # #         tko_je = Zagonetke()
# # #         tko_je.enter()

# # #         pogodak = input("pogodi: >>> ")
# # #         pokusaji = 0

# # #         while pogodak != "dabar" and pogodak != "zec" and pogodak != "vjeverica" and pokusaji < 10:
# # #             pokusaji += 1
# # #             print("pokusaj ponovno")
# # #             pogodak = input("pogodi: >>> ")

# # #         if pogodak == 'dabar' or pogodak == 'zec' or pogodak =='vjeverica':
# # #             print(dedent("""
# # #                 Još prije podne stigao je na brežuljak Zečevo sa kupusom i mrkvom.
# # #                 Pozvao je na ručak sve zečeve iz cijele šume i spasio ih od gladi.
# # #                 Svi su mu zečevi bili zahvalni što ih je nahranio usred zime.
# # #                 Na njihova lica vratila se radost, a iz očiju zablistao je vedar sjaj.
# # #                 Od tada Zeko je među svojim rođacima uživao veliki ugled i povjerenje.
# # #                 """))

# # #             return 'potok'


# # #         else:
# # #             print(dedent("""
# # #                 Lovac je uhvatio mladog nadobudnog zeca.
# # #                 Jedina prava mudrost je u spoznaji -da ništa ne znaš.
# # #                 """))

# # #             return 'smrt'


# # # class Potok(Scene):

# # #     def enter(self):
# # #         print(dedent("""
# # #             A onda su došli hladniji dani, zekina braća i sestre su sve češće
# # #             ostajali kod tople kuće umjesto igre u potočiću… Ali mali zeko nije
# # #             odustajao, svaki dan on bi došao, skakao i šljapkao po svom potočiću.
# # #             Zeku nije smetala ni kiša ni vjetar ni hladnoća, sve dok je čuo žubor
# # #             svog voljenog potočića zeko je bio sretan.
# # #             No, jedne zimske noci, u Zecevu smrzno se, potocic i pokrio ga snijeg.
# # #             I tuzanm mislio Zeko ta gdje je potok taj, uskoro ce i prvi maj.

# # #             Konačno je zeko odlučio potražiti pomoć šumskih životinja…
# # #             I tako se zaputio u šumu. Prvo je sreo veliko vuka i upitao ga zna li
# # #             možda gdje je nestao njegov potočić… Ali vuk nije znao. Zatim je sreo medu,
# # #             ali ni medo nije znao. Ipak, mali zeko se nije dao obeshrabriti.
# # #             Sljedeća životinja koju je sreo bio je šumski jež, ali ni od njega nije bilo pomoći.

# # #             I tako je zeko tumarao šumom sve dok nije sreo šumsku liju.
# # #             Na njegovo pitanje lija je odgovorila: “Mali zeko nemoj biti tužan.
# # #             Tvoj potočić nije nestao! Samo se zaledio. Čim dođe ljepše vrijeme i
# # #             snijeg malo okopni, tvoj potočić će veselo žuboriti.

# # #             No Zeko nije zelio cekati, i nisu mu se svidali odgovori.
# # #             Zeko je razmisljao kako si moze pomoci i dosao na  ideju.
# # #             odmrznuti potok vatrom ili usnuti te docekati potocic jer nema strpljenja.
# # #             """))
# # #         radnja = input("> ")

# # #         if radnja == 'odmrznuti':
# # #             print(dedent("""
# # #                 Zeko nije naucen na vatru, sve je poslo po zlu. Niti je zapalio vatru niti
# # #                 otpoio led. Niti dosao do vode a jos se dobro i prehladio.
# # #                 """))
# # #             return 'smrt'

# # #         elif radnja == 'usnuti':
# # #             print(dedent(""" Zeko je odabra da ce poci spavati kako bi proljece sto prije
# # #                 doslo i kako bi mogao uzivati sa svojim prijateljima pored potocica koji
# # #                 ih je tako smijelo mamio svojim plavim ljeskanjem i suncem te cvijecm koje
# # #                 se savrseno uklapalo u idilu te male doline.

# # #                 Tako je Zeko radosno odskakuto u svoj krevetic.
# # #                 """))
# # #             return 'zecja_rupa'

# # #         else:
# # #             print("krivo upisan tekst")
# # #             return 'potok'

# # # # class Zivotinja(Scene):
# # # #     zivotinje = [
# # # #     "medo"
# # # #     "vuk"
# # # #     "lisica"
# # # #     ]
# # # #     def zivotinja(self):
# # # #                 print(Zivotinja.zivotinje[randint(0,len(self.zivotinje)-1)])
# # # #                 exit(0)

# # # class ZecjaRupa(Scene):
# # #     def enter(self):
# # #         print(dedent("""




# # #             Kako bi se maleni zeko probudio iz najljpseg ziskog sna i shvatio da je
# # #             doslo proljece te ugledao svoje predivno malo mjesto sa potocicem sumom
# # #             i zivahnim zivotinjama te radnosnim pricicama koje cvrkucu pozdravljajucuci
# # #             prekrasan sucnani dan :D potrenbno je otvoriti prava vratila!

# # #             Pogodi broj vrata u kojima zeko spava.
# # #             """))

# # #         vrata = randint(1,4)
# # #         print(vrata)
# # #         pogodak = input ("[pogodi]> ")
# # #         print(pogodak)

# # #         if int(pogodak) != vrata:
# # #             # a = Zivotinja.zvivotinje()
# # #             print("Bili ste tik do pobjede sa budenjem zeke. Pojeo vas je ljuti")
# # #             return 'smrt'

# # #         else:
# # #             print(" Zeko je zato postao najpoznatiji i najslavniji zec u cijeloj šumi na Zečevu.")
# # #             return 'kraj'


# # # class Kraj(Scene):

# # #     def enter(self):
# # #         print("Pobjedili ste zimu, Bravo!")

# # #         return 'kraj'


# # # class Mapa(object):

# # #     scene = {
# # #         'vrt': Vrt(),
# # #         'lovac': LovSuma(),
# # #         'potok': Potok(),
# # #         'zecja_rupa': ZecjaRupa(),
# # #         'smrt': Smrt(),
# # #         'kraj': Kraj()
# # #         }

# # #     def __init__(self, startna_scena):
# # #         self.startna_scena = startna_scena

# # #     def sljedeca_scena(self, ime_scene):
# # #         ime = Mapa.scene.get(ime_scene)
# # #         return ime

# # #     def scena_otvaranja(self):
# # #         return self.sljedeca_scena(self.startna_scena)


# # # zeko_mapa = Mapa('vrt')
# # # zeko_igra = Organizacija(zeko_mapa)
# # # zeko_igra.igra()

# # li = [
# #         """Kraj potoka ili rijeke
# #             On prepreke pravi neke.
# #             Drvosječa to je hrabar,
# #             to bi bio mudri ___?___.""",
# #                     #dabar

# #         """Duge uši, kratke noge,
# #             one pamte staze mnoge:
# #             mene jure redom svi -
# #             sove, lije, lovci, psi.
# #             I kad spavam, tj. ležim,
# #             ja sve mislim kud da bježim.
# #             Eci, peci, pec,
# #             ja sam mali___?___.""",
# #                     #zec

# #         """Po krošnjama šećem
# #             i veselo skakućem.
# #             Volim šumski mir.
# #             Da zimi ne prosim
# #             u kućicu nosim
# #             lešnike i žir, da
# #             mi bude fina vecerica,
# #             ja sam slatka ___?___."""
# #                 #vjeverica
# #     ]
# # from sys import exit
# # brojac = 0
# # while True:
# #     a = input(">>> ")
# #     if a == "5":
# #         print(" izlaz ")
# #         exit(1)
# #     elif a != "5" and brojac < 3:
# #         for elem in li:
# #             thiselem = elem
# #             nextelem = li[li.index(elem)+1]
# #         brojac +=1
        
# # vrata = 2003
# # print("Broj koji otvara vrata je cetveroznamen broj i predstavlja datum dolaska proljeca(dan i mjesec)")

# # pogodak = input ("[pogodi]> ")

# # brojac = 1
# # while int(pogodak) != vrata and brojac < 3:
# #     brojac += 1
# #     print("pokusaj ponovno")
# #     pogodak = input("pogodi: >>> ")


# # if pogodak == vrata:
# #     print("Bili ste tik do pobjede sa budenjem zeke. Pojeo vas je ljuti", "medo")
# #     print('smrt')


# # else:
# #     print(" Zeko je zato postao najpoznatiji i najslavniji zec u cijeloj šumi na Zečevu.")
# #     print ('kraj')



# from test import class Zivotinje()
# class ZecjaRupa(Scene):
#     def enter(self):
#         print(dedent("""
#             Kako bi se maleni zeko probudio iz najljpseg ziskog sna i shvatio da je
#             doslo proljece potrenbno je pogoditi pravilnu sifru na vratima.
#             """))

#         vrata = 2003
#         print("Broj koji otvara vrata je cetveroznamen broj i predstavlja datum dolaska proljeca(dan i mjesec)")

#         pogodak = input ("pogodi sifru >>> ")

#         brojac = 1
#         while int(pogodak) != vrata and brojac < 3:
#             brojac += 1
#             print("pokusaj ponovno")
#             pogodak = input("pogodi: >>> ")

#         if pogodak == vrata:
#             print("Bili ste tik do pobjede sa budenjem zeke. Pojeo vas je ljuti:")
#             ljuti= Zivotinje()
#             ljuti.enter()
#             return 'smrt'

#         else:
#             print("""Zeko je zato postao najpoznatiji i najslavniji zec
#                             u cijeloj šumi na Zečevu.""")
#             return 'kraj'
