#!/usr/bin/python3
"""
Start a web application with three routes.
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

@app.route('/c/<text>')
def c_is_fun(text):
    """
    Handle requests to the "/c/<text>" URL, replace underscores with spaces, 
    and return the formatted string.
    """
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.url_map.strict_slashes = False  # Disable strict slashes for routes
    app.run(host='0.0.0.0', port=5000)  # Run the application on 0.0.0.0:5000
