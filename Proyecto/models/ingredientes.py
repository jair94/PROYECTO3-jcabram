from db import db

class Ingredientes(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    inventario = db.Column(db.Double, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo_ingrediente.id'), nullable=False)
    sabor = db.Column(db.String(50), nullable=True)

    tipo = db.relationship('TipoIngrediente', backref=db.backref('ingredientes', lazy=True))
    
    def es_sano(self):
        return self.calorias < 100 or self.es_vegetariano

    def abastecer(self, cantidad):
        if cantidad == 10:
            self.inventario += 10
        else:
            self.inventario += 5

    def renovar_inventario(self):
        self.inventario = 0        

    def __repr__(self):
        return f'<Ingrediente {self.nombre}>'


    