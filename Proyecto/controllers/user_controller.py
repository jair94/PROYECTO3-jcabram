from flask import request, jsonify, redirect, render_template, make_response
from flask_restful import Resource
from flask_login import login_user, logout_user
from models.user import User
from db import db

class RegisterController(Resource):
    def get(self):
        return make_response(render_template('register.html'))

    def post(self):
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form

        # Crear el nuevo usuario sin pasar el id, ya que es autogenerado
        new_user = User(
            username=data.get('username'),
            password=data.get('password'),
            is_admin=bool(data.get('is_admin')),
            is_empleado=bool(data.get('is_empleado'))
        )
        db.session.add(new_user)
        db.session.commit()

        if request.content_type == 'application/json':
            return {'message': 'User registered successfully'}, 201
        return redirect('/login')

class LoginController(Resource):
    def get(self):
        return make_response(render_template('login.html'))

    def post(self):
        if request.content_type == 'application/json':
            data = request.json
        else:
            data = request.form

        # Verificar si el usuario se autentica correctamente
        if User.authenticate(data.get('username'), data.get('password')):
            if request.content_type == 'application/json':
                return {'message': 'Login successful'}, 200
            login_user(User.query.filter_by(username=data.get('username')).first())
            return redirect('/welcome')  # O renderiza una plantilla
        else:
            if request.content_type == 'application/json':
                return {'message': 'Invalid credentials'}, 401
            return redirect('/login')  # O renderiza una plantilla
