"""Koostada programm, mis küsib kasutajalt Leedu perekonnanime ja väljastab:

Abielus, kui nimi lõpeb tähtedega "ne",
Vallaline, kui nimi lõpeb tähtedega "te",
Määramata, kui nimi lõpeb tähega "e" (aga mitte "ne" ja "te"),
Pole ilmselt leedulanna perekonnanimi, kui nimi ei lõpe tähega "e".
"""

name = str(input("Sisestage Leedu perekonnanimi: "))
List = ["n", "t"]

if name[-2:] == "ne":
    print("Abielus")
elif name[-2:] == "te":
    print("Vallaline")
elif name[-1] == "e" and (name[-2] != "n" or name[-2] != "t"):
    print("Määramata")
else:
    print("Pole ilmselt leedulanna perekonnanimi")
