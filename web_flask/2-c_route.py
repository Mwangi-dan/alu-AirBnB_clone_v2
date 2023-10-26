#!/usr/bin/python3
""" Start Flask application and display HBNB """


from flask import Flask


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
