#!/usr/bin/python3
"""
A simple Flask web application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route that displays "Hello HBNB!".
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Route that displays "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Route that displays "C "
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """
    Route that displays "Python "
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Route that displays “n is a number” only if n is an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """
    Route that displays a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
