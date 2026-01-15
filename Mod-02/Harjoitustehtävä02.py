r_str = input("Mikä on ympyrän säde?")

#kysyn aluksi ympyrän säteen

r = float(r_str)

# muunnan seuraavaksi r_str muuttujan float muotoon jotta voin tehdä lasku toimituksen pinta-alalle

pa = (r*r)*3.14159
print("ympyrän pinta-ala on: " +str(pa))

# lopuksi on pinta-alan lasku ja vastauksen printtaaminen ohjelmassa