#!/usr/bin/python3
"""Start flask app expoisn / and /hbnb."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Print hello HBNB."""

    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Print HBNB."""

    return 'HBNB'


if __name__ == '__main__':
    app.run()
