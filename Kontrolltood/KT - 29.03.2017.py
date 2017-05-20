# Umbkaudne juhend on kättesaadav kasutades järgnevat linki:
# https://github.com/stenmirski/PA1/blob/master/Kontrolltood/Juhend%20-%20KT%20-%2029.03.2017

def legaalsed(järjend): #Funktsioon legaalsed
    summa = 0
    for i in range(len(järjend)):
        if järjend[i] <= 100:
            summa += järjend[i]
    return summa

failinimi = input("Sisestage failinimi: ")
fail = open(failinimi, encoding="UTF-8")

vahemaad = [] #Vahemaade järjend
for rida in fail:
    rida = rida.strip(" \n\ufeff")
    vahemaad.append(int(rida))
fail.close()

kogusumma = 0
for i in range(len(vahemaad)): #Vahemaade kokkuliitmine
    kogusumma += vahemaad[i]

print("Malle läbis kokku " + str(kogusumma) + " kilomeetrit.")

legaalsedkilomeetrid = legaalsed(vahemaad) #Funktsiooni rakendamine
print("Neist on legaalselt läbitud " + str(legaalsedkilomeetrid) + " kilomeetrit.")

mitu = int(input("Mitu kilomeetrit on plaanis sõita: "))
täisosa = mitu//100
print("Sõidu jooksul on vaja teha vähemalt " + str(täisosa) + " peatust.")



    
