"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää.
"""

class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus_th = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus_th += muutos


        if self.nopeus_th < 0:
            self.nopeus_th = 0


        if self.nopeus_th > self.huippunopeus:
            self.nopeus_th = self.huippunopeus


# -- Pääohjelma --

auto1 = Auto("ABC-123", 142)


auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"Auton nopeus kiihdytysten jälkeen: {auto1.nopeus_th} km/h")


auto1.kiihdyta(-200)

print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto1.nopeus_th} km/h")