from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

def main():
    """
    Función principal que ejecuta el sistema de gestión de tiendas.

    El usuario puede crear una tienda, ingresar productos, listar productos, 
    realizar ventas y salir del programa. Dependiendo del tipo de tienda 
    seleccionado, las opciones y comportamientos pueden variar.

    El flujo del programa es el siguiente:
    1. El usuario selecciona el tipo de tienda y define su nombre y costo de delivery.
    2. El usuario puede ingresar productos, listarlos, realizar ventas o salir.
    3. El programa se repite hasta que el usuario decide salir.

    Opciones del menú:
    ------------------
    1. Ingresar producto:
        Solicita los detalles del producto y lo agrega a la tienda.
    2. Listar productos:
        Muestra una lista de productos disponibles en la tienda.
    3. Realizar venta:
        Permite vender un producto ajustando el stock disponible.
    4. Salir:
        Finaliza la ejecución del programa.
    """
    print("Bienvenido al sistema de gestión de tiendas")
    
    # Solicitar al usuario que elija el tipo de tienda y sus detalles.
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante, Supermercado, Farmacia): ")
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))

    # Crear la instancia de la tienda según el tipo seleccionado
    if tipo_tienda.lower() == "restaurante":
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "supermercado":
        tienda = Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "farmacia":
        tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return

    # Bucle principal del programa
    while True:
        # Mostrar el menú de opciones al usuario
        print("\nOpciones:")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        # Opción 1: Ingresar producto
        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            stock_producto = int(input("Ingrese el stock del producto (o 0 si no tiene stock): "))
            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.ingresar_producto(producto)
            print("Producto ingresado correctamente.")
        
        # Opción 2: Listar productos
        elif opcion == "2":
            print("Listado de productos:")
            print(tienda.listar_productos())
        
        # Opción 3: Realizar venta
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto que desea vender: ")
            cantidad_producto = int(input("Ingrese la cantidad a vender: "))
            if tienda.realizar_venta(nombre_producto, cantidad_producto):
                print("Venta realizada con éxito.")
            else:
                print("No se pudo realizar la venta.")
        
        # Opción 4: Salir del programa
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        # Opción inválida
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
