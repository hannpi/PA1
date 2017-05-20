"""Tervisesport on tervisele kasulik, kui sellega jäädakse mõõdukuse piiridesse.
On erinevaid variante sobiva koormuse valimiseks. Näiteks saab kasutada
sellist arvestust, et maksimaalne pulsisagedus on meestel 220 miinus vanus ja
naistel 206 miinus 88% vanusest. Seejuures erinevate treeningutüüpide puhul
peaks pulsisagedus jääma järgmistesse vahemikesse:

1. tervisetreening 50-70% maksimaalsest pulsisagedusest,
2. põhivastupidavuse treening 70-80% maksimaalsest pulsisagedusest,
3. intensiivne aeroobne treening 80-87% maksimaalsest pulsisagedusest.

Koostada programm, mis küsib kasutajalt

1. vanuse (täisarvuna aastates),
2. soo (kasutaja sisestab M, m, N või n),
3. treeningu tüübi (1 - tervisetreening, 2 - põhivastupidavuse treening,
                    3 - intensiivne aeroobne treening)

ja lõpuks väljastab pulsisageduse vahemiku vastavatel tingimustel formaadis
<vähim pulss> kuni <suurim pulss>, kus vastuses leiduvad arvud on ümardatud
täisarvudeks."""


import math
age = int(input("Sisestage enda vanus: "))
sx = input("Sisestage enda sugu: ")
Caps = sx.capitalize()
TT = input("Sisestage treeningu tüüp: ")

maxping4N = 206-(0.88*age)
maxping4M = 220-age

if Caps == 'M':  
    if str(TT) == '1':
        print("Pulsisagedus peaks olema vahemikus " + str(round(0.5*maxping4M)) + " kuni " + str(round(0.7*maxping4M)) +".")
    elif str(TT) == '2':
        print("Pulsisagedus peaks olema vahemikus " + str(round(0.7*maxping4M)) + " kuni " + str(round(0.8*maxping4M)) +".")
    elif str(TT) == '3':
        print("Pulsisagedus peaks olema vahemikus " + str(round(0.8*maxping4M)) + " kuni " + str(round(0.87*maxping4M)) +".")
    else:
        print("Vale treeningu tüüp.")
elif Caps == 'N':
    if str(TT) == '1':
        print("Pulsisagedus peaks olema vahemikus " + str(round(0.5*maxping4N)) + " kuni " + str(round(0.7*maxping4N)) +".")
    elif str(TT) == '2':
        print("Pulsisagedus peaks olema vahemikus " + str(round(0.7*maxping4N)) + " kuni " + str(round(0.8*maxping4N)) +".")
    elif str(TT) == '3':
        print("Pulsisagedus peaks olema vahemikus " + str(round(0.8*maxping4N)) + " kuni " + str(round(0.87*maxping4N)) +".")
    else:
        print("Vale treeningu tüüp.")
else:
    print("Vale sugu.")
