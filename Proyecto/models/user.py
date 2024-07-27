from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user
from db import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Incrementar longitud para el hash
    is_admin = db.Column(db.Boolean, nullable=False)
    is_empleado = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, password, is_admin, is_empleado):
        self.username = username
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        self.is_empleado = is_empleado
    
    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()  
        if user and check_password_hash(user.password, password):
            login_user(user)
            return True
        return False
