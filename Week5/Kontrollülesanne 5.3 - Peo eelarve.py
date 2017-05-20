"""Juubelile on kutsutud hulk inimesi, kellest osa on teatanud, et nad tulevad
ja ülejäänute kohta ei ole midagi teada. Peo eelarve koosneb kahest osast:
söök ja ruumi rent. Söögi peale arvestatakse iga osaleja kohta 10 eurot. Ruumi
rent maksab sõltumata osalejate arvust 55 eurot. Planeerimiseks on vaja
programmi, mis arvutab

 - maksimaalse eelarve (arvestades, et kõik kutsutud inimesed tulevad kohale)
 ja
 - minimaalse eelarve (arvestades, et kohale tulevad ainult need, kes on juba
 seda teatanud).
 
Esmalt koostada funktsioon eelarve, mis
1. võtab argumendiks külaliste arvu tähistava täisarvu;
2. arvutab selle põhjal eelarve kogusumma;
3. tagastab eelarve kogusumma. Näiteks argumendiga 5 tagastab funktsioon arvu 105.
 
Teiseks koostada programm, mis
1. küsib kasutajalt kutsutud inimeste arvu;
2. küsib kasutajalt inimeste arvu, kes on juba tulemisest teatanud;
3. arvutab ja väljastab ekraanile maksimaalse eelarve, kasutades koostatud
funktsiooni eelarve;
4. arvutab ja väljastab ekraanile minimaalse eelarve, kasutades koostatud
funktsiooni eelarve."""

def eelarve(kyl):
    return (int(kyl)*10 + 55)

a = input("Mitu inimest on kutsutud? ")
b = input("Mitu inimest tuleb? ")

print("Maksimaalne eelarve: " + str(eelarve(a)))
print("Minimaalne eelarve: " + str(eelarve(b)))
