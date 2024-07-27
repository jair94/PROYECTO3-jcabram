import unittest
from models.heladeria import Heladeria, Ingredientes, Producto

class Test_heladeria(unittest.TestCase): 
    def setup_heladeria(self):
        heladeria = Heladeria()
    # Initialize heladeria with test data
        return heladeria

    def test_es_sano():
        assert es_sano(90, False) == True
        assert es_sano(110, True) == True
        assert es_sano(110, False) == False

    def test_abastecer_ingrediente(setup_heladeria):
        ingrediente = setup_heladeria.ingredientes[0]
        old_inventory = ingrediente.inventario
        ingrediente.abastecer()
        assert ingrediente.inventario == old_inventory + 5  # or 10 depending on the type

    def test_renovar_inventario(setup_heladeria):
        complemento = setup_heladeria.ingredientes[0]
        complemento.renovar_inventario()
        assert complemento.inventario == 0

    def test_calcular_calorias_copa(setup_heladeria):
        # Assuming a copa product for testing
        copa = setup_heladeria.productos[0]
        assert copa.calcular_calorias() == round(sum(ing.calorias for ing in copa.ingredientes) * 0.95, 2)

    def test_calcular_calorias_malteada(setup_heladeria):
        # Assuming a malteada product for testing
        malteada = setup_heladeria.productos[1]
        assert malteada.calcular_calorias() == sum(ing.calorias for ing in malteada.ingredientes) + 200

    def test_calcular_costo_produccion(setup_heladeria):
        copa = setup_heladeria.productos[0]
        assert copa.calcular_costo() == sum(ing.precio for ing in copa.ingredientes)

    def test_calcular_rentabilidad(setup_heladeria):
        copa = setup_heladeria.productos[0]
        assert copa.calcular_rentabilidad() == copa.precio_publico - copa.calcular_costo()

    def test_producto_mas_rentable(setup_heladeria):
        assert setup_heladeria.producto_mas_rentable() == "Expected Product Name"

    def test_vender_producto(setup_heladeria):
        result = setup_heladeria.vender("Nombre del producto")
        assert result == "¡Vendido!" or "¡Oh no! Nos hemos quedado sin XXXX"
