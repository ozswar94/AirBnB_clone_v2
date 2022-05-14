#!/usr/bin/python3
""" hello world flask """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ print hello world on web page """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
