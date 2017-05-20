"""Optimaalseks kauguseks teleri ja vaataja silmade vahel arvatakse olevat
2,5 korda ekraani diagonaali pikkus. Seega kui on teada kaugus diivanist
teleri asukohani, siis teleri sobiva diagonaali saab arvutada valemi järgi:

(teleri diagonaal tollides) = (kaugus meetrites) * 100 * 0,39 / 2,5

Esiteks defineerida funktsioon nimega teleri_diagonaal, mis
1. võtab argumendiks ühe arvu, mis tähistab kaugust diivanist teleri asukohani
meetrites;
2. arvutab selle põhjal teleri diagonaali tollides;
3. tagastab teleri diagonaali tollides.

Tagastatud teleri diagonaal peab olema ümardatud täisarvuni. Ümardamist peab
sooritama funktsioon ise ja selleks tuleb kasutada funktsiooni round.

Teiseks rakendada loodud funktsiooni programmis, kus
1. kaugus diivanist telerini (meetrites) küsitakse kasutaja käest;
2. väljastatakse teleri diagonaal (tollides) ekraanile.

Oluline on, et teleri diagonaali arvutamise funktsioon ise ei küsiks kasutajalt
midagi ja see funktsioon ise ka ei väljastaks tulemust ekraanile. Need
tegevused peab tegema programmis väljaspool funktsiooni, funktsiooni töö on
vaid arvutada."""

import math
def teleri_diagonaal(dist):
    diag = (dist*100*0.39)/2.5
    return round(diag)

distance = float(input("Sisesta kaugus: "))

print(teleri_diagonaal(distance))
