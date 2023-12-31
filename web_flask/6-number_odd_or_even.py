#!/usr/bin/python3
"""Flask app."""
from flask import Flask, render_template

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


@app.route('/python/', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Display Python followed by the value of text."""

    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display <n> is a number if its a number."""

    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display HTML page if <n> is a number."""

    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display HTML page if <n> is a number."""

    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run()
