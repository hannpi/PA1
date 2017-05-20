# Umbkaudne juhend on kättesaadav kasutades järgnevat linki:
# https://github.com/stenmirski/PA1/blob/master/Kontrolltood/Juhend%20-%20KT%20-%2005.04.2017

failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")

töötunnid = [] #Töötundide järjend
for rida in fail: 
    rida = rida.strip(" \n\ufeff") #Eemaldame tühikud, reavahetused, ufeff täh.
    töötunnid.append(float(rida))
fail.close()

MilleAlusel = input("Kas palka makstakse tunnitöö või fikseeritud tasu alusel? ")
PäevadeArv = int(input("Palun sisesta mitu tööpäeva on kuus: "))

def tunnid(järjend):
    summa = 0
    for i in range(len(järjend)):
        summa += järjend[i]
    return summa

summa_kasutamine = tunnid(töötunnid)
normaalajal_tehtud_tunnid = PäevadeArv*8
üleajal_tehtud_tunnid = summa_kasutamine-normaalajal_tehtud_tunnid

if MilleAlusel == "Fikseeritud":
    info3 = int(input("Kui suur on töötaja lepingujärgne brutopalk? "))
    print("Töötaja ületundide arv on " + str(üleajal_tehtud_tunnid) + ", aga töötasu suurus on " + str(info3) + ".")
elif MilleAlusel == "Tunnitöö":
    print("Töötaja tegi kuus " + str(summa_kasutamine) + " töötundi.")
    print("Töötaja ületundide arv on " + str(üleajal_tehtud_tunnid) + " ja ta teenis lisatasu " + str(üleajal_tehtud_tunnid*1.5*6) + " eurot.")
    tasu = üleajal_tehtud_tunnid*1.5*6 + normaalajal_tehtud_tunnid*6
    print("Töötaja töötasu on " + str(tasu) + " eurot.")
          


