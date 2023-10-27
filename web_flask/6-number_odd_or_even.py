#!/usr/bin/python3
""" Start Flask application and display HBNB """


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
    Returns `HBNB`
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """
    returns other text
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    returns text with text witten after c
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    python text
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    prints n if n is a number
    """
    n = str(n)
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Number template in html file only if number is an integer
    """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_even_odd(n):
    """
    display html page if number is even or odd
    """
    if n % 2 == 0:
        state = "even"
    else:
        state = "odd"
    return render_template('6-number_odd_or_even.html', n=n, state=state)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
