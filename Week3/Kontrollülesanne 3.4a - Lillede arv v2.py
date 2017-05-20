"""On traditsioon, et rõõmsatel puhkudel kingitakse paaritu arv lilli. Üks
teine lillepood on otsustanud, et nende sünnipäeval saab iga klient
kingituseks lilli nii, et esimene ostja saab ühe lille, teine ostja saab kolm
lille, kolmas ostja saab viis lille, neljas ostja seitse lille jne.

Koostada programm, mis

1. küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
2. arvutab while-tsükli abil lillede koguarvu, mida pood klientidele kingib;
3. väljastab kingitavate lillede koguarvu.

Näiteks, kui kasutaja sisestas 4, siis paaritute arvude summa on
16, sest 1 + 3 + 5 + 7 = 16. Kui kasutaja sisestas 7, siis on summaks 49, sest
1 + 3 + 5 + 7 + 9 + 11 + 13 = 49."""

clients = int(input("Sisestage ostjate arv: "))
FL=0
while clients > 0:
    FL+=((clients-1)*2)+1
    clients-=1
print("Lillede koguarv on " + str(FL) + ".")


    
