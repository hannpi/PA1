"""Kirjade seast rämpsposti (spämmi) leidmiseks saab kasutada filtreid, mis
filtreerivad välja konkreetsetele tingimustele vastavaid kirju. Kalmer teeb
filtrit, kus filtreeritakse välja kirjad, mille kohta on vähemalt üks
järgmistest tingimustest tõene:

1. kirjal ei ole teema pealkirja,
2. kiri sisaldab manusena faili ja kirja suurus ületab 1 MB.

Koostada Kalmeri jaoks programm, milles

1. küsitakse kirja suurust megabaitides (kasutaja sisestab ujukomaarvu),
2. küsitakse kirja teema pealkirja (kasutaja sisestab teema pealkirja või kasutaja sisestus on tühi),
3. küsitakse, kas kirjaga on kaasas fail (kasutaja sisestab "jah" või "ei"),
4. väljastatakse ekraanile "Kiri on spämm", kui kiri filtreeritakse välja, vastasel juhul väljastatakse "Kiri ei ole spämm".

Proovige kirjutada programm, kasutades ainult ühte tingimuslauset. Kui see ei
õnnestu, siis võib ka mitmega."""


size = float(input("Sisestage kirja suurus: "))
title = str(input("Sisestage kirja teema pealkiri: "))
addOn = str(input("Kas kirjaga on kaasas fail?: "))
List = ["jah", "ei"]
if addOn not in List:
    print("KIRJUTA JAH VÕI EI")
else:
    if title == "" or (float(size) > 1 and str(addOn) == "jah"):
        print("Kiri on spämm")
    else:
        print("Kiri ei ole spämm")
