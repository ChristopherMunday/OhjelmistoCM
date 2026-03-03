# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
# nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def heitot():
    tulos = random.randint(1,6)
    return tulos

# -- Pääohjelma --
heitto = 0
while heitto != 6:
    heitto = heitot()
    print(heitto)




