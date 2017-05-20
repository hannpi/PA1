"""Meil on vaja transportida teatud arv inimesi mingi arvu identsete
bussidega. Eeldame, et reisijaid on vähemalt üks.

Koostada programm, mis küsib transporditavate inimeste arvu ja ühe bussi
kohtade arvu (just sellises järjekorras) ning väljastab ekraanile, mitu bussi
on vaja ja mitu inimest on viimases bussis (eeldusel, et kõik eelnevad bussid
on täis)."""

import math
ppl = int(input("Inimeste arv: "))
spots = int(input("Kohtade arv: "))

INeedBus = math.ceil(ppl/spots)
defo = ppl%spots
if defo == 0:
    last = spots
else:
    last = defo
print("Busse vaja: " + str(INeedBus))
print("Viimases bussis inimesi: " + str(last))
