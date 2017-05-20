"""Euromüntide seerias on kuus erineva nimiväärtusega senti: 1 sent, 2 senti,
5 senti, 10 senti, 20 senti, 50 senti. Sendid väärtustega 1, 2 ja 5 on
pronksikarva (vasega kaetud teras), sendid väärtustega 10, 20 ja 50 on
kullakarva (vasesulam, mis sisaldab alumiiniumi, tsinki ja tina, nn Nordic Gold).

Peres on kombeks, et pronksikarva mündid panna hoiupõrsasse.

Müntide andmed on failis kirjas nii, et iga mündi väärtus on eraldi real.

Esmalt koostada funktsioon pronksikarva_summa, mis

1. võtab argumendiks täisarvude järjendi;
2. tagastab selles järjendis olevate arvude 1, 2 ja 5 summa.

Teiseks koostada programm, mis
1. küsib kasutajalt selle faili nime, milles asuvad sentide väärtused;
2. moodustab täisarvujärjendi vastavast failist loetud väärtustest;
3. rakendab funktsiooni pronksikarva_summa, andes argumendiks koostatud
täisarvujärjendi;
4. väljastab ekraanile tulemuseks saadud kõikide pronksikarva sentide summa."""

def pronksikarva_summa(järjend):
    summa = 0
    for i in range(len(järjend)):
        if järjend[i] == 1 or järjend[i] == 2 or järjend[i] == 5:
            summa += järjend[i]
    return summa

Faili_nimi = input("Sisestage failinimi: ")
file = open(Faili_nimi, encoding="UTF-8")

sendid = []
for rida in file:
    rida = rida.strip()
    sendid.append(int(rida))

print("Hoiupõrsasse läheb " + str(pronksikarva_summa(sendid)) + " senti.")
