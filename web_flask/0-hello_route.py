#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Show a response when route is accessed."""

    return 'Hello HBNB!''
