"""soovitud reklaamlauset korduvalt kuvavad.

Esmalt koostada funktsioon banner, mis
1. võtab argumendiks reklaamlause, mida soovitakse kuvada;
2. tagastab reklaamlause, kus kõik tähed on suured tähed.

Teiseks koostada programm, mis
1. küsib kasutajalt, mitu korda soovitakse reklaamlauset kuvada;
2. küsib kasutajalt, millist reklaamlauset ta soovib kasutada;
3. rakendab tsükli abil kasutaja sisestatud arv kordi funktsiooni banner, kus
igal tsükli sammul kutsutakse funktsioon välja argumendiga, milleks on
kasutaja sisestatud reklaamlause;
4. väljastab loodud tsükli abil reklaamlause kasutaja sisestatud arv kordi."""

def banner(fraas):
    return fraas.upper()

kordaja = int(input("Mitu korda soovite reklaamlauset kuvada? "))
sisendfraas = input("Sisestage reklaamlause: ")

while kordaja > 0:
    print(banner(sisendfraas))
    kordaja-=1
