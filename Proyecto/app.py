from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_restful import Api
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from models.heladeria import Heladeria
from models.producto import Producto
from models.ingredientes import Ingredientes
from models.tipo_ingrediente import TipoIngrediente
from models.user import User
from models.heladeria import Heladeria
from db import db
from dotenv import load_dotenv
from controllers.ingredientes_controllers import IngredienteController, IngrdienteSanoController, IngredienteReabastecerController, RenovarInventario
from controllers.producto_controllers import ProductoController, ProductoCaloriasController, ProductoCalcularRentabilidadController, ProductoCostoController
from controllers.heladeria_controllers import HeladeriaController
from controllers.user_controller import RegisterController, LoginController
from decorators import admin_required, empleado_required, cliente_required

import os

load_dotenv()

secret_key = os.urandom(24)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://root:PYecFxYAGXlFbNWMhcLNiuvOujHPpRUQ@monorail.proxy.rlwy.net:24811/railway'
app.config["SECRET_KEY"] = secret_key
db.init_app(app)
api = Api(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user
    return None
api.add_resource(RegisterController, '/register')
api.add_resource(LoginController, '/login')
api.add_resource(HeladeriaController, '/heladeria', '/heladeria/<int:id>')
api.add_resource(ProductoController, '/producto', '/producto/<int:id>')
api.add_resource(IngredienteController, '/ingrediente', '/ingrediente/<int:id>')
api.add_resource(IngrdienteSanoController, '/ingrediente/<int:id>/sano')
api.add_resource(ProductoCaloriasController, '/producto/<int:id>/calorias')
api.add_resource(ProductoCalcularRentabilidadController, '/producto/<int:id>/rentabilidad')
api.add_resource(ProductoCostoController, '/producto/<int:id>/costo')
api.add_resource(IngredienteReabastecerController, '/ingrediente/<int:id>/reabastecer')
api.add_resource(RenovarInventario, '/ingrediente/<int:id>/renovar')



@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@app.route('/ingrediente/form', methods=['GET'])
@login_required
@empleado_required
def ingrediente_form():
    return render_template('ingrediente_form.html')

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/vender/<int:id_producto>', methods=['POST'])
@cliente_required
def vender_producto(id_producto):
    heladeria = Heladeria.query.first()
    try:
        resultado = heladeria.vender(id_producto)
        if resultado == "¡Vendido!":
            return jsonify({"message": resultado})
        else:
            return jsonify({"message": "Producto no encontrado"}), 404
    except ValueError as e:
        return jsonify({"message": f"¡Oh no! {str(e)}"}), 400
    except Exception as e:
        return jsonify({"message": f"Error inesperado: {str(e)}"}), 500
    
@app.route('/ingrediente/<int:id>/renovar', methods=['GET', 'POST'])
@login_required
@empleado_required
def renovar_ingrediente(id):
    ingrediente = Ingredientes.query.get_or_404(id)
    if request.method == 'POST':
        ingrediente.renovar_inventario()
        db.session.commit()
        flash(f'Ingrediente {ingrediente.nombre} renovado con éxito.')
        return redirect('/ingrediente')
    return render_template('renovar_ingrediente.html', ingrediente=ingrediente) 


@app.route('/ingrediente/<int:id>/reabastecer', methods=['GET', 'POST'])
@login_required
@empleado_required
def reabastecer_ingrediente(id):
    ingrediente = Ingredientes.query.get_or_404(id)
    if request.method == 'POST':
        cantidad = request.form.get('cantidad', type=int)
        if cantidad and cantidad > 0:
            ingrediente.abastecer(cantidad)
            db.session.commit()
            flash(f'Ingrediente {ingrediente.nombre} reabastecido con éxito.')
            return redirect('/ingrediente')
        else:
            flash('Cantidad inválida.')
    return render_template('reabastecer_ingrediente.html', ingrediente=ingrediente)    

@app.route('/menu')
def menu():
    productos = Producto.query.all()
    return render_template('menu.html', productos=productos)

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html')

if __name__ == '__main__':
    app.run(debug=True)
