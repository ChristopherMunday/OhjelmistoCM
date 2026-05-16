"""
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on
parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen.

Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
"""


class Hissi:

    def __init__(self, alin, ylin):
        self.alin_kerros = alin
        self.ylin_kerros = ylin
        self.nykyinen_kerros = alin

    def kerros_ylos(self):

        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1

        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):

        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1

        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}")

    def siirry_kerrokseen(self, kohde):

        while self.nykyinen_kerros < kohde:
            self.kerros_ylos()

        while self.nykyinen_kerros > kohde:
            self.kerros_alas()


class Talo:

    def __init__(self, alin, ylin, hissien_lkm):

        self.alin_kerros = alin
        self.hissit = []

        for i in range(hissien_lkm):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):

        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):

        print("PALOHÄLYTYS!")

        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alin_kerros)


# --- Pääohjelma ---

talo = Talo(1, 10, 3)

talo.aja_hissia(1, 7)
talo.aja_hissia(2, 5)
talo.aja_hissia(3, 9)

talo.palohalytys()