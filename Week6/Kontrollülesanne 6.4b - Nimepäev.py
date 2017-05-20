"""Kui aadressile https://courses.cs.ut.ee/MTAT.TK.012/2015_fall/uploads/Main/
lisada kuunimi (nt. https://courses.cs.ut.ee/MTAT.TK.012/2015_fall/uploads/Main/jaanuar),
siis sellelt aadressilt võib leida lehe, kus on kirjas selle kuu nimepäevalised
nii, et igal real on ühe päeva nimepäevalised (esimesel real on selle kuu
esimese päeva nimepäevalised, teisel real on selle kuu teise päeva
nimepäevalised jne.). "märts" asemel tuleb kasutada ilma täpitähtedeta versiooni "marts".

NB! Kui ülaltoodud aadressilt andmeid ei saa kätte (nt Macide kasutajad), siis
palun proovida http://kodu.ut.ee/~eno/mooc/jaanuar jt.

Kirjutada programm, mis
1. küsib kasutajalt kuunime (võib eeldada, et kasutaja sisestab kuunime
õigesti ja "märts" asemel kirjutab "marts"),
2. küsib kasutajalt päeva (võib eeldada, et sisestatud kuus leidub sellise
järjekorranumbriga päev),
3. loeb vastavalt aadressilt selle kuu nimepäevad (kasulik oleks nendest
koostada järjend, abiks võib olla meetod splitlines())
4. väljastab ekraanile sisestatud kuupäevale vastavad nimepäevalised."""

from urllib.request import urlopen

kuu = input("Sisestage kuunimi: ")
päev = int(input("Sisestage päev: "))

url = "https://courses.cs.ut.ee/MTAT.TK.012/2015_fall/uploads/Main/"
improvedUrl = url+kuu

read = []
file = urlopen(improvedUrl)
sisu = file.read()
stringTeisendus = sisu.decode()
ridadeKaupa = stringTeisendus.splitlines()
file.close()

print(ridadeKaupa[päev-1])

