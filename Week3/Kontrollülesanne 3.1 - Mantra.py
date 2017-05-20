"""Mantra on silp, sõna, lause või heli, mida kasutatakse paljudes idamaistes
religioonides mediteerimisel. Mantrat korratakse nii kaua kui vajalikuks
peetakse.

Koostada programm, mis

1. küsib kasutajalt lause, mida ta soovib mantrana kasutada,
2. küsib kasutajalt, mitu korda ta soovib mantrat korrata,
3. väljastab sama arv kordi ekraanile kasutaja sisestatud mantra."""

sisend = input("Sisestage mantra: ")
kordaja = int(input("Sisestage mitu korda soovite mantrat korrata: "))

while kordaja > 0:
    print(sisend)
    kordaja -= 1
    
