from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['first_name']
        self.apellido = data['last_name']
        self.edad = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name , last_name, age, created_at, updated_at, dojo_id ) VALUES ( %(nombre)s, %(apellido)s, %(edad)s, NOW(), NOW(), %(id_dojo)s );"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db( query, data )

    