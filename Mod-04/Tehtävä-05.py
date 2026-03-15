# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules)

OIKEA_TUNNUS = "python"
OIKEA_SALASANA = "rules"

max_yritykset = 5
yritykset = 0
onnistui = False

while yritykset < max_yritykset and not onnistui:
    kayttajatunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if kayttajatunnus == OIKEA_TUNNUS and salasana == OIKEA_SALASANA:
        print("Tervetuloa")
        onnistui = True
    else:
        yritykset += 1
        if yritykset < max_yritykset:
            print(f"Väärä tunnus tai salasana. Yrityksiä jäljellä: {max_yritykset - yritykset}")

if not onnistui:
    print("Pääsy evätty")