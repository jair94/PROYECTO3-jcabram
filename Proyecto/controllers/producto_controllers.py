from flask_restful import Resource
from flask import request, jsonify, render_template, make_response
from decorators import admin_required, empleado_required, cliente_required
from models.producto import Producto
from db import db

class ProductoController(Resource):

    def get(self, id=None):
        nombre = request.args.get('nombre', None)
        if id:
            producto = Producto.query.get_or_404(id)
            if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
                return jsonify({
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio_publico': producto.precio_publico,
                    'tipo_vaso': producto.tipo_vaso,
                    'volumen': producto.volumen,
                    'heladeria_id': producto.heladeria_id,
                    'tipo_producto': producto.tipo_producto
                })
            else:
                return make_response(render_template('producto.html', producto=producto))
        elif nombre:
            producto = Producto.query.filter_by(nombre=nombre).first_or_404()
            if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
                return jsonify({
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio_publico': producto.precio_publico,
                    'tipo_vaso': producto.tipo_vaso,
                    'volumen': producto.volumen,
                    'heladeria_id': producto.heladeria_id,
                    'tipo_producto': producto.tipo_producto
                })
            else:
                return make_response(render_template('producto.html', producto=producto))
        else:
            productos = Producto.query.all()
            if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
                result = []
                for producto in productos:
                    result.append({
                        'id': producto.id,
                        'nombre': producto.nombre,
                        'precio_publico': producto.precio_publico,
                        'tipo_vaso': producto.tipo_vaso,
                        'volumen': producto.volumen,
                        'heladeria_id': producto.heladeria_id,
                        'tipo_producto': producto.tipo_producto
                    })
                return jsonify(result)
            else:
                return make_response(render_template('productos.html', productos=productos))
    
    @empleado_required
    def post(self):
        data = request.json
        nuevo_producto = Producto(
            nombre=data['nombre'],
            precio_publico=data['precio_publico'],
            tipo_vaso=data.get('tipo_vaso'),
            volumen=data.get('volumen'),
            heladeria_id=data['heladeria_id'],
            tipo_producto=data['tipo_producto']
        )
        db.session.add(nuevo_producto)
        db.session.commit()
        return jsonify({'message': 'Producto creado con éxito'}), 201
    
    @empleado_required
    def put(self, id):
        data = request.json
        producto = Producto.query.get_or_404(id)
        producto.nombre = data['nombre']
        producto.precio_publico = data['precio_publico']
        producto.tipo_vaso = data.get('tipo_vaso')
        producto.volumen = data.get('volumen')
        producto.heladeria_id = data['heladeria_id']
        producto.tipo_producto = data['tipo_producto']
        db.session.commit()
        return jsonify({'message': 'Producto actualizado con éxito'})
    
    @empleado_required
    def delete(self, id):
        producto = Producto.query.get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return jsonify({'message': 'Producto eliminado con éxito'})

class ProductoCaloriasController(Resource):
    @cliente_required
    def get(self, id):
        producto = Producto.query.get_or_404(id)
        calorias = producto.calcular_calorias()
        if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
            return jsonify({'calorias': calorias})
        else:
            return make_response(render_template('producto_calorias.html', producto=producto, calorias=calorias))
        
class ProductoCalcularRentabilidadController(Resource):
    @admin_required
    def get(self, id):
        producto = Producto.query.get_or_404(id)
        rentabilidad = producto.calcular_rentabilidad()
        if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
            return jsonify({'Rentabilidad': rentabilidad})
        else:
            return make_response(render_template('rentabilidad_producto.html', producto=producto, rentabilidad=rentabilidad))

class ProductoCostoController(Resource):
    @empleado_required
    def get(self, id):
        producto = Producto.query.get_or_404(id)
        costo = producto.calcular_costo()
        if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
            return jsonify({'costo': costo})
        else:
            return make_response(render_template('producto_costo.html', producto=producto, costo=costo))