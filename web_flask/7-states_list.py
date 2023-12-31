#!/usr/bin/python3
"""Flask app for HBNB."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=True)
def states_list():
    """Display the states list."""
    states = storage.all('States')

    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run()
