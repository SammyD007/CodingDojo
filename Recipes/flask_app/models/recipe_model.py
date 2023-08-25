from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request, session

db = 'recipes_schema'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30_mins = data['under_30_mins']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def submit_recipe(cls, data, user_id):
        query = '''INSERT INTO recipes (name, description, instructions, date_made, under_30_mins, user_id) 
                VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30_mins)s, %(user_id)s);'''

        data['user_id'] = user_id
        db_response = connectToMySQL(db).query_db(query, data)
        return db_response

    @classmethod
    def get_user_recipes(cls):
        query = ''' SELECT * 
        FROM recipes
        LEFT JOIN users
        ON recipes.user_id = users.id'''
        db_response = connectToMySQL(db).query_db(query)
        return db_response

    @classmethod
    def get_one_recipe(cls, data):
        query = 'SELECT * FROM recipes WHERE id = %(id)s;'
        db_response = connectToMySQL(db).query_db(query, data)
        return cls(db_response[0])

    @classmethod
    def edit_recipe(cls, data, recipe_id):
        data_dict = {
            'name': request.form['name'],
            'description': request.form['description'],
            'instructions': request.form['instructions'],
            'date_made': request.form['date_made'],
            'under_30_mins': request.form['under_30_mins'],
            'recipe_id': recipe_id
        }
        query = '''
            UPDATE recipes
            SET name = %(name)s,
            description = %(description)s,
            instructions = %(instructions)s,
            date_made = %(date_made)s,
            under_30_mins = %(under_30_mins)s
            WHERE id = %(recipe_id)s;
            '''
        db_response = connectToMySQL(db).query_db(query, data_dict)
        if db_response:
            db_response = cls(db_response[0])
        
        print('******data*******', data)
        print('~!!~!~!~!~! db_response', db_response)
        return db_response

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes where id = %(id)s"
        db_response = connectToMySQL(db).query_db(query, data)
        return db_response

    @classmethod
    def view_recipe(cls, data):
        query = "SELECT * FROM recipes;"
        db_response = connectToMySQL(db).query_db(query, data)
        return db_response
