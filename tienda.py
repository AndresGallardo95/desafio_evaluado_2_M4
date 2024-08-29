# tienda.py
from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, producto):
        for prod in self.__productos:
            if prod == producto:
                prod.stock += producto.stock
                return
        self.__productos.append(producto)

    def listar_productos(self):
        return "\n".join([f"{prod.nombre}: {prod.precio} (Stock: {prod.stock})" for prod in self.__productos])

    def realizar_venta(self, nombre_producto, cantidad):
        for prod in self.__productos:
            if prod.nombre == nombre_producto:
                if prod.stock >= cantidad:
                    prod.stock -= cantidad
                else:
                    prod.stock = 0
                return True
        return False

class Restaurante(Tienda):
    def ingresar_producto(self, producto):
        producto.stock = 0  # Siempre se crea con stock 0
        super().ingresar_producto(producto)

    def listar_productos(self):
        return "\n".join([f"{prod.nombre}: {prod.precio}" for prod in self._Tienda__productos])

    def realizar_venta(self, nombre_producto, cantidad):
        pass  # Siempre se vende, no importa el stock

class Supermercado(Tienda):
    def listar_productos(self):
        productos_listados = []
        for prod in self._Tienda__productos:
            mensaje_stock = f"Stock: {prod.stock}"
            if prod.stock < 10:
                mensaje_stock += " (Pocos productos disponibles)"
            productos_listados.append(f"{prod.nombre}: {prod.precio} ({mensaje_stock})")
        return "\n".join(productos_listados)

class Farmacia(Tienda):
    def listar_productos(self):
        productos_listados = []
        for prod in self._Tienda__productos:
            mensaje_precio = f"{prod.precio}"
            if prod.precio > 15000:
                mensaje_precio += " (Envío gratis al solicitar este producto)"
            productos_listados.append(f"{prod.nombre}: {mensaje_precio} (Stock: {prod.stock})")
        return "\n".join(productos_listados)

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            return False  # No se permite vender más de 3 unidades
        return super().realizar_venta(nombre_producto, cantidad)
