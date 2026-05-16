"""
Tutustu avoimeen OpenWeather-säärajapintaan:
https://openweathermap.org/api

Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen
ja tulostaa sitä vastaavan säätilan tekstin
sekä lämpötilan Celsius-asteina.

Palveluun rekisteröityminen on tarpeen,
jotta saat rajapintapyynnöissä tarvittavan API-avaimen.
"""

import requests


api_avain = "b81d3704de2fbf91dad434fc04883833"

paikkakunta = input("Anna paikkakunta: ")

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={paikkakunta}"
    f"&appid={api_avain}"
    f"&units=metric"
    f"&lang=fi"
)

vastaus = requests.get(url)

if vastaus.status_code == 200:

    data = vastaus.json()

    saakuvaus = data["weather"][0]["description"]

    lampotila = data["main"]["temp"]

    print(f"Säätila: {saakuvaus}")

    print(f"Lämpötila: {lampotila} °C")

else:

    print("Sään hakeminen epäonnistui.")