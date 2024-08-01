#!/usr/bin/python3
"""
Write a flask script that
starts a flask application.
"""

from flask import Flask

"""
Create an instance of the flask
application
"""
app = Flask(__name__)

"""
Route the URL to the home directory
"""


@app.route('/', strict_slashes=False)
def index():
    """
    return Hello HBNB!"
    """
    return "Hello HBNB!"


if __name__ == "__main__":

    app.run(host='0.0.0.0', port='5000')
