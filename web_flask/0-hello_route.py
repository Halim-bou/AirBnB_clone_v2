#!/usr/bin/python3
from flask import Flask
"""..."""

app = Flask(app)


@app.route('/', strict_slashes=False)
def hbnb():
    """retur string"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
