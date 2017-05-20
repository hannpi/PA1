# Juhend kättesaadav kasutades järgnevat linki:
# https://github.com/stenmirski/PA1/blob/master/Kontrolltood/Juhend%20-%20KT%20-%2023.03.2017

faili_nimi = input("Sisestage failinimi: ")
fail = open(faili_nimi, encoding="UTF-8")
kaalud = []
for rida in fail:
    rida = rida.strip(" \n\ufeff")
    kaalud.append((rida))

print(kaalud)
def ostude_kaal_kilogrammides(list):
    summa = 0
    for i in range(len(list)):
        kgdes = int(list[i])/1000
        summa += kgdes
    return summa

kilosid = ostude_kaal_kilogrammides(kaalud)
print("Kaalude kogusumma kilogrammides: " + str(kilosid))

bag = input("Milline kott on kaasas: ")

if bag == "Kilekott":
    print("Eva koti kandevõime (kg): 3")
    if kilosid <= 3:
        print("Kott sobib")
    else:
        print("Kott ei sobi")
elif bag == "Paberkott":
    print("Eva koti kandevõime (kg): 1.5")
    if kilosid <= 1.5:
        print("Kott sobib")
    else:
        print("Kott ei sobi")
elif bag == "Kangaskott":
    print("Eva koti kandevõime (kg): 5")
    if kilosid <= 5:
        print("Kott sobib")
    else:
        print("Kott ei sobi")
else:
    print("Invalid")
