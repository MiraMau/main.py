import sys

# user
UZIVATELE = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# texts
TEXTY = [
    "Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30 and the Union Pacific Railroad, which traverse the valley.",
    "At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.",
    "The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present."
]

# input
jmeno = input("Zadej uzivatelske jmeno: ")
heslo = input("Zadej heslo: ")

if jmeno not in UZIVATELE or UZIVATELE[jmeno] != heslo:
    print("Spatne jmeno nebo heslo, konec.")
    sys.exit()
else:
    print("Vitej,", jmeno)

print("Mame 3 texty.")
cislo = input("Vyber cislo textu (1-3): ")

if not cislo.isdigit():
    print("Nezadal jsi cislo, konec.")
    sys.exit()

cislo = int(cislo)
if cislo < 1 or cislo > 3:
    print("Spatne cislo, konec.")
    sys.exit()

# metrics
text = TEXTY[cislo-1]
slova = text.split()

pocet_slov = len(slova)
velke_pocatecni = 0
velkymi = 0
malymi = 0
cisla = []
delky = {}


for slovo in slova:
    ciste = slovo.strip(".,!?;:")
    if ciste.istitle():
        velke_pocatecni += 1
    if ciste.isupper():
        velkymi += 1
    if ciste.islower():
        malymi += 1
    if ciste.isdigit():
        cisla.append(int(ciste))
    if ciste.isalpha():
        d = len(ciste)
        if d not in delky:
            delky[d] = 1
        else:
            delky[d] += 1

print("Pocet slov:", pocet_slov)
print("Slova velkym pismenem:", velke_pocatecni)
print("Slova VELKYMI:", velkymi)
print("Slova malymi:", malymi)
print("Pocet cisel:", len(cisla))
print("Soucet cisel:", sum(cisla))

