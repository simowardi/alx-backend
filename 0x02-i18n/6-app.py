#!/usr/bin/env python3
"""Flask app with i18n and user context"""

from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Flask-Babel config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    # User data
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Gets user from 'login_as' URL param"""
    usr_id = request.args.get('login_as')
    if usr_id:
        return users.get(int(usr_id))
    return None


@app.before_request
def before_request():
    """Stores user in 'g' object"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Selects user's preferred or default language"""
    user_locale = request.args.get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    header_locale = request.headers.get('locale')
    if header_locale in app.config['LANGUAGES']:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders the home/index page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
