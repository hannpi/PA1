"""Odavlennufirmad pakuvad reisijatele küllaltki soodsaid lennupileteid, kuid
lisaväärtuse eest peavad reisijad juurde maksma. Näiteks kui tahetakse
lennukis istekoht ise valida, siis ka seda saab lisatasu eest. Istekohta
valides küsitakse inimeselt, kas ta soovib istuda akna äärde või mujale. Kui
reisija ei taha valida, siis loositakse istekoht nii, et 1/3 tõenäosusega on
see akna ääres ja 2/3 tõenäosusega mujal.

Koostada programm, mis vastab järgmistele tingimustele:

1. Kasutajalt küsitakse, kas ta soovib istekoha ise valida. Ise valimiseks
sisestab kasutaja ”ise”. Vastasel juhul kirjutab kasutaja ”loos”.

 - Kui kasutaja soovis ise valida, siis küsitakse tema käest, kas ta soovib
 istuda akna ääres (kasutaja sisestab ”aken”) või mitte (kasutaja sisestab
 ”muu”).

 - Kui kasutaja valis loosi, siis loositakse talle istekoht nii, et 1/3
 tõenäosusega on see akna ääres ja 2/3 tõenäosusega mujal.

2. Väljastatakse, kas kasutaja valis istekoha ise (”Valisite ise”) või valiti see loosiga (”Istekoht loositi”).

3. Väljastatakse, kas kasutaja istekoht on akna ääres (”Aknakoht”) või mitte (”Vahekäigukoht”).
"""

from random import randint
pick = input("Kas soovite istekoha ise valida?: ")

if pick == "ise":
    WON = input("Kas soovite akna ääres istuda?: ")
    print("Valisite ise")
    if WON =="aken":
        print("Aknakoht")
    else:
        print("Vahekäigukoht")
else:
    print("Istekoht loositi")
    yolo = randint(1, 3)
    lucky=1
    if yolo==lucky:
        print("Aknakoht")
    else:
        print("Vahekäigukoht")
          
