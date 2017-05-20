"""Ada tahab minna reisile ja uurib viimase hetke pakkumisi. Võimalikud
sihtkohad on kirjas failis (iga sihtkoht on eraldi real). Faili võite
salvestada siit või koostada ise mõne tekstiredaktoriga.

Koostada programm, mis

1. küsib kasutajalt failinime (kasutaja sisestab failinime koos
laiendiga, nt sihtkohad.txt);
2. loeb sisestatud nimega failist andmed;
3. näitab kõik sihtkohad koos järjekorranumbritega (alates 1);
4. küsib kasutajalt, mitmes sihtkoht broneerida (kasutaja sisestab alati täisarvu);
5. väljastab ekraanile vastavalt valitud arvule sihtkoha. """

sisend = input("Palun sisestage failinimi: ")
file = open(sisend, encoding="UTF-8")
dest = []

for rida in file:
    rida = rida.strip()
    dest.append(str(rida))

file.close()

print("Võimalikud sihtkohad: ")

for i in range(0, len(dest)):
    print(str(i+1) + ". " + str(dest[i]))

b = int(input("Valige mitmes sihtkoht broneerida: "))
print("Reis on broneeritud. Sihtkoht on " + str(dest[b-1]) + ".")
