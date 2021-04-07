
from mongoengine import *


class Invitado(Document):
    nombre = StringField(required=True)
    confirmo = BooleanField(default=False)
    meta = {'db_alias': 'db_base'}
