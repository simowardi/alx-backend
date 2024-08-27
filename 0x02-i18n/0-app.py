#!/usr/bin/env python3

"""
Flask application: Serves the basic index page

This script defines a simple Flask application that serves the
'0-index.html' template as the main content when the root URL (`/`)
is accessed. It also includes a comment to explain its purpose.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Renders the '0-index.html' template for the root URL (`/`).

    This function handles requests to the root URL (`/`) and returns
    the rendered content of the '0-index.html' template.
    """
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
