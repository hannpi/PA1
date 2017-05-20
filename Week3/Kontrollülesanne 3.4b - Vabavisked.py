"""Korvpalluri vabavisete senist visketabavust saab (teatud mööndustega)
kasutada tuleviku visete tõenäosusena.

Koostada programm, mis

1. küsib kasutajalt visketabavuse (tabavustõenäosuse) protsentides (täisarv 0
kuni 100);
2. simuleerib while-tsükli abil 1000 viset ja igal viskel (arvestades
tõenäosust) väljastab, kas see tabas;
 - iga viske kohta peab väljastama ühe rea ja see rida peab sisaldama sõna
 tabas või mööda
3. arvutab kokku tabanud visete arvu ja see väljastab selle kõige viimasena.
"""

import random
Tõenäosus = int(input("Sisestage visketabavuse protsent: "))
ViskeidTabatud = 0
ViskeidMööda = 0
vise = 0
if Tõenäosus < 101 and (Tõenäosus > 0 or Tõenäosus == 0):
    while vise < 1000:
        vise+=1
        Suvaline_arv = random.randint(0, 100)
        if Suvaline_arv > Tõenäosus or Tõenäosus == 0:
            print(str(vise) + ". vise mööda")
            ViskeidMööda += 1
        elif Tõenäosus == 100 or Suvaline_arv == Tõenäosus:
            print(str(vise) + ". vise tabas")
            ViskeidTabatud += 1
        else:
            print(str(vise) + ". vise tabas")
            ViskeidTabatud += 1
            
else:
    print("Tabavuse protsent ei saa olla negatiivne ega suurem kui 100%.")

print("Tabas " + str(ViskeidTabatud) + " viset.")
    

