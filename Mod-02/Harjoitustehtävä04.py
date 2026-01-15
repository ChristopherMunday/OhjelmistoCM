luku1_str = input("Annatko minulle jonkun luvun kiitos!")
luku2_str = input("Tarvitsen vielä toisen luvun")
luku3_str = input("Viimeinen luku")

# kysyn ensin kaikki luvut (löydä parempi tapa kysyä luvut esim samassa kysymyksessä??)

luku1 = float(luku1_str)
luku2 = float(luku2_str)
luku3 = float(luku3_str)

# muunnan _str muuttujat float muotoon

keskiarvo = (luku1+luku2+luku3)/3
print("lukujen keskiarvo on " + str(keskiarvo))

# lasken keskiarvon ja printtaan vastauksen