#!/usr/bin/python3
"""
A simple Flask web application that listens on 0.0.0.0:5000 and
displays "Hello HBNB!" at the root route.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL that returns a greeting message.
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
