"""nimesed on ikka päevikut pidanud - mõned salaja, mõned avalikult.
Ülesandeks on päevikupidamise programm teha.

Kirjutada programm, mis

1. küsib kasutaja käest ühe sissekande (võib eeldada, et sissekanne on ilma reavahetusteta);
2. kirjutab (UTF-8 kodeeringus) faili paevik.txt lõppu kolm rida:
 - esimesel real praegune kuupäev ja kellaaeg sellisel kujul, nagu seda
 tagastab funktsioon datetime.today();
 - teisel real kasutaja sisestatud kirje;
 - tühi rida (pole kohustuslik).

Kui faili paevik.txt ei eksisteeri, siis tuleb see luua. Kui aga fail juba
eksisteerib, siis ei tohi selle faili olemasolevast sisust midagi üle
kirjutada. Failinimi peab automaatkontrolli läbimiseks kindlasti olema
paevik.txt (mitte päevik.txt) ja fail peab olema kodeeringus UTF-8
(encoding="UTF-8")."""

from datetime import datetime
kuupaev_kell = datetime.today()

fail = open("paevik.txt", 'a', encoding="UTF-8")
sisend = input("Sisesta sissekande tekst: ")

fail.write(str(kuupaev_kell))
fail.write("\n")
fail.write(sisend)
fail.write("\n\n")
fail.close()
