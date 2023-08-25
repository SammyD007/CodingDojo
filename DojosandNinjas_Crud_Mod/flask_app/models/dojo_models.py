from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def __repr__(self) -> str:
        return f"Dojo REPR -> {self.id}{self.name}"
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for i in results:
            dojos.append( cls(i) )
        return dojos
    
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE name = (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return result
    
    @classmethod
    def get_name(cls,data):
        query  = "SELECT name FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return result
    
    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, {'name' : data['name']})
        return result
    
    @classmethod
    def get_all_ninjas_for_dojo(cls, data):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON dojos.id = ninjas.dojo_id WHERE ninjas.dojo_id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return results