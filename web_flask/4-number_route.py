#!/usr/bin/python3
""" print number """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb')
def print_hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def print_c(text):
    text = text.replace('_', ' ')
    return 'C ' + text


@app.route('/python')
@app.route('/python/<text>')
def print_python(text='is_cool'):
    text = text.replace('_', ' ')
    return 'Python ' + text


@app.route('/number/<int:n>')
def print_number(n):
    return '{:d} is a number'.format(n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
