class Producto:
    """
    Clase que representa un producto en una tienda.

    Atributos:
    ----------
    nombre : str
        El nombre del producto.
    precio : float
        El precio del producto.
    stock : int, opcional
        La cantidad de stock disponible para el producto. Si no se especifica, el stock será 0.
    
    Métodos:
    --------
    nombre:
        Devuelve el nombre del producto.
    precio:
        Devuelve el precio del producto.
    stock:
        Devuelve el stock del producto.
    stock.setter:
        Establece el stock del producto, asegurándose de que no sea negativo.
    __add__(other):
        Suma el stock de dos productos con el mismo nombre.
    __eq__(other):
        Compara dos productos por su nombre.
    """

    def __init__(self, nombre, precio, stock=0):
        """
        Inicializa un nuevo producto con el nombre, precio y stock especificados.

        Parámetros:
        -----------
        nombre : str
            El nombre del producto.
        precio : float
            El precio del producto.
        stock : int, opcional
            La cantidad de stock disponible para el producto. Si no se especifica, el stock será 0.
        """
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)  # El stock no puede ser negativo

    @property
    def nombre(self):
        """
        Devuelve el nombre del producto.

        Returns:
        --------
        str:
            El nombre del producto.
        """
        return self.__nombre

    @property
    def precio(self):
        """
        Devuelve el precio del producto.

        Returns:
        --------
        float:
            El precio del producto.
        """
        return self.__precio

    @property
    def stock(self):
        """
        Devuelve el stock del producto.

        Returns:
        --------
        int:
            La cantidad de stock disponible del producto.
        """
        return self.__stock

    @stock.setter
    def stock(self, cantidad):
        """
        Establece el stock del producto, asegurándose de que no sea negativo.

        Parámetros:
        -----------
        cantidad : int
            La nueva cantidad de stock. Si es menor a 0, se establece en 0.
        """
        self.__stock = max(0, cantidad)

    def __add__(self, other):
        """
        Suma el stock de dos productos con el mismo nombre.

        Parámetros:
        -----------
        other : Producto
            El otro producto con el que se sumará el stock.

        Returns:
        --------
        Producto:
            Un nuevo producto con el mismo nombre y precio, pero con el stock sumado.
        """
        if self.__nombre == other.nombre:
            nuevo_stock = self.__stock + other.stock
            return Producto(self.__nombre, self.__precio, nuevo_stock)
        else:
            return self

    def __eq__(self, other):
        """
        Compara dos productos por su nombre.

        Parámetros:
        -----------
        other : Producto
            El otro producto a comparar.

        Returns:
        --------
        bool:
            True si los productos tienen el mismo nombre, False en caso contrario.
        """
        return self.__nombre == other.nombre
