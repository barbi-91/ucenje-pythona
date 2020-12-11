listastavki= {
    "cvijet": ["bijeli", "crveni", "plavi"],
    "automobil": ["bijeli","crveni","srebrni"],
    "kuca":["roza","zuta", "plava", "zelena"]

}

for stavke in listastavki.keys():
    print(stavke.title(), ":", len(listastavki[stavke]))
