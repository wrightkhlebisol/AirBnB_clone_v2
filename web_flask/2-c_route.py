#!/usr/bin/python3
"""Start flask app."""
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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display C followed by the value of text."""

    return f'C {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run()
