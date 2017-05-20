"""Koostada programm, mis

1. küsib kasutajalt õhutemperatuuri,
2. väljastab ekraanile Ei ole jäätumise ohtu, kui sisestatu on üle 4,0,
3. väljastab On jäätumise oht, kui temperatuur on 4,0 või alla selle.

Temperatuuri võib sisestada nii täisarvuna kui ka ujukomaarvuna, nt -1.3."""

temp = float(input("Sisesta õhutemperatuur: "))

if temp>4:
    print("Ei ole jäätumise ohtu")
else:
    print("On jäätumise oht")

