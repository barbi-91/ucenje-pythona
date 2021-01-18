from random import randint

class Zagonetke():
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
