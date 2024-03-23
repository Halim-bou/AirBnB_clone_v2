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


@app.route('/python/<text>')
@app.route('/python', strict_slashes=False)
def python(text="is cool"):
    """display    python   """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>/')
def number(n):
    """return n if n is integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
