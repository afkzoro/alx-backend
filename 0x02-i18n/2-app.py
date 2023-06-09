#!/usr/bin/env python3
""" Task-1 Flask-Babel """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Babel config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """ index function
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """
    This function determines the best-matching language based
    on the Accept-Language header of the request.

    It selects the language that matches the supported languages in the order
    of preference.

    Returns:
        str: The selected language code.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
