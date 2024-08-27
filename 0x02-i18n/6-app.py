#!/usr/bin/env python3
"""
Flask app with i18n and user context

This script demonstrates a Flask application with:

- Internationalization support using Flask-Babel (en, fr)
- User context based on a user dictionary or URL parameter
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict, Union


class Config(object):
    """Configuration for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves user info based on 'login_as' URL parameter"""
    user_id = request.args.get('login_as')
    if user_id and user_id in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """Stores user in 'g' object if found"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Selects user's preferred language or default"""
    user_locale = request.args.get('locale')  # Check URL parameter
    if user_locale in app.config['LANGUAGES']:
        return user_locale

    # Check user context (if available)
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    # Check browser preference and fallback to default
    user_locale = request.headers.get('locale', None)
    if user_locale in app.config['LANGUAGES']:
        return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """Renders the '5-index.html' template"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
