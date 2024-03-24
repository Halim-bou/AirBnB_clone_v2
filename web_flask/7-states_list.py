#!/usr/bin/python3
""" start web flask for hbnb project"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(error):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """ display file html with route"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
