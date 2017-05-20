"""On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv lilli.
Lillepoel on sünnipäev ja pood otsustas klientidele kinkida lilli nii, et
päeva esimene ostja saab ühe lille, teine ei saa ühtegi, kolmas ostja saab
kolm lille, neljas ei saa midagi, viies ostja saab viis lille jne.

Koostada programm, mis

1. küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
2. arvutab while-tsükli abil lillede koguarvu, mida pood kingib;
3. väljastab saadud lillede arvu ekraanile.

Vihje: lillede koguarvust võib mõelda kui summast, milles liidetavad on
paaritud arvud alates 1 kuni esimese paaritu arvuni, mis pole suurem kui
klientide arv. 

Näiteks, kui kasutaja sisestas 7, siis paaritute arvude summa on 16, sest
1 + 3 + 5 + 7 = 16. Kui kasutaja sisestas 8, siis on summaks samuti 16, sest
1 + 3 + 5 + 7 = 16."""

clients = int(input("Sisesta ostjate arv: "))
Flowers = 0
while clients > 0:
    if clients%2 == 0:
        clients -= 1
    else:
        Flowers += clients
        clients -= 2

print("Lillede koguarv on " + str(Flowers) + ".")
