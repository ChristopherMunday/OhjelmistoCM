# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def bensiini(bensa_gallona):
    bensa_litra = bensa_gallona * 3.785
    return bensa_litra

# -- Pääohjelma --

bensa_gallona = int(input("Montako gallonaa muunnan? "))

while bensa_gallona:
    bensiini(bensa_gallona)
    print(bensiini(bensa_gallona))
    bensa_gallona = int(input("Montako gallonaa muunnan? "))
    if bensa_gallona == "":
        print("Ohjelma lopetettu! ")
