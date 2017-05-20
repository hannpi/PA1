"""On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv lilli.
Lillepoel on sünnipäev ja pood otsustas klientidele kinkida lilli nii, et
päeva esimene ostja saab ühe lille, teine ei saa ühtegi, kolmas ostja saab
kolm lille, neljas ei saa midagi, viies ostja saab viis lille jne.

Koostada programm, mis

1. küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
2. arvutab for-tsükli ja funktsiooni range() abil lillede koguarvu, mida pood
kingib;
3. väljastab saadud lillede arvu ekraanile."""

clients = int(input("Sisestage ostjate arv: "))
flowers = 0
for i in range(1, clients+1):
    if i%2==1:
        flowers += i
    else:
        pass

print("Lillede koguarv on " + str(flowers) + ".")
