from flask import Flask, render_template, request, redirect
from data import lista_invitados, agregar_invitado, confirmar_invitacion

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('lista.html', lista=lista_invitados)


@app.route('/add/', methods=['GET', 'POST'])
def agregar():
    if request.method == 'GET':
        return render_template('agregar.html')
    else:
        nombre = request.form.get("nombre")
        agregar_invitado(nombre)
        return redirect('/')


@app.route('/confirmar/<nombre>')
def confirmar(nombre=''):
    print(nombre)
    confirmar_invitacion(nombre)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
