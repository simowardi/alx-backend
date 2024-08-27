#!/usr/bin/env python3

"""
Flask app with multilingual support using Flask-Babel

This script defines a Flask application that supports multiple languages
using the Flask-Babel extension. It allows users to switch between
languages like English (en) and French (fr). You'll need to create translation
files (e.g., .po files) for each supported language.
"""

from flask import Flask, render_template
from flask_babel import Babel, gettext


# Configuration class for Babel (optional)
class Config(object):
    """
    Configuration for Babel (can be moved to a separate file)
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)  # Load configuration from Config class
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Retrieves the user's preferred locale from various sources.

    - Browser language preferences
    - URL arguments (e.g., /?lang=fr)
    - Session data (if a user is logged in)

    This is a hook function that Babel uses to determine the user's
    preferred language. You can customize this logic by overriding it.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Renders the '1-index.html' template, potentially in the user's
    preferred language.

    This function uses the gettext function from Babel to translate strings
    based on the user's locale. You can use `gettext` within your templates
    to mark strings for translation.
    """
    return render_template('1-index.html', title=gettext('Welcome'))


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
