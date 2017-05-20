"""Koostada EasyGUI graafilise kasutajaliidesega kalkulaatori programm, mis

1. laseb kasutajal
 - sisestada kaks täisarvu lõigus 1-10 (integerbox);
 - nuppude abil valida liitmise, lahutamise või korrutamise vahel (buttonbox);
2. väljastab arvutuse tulemuse (msgbox).

Automaatkontrolliks peab faili nimi olema yl63.py."""

from easygui import * # EasyGui kasutamiseks importida

firstNr = integerbox("Sisestage esimene täisarv lõigus 1-10: ", lowerbound = 1, upperbound = 10)
secondNr = integerbox("Sisestage teine täisarv lõigus 1-10: ", lowerbound = 1, upperbound = 10)
valikud = ["+", "-", "*"]
vajutati = buttonbox("Valige tehe: ", choices = valikud)

if vajutati == "+":
    summa = firstNr + secondNr
    msgbox("Tehte tulemus on " + summa + ".")
elif vajutati == "-":
    vahe = firstNr - secondNr
    msgbox("Tehte tulemus on " + vahe + ".")
else:
    korrutis = int(firstNr)*int(secondNr)
    msgbox("Tehte tulemus on " + korrutis + ".")
# teateaken

