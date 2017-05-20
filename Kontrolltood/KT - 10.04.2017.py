# Juhend kättesaadav kasutades järgnevat linki:
# https://github.com/stenmirski/PA1/blob/master/Kontrolltood/Juhend%20-%20KT%20-%2010.04.2017

def sobiv_pikkus(raamisuurus): #funktsioon inimese pikkuse jaoks
    inimese_pikkus = (raamisuurus)* 2.54 / 0.66 + 100
    return round(inimese_pikkus, 0)

faili_nimi = input("Sisestage failinimi: ")
fail = open(faili_nimi, encoding="UTF-8")
sisu = []
for rida in fail:
    rida = rida.strip(" \n\ufeff") #eemaldab tühikud, ufeff, reavahetused
    sisu.append(float(rida))

pikkus = int(input("Sisestage pikkus: "))
print("Sobivad jalgrataste raamid:")
for i in range(len(sisu)):
    if pikkus+5 >= sobiv_pikkus(sisu[i]) >= pikkus-5: #Kui pikkus on +5 või -5
        print(sisu[i])

print("Kõige väiksem raam on suurusega " + str(min(sisu))) #print minimum
print("Kõige suurem raam on suurusega " + str(max(sisu))) #print maximum
                                                       
