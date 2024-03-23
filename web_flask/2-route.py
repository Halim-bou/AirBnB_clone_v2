#!/usr/bin/python3
""" script to practice flask """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """print  string"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """print     hbnb"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """display    C    """
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
