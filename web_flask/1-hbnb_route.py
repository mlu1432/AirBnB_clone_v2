#!/usr/bin/python3
"""
A simple Flask web application with two routes.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """
    Handle requests to the root URL ("/") and return a greeting.
    """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """
    Handle requests to the "/hbnb" URL and return a string.
    """
    return 'HBNB'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
