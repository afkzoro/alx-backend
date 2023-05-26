#!/usr/bin/env python3
""" Flask app Task-0"""
from flask import Flask, render_template
import typing

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """ index function
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
