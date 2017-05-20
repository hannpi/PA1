"""Kuupäevade esitamisel tekib enim probleeme, kui kuupäev kirjutatakse
kujul „05.06.2005“ – sellisel puhul pole võimalik aru saada, kas on mõeldud
5. juunit või hoopis 6. maid. Eestis ja enamikes teistes riikides kirjutatakse
kuupäev reeglina formaadis DD.MM.YYYY, kuid Ameerika Ühendriikides on levinum
järjekord MM.DD.YYYY. Segaduse vältimiseks tuleks kuu nimi välja kirjutada.

Esmalt kirjutada funktsioon kuu_nimi, mis
1. võtab argumendiks kuu järjekorranumbri;
2. tagastab vastava kuu nime (väikeste tähtedega).

Teiseks luua funktsioon kuupäev_sõnena, mis
1. võtab argumendiks ühe sõnena esitatud kuupäeva formaadis “DD.MM.YYYY”
(nt '24.02.1918');
2. tagastab selle sama kuupäeva kujul <päev>. <kuu_nimi> <aasta>. a
(nt '24. veebruar 1918. a'), kusjuures kuupäev_sõnena peab ühe toimingu
delegeerima funktsioonile kuu_nimi. Abiks võib ka olla funktsioon split.

Kolmandaks kirjutada programm, mis
1. küsib kasutajalt kuupäeva kujul “DD.MM.YYYY”;
2. väljastab ekraanile vastava kuupäeva sõnena kujul
<päev>. <kuu_nimi> <aasta>. a."""

def kuu_nimi(number):
    if number == 1:
        return "jaanuar"
    elif number == 2:
        return "veebruar"
    elif number == 3:
        return "märts"
    elif number == 4:
        return "aprill"
    elif number == 5:
        return "mai"
    elif number == 6:
        return "juuni"
    elif number == 7:
        return "juuli"
    elif number == 8:
        return "august"
    elif number == 9:
        return "september"
    elif number == 10:
        return "oktoober"
    elif number == 11:
        return "november"
    else:
        return "detsember"


def kuupäev_sõnena(kuupäev):
    kuupäev = kuupäev.split(".")
    päev = str(kuupäev[0])
    kuu = str(kuu_nimi(kuupäev[1]))
    aasta = str(kuupäev[2])
    formaat = päev + ". " + kuu + " " + aasta + ". a"
    return formaat

sisestatud_päev = str(input("Sisetage kuupäev formaadis 'DD.MM.YY': "))
print(kuupäev_sõnena(sisestatud_päev))
