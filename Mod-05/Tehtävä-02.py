# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla
# sort-metodille argumentiksi reverse=True.

syote = input("Anna luku PERKELE! ")
lista = []
if syote != "":
    syote_int = int(syote)
    lista.append(syote_int)
while syote != "":
    syote = input("Anna luku PERKELE! ")
    if syote != "":
        syote_int = int(syote)
        lista.append(syote_int)
lista.sort(reverse=True)
for luku in lista:
    print(luku)


