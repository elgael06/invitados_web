from controllers.hello import hello, hello_word


list_url_apis = [
    {'view': 'hello', 'func': hello, 'url': '/api/hello/<name>'},
    {'view': 'word', 'func': hello_word, 'url': '/api/hello'},
]
