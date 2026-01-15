kanta_str = input("Mikä on suorakulmion Kanta?")
korkeus_str = input("Entä suorakulmion korkeus?")

# ensin tässä kysytään suorakulmion kanta ja korkeus

kanta = float(kanta_str)
korkeus = float(korkeus_str)

# tässä muunnan ne float muotoon jotta voin laskea ne

pa = (kanta*korkeus)
piiri = (kanta+korkeus)*2
print("Suorakulmion pinta-ala on " +str(pa))
print("Ja suorakulmion piiri on " +str(piiri))

# sitten vielä laskut ja vastauksen printtaaminen