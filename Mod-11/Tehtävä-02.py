"""
Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat
Sähköauto ja Polttomoottoriauto.

Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.

Polttomoottoriauton ominaisuutena on bensatankin koko litroina.

Kirjoita aliluokille alustajat.

Esimerkiksi sähköauton alustaja saa parametreinaan
rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.

Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi
sekä asettaa oman kapasiteettinsa.

Kirjoita pääohjelma, jossa luot yhden sähköauton
(ABC-15, 180 km/h, 52.5 kWh)

ja yhden polttomoottoriauton
(ACD-123, 165 km/h, 32.3 l).

Aseta kummallekin autolle haluamasi nopeus,
käske autoja ajamaan kolmen tunnin verran
ja tulosta autojen matkamittarilukemat.
"""


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


class Sahkoauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):

        super().__init__(rekisteritunnus, huippunopeus)

        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):

        super().__init__(rekisteritunnus, huippunopeus)

        self.bensatankki = bensatankki


# --- Pääohjelma ---

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)

polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdyta(120)

polttomoottoriauto.kiihdyta(100)

sahkoauto.kulje(3)

polttomoottoriauto.kulje(3)

print(f"Sähköauton matkamittari: {sahkoauto.kuljettu_matka} km")

print(f"Polttomoottoriauton matkamittari: "
      f"{polttomoottoriauto.kuljettu_matka} km")