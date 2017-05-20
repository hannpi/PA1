# Juhend kättesaadav siit:
# https://github.com/stenmirski/PA1/blob/master/Kontrolltood/Juhend%20-%20N%C3%A4idisKT%201
# või: https://courses.cs.ut.ee/2017/prog-alused/spring/Main/KtNaidis (20.05.17)

def hind_käibemaksuga(hind, protsent):
    kmga = hind*(1+ protsent/100)
    return kmga

fn = input("Sisestage failinimi: ")
proc = int(input("Sisestage riigi käibemaks: "))
newsum = float(input("Sisestage summa, millest alates saab käibemaksu tagasi: "))

fail = open(fn, encoding="UTF-8")
read = []
for rida in fail:
    rida = rida.strip()
    read.append(float(rida))
print("Ilma käibemaksuta hinnad failis on: ", read)

summa = 0
kmgaread = []
for i in range(len(read)):
    uusHind = hind_käibemaksuga(read[i], proc)
    print(str(uusHind), "uus hind")
    summa += uusHind
    kmgaread.append(uusHind)

print("Käibemaksuga on hinnad:", kmgaread)
sobivad = []
for i in range(len(kmgaread)):
    if kmgaread[i] >= newsum:
        sobivad.append(kmgaread[i])
    else:
        pass

#print("Hinnad koos käibemaksuga, mis suuremad kui summa, millest alates saab tagasi: ")
#print(sobivad)

anothersumma = 0
for i in range(len(sobivad)):
    anothersumma += sobivad[i]

#print("Nende summa on " + str(anothersumma))

print("Kokku on kulutatud: " + str(round(summa, 2)))

UUSIM = 0
for i in range(len(sobivad)):
    uus = (sobivad[i] - (sobivad[i]/(1+(proc/100))))
    UUSIM += float(uus)

print("Tagasi saab " + str(round(UUSIM, 2)))
    
