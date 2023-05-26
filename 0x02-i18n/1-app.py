#!/usr/bin/env python3
""" Flask app Task-0"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ index function
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
