from functools import wraps
from flask_login import current_user
from flask import make_response, redirect, render_template

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated: 
            return make_response(render_template('403.html')) 
        if not current_user.is_admin:
            return  make_response(render_template('403.html'))  # Redirige a una página de acceso denegado
        return f(*args, **kwargs)
    return decorated_function

def empleado_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated: 
            return make_response(render_template('403.html')) 
        elif not current_user.is_empleado and not current_user.is_admin:
            return make_response(render_template('403.html'))  # Redirige a una página de acceso denegado
        return f(*args, **kwargs)
    return decorated_function

def cliente_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return make_response(render_template('403.html'))  # Redirige a una página de acceso denegado
        return f(*args, **kwargs)
    return decorated_function
