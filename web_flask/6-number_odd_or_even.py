#!/usr/bin/python3
from flask import Flask, render_template
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
def print_python(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python ' + text


@app.route('/number/<int:n>')
def print_number(n):
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def print_number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def print_number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
