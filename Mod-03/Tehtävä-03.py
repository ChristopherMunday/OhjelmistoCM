# tein muuttujat ja annoin hemo muuttujalle floatin

sukupuoli = input("mikä on sukupuolesi? ").lower()
hemo = float(input("Kerrotko hemoglobiini arvosi? "))

# miehen hemoglobiini arvio

if sukupuoli == "mies":
    if 134 <= hemo <= 195:
        print("Hemoglobiini arvosi ovat normaalit")
    elif hemo < 134:
        print("Hemoglobiini arvosi ovat liian alhaiset")
    else:
        print("Hemoglobiini arvosi ovat liian korkeat")

# naisen hemoglobiini arvio

elif sukupuoli == "nainen":
    if 117 <= hemo <= 175:
        print("Hemoglobiiniarvosi ovat normaalit")
    elif hemo < 117:
        print("Hemoglobiiniarvosi ovat liian alhaiset")
    else:
        print("Hemoglobiiniarvosi ovat liian korkeat")

# lisäsin else lauseen joka kertoo jos antama sukupuoli ei kelpaa

else:
    print("Sukupuoli ei kelpaa. Anna 'mies' tai 'nainen'.")
