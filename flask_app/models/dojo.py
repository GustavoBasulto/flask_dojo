from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id=%(dojo_id)s;"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        print(results)
        if len(results) == 0:
            return None
        dojo_data = {
            'id': results[0]['id'],
            'name':  results[0]['name'],
            'created_at': results[0]['created_at'],
            'updated_at': results[0]['updated_at'] 
        }
        dojo = Dojo(dojo_data)
        all_ninjas = []
        for data in results:
            print('*'*20)
            print(data)
            ninja_data = {
                'id': data['ninjas.id'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'age': data['age'],
                'created_at': data['ninjas.created_at'],
                'updated_at': data['ninjas.updated_at']
            }
            new_ninja = Ninja(ninja_data)
            print(new_ninja)
            all_ninjas.append(new_ninja)
        dojo.ninjas = all_ninjas
        return dojo

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(nombre)s , NOW() , NOW() );"
        return connectToMySQL('esquema_dojos_y_ninjas').query_db( query, data )
