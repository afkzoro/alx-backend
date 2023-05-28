#!/usr/bin/env python3
""" Task-4 Flask-Babel """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from typing import List

app: Flask = Flask(__name__)
babel: Babel = Babel(app)


class Config:
    """ Babel config
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'
    BABEL_TRANSLATION_DIRECTORIES: str = 'translations'


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """ index function
    """
    return render_template('4-index.html', gettext=gettext)


@babel.localeselector
def get_locale() -> str:
    """
    This function determines the best-matching language based
    on the Accept-Language header of the request.

    It selects the language that matches the supported languages in the order
    of preference.

    Returns:
        str: The selected language code.
    """
    if 'locale' in request.args and request.args[
            'locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
