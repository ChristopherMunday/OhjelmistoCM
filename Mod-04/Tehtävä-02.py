# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

while True:
    tuumat = float(input("Kuinka monta tuumaa haluat että muunnan? "))
    if tuumat >= 0:
        print(f"{tuumat * 2.54}cm")
    else:
        print("Ohjelma lopetettu!")
        break

# ensin tein while silmukan (niin kauan kun totta) sitten kysyn käyttäjältä tuuma määrää jonka jälkeen käytin
# if ja else rakenteita muuntamaan tuumat senttimetreiksi tai lopettaa ohjelman riippuen käyttäjän vastauksesta
# lopuksi käytin break rakennetta lopettaa ohjelman jos käyttäjän vastaus ei ole positiivinen tuuma määrä