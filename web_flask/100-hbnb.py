#!/usr/bin/python3
""" module doc """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ display hello world"""
    return "Hello HBNB!"



@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ display text will colling the route"""
    return 'c {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ diplay pytho with default text"""
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ display n if n is integer """
    return '{} is a number'.format(n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ display n if even or odd """
    if n % 2 == 0:
        p = 'even'
    else:
        p = 'odd'
    return render_template('6-number_odd_or_even.html', number=n, parity=p)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ display list of states """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """ method clode call"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ display cities in sp route"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ diplay states if id or if not"""
    if id:
        states = storage.all(State, id)
        id_present = True
    else:
        states = storage.all(State)
        id_present = False
    return render_template(
            '9-states.html',
            states=states,
            id_present=id_present
            )


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display HBNB web static """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states,
                           amenities=amenities)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)

    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
