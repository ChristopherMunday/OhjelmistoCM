leviskat_str = input("Anna leviskät")
naulat_str = input("Anna naulat")
luodit_str = input("Anna luodit")

# kysyn ensin leviskät, naulat ja luodit

leviskat = float(leviskat_str)
naulat = float(naulat_str)
luodit = float(luodit_str)

# muunnan muuttujat float muotoihin

luodit = leviskat*20*32+naulat*32
massa = (luodit*13.3)/1000
print(f"Massa on {massa: .3f} Kilogrammaa")

# laskin luotien yhteis summan ja siitä laskin massan
# muunsin massan grammoista kilogrammoiksi ja merkitsin sen 3 desimaalin tarkkuudella
# lopuksi annoin vielä massalle yksikön eli kilogrammaa