from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.login_reg_model import User
from flask_app.models.recipe_model import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('login_reg.html', users = User.get_all_users())

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    user_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash,
    }
    
    user_id = User.create_user(user_data)
    session['user_id'] = user_id
    session['user_name'] = request.form['first_name']

    return redirect('/welcome')

@app.route('/login', methods=["POST"])
def login():
    user = User.validate_login(request.form)

    if not user:
        flash('Invalid Email or Password')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email or Password")
        return redirect('/')

    session['user_id'] = user.id
    session['user_name'] = user.first_name

    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    users = User.get_all_users()
    user_name = session.get('user_name')
    recipes = Recipe.get_user_recipes()
    return render_template('welcome.html', user_name = user_name, users = users, recipes = recipes)

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# --------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                RECIPES                                                                  #

@app.route('/create_recipe', methods = ['POST'])
def create_recipe():
    return render_template('create_recipe.html')

@app.route('/submit_recipe', methods=['POST'])
def submit_recipe():
    user_id = session.get('user_id')

    recipe_data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made': request.form['date_made'],
        'under_30_mins': request.form['under_30_mins'],
    }

    Recipe.submit_recipe(recipe_data, user_id)

    return redirect('/welcome')

@app.route('/display_edit_page/<int:recipe_id>')
def display_edit_page(recipe_id):
    data ={
        'id': recipe_id
    }
    return render_template('/edit_recipe.html', recipe = Recipe.get_one_recipe(data))

@app.route('/edit_recipe/<int:recipe_id>', methods = ['POST'])
def edit_recipe(recipe_id):
    Recipe.edit_recipe(request.form, recipe_id)
    return redirect('/welcome')

@app.route('/view_recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    data ={
        'id': recipe_id
    }
    return render_template('view_recipe.html', get_recipe = Recipe.get_one_recipe(data))

@app.route('/delete_recipe/<int:recipe_id>')
def delete_recipe(recipe_id):
    data ={
        'id': recipe_id
    }
    Recipe.delete_recipe(data)
    return redirect('/welcome')