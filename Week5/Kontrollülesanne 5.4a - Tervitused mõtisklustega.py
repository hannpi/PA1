"""Väiksematel üritustel on külaliste ühekaupa tervitamine lihtne. Suurematel
üritustel võib ühekaupa tervitamine olla juba kurnavam tegevus.

Esmalt koostada funktsioon tervitus, mis
1. võtab argumendiks tervituse järjekorranumbri arvuna, mis näitab mitmes
tervitus on käsil;
2. kuvab väljakutsel ekraanile täpselt sellisel kujul tervituse ja vastuse
koos tervituse järjekorranumbriga (n tähistab tervituse järjekorranumbrit):

Võõrustaja: "Tere!"
Täna n. kord tervitada, mõtiskleb võõrustaja.
Külaline: "Tere, suur tänu kutse eest!"

Teiseks koostada programm, mis
1. küsib kasutajalt külaliste arvu;
2. rakendab tsükli abil vastav arv kordi funktsiooni tervitus, kus igal tsükli
sammul tuleb funktsioon välja kutsuda ühe võrra suurema argumendiga kui
eelmisel korral."""

def tervitus(järjekorranumber):
    print('Võõrustaja: "Tere!"')    
    print('Täna ' + str(järjekorranumber+1) + '.kord tervitada, mõtiskleb võõrustaja.')
    print('Külaline: "Tere, suur tänu kutse eest!"')    
külaliste_arv = int(input('Sisestage külaliste arv: '))
for i in range(külaliste_arv):
    tervitus(i)
 
    
    
