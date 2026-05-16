"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.

Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
pituus kilometreinä ja osallistuvien autojen lista.

Luokassa on alustaja, joka saa parametreinaan nimen,
kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.

Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä
mainitut tunnin välein tehtävät toimenpiteet eli arpoo
kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle
kulje-metodia.

tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot
selkeäksi taulukoksi muotoiltuna.

kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa
eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun
nimeltä "Suuri romuralli".

Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan
kuin aiemmassa tehtävässä.

Pääohjelma simuloi kilpailun etenemistä kutsumalla
toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina
tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.

Ajantasainen tilanne tulostetaan tulosta_tilanne-metodin avulla
kymmenen tunnin välein sekä kertaalleen sen jälkeen,
kun kilpailu on päättynyt.
"""

import random


class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):

        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):

        self.nopeus += muutos

        if self.nopeus < 0:
            self.nopeus = 0

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):

        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:

    def __init__(self, nimi, pituus, autot):

        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):

        for auto in self.autot:

            muutos = random.randint(-10, 15)

            auto.kiihdyta(muutos)

            auto.kulje(1)

    def tulosta_tilanne(self):

        print(f"\nKilpailu: {self.nimi}")
        print(f"{'Rekisteri':<15}{'Huippu':<10}{'Nopeus':<10}{'Matka':<10}")

        for auto in self.autot:

            print(f"{auto.rekisteritunnus:<15}"
                  f"{auto.huippunopeus:<10}"
                  f"{auto.nopeus:<10}"
                  f"{round(auto.kuljettu_matka, 1):<10}")

    def kilpailu_ohi(self):

        for auto in self.autot:

            if auto.kuljettu_matka >= self.pituus:
                return True

        return False


# --- Pääohjelma ---

autot = []

for i in range(1, 11):

    huippunopeus = random.randint(100, 200)

    auto = Auto(f"ABC-{i}", huippunopeus)

    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu.kilpailu_ohi():

    kilpailu.tunti_kuluu()

    tunnit += 1

    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()