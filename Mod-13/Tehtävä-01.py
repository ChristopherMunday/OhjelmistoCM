"""
Toteuta Flask-taustapalvelu, joka ilmoittaa,
onko parametrina saatu luku alkuluku vai ei.

Esimerkiksi:
http://127.0.0.1:3000/alkuluku/31

Vastauksen tulee olla muodossa:
{"Number":31, "isPrime":true}
"""

from flask import Flask, jsonify

app = Flask(__name__)


def onko_alkuluku(syote):

    if syote < 2:
        return False

    for i in range(2, syote):

        if syote % i == 0:
            return False

    return True


@app.route("/")

def etusivu():

    return (
        'Kokeile esimerkiksi: '
        '<a href="/alkuluku/31">/alkuluku/31</a>'
    )


@app.route("/alkuluku/<int:luku>")

def alkuluku(luku):

    vastaus = {
        "Number": luku,
        "isPrime": onko_alkuluku(luku)
    }

    return jsonify(vastaus)


if __name__ == "__main__":

    app.run(port=3000)