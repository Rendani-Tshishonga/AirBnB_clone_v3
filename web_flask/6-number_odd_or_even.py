#!/usr/bin/python3
"""
Write a python script that
starts a flask application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    return Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    return HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """Display C is fun"""
    return "C " + text.replace("_", " ")


"""Route to /Python"""


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text="is cool"):
    """Display Python is Cool"""
    return "Python " + text.replace("_", " ")


"""Route /number/<n>"""


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display n as an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_temp(n):
    """Display HTML if n is a integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int: n>', strict_slahes=False)
def number_odd_even(n):
    """Disaplay HTML if n is integer"""
    if (n % 2 == 0):
        odd_even = "even"
    else:
        odd_even = "odd"
    return render_template('6-number_odd_or_even.html', n=n, odd_even=odd_even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
