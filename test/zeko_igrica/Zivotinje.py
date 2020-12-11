class Zivotinja(Scene):
    bice = [
            "MEDVJED",
            "VUK",
            "LISICA",
            "CAGALJ",
            "KUNA",
        ]
    def enter(self):
        print(Zivotinja.bice[randint(0,len(self.bice)-1)])
