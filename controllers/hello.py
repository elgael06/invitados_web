import json


def hello_word():
    return json.dumps({
        'message': 'hola word!'
    })


def hello(name=''):
    return json.dumps({
        'message': 'hola {name}!'.format(name=name)
    })


hello_word.provide_automatic_options = False
hello_word.methods = ['GET', 'OPTIONS']

hello.provide_automatic_options = False
hello.methods = ['GET', 'OPTIONS']
