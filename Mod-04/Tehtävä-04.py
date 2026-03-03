# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti,
# kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus,
# Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä

import random
kysyttyluku = int(input("Anna luku! "))
luku = random.randint(1,10)

loop = True

while kysyttyluku != luku:
    if kysyttyluku < luku:
        print("Arvaus oli liian pieni ")
    if kysyttyluku > luku:
        print("Arvaus oli liian suuri ")
    kysyttyluku = int(input("Anna luku! "))
print("Arvasit oikein ")
