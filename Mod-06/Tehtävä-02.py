# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def heitto(perhana):
    tulos = random.randint(1, perhana)
    return tulos
# ^ Tää on erillinen paske ^ ÄLÄ VITTU KOSKE


# -- Pääohjelma --
tahkot1 = int(input("Anna tahkojen määrä (1-21) "))
testi = tahkot1

looppi = True

while looppi:
    heitot = heitto(tahkot1)
    print(heitot)
    if heitot == testi:
        looppi = False



