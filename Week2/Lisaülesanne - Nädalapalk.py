"""Kui inimene töötab nädalas 40 tundi või vähem, siis nende tundide eest saab
ta palka vastavalt oma tavalisele tunnitasule. Kui inimene töötab rohkem kui 40
tundi, siis ületundide eest on tunnitasu 50% kõrgem.

Koostage programm, mis küsib kasutajalt töötundide arvu nädalas ja tavalise
tunnitasu (küsige just sellises järjekorras, esimese asjana - töötundide arvu
ja teise asjana - tunnitasu) ning väljastab vastava nädalapalga arvestades ka
ületundidega, kui neid on."""


hours = int(input("Mitu tundi nädalas töötate?: "))
fee = int(input("Kui suur on teie tunnitasu?: "))
multiplier=1.5

if hours < 40 or hours==40:
    palk = hours*fee
    print("Teie nädalapalk on " + str(palk) + " eurot.")
else:
    boonus = (hours-40)*multiplier*fee
    palk2 = 40*fee + boonus
    print("Teie nädalapalk on " + str(palk2) + " eurot.")
    

