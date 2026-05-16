# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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


# -- Pääohjelma --

auto1 = Auto("ABC-123", 142)

auto1.kiihdyta(60)


auto1.kulje(1.5)

print(f"Nopeus: {auto1.nopeus_th} km/h")
print(f"Kuljettu matka: {auto1.kuljettu_matka} km")