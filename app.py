from flask import Flask, render_template
import json

from data import lista_invitados, agregar_invitado

app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps(lista_invitados)


@app.route('/add/<nombre>/')
def agregar(nombre=''):
    agregar_invitado(nombre)
    return 'listo {nombre}'.format(nombre=nombre)


@app.route('/about')
def about():
    nombre = 'gael'
    return render_template('about.html', nombre=nombre)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
