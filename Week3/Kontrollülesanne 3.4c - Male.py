"""Legend räägib, et malemängu leiutajale olla tollane valitseja pakkunud tasu.

Leiutaja oli “tagasihoidlik” ja palus tasuks

 - esimese ruudu eest 1 nisutera,
 - teise ruudu eest 2 korda rohkem ehk 2,
 - kolmanda ruudu eest veel 2 korda rohkem ehk 4,
 - neljanda ruudu eest siis 8,
 - viienda ruudu eest 16 jne
 
Malelaual on 64 ruutu.

Koostada programm, mis

 - küsib kasutajalt ühe täisarvu;
 - arvutab while-tsükli abil, mitu nisutera sellise järjekorranumbriga ruudu
 eest leiutaja küsis;
 - tulemus väljastatakse ekraanile pärast tsüklit. 
"""

RuutudeArv = int(input("Sisestage täisarv: "))
Esialgne = RuutudeArv
arv = 0
while RuutudeArv > 0:
    if arv == 0:
        arv += 1
        RuutudeArv -= 1
    else:
        arv *= 2
        RuutudeArv -= 1
        

print("Nisuteri " + str(Esialgne) +". ruudu eest: " + str(arv))
