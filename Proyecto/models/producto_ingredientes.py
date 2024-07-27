from db import db

producto_ingredientes = db.Table('producto_ingredientes',
    db.Column('producto_id', db.Integer, db.ForeignKey('producto.id'), primary_key=True),
    db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingredientes.id'), primary_key=True)
)
