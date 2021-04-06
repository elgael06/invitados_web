import json


def hello(name=''):
    print('hello')
    return json.dumps({
        'message': 'hola {name}!'.format(name=name)
    })


hello.provide_automatic_options = False
hello.methods = ['GET', 'OPTIONS']
