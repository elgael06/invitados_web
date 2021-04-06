from flask import Flask, render_template, request, redirect
from data import lista_invitados, agregar_invitado, confirmar_invitacion, eliminar_invitacion

from config.url_api import list_url_apis
from controllers.hello import hello

app = Flask(__name__)


def create_apis():

    for api in list_url_apis:
        view = api['view']
        func = api['func']
        url = api['url']
        # apis
        app.view_functions[view] = func
        app.add_url_rule(url, view, func)


# llamar apis
create_apis()


@app.route('/')
def index():
    return redirect('/invitados')


@app.route('/invitados')
def invitados():
    ###
    # mustra el listado de invitados.
    ###
    return render_template('lista.html', lista=lista_invitados)


@app.route('/add/', methods=['GET', 'POST'])
def agregar():
    ###
    # en el metodo get muestra la pagina de el formularui para agregar.
    # agregar invitado ingresa el nombre en el listado llamando la funcion de agregar
    ###
    if request.method == 'GET':
        return render_template('agregar.html')
    else:
        nombre = request.form.get("nombre")
        agregar_invitado(nombre)
        return redirect('/')


@app.route('/confirmar/<nombre>')
def confirmar(nombre=''):
    ###
    # Este metodo solo cambia el estado de confirmacion mediante el nombre.
    # y redirecciona a la pagina principal.
    ###
    confirmar_invitacion(nombre)
    return redirect('/')


@app.route('/eliminar/<nombre>')
def eliminar(nombre=''):
    eliminar_invitacion(nombre)
    return redirect('/')


###
# inicia la aplicacion web si el app esta en el main.
###
if __name__ == "__main__":
    app.run(debug=True, port=8000)
