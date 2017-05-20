"""Mõned õpetajad on tavatsenud õpilasi tahvli juurde vastama kutsuda kuupäeva
järgi vastavalt õpilaste nimekirjale. Näiteks 4. kuupäeval tuleb esimesena
vastama nimekirjas 4. olev õpilane. Failis nimekiri.txt on õpilaste nimed,
igaüks eraldi real. Üks selline, mis on genereeritud leheküljel
http://random-name-generator.info/, on siin. Võite ise koostada ka teistsuguse
nimekirja.

Koostada programm, mis

1. küsib failinime (eeldame, et kasutaja sisestatud nimega fail leidub ja seal
on vähemalt 31 nime);
2. loeb sisestatud nimega failist andmed;
3. väljastab vastavalt tänasele kuupäevale õpilase nime, kes peab vastama tulema. 

Programm peab tänase kuupäeva leidma automaatselt."""

from datetime import *
a = input("Sisestage failinimi: ")
f = open(a, encoding="UTF-8")
nimed = []

for rida in f:
    rida = rida.strip()
    nimed.append(str(rida))

p2 = datetime.now().day #p2 ehk päev

print("Vastama tuleb: " + nimed[p2-1])
