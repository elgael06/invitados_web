from models.Invitado import Invitado
# creamos una lista de invitados
lista_invitados = []


def todos_invitados():
    # obtenemos los invitados de la base de datos
    lista = []
    for inv in Invitado.objects:
        lista.append(inv.parseJSON())
    return lista


def agregar_invitado(nombre=''):
    # agregamos invitados a la base de datos
    new_inv = Invitado(nombre=nombre)
    new_inv.save()
    print('Nuevo: ', new_inv.id)


def confirmar_invitacion(invitado=''):
    # confirmamos invitacion
    print('confirmar id: ', invitado)
    inv = Invitado.objects(id=invitado).first()
    inv.confirmo = True
    inv.save()


def eliminar_invitacion(nombre=''):
    # eliminar invitacion
    inv = Invitado.objects(id=nombre).first()
    print('Eliminado: ', inv.id)
    inv.delete()
