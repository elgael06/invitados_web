
from mongoengine import *


class Invitado(Document):
    nombre = StringField(required=True)
    confirmo = BooleanField(default=False)
    meta = {'db_alias': 'db_base'}

    def parseJSON(self):
        if self.id is not None:
            return {
                'id': self.id,
                'nombre': self.nombre,
                'confirmado': self.confirmo
            }
