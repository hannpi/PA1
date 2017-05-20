"""2016. aastal registreeriti Eestis 637 uut mopeedi (http://www.stat.ee/34654).
Registreeritud mopeedide andmed on kuude kaupa failis mopeedid.txt, kus
esimesel real on jaanuaris registreeritud mopeedide arv, teisel real
veebruaris registreeritud mopeedide arv jne. Faili võite salvestada siit või
koostada ise mõne tekstiredaktoriga.

Koostada programm, mis

1. loeb failist registreeritud mopeedite andmed kuude järgi järjendisse;
2. küsib kasutajalt täisarvu, mis tähistab ühe kuu järjekorranumbrit
(jaanuar 1, veebruar 2 jne);
3. väljastab, mitu uut mopeedi sel kuul registreeriti."""

f = open("mopeedid.txt", encoding="UTF-8")
rida = f.readlines()
mopeedid = []
with open("mopeedid.txt") as f:
    for rida in f:
        rida = rida.strip()
        mopeedid.append(int(rida))

f.close()
#print(mopeedid)

kuu = int(input("Palun sisestage mitmes kuu: "))
mop = mopeedid[kuu-1]
print(str(kuu) + ". kuul registreeriti " + str(mop) + " uut mopeedi.")
