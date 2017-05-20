"""Failis konto.txt on kirjas ujukomaarvudena pangakonto tehingud (kus
positiivsed arvud on sissetulekud ja negatiivsed arvud on väljaminekud). Iga
arv on eraldi real. Näitefaili võite salvestada siit või koostada ise mõne
tekstiredaktoriga (kasvõi Thonnyga). Tekstifaili kasutamiseks programmi sees
peab fail asuma programmifailiga samas kaustas.

Koostada programm, mis

1. loeb failist nimega konto.txt andmed;
2. väljastab ekraanile kõik sissetulekud ehk failist leitud positiivsed arvud.
Iga arv peab olema eraldi real ja positiivsete arvude omavaheline järjekord
peab jääma samaks nagu failis."""

f = open("konto.txt", encoding="UTF-8")
rida = f.readlines()
tehingud = []
with open("konto.txt") as f:
    for rida in f:
        rida = rida.strip()
        tehingud.append(float(rida))

f.close()
#print(tehingud)

for i in range(len(tehingud)):
    #print(i)
    if tehingud[i] > 0:
        print(tehingud[i])
    else:
        pass
