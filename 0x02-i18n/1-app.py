#!/usr/bin/env python3
"""Simple Flask app with basic internationalization support (en, fr)

This script demonstrates a very basic Flask application
with internationalization configured for English (en) and French (fr).
You'll need to create translation files for each language.

To use a specific language, add the language code as a query parameter
to the URL (e.g., http://localhost:5000/?locale=fr).

This example doesn't handle user context or timezones yet.
"""

from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """Flask-Babel configuration for English and French"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def index():
    """Renders the home/index page (1-index.html)"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
