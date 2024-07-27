from flask_restful import Resource
from flask import request, jsonify, render_template, make_response
from decorators import admin_required, empleado_required, cliente_required
from models.ingredientes import Ingredientes
from db import db

class IngredienteController(Resource):
    @empleado_required
    def get(self, id=None):
        nombre = request.args.get('nombre', None)
        if id:
            ingrediente = Ingredientes.query.get_or_404(id)
            tipo_nombre = ingrediente.tipo.nombre
            if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
                 return jsonify({
                'id': ingrediente.id,
                'nombre': ingrediente.nombre,
                'precio': ingrediente.precio,
                'calorias': ingrediente.calorias,
                'inventario': ingrediente.inventario,
                'es_vegetariano': ingrediente.es_vegetariano,
                'tipo_id': ingrediente.tipo_id,
                'tipo_nombre': tipo_nombre,
                'sabor': ingrediente.sabor
                })
            else:
                return make_response(render_template('ingrediente.html', ingrediente=ingrediente, tipo_nombre=tipo_nombre))
        elif nombre:       
            ingrediente = Ingredientes.query.filter_by(nombre=nombre).first_or_404()
            tipo_nombre = ingrediente.tipo.nombre
            if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
                 return jsonify({
                'id': ingrediente.id,
                'nombre': ingrediente.nombre,
                'precio': ingrediente.precio,
                'calorias': ingrediente.calorias,
                'inventario': ingrediente.inventario,
                'es_vegetariano': ingrediente.es_vegetariano,
                'tipo_id': ingrediente.tipo_id,
                'tipo_nombre': tipo_nombre,
                'sabor': ingrediente.sabor
                })
            else:
                return make_response(render_template('ingrediente.html', ingrediente=ingrediente, tipo_nombre=tipo_nombre))
        else:
            ingredientes = Ingredientes.query.all()
            if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
                 result = []
                 for ingrediente in ingredientes: 
                    result.append({
                    'id': ingrediente.id,
                    'nombre': ingrediente.nombre,
                    'precio': ingrediente.precio,
                    'calorias': ingrediente.calorias,
                    'inventario': ingrediente.inventario,
                    'es_vegetariano': ingrediente.es_vegetariano,
                    'tipo_id': ingrediente.tipo_id,
                    'tipo_nombre': ingrediente.tipo.nombre,
                    'sabor': ingrediente.sabor
                    })
                 return jsonify(result)
            else:
                return make_response(render_template('ingredientes.html', ingredientes=ingredientes))
    @empleado_required
    def post(self):
        try:
            # Determina el tipo de datos de la solicitud
            if request.content_type == 'application/json':
                data = request.get_json()
            else:
                data = request.form.to_dict()
            
            # Convertir es_vegetariano a booleano
            es_vegetariano = data.get('es_vegetariano', 'false').lower() in ['true', '1', 't', 'y', 'yes']
            
            # Crear nuevo ingrediente
            nuevo_ingrediente = Ingredientes(
                nombre=data['nombre'],
                precio=float(data['precio']),
                calorias=int(data['calorias']),
                inventario=int(data['inventario']),
                es_vegetariano=es_vegetariano,
                tipo_id=int(data['tipo_id']),
                sabor=data.get('sabor', '')  # Usa una cadena vacía si no hay sabor
            )
            db.session.add(nuevo_ingrediente)
            db.session.commit()

            # Respuesta JSON
            response = {
                'message': 'Ingrediente creado con éxito',
                'id': nuevo_ingrediente.id
            }
            return f'Ingrediente creado con éxito {nuevo_ingrediente.id}', 201

        except Exception as e:
            # Manejo de errores
            error_response = {
                'message': 'Error al crear el ingrediente',
                'error': str(e)
            }
            return jsonify(error_response), 400

    @empleado_required
    def put(self, id):
        data = request.json
        ingrediente = Ingredientes.query.get_or_404(id)
        ingrediente.nombre = data['nombre']
        ingrediente.precio = data['precio']
        ingrediente.calorias = data['calorias']
        ingrediente.inventario = data['inventario']
        ingrediente.es_vegetariano = data['es_vegetariano']
        ingrediente.tipo_id = data['tipo_id']
        ingrediente.sabor = data.get('sabor')
        db.session.commit()
        return jsonify({'message': 'Ingrediente actualizado con éxito'})

    def delete(self, id):
        ingrediente = Ingredientes.query.get_or_404(id)
        db.session.delete(ingrediente)
        db.session.commit()
        return jsonify({'message': 'Ingrediente eliminado con éxito'})
    
class IngrdienteSanoController(Resource):
     @empleado_required
     def get(self, id):
        ingrediente = Ingredientes.query.get_or_404(id)
        es_sano = ingrediente.es_sano()
        if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
             return jsonify({
            'id': ingrediente.id,
            'nombre': ingrediente.nombre,
            'es_sano': es_sano
            })
        else:
            return make_response(render_template('esSano.html', ingrediente=ingrediente, es_sano = es_sano))

class IngredienteReabastecerController(Resource):
    @empleado_required
    def put(self, id):
        data = request.get_json()
        cantidad = data.get('cantidad', None)

        if cantidad is None or cantidad <= 0:
            return jsonify({'error': 'Cantidad inválida'})

        ingrediente = Ingredientes.query.get_or_404(id)
        ingrediente.abastecer(cantidad)
        db.session.commit()

        return jsonify({'message': f'Ingrediente {ingrediente.nombre} reabastecido con éxito, nuevo inventario: {ingrediente.inventario}'})

class RenovarInventario(Resource):
    @empleado_required
    def post(self, id):
        ingrediente = Ingredientes.query.get_or_404(id)
        ingrediente.renovar_inventario()
        db.session.commit()
        return jsonify({'message': 'Inventario renovado con éxito', 'nuevo_inventario': ingrediente.inventario})
