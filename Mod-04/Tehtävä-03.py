# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
from cmath import inf

syote = input("Anna kokonaisluku ")


suurin_luku = -inf
pienin_luku = +inf

while syote != "":
    luku = int(syote)
    if luku > suurin_luku:
        suurin_luku = luku
    if luku < pienin_luku:
        pienin_luku = luku
    syote = input("Anna kokonaisluku ")

if suurin_luku != -inf:
    print(f"pienin luku on {pienin_luku}")
    print(f"Suurin luku on {suurin_luku}")
else:
    print("Et syöttäny sopivaa lukua ")