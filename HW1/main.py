import random

from flask import Flask

app = Flask(__name__)


@app.route('/')

def hello():
    return "<h1>Hello CSC330</h1>"

@app.route('/random/')

def generate_random():
    num = random.randint(1,100)
    return "Your lucky number is " + str(num)


@app.route('/name/<name_str>/')

def print_greeting(name_str):
    return '<h1> Hey, ' + name_str+ '!!</h1>'

@app.route('/reverse/<some_string>/')

def reverse_string(some_string):
    return '<h1> ' +  some_string[::-1]+ '</h1>'

@app.route('/tobinary/<some_integer>/')

def tobinary(some_integer):
    num = int(some_integer)
    return '<h1> The binary conversion of ' + some_integer + '='+ bin(num) + '<h1>'

