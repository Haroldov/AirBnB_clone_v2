#!/usr/bin/python3
""" starts a Flask web application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ return Hello HBNB! """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ return HBNB """

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ return C text """

    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ return Python text """

    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ return number """

    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number2temp(n):
    """ return HTML template number """

    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num2temp(n):
    """ return HTML template number """

    if n % 2 == 0:
        string = "even"
    else:
        string = "odd"
    return render_template('6-number_odd_or_even.html', n=n, str=string)

if __name__ == '__main__':
    app.run()
