kuha = float(input("Kuinka monta cm kuha on? "))
# kysytään ensin kuhan pituus
pituus = 37-kuha
if kuha >= 37:
    print("Onneksi olkoon saat pitää kuhan!")
else:
    print("Kuha pitää heittää takaisin! se on liian lyhyt siitä puuttuu " + str(pituus) + "cm sen pitää olla vähintään 37cm")

# jos kuha on 37 cm tai suurempi (>=) tulee onnittelu
# jos kuha on alle 37 cm kerrotaan ettei kalastaja voi pitää sit ja
# ilmoitetaan hänelle miten pitkä kuhan pitää olla