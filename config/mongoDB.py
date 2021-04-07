from mongoengine import connect


def init_mongo_db():
    connect(
        db='invitatos_web',
        username='admin',
        password='1234',
        host='mongodb+srv://admin:1234@cluster0.4geja.mongodb.net',
        # 'mongodb://localhost:27017',
        alias='db_base'
    )
