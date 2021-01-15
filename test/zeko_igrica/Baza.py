from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):
    def enter(self):
        print("Slika scene")
        exit(0)
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
    from smrt import Smrt
    from vrt import Vrt
    from zagonetke import Zagonetke
    from lov_suma import Lov_Suma
    from potok import Potok
    from zivotinje import Zivotinja
    from zecja_rupa import Zecja_Rupa
    from kraj import Kraj

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




