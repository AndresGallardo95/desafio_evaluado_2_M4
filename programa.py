# programa.py
from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

def main():
    print("Bienvenido al sistema de gestión de tiendas")
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante, Supermercado, Farmacia): ")
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))

    if tipo_tienda.lower() == "restaurante":
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "supermercado":
        tienda = Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "farmacia":
        tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return

    while True:
        print("\nOpciones:")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            stock_producto = int(input("Ingrese el stock del producto (o 0 si no tiene stock): "))
            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.ingresar_producto(producto)
            print("Producto ingresado correctamente.")
        elif opcion == "2":
            print("Listado de productos:")
            print(tienda.listar_productos())
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto que desea vender: ")
            cantidad_producto = int(input("Ingrese la cantidad a vender: "))
            if tienda.realizar_venta(nombre_producto, cantidad_producto):
                print("Venta realizada con éxito.")
            else:
                print("No se pudo realizar la venta.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
