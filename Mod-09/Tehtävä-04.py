# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti
# "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia. Kaikkia autoja käsketään liikkumaan yhden tunnin ajan.
# Tämä tehdään kutsumalla kulje-metodia. Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.


import random


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

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus_th * tunnit


# --- Pääohjelma ---

autot = []


for i in range(1, 11):
    huippunopeus = random.randint(100, 200)
    auto = Auto(f"ABC-{i}", huippunopeus)
    autot.append(auto)

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:

    for auto in autot:


        muutos = random.randint(-10, 15)


        auto.kiihdyta(muutos)


        auto.kulje(1)


        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False

# --- Tulostus ---

print(f"{'Rekisteri':<10} {'Huippu':<10} {'Nopeus':<10} {'Matka':<10}")

for auto in autot:
    print(f"{auto.rekisteritunnus:<10} "
          f"{auto.huippunopeus:<10} "
          f"{auto.nopeus_th:<10} "
          f"{round(auto.kuljettu_matka, 1):<10}")