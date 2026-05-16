"""
Toteuta taustapalvelu, joka palauttaa annettua
lentokentän ICAO-koodia vastaavan lentokentän nimen
ja kaupungin JSON-muodossa.

Esimerkiksi:
http://127.0.0.1:3000/kentta/EFHK

Vastauksen tulee olla muodossa:

{
    "ICAO": "EFHK",
    "Name": "Helsinki Vantaa Airport",
    "Municipality": "Helsinki"
}
"""

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="root",
    password="1507:Chris!05",
    autocommit=True
)


@app.route("/")

def etusivu():

    return (
        'Kokeile esimerkiksi: '
        '<a href="/kentta/EFHK">/kentta/EFHK</a>'
    )


@app.route("/kentta/<icao>")

def hae_kentta(icao):

    sql = """
        SELECT name, municipality
        FROM airport
        WHERE ident = %s
    """

    kursori = yhteys.cursor()

    kursori.execute(sql, (icao,))

    tulos = kursori.fetchone()

    if tulos:

        vastaus = {
            "ICAO": icao,
            "Name": tulos[0],
            "Municipality": tulos[1]
        }

    else:

        vastaus = {
            "Virhe": "Lentokenttää ei löytynyt"
        }

    return jsonify(vastaus)


if __name__ == "__main__":

    app.run(port=3000)