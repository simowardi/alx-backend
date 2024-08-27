#!/usr/bin/env python3
"""
Flask multilingual app (en, fr)

This script defines a basic Flask application with multilingual
support using Flask-Babel. It currently supports English (en) and
French (fr). You'll need to create translation files for each language.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Config for Babel (optional, can be in separate file)"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Selects user's preferred language (browser, URL, session)"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Renders the '2-index.html' template"""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
