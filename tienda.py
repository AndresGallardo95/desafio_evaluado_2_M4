from producto import Producto

class Tienda:
    """
    Clase base que representa una tienda genérica.

    Atributos:
    ----------
    nombre : str
        El nombre de la tienda.
    costo_delivery : float
        El costo de delivery asociado a la tienda.
    productos : list
        La lista de productos disponibles en la tienda.

    Métodos:
    --------
    ingresar_producto(producto):
        Ingresa un producto a la tienda o actualiza su stock si ya existe.
    listar_productos():
        Lista los productos disponibles en la tienda.
    realizar_venta(nombre_producto, cantidad):
        Realiza la venta de un producto, ajustando su stock.
    """

    def __init__(self, nombre, costo_delivery):
        """
        Inicializa una tienda con un nombre y un costo de delivery.

        Parámetros:
        -----------
        nombre : str
            El nombre de la tienda.
        costo_delivery : float
            El costo de delivery asociado a la tienda.
        """
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, producto):
        """
        Ingresa un producto a la tienda. Si el producto ya existe, se actualiza su stock.

        Parámetros:
        -----------
        producto : Producto
            El producto a ingresar o actualizar en la tienda.
        """
        for prod in self.__productos:
            if prod == producto:
                prod.stock += producto.stock
                return
        self.__productos.append(producto)

    def listar_productos(self):
        """
        Lista los productos disponibles en la tienda, mostrando su nombre, precio y stock.

        Returns:
        --------
        str:
            Una cadena de texto con los productos listados.
        """
        return "\n".join([f"{prod.nombre}: {prod.precio} (Stock: {prod.stock})" for prod in self.__productos])

    def realizar_venta(self, nombre_producto, cantidad):
        """
        Realiza la venta de un producto, ajustando su stock.

        Parámetros:
        -----------
        nombre_producto : str
            El nombre del producto a vender.
        cantidad : int
            La cantidad del producto a vender.

        Returns:
        --------
        bool:
            True si la venta fue exitosa, False si no fue posible realizarla.
        """
        for prod in self.__productos:
            if prod.nombre == nombre_producto:
                if prod.stock >= cantidad:
                    prod.stock -= cantidad
                else:
                    prod.stock = 0
                return True
        return False

class Restaurante(Tienda):
    """
    Clase que representa una tienda de tipo Restaurante.

    Métodos:
    --------
    ingresar_producto(producto):
        Ingresa un producto a la tienda, estableciendo siempre el stock en 0.
    listar_productos():
        Lista los productos disponibles en la tienda, ocultando el stock.
    realizar_venta(nombre_producto, cantidad):
        Realiza una venta de un producto, sin importar el stock.
    """

    def ingresar_producto(self, producto):
        """
        Ingresa un producto a la tienda, estableciendo siempre el stock en 0.

        Parámetros:
        -----------
        producto : Producto
            El producto a ingresar en la tienda.
        """
        producto.stock = 0  # Siempre se crea con stock 0
        super().ingresar_producto(producto)

    def listar_productos(self):
        """
        Lista los productos disponibles en la tienda, mostrando solo su nombre y precio.

        Returns:
        --------
        str:
            Una cadena de texto con los productos listados sin stock.
        """
        return "\n".join([f"{prod.nombre}: {prod.precio}" for prod in self._Tienda__productos])

    def realizar_venta(self, nombre_producto, cantidad):
        """
        Realiza una venta de un producto, sin importar el stock.

        Parámetros:
        -----------
        nombre_producto : str
            El nombre del producto a vender.
        cantidad : int
            La cantidad del producto a vender.
        """
        pass  # Siempre se vende, no importa el stock

class Supermercado(Tienda):
    """
    Clase que representa una tienda de tipo Supermercado.

    Métodos:
    --------
    listar_productos():
        Lista los productos disponibles en la tienda, mostrando un mensaje si el stock es bajo.
    """

    def listar_productos(self):
        """
        Lista los productos disponibles en la tienda, mostrando el stock y un mensaje si es bajo.

        Returns:
        --------
        str:
            Una cadena de texto con los productos listados, incluyendo mensajes adicionales si el stock es bajo.
        """
        productos_listados = []
        for prod in self._Tienda__productos:
            mensaje_stock = f"Stock: {prod.stock}"
            if prod.stock < 10:
                mensaje_stock += " (Pocos productos disponibles)"
            productos_listados.append(f"{prod.nombre}: {prod.precio} ({mensaje_stock})")
        return "\n".join(productos_listados)

class Farmacia(Tienda):
    """
    Clase que representa una tienda de tipo Farmacia.

    Métodos:
    --------
    listar_productos():
        Lista los productos disponibles en la tienda, ocultando el stock y mostrando un mensaje si el precio es alto.
    realizar_venta(nombre_producto, cantidad):
        Realiza la venta de un producto, con restricciones sobre la cantidad.
    """

    def listar_productos(self):
        """
        Lista los productos disponibles en la tienda, mostrando el precio y un mensaje si es alto.

        Returns:
        --------
        str:
            Una cadena de texto con los productos listados, incluyendo mensajes adicionales si el precio es alto.
        """
        productos_listados = []
        for prod in self._Tienda__productos:
            mensaje_precio = f"{prod.precio}"
            if prod.precio > 15000:
                mensaje_precio += " (Envío gratis al solicitar este producto)"
            productos_listados.append(f"{prod.nombre}: {mensaje_precio}")
        return "\n".join(productos_listados)

    def realizar_venta(self, nombre_producto, cantidad):
        """
        Realiza la venta de un producto, con restricciones sobre la cantidad.

        Parámetros:
        -----------
        nombre_producto : str
            El nombre del producto a vender.
        cantidad : int
            La cantidad del producto a vender (no más de 3 unidades por venta).

        Returns:
        --------
        bool:
            True si la venta fue exitosa, False si no fue posible realizarla.
        """
        if cantidad > 3:
            return False  # No se permite vender más de 3 unidades
        return super().realizar_venta(nombre_producto, cantidad)
