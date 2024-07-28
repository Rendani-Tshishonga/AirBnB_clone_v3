#!/usr/bin/python3
"""
Write a python script that
starts a flask application
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    return Hello HBNB!
    """
    return "Hello HBNB!"
"""
We will route to /hbnb
"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    return HBNB
    """
    return "HBNB"
"""
We will route to /c/<text>
"""
@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    return "C " + text.replace("_", " ")
"""
Web application must listen to all
public addresses on port 5000.
"""
if __name__ =="__main__":
    app.run(host='0.0.0.0', port='5000')
