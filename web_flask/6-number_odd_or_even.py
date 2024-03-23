#!/usr/bin/python3
""" script to practice flask """
from flask import Flask, render_template


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


@app.route('/number_template/<int:n>')
def number_template(n):
    """render template return in html"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """return n to jinja checking if it's odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
