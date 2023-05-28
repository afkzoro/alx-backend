#!/usr/bin/env python3
""" Task-5 Flask-Babel """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from typing import Dict, Optional

app: Flask = Flask(__name__)
babel: Babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Babel config class
    """
    LANGUAGES: list[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'
    BABEL_TRANSLATION_DIRECTORIES: str = 'translations'


app.config.from_object(Config)


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
    if g.user and g.user.get("locale"):
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request() -> None:
    """ before_request function
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


def get_user(user_id: int) -> Optional[Dict[str, Optional[str]]]:
    """ get_user function
    """
    return users.get(user_id)


@app.route('/')
def index() -> str:
    """ index function
    """
    if g.user:
        welcome_msg = gettext("You are logged in as %(username)s.") % {
            "username": g.user["name"]}
    else:
        welcome_msg = gettext("You are not logged in.")
    return render_template('5-index.html', welcome_msg=welcome_msg)


if __name__ == '__main__':
    app.run()
