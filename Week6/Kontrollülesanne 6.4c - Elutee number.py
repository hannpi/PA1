"""Numeroloogias peetakse tähtsaks elutee numbrit, mille arvutamiseks tuleb
liita kokku sünnikuupäeva ja -aasta numbrid nii, et jõutakse lõpuks ühe numbrini.

Näiteks, oletame, et sünnikuupäev on 15.05.1975. Teha tuleb niisiis järgnev
tehe: 1+5+5+1+9+7+5 = 33, 3+3 = 6, seega on elutee number 6.

Aga kui sünnikuupäevaks on nt. 17.11.1981, siis arvutada tuleb järgmiselt:
1+7+1+1+1+9+8+1 = 29, 2+9 = 11, 1+1=2.

Elutee numbrit arvutab (rekursiivne) funktsioon (etteantud).

Failis sunnikuupaevad.txt on mingi hulk sünnikuupäevi, iga sünnikuupäev eraldi
real. Kirjutada programm, mis tekitab selle faili põhjal 9 tekstifaili nimedega
eluteenumber1.txt, eluteenumber2.txt, ..., eluteenumber9.txt ning jagab
sünnikuupäevad nendesse failidesse vastavalt elutee numbrile (elutee numbri
arvutamiseks kasutada funktsiooni elutee). Näiteks sünnikuupäev 15.05.1975
tuleb kirjutada faili eluteenumber6.txt."""

#argument s on sõne, esialgu see on kuupäev, edasi juba arvutatud arv
def elutee(s):
    #abimuutaja numbri arvutamiseks
    n = 0
    # tsükkel, mis vaatab iga sümboli sõnes
    for i in s:
        if i != ".":
            n += int(i) # arvutame summat
    # kui saadud arv on väiksem kui 10, siis ongi elutee number käes
    if n < 10:
        return n
    # kui saadud arv on 10 või suurem, siis on vaja uuesti arvutada,
    #selleks kasutame jälle sama funktsiooni
    else:
        return elutee(str(n))

file = open("sunnikuupaevad.txt", encoding="UTF-8")
read = []
for rida in file:
    rida = rida.strip()
    read.append(rida)

print(read)

for i in range(len(read)):
    number = elutee(read[i])
    print("Number: " + str(number))
    for j in range(1, 10):
        file = open("eluteenumber"+str(j)+".txt", "a")
        print("File: " + str(file))
        if int(number) == (j):
            file.write(read[i] + "\n")
        else:
            pass


        
        
        

