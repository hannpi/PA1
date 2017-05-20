"""Loomulik iive on elussündide arvu ja surmajuhtude arvu vahe. Failis synnid.txt on esitatud Eesti eelmise aasta sündide registreerimisandmed kuude lõikes (http://www.stat.ee/34270 ). Failis surmad.txt on kirjas Eesti eelmise aasta surmajuhtude registreerimise andmed (http://www.stat.ee/34271 ).

Programmi testimiseks kasutatakse lisaks ka teisi faile.

Kirjutada programm, mis

1. loeb failist synnid.txt sündide arvud kuude kaupa järjendisse nii, et
esimene element on jaanuari kuu sündide arv, teine element on veebruari
sündide arv jne;
2. loeb failist surmad.txt surmade arvud kuude kaupa järjendisse nii, et
esimene element on jaanuari kuu surmade arv, teine element on veebruari
surmade arv jne;
3. koostab loodud järjendite põhjal järjendi, kus elementideks on vastava kuu
loomulik iive;
4. väljastab ekraanile loomuliku iibe järjendi;
5. väljastab kuu numbrid (jaanuar 1, veebruar 2 jne), mille korral oli iive
positiivne."""

f = open("surmad.txt", encoding="UTF-8")
surmad = []

for rida in f:
    rida = rida.strip()
    surmad.append(int(rida))

f.close()

f = open("synnid.txt", encoding="UTF-8")
synnid = []

for rida in f:
    rida = rida.strip()
    synnid.append(int(rida))

iive = []

for i in range(len(synnid)):
    iive.append(synnid[i]-surmad[i])

print(iive)
print("2016. aasta positiivse iibega kuu numbrid: ")

for i in range(len(iive)):
    if iive[i] > 0:
        print(i+1)
        
