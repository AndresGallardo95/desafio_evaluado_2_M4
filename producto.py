# producto.py

class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)  # El stock no puede ser negativo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, cantidad):
        self.__stock = max(0, cantidad)

    def __add__(self, other):
        if self.__nombre == other.nombre:
            nuevo_stock = self.__stock + other.stock
            return Producto(self.__nombre, self.__precio, nuevo_stock)
        else:
            return self

    def __eq__(self, other):
        return self.__nombre == other.nombre
