from flask import Flask
import json

from main import lista_invitados, agregar_invitado

app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps(lista_invitados)


@app.route('/add/<nombre>/')
def agregar(nombre=''):
    agregar_invitado(nombre)
    return 'listo {nombre}'.format(nombre=nombre)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
