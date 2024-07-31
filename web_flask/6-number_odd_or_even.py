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
We will create a route for
/python/<text>
"""
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text="is cool"):
    return "Python " + text.replace("_", " ")
"""
We will create a route for
/number/<n> ensure n is a number
"""
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"
"""
We will create a route to
/number_template/<n>, which will render a
HTML page only if n is an integer.
"""
@app.route('/number_template/<int:n>', strict_slashes=False)
def  number_temp(n):
    return render_template('5-number.html', n=n)

"""
We will create a route to
/number_odd_or_even/<int: n> which will render
a HTML page only if n is integer.
"""

@app.route('/number_odd_or_even/<int: n>', strict_slahes=False)
def number_odd_even(n):
    if (n % 2 == 0):
        odd_even = "even" 
    else
        odd_even = "odd"
    return render_template('6-number_odd_or_even.html', n=n, odd_even=odd_even)

"""
Web application must listen to all
public addresses on port 5000.
"""
if __name__ =="__main__":
    app.run(host='0.0.0.0', port='5000')
