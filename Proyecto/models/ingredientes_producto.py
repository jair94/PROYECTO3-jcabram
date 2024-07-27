from db import db


class Ingredientes_producto(db.Model):
    id = db.Column (db.Integer(45), primari_key = True )
    id_producto = db.Column (db.Interger,nullable = False)
    id_ingredientes =db.Column (db.Interger,nullable = False)