from models.base import Base
from models.complemento import Complemento
from models.copa import Copa
from models.malteada import Malteada
from models.heladeria import Heladería

def main():
    # Crear ingredientes
    helado_fresa = Base("Helado de Fresa",1200, 200, 10, True, "Fresa")
    helado_Mandarina = Base("Helado de Mandarina",1200, 200, 10, True, "Mandarina")
    mani_japones = Complemento("Maní Japonés", 500, 100, 20, True)
    chispa_chocolate = Complemento("Chispa de Chocolate", 900, 50, 30, False)
    print("\nIngredientes':")
    print(f"Nombre: {helado_fresa.mostrar_nombre()} Precio: $ {helado_fresa.mostrar_precio()} Calorias: {helado_fresa.mostrar_calorias()} es Sano:{helado_fresa.es_sano()} Cantidades dis: {helado_fresa.mostrar_inventario()}")
    print(f"Nombre: {helado_Mandarina.mostrar_nombre()} Precio: $ {helado_Mandarina.mostrar_precio()} Calorias: {helado_Mandarina.mostrar_calorias()} es Sano:{helado_Mandarina.es_sano()} Cantidades dis: {helado_Mandarina.mostrar_inventario()}")
    print(f"Nombre: {mani_japones.mostrar_nombre()} Precio: $ {mani_japones.mostrar_precio()} Calorias: {mani_japones.mostrar_calorias()} es Sano:{mani_japones.es_sano()} Cantidades dis: {mani_japones.mostrar_inventario()}")
    print(f"Nombre: {chispa_chocolate.mostrar_nombre()} Precio: $ {chispa_chocolate.mostrar_precio()} Calorias: {chispa_chocolate.mostrar_calorias()} es Sano:{chispa_chocolate.es_sano()} Cantidades dis: {chispa_chocolate.mostrar_inventario()}")


    # Crear productos
    ingredientes_copa = [helado_fresa, mani_japones, chispa_chocolate]
    copaFresas = Copa("Samurai de fresas", 4900, "Vaso Grande", ingredientes_copa)

    ingredientes_copa = [helado_Mandarina, mani_japones]
    copaMandarina = Copa("Samurai de mandarinas", 4900, "Cono", ingredientes_copa)

    ingredientes_malteada = [helado_fresa, chispa_chocolate, mani_japones]
    malteadaChocoEspacial = Malteada("chocoespacial", 11000, 500, ingredientes_malteada)

    ingredientes_malteada = [helado_fresa, mani_japones]
    malteadaCupihelado = Malteada("Cupihelado", 3200, 300, ingredientes_malteada)

    # Crear heladería y agregar productos
    productos =[copaFresas, copaMandarina, malteadaChocoEspacial, malteadaCupihelado]
    heladeria = Heladería("Heladería ChocoFresa", productos)
    
    # Mostrar productos
    print("\nProductos disponibles:")
    heladeria.mostrar_productos()

    # Vender un producto que no existe
    print("\nVendiendo 'Copa de Fresa':")
    if heladeria.vender("Copa de Fresa"):
        print("Venta exitosa")
        
    else:
        print("No Se puede realizar la Venta No existe ese producto.")

    # Vender un producto que existe
    print("\nVendiendo 'Samurai de fresas':")
    if heladeria.vender("Samurai de fresas"):
        print("Venta exitosa")
    else:
        print("No Se puede realizar la Venta.")

    #Mostrar ingredientes despues de las ventas
    print("\nIngredientes disponibles':")
    print(f"Nombre: {helado_fresa.mostrar_nombre()} Precio: $ {helado_fresa.mostrar_precio()} Calorias: {helado_fresa.mostrar_calorias()} es Sano:{helado_fresa.es_sano()} Cantidades dis: {helado_fresa.mostrar_inventario()}")
    print(f"Nombre: {helado_Mandarina.mostrar_nombre()} Precio: $ {helado_Mandarina.mostrar_precio()} Calorias: {helado_Mandarina.mostrar_calorias()} es Sano:{helado_Mandarina.es_sano()} Cantidades dis: {helado_Mandarina.mostrar_inventario()}")
    print(f"Nombre: {mani_japones.mostrar_nombre()} Precio: $ {mani_japones.mostrar_precio()} Calorias: {mani_japones.mostrar_calorias()} es Sano:{mani_japones.es_sano()} Cantidades dis: {mani_japones.mostrar_inventario()}")
    print(f"Nombre: {chispa_chocolate.mostrar_nombre()} Precio: $ {chispa_chocolate.mostrar_precio()} Calorias: {chispa_chocolate.mostrar_calorias()} es Sano:{chispa_chocolate.es_sano()} Cantidades dis: {chispa_chocolate.mostrar_inventario()}")
    # Mostrar productos después de la venta
    print("\nProductos disponibles después de la venta:")
    heladeria.mostrar_productos()

    # Mostrar producto más rentable
    producto_rentable = heladeria.producto_mas_rentable()
    print(f"\nEl producto más rentable es: {producto_rentable.nombre}")

    #Total Ventas del día
    print(f"\nVentas del día: {heladeria.mostar_ventas_del_dia()}")

if __name__ == "__main__":
    main()
