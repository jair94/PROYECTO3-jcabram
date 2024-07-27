from db import db
from models.producto import Producto
from models.ingredientes import Ingredientes

class Heladeria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    productos = db.relationship('Producto', backref='heladeria', lazy=True)

    def __init__(self):
        self.productos = Producto.query.all()

    def get_productos(self):
        return self.productos

    def vender(self, id_producto):
        producto = Producto.query.get(id_producto)
        if not producto:
            return False
        
        for ingrediente in producto.ingredientes:
            if ingrediente.tipo_id == 1 and ingrediente.inventario < 0.2:
                raise ValueError(f"Nos hemos quedado sin {ingrediente.nombre}")
            elif ingrediente.tipo_id == 2 and ingrediente.inventario < 1:
                raise ValueError(f"Nos hemos quedado sin {ingrediente.nombre}")
        
        for ingrediente in producto.ingredientes:
            if ingrediente.tipo_id == 1:
                ingrediente.inventario -= 0.2
            elif ingrediente.tipo_id == 2:
                ingrediente.inventario -= 1

        db.session.commit()
        return "¡Vendido!"