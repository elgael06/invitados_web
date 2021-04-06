
# creamos una lista de invitados
lista_invitados = []

# agregamos invitados a la lista


def agregar_invitado(nombre=''):
    for persona in lista_invitados:
        if persona['nombre'] == nombre.upper():
            return None
    persona = {
        'nombre': nombre.upper(),
        'confirmado': False
    }
    print(persona)
    lista_invitados.append(persona)

# confirmamos invitacion


def confirmar_invitacion(invitado=''):
    for persona in lista_invitados:
        if persona['nombre'] == invitado:
            print(persona)
            persona['confirmado'] = True
            break
    print(lista_invitados)

# eliminar invitacion


def eliminar_invitacion(nombre=''):
    for persona in lista_invitados:
        print(persona)
        if persona['nombre'] == nombre:
            lista_invitados.remove(persona)
            break

# calcular invitados


def calcular_invitados():
    cantidad = 0
    personas = []
    for persona in lista_invitados:
        if persona.confirmado:
            print('confirmo: ', persona.nombre)
            cantidad += 1
            personas.append(persona)
    print('asistiran:', cantidad)
    return {
        'cantidad': cantidad,
        'personas': personas
    }


# # agregar
# agregar_invitado('luis')
# agregar_invitado('juan')
# agregar_invitado('pepe')

# # confirmar
# confirmar_invitacion('juan')

# calcular_invitados()
