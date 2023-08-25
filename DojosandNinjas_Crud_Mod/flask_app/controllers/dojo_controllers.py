from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.dojo_models import Dojo
from flask_app.models.ninja_models import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def display_dojos():
    return render_template('dojos.html', dojos = Dojo.get_all())

@app.route('/dojos/created', methods = ['POST'])
def created_dojo():
    Dojo.add_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/new_ninja')
def new_ninja():
    return render_template('new_ninja.html', dojos = Dojo.get_all())

@app.route('/dojos/create_ninja', methods = ['POST'])
def new_ninja_create():
    Ninja.create(request.form)
    return redirect('/dojos')

@app.route('/delete')
def delete_user():
    Ninja.delete(request.form)
    return redirect('/dojos')

@app.route('/show_dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    data ={
        'id':dojo_id
    }
    return render_template('show_dojo.html', ninjas = Ninja.get_all_dojos_for_ninja(data), dojos = Dojo.get_name(data))