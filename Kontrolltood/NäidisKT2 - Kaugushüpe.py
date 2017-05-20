# Juhend originaalselt loenguslaididelt, lühikokkuvõte kommenteerituna:

#1. KÜSIB FAILINIME
#2. LOEB FAILIST SISSE ARVUD (meetrites) MINGISSE LISTI
#3. KÜSIB PARENDUST (sentimeetrites)
#4. EDASTAB LISTI TEGELIKE TULEMUSTEGA
#5. NÄITAB, MILLISED NEIST TÄITSID MIINIMUMI
#6. ARVUTAB ARITMEETILISE KESKMISE KOGU HULGA PEALE.

import math

def parandatud_tulemus(hüpe, parendus):
    TegelikTulemus = (hüpe+(parendus/100))
    return TegelikTulemus

def aritmeetiline_keskmine(list):
    summa = 0
    for i in range(len(list)):
        summa += list[i]
    return round((summa/(len(list))), 3)

fNimi = input("Sisestage failinimi: ")
f = open(fNimi, encoding="UTF-8")
FakeResults = []

for rida in f:
    rida = rida.strip()
    FakeResults.append(float(rida))

#print(FakeResults)
Viga = float(input("Kui suurt parendust on vaja (cm): "))
Quota = float(input("Mis tulemusega kvalifitseerutakse: "))
RealResults = []

for i in range(len(FakeResults)):
    RealResults.append(parandatud_tulemus(FakeResults[i], Viga))
print(RealResults)

print("Aritmeetiline keskmine kõikide tulemuste peale on", aritmeetiline_keskmine(RealResults))

for i in range(len(RealResults)):
    if RealResults[i] > Quota or RealResults[i] == Quota:
        print(str(i+1) + ". hüppaja kvalifitseerus tulemusega " + str(RealResults[i]) + ".")

    
