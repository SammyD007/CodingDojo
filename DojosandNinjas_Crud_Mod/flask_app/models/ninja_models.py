from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def __repr__(self) -> str:
        return f"Ninja REPR -> {self.id}{self.first_name}"
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        ninjas = []
        for i in results:
            ninjas.append( cls(i) )
        return ninjas
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return result

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM ninjas WHERE first_name = %(first_name)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return result

    @classmethod
    def get_all_dojos_for_ninja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        dojos_with_ninjas = []
        for i in results:
            dojos_with_ninjas.append( cls(i) )
        return results