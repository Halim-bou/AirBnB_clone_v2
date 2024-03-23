#!/usr/bin/python3
from web_flask import app


@app.route('/', strict_slashes=False)
def hbnb():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
