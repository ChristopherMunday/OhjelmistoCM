"""
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.

Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
Hissien lista tallennetaan talon ominaisuutena.

Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan
hissin numeron ja kohdekerroksen.

Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
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

        self.hissit = []

        for i in range(hissien_lkm):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohdekerros):

        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)


# --- Pääohjelma ---

talo = Talo(1, 10, 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)
talo.aja_hissia(3, 3)

talo.aja_hissia(1, 1)