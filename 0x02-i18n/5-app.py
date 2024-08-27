#!/usr/bin/env python3
"""Basic Flask app with i18n support (en, fr)

This script demonstrates a simple Flask application
with internationalization for English (en) and French (fr).
You'll need to create translation files for each language.
"""

from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """Flask-Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    # User data with name, locale, and timezone
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves user info from 'login_as' URL parameter"""
    log_id = request.args.get('login_as')
    if log_id:
        return users.get(int(log_id))
    return None


@app.before_request
def before_request():
    """Stores user info in 'g' object (if found)"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """Selects user's preferred or default language"""
    user_locale = request.args.get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale

    # Use user context if available
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    # Fallback to browser preference and default
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_index():
    """Renders the home/index page (5-index.html)"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
