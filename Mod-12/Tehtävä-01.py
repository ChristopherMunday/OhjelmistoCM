"""
Kirjoita ohjelma, joka hakee ja tulostaa
satunnaisen Chuck Norris -vitsin käyttäjälle.

Käytä seuraavaa rajapintaa:
https://api.chucknorris.io/

Käyttäjälle on näytettävä pelkkä vitsin teksti.
"""

import requests


url = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(url)

if vastaus.status_code == 200:

    data = vastaus.json()

    print(data["value"])

else:

    print("Vitsin hakeminen epäonnistui.")