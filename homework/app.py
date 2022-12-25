from flask import Flask
from fibo import *

app = Flask('Fibonachi')


# <h1> used to increase text size
@app.route('/')
def welcome():
    return "<h1>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FiboApp~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<h1>"


@app.route('/<int:n>')
def index(n):
    a = list(fibonachi(n))
    return a


@app.errorhandler(404)
def page_not_found(e):
    return "Please enter integers!"


if __name__ == '__main__':
    app.run(debug=True)