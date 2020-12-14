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
