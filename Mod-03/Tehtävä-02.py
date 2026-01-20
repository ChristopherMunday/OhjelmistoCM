luokka = input("Mikä on hyttiluokkasi? ")
# Kysytään ensin hyttiluokka
hyttiluokka = luokka.upper()
if hyttiluokka == "LUX":
    print("Hyttisi on parvekkeellinen hytti yläkannella")
elif hyttiluokka == "A":
    print("Hyttisi on ikkunallinen hytti autokannen yläpuolella")
elif hyttiluokka == "B":
    print("Hyttisi on ikkunaton hytti autokannen yläpuolella")
elif hyttiluokka == "C":
    print("Hyttisi on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")

# käytetään if jaelif toimintoja kertomaan missä hyttiluokan hytti on
# ja jos ei ole mikää (LUX,A,B tai C) käytetään else että voidaan antaa
# vastaus, Virheellinen hyttiluokka