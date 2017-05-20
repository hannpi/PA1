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

Fail = input("Sisetage failinimi: ")
Tekst = open(Fail, encoding="UTF-8")

järjend = []
for rida in Tekst: #iga rea
    for täht in rida: #iga täht & tühik & koma & muu sarnane
        järjend.append(täht) #lisatakse listi

for i in range(len(järjend)): #iga täht järjendis 
    järjend[i] = järjend[i].capitalize() #tehakse suureks
    #capitalize() ja upper() on samad
print(järjend)

for i in range(len(järjend)):
    if järjend[i] == "Ä": #if Ä
        järjend[i] = "AE" #rewrite with AE
    elif järjend[i] == "Ö" or järjend[i] == "Õ": #if Ö or Õ
        järjend[i] = "OE" #rewrite with OE
    elif järjend[i] == "Ü": #if Ü
        järjend[i] = "UE" #rewrite with UE
    else: #if not Õ, Ä, Ö, Ü
        järjend[i] = järjend[i] #põhimõtteliselt ignore or 1=1

print(''.join(järjend)) #järjend pannakse uuesti kokku tervikuks
