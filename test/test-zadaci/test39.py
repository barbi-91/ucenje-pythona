# # # # things : ['a', 'b','c','d']
# # # # print (things[1])
# # # # things[1] : 'z'
# # # # print(things[1])
# # # stuff : {'name': 'Zed', 'age':39, 'height': 12*6+2}
# # # print(stuff['name'])
# # # print(stuff['age'])
# # # stuff['city'] : "new york"
# # # print(stuff['city'])
# # # print(stuff)
# # #
# # # stuff[1] : "wow"
# # # stuff[2] : "Miaju"
# # # print(stuff[1])
# # # print(stuff[2])
# # # print(stuff)
# # #
# # # del stuff['city']
# # # del stuff[1]
# # # del stuff[2]
# # # print(stuff)
# # #create amapping of states to abbrtrition
# # #states:drzave : curly parentheses, key colon values
# # #drzave i njihove skracenice
# states = {
# 'Oregon':'OR',
# 'Florida':'FL',
# 'California': 'CA',
# 'New York':'NY',
# 'Michigan':'MI'
# }
# print("states",states)
# #creat a basic set os states and some cities in them
# #gradovi i njihovi kljucevi drazave
# cities = {
# 'CA':'San Fencisco',
# 'MI':'Detorit',
# 'FL':'Jacksonvil'
# }
# print("cities",cities)
# #add some cityes
# #dodajemo grad njegova drzava kao kljuc i grad kao values
# cities['NY'] = "New York"
# cities['OR'] = 'Portland'
# print("cities",cities)
#
# #print out cities
# #printamo grad pozivajuci se na drzava dictionari i njegovu value skracenicu
# print('-' * 10)
# print("NY States has:", cities['NY']),
# print("OR states has:", cities['OR'])
#
#
# #printao drzave pozivajuci se na drzava dictionari i kljucnu vrijednost
# # print some states
# #abbreviation skracenica
# print ('-' * 10)
# print ("Michigan's abbreviation is: ", states['Michigan']);
# print ("Florida's abbreviation is: ", states['Florida'])
#
# # do it by using the state then cities dict
# print( '-' * 10)
# print ("Michigan has: ", cities[states['Michigan']]);
# print ("Florida has: ", cities[states['Florida']])
#
#
# # print every state abbreviation
# print('-'*10)
# for state, abbrev in list(states.items()):
#     print (f"{state} is abbreviated {abbrev}")
#
# # print every city in state
# print('-' * 10)
# for abbrev, city in list(cities.items()):
#     print (f"{abbrev} has the city {city}")
#
# # now do both at the same time
# print('##' * 10)
# for state, abbrev in list(states.items()):
#     print (f"{state} state is abbreviated {abbrev}");
#     print (f"and has city {cities[abbrev]}")
#
# print ('-' * 10)
# # safely get a abbreviation by state that might not be there
# state : states.get('Texas')
#
# if not state:
#     print( "Sorry, no Texas.")
#
# # get a city with a default value
# city : cities.get('TX', 'Does Not Exist')
# print (f"The city for the state 'TX' is: {city}")


drzave = {
'Hrvatska': 'HR',
'Slovenija' : 'SI',
'Austrija' : 'AU'
}
print(drzave, "drzave")

gradovi = {
'HR' : 'Zagreb',
'SI' : 'Ljubljana',
'AU' : 'Beč'
}
print(gradovi, "gradovi")
#add some cities
gradovi['HU'] = 'Budimpesta'
gradovi['F'] = 'Paris'
print(gradovi, "gradovi")

gradovi['BIH'] = 'Jajce'
gradovi['I'] = 'Rim'
gradovi['R'] = 'Moskov'
print(gradovi, "add more")

del gradovi['R']
print(gradovi, "del")
# vazno je dati razlicita imaena kad se poziva petlja for jer to nam moze omesti atribute pa se pythn zbuni i na taj naci ne daje rijesenje vec error AttributeError: 'str' object has no attribute 'items'
#dakle for jedan item grad ili drzava in lista drzeve item....
print("grad odredene drzave", gradovi[drzave['Hrvatska']]);
print("drzava odredenog grada", gradovi[drzave['Slovenija']])

for jedna_drzava, kratica  in list (drzave.items()):
    print(f"###{jedna_drzava} i njihova kratica {kratica}")

for kratica, grad in list(gradovi.items()):
    print(f"***{kratica} i njihovi gradovi {grad}")

for drzava, kratica in list(drzave.items()):

    print(f"???{drzava} drzava i njihova kratica {kratica}");
    print(f"??i njihovi gradovi{gradovi[kratica]}")



#################
drzava = drzave.get('Hrvatska')
if drzava:
    print(f"Proneadena je {drzava} u listi")
if not drzava:
    print("Sorry nije")
drzava = drzave.get('Texas')
if not drzava:
    print(f"Nije {drzava} pronadena")

grad = gradovi.get('Hrv', 'Vukovar')# drugi kometar koji dajemo je kljuc za value umjesto tog value mozemo bilo sto napisati ka stojje i orginalno da on ne postji ako odabermo drzavu koja je tamo i ne postoji
print(f" grad za 'Hrv' drzavu je {grad}")

grad = gradovi.get('Hrv', 'Vukovar')# drugi kometar koji dajemo je kljuc za value umjesto tog value mozemo bilo sto napisati ka stojje i orginalno da on ne postji ako odabermo drzavu koja je tamo i ne postoji
print(f" grad za 'Hrv' drzavu je {grad}")

grad = gradovi.get('SI', "nije pronaden")
print(f"u listi gradova drzave 'si' je {grad}")
grad = gradovi.get('ako', "nije pronaden")
print(f"u listi gradova drzave 'ako' je {grad}")
grad = gradovi.get('Bel', "Sofi")
print(f"u listi gradova drzave 'bel' je {grad}")

grad = gradovi.get('Moskov', "Rusija")
print(f"U LISTI GRDOVA MOSKOV JE{grad}")
