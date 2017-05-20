"""Erinevate täringumängude jaoks on vajalik erinev arv täringuid. Näiteks
Yahtzee (Yatzy) jaoks on vaja 5 täringut, Crapsi jaoks aga 2 täringut.

Koostada programm, mis

1. küsib kasutajalt vajalike täringute arvu;
2. viskab vastava arvu täringuid (genereerib vastava arvu suvalisi arve, mis
jäävad 1 ja 6 vahele);
3. väljastab iga arvu eraldi reale."""

from random import randint

dice = int(input("Täringute arv: "))

while dice > 0:
    print(str(randint(1, 6)))
    dice -= 1

