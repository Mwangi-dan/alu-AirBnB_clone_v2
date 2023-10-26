#!/usr/bin/python3
""" Script that starts a Flaks web application """


from flask import flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns Hello world text """
    return 'Hello HBNB!'


if __name__ == "__main__":
    """ main module """
    app.run(host='0.0.0.0', port=5000)
