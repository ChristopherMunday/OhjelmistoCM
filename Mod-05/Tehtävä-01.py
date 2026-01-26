# käytetään satunnaislukujen kirjasto
import random

# kysytään käyttäjältä noppien määrä
lkm = int(input("Kuinka monta noppaa? "))

# Annetaan alkuarvokis 0
summa = 0

# heitetään haluttu lukumäärä noppia
# muuttuja nopan_nro on ns. kierroslaskuri
for nopan_nro in range(lkm):
    # heitetään noppaa haluttu lukumäärä
    silmaluku = random.randint(1,6)
    # lisätään saatu silmaluku muuttujan summa arvoon
    summa += silmaluku # summa = summa + silmaluku
    print(f"noppa {nopan_nro + 1}, tulos = {silmaluku}")
print(f"silmälukujen summa = {summa}")