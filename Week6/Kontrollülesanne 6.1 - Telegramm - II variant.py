"""Aastakümneid oli telegramm infovahetamisel väga olulisel kohal. Telegrammiga
teatati saabumistest, õnnitleti jpm. Praeguseks on telegrammid paljudes maades
(ka Eestis) ajalukku jäänud ja teisteski kasutatakse neid järjest vähem. Noorem
generatsioon pole telegrammidega tõenäoliselt üldse kokku puutunud ja ka
vanemad ei mõtle telegrammidele eriti sageli. Muuseumides ja ajalooblogides
võib ühtteist siiski leida. Ilmselt on telegramme ka kodustes arhiivides.

Telegrammis kasutati ainult suurtähti. Täpitähti kasutada ei saanud ja nii oli
Ä asemel kasutusel AE, Õ ja Ö asemel OE ja Ü asemel UE.

Olgu (UTF-8 kodeeringus) failis sõnum, mis on kirjutatud tavalisel moel.

Kirjutada programm, mis

1. küsib kasutajalt failinime,
2. loeb vastavast failist sõnumi ja
3. väljastab selle ekraanile telegrammi stiilis. Teha tuleb asendused
 - Ä, ä → AE
 - Õ, õ, Ö, ö → OE
 - Ü, ü → UE
 - Kõik tähed tuleb muuta suurtähtedeks.
 - Teisi märke ei muudeta."""

FN = input("Sisestage failinimi: ")
fail = open(FN, encoding="UTF-8")

def correction(text):
    for i in range(len(text)):
        if text[i] == "Ä":
            text.remove(text[i])
            text.insert(i, "AE")
        elif text[i] == "Õ" or text[i] == "Ö":
            text.remove(text[i])
            text.insert(i, "OE")
        elif text[i] == "Ü":
            text.remove(text[i])
            text.insert(i, "UE")
        else:
            pass
    return text

tekst = []
for rida in fail:
    for täht in rida:
        tekst.append(täht)

for i in range(len(tekst)):
    tekst[i] = tekst[i].upper()

for i in range(len(tekst)):
    correction(tekst)

print(''.join(tekst))
