
# creamos una lista de invitados
lista_invitados = []

# agregamos invitados a la lista


def agregar_invitado(nombre=''):
    persona = {
        'nombre': nombre,
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

# calcular invitados


def calcular_invitados():
    cantidad = 0
    personas = []
    for persona in lista_invitados:
        if persona['confirmado']:
            print('confirmo: ', persona['nombre'])
            cantidad += 1
            personas.append(persona)
    print('asistiran:', cantidad)
    return {
        'cantidad': cantidad,
        'personas': personas
    }


# agregar
agregar_invitado('luis')
agregar_invitado('juan')
agregar_invitado('pepe')

# confirmar
confirmar_invitacion('juan')

calcular_invitados()
