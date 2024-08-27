#!/usr/bin/env python3
"""
Flask app with i18n support (en, fr)

This script defines a basic Flask application with internationalization
support using Flask-Babel. It currently supports English (en) and French (fr).
"""

from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Configuration for Flask-Babel (optional, separate file)"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Selects user's preferred language (browser, URL, session)"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """Renders the '3-index.html' template (home/index page)"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
