# desafio_evaluado_2_M4

# Sistema de Gestión de Tiendas

Este proyecto implementa un sistema de gestión de tiendas que permite crear diferentes tipos de tiendas (`Restaurante`, `Supermercado`, `Farmacia`), ingresar productos, listar productos y realizar ventas. El sistema está diseñado en Python utilizando el paradigma de programación orientada a objetos (OOP).

## Descripción

El proyecto está dividido en tres partes principales:

1. **Clase Producto:** Representa los productos que pueden ser vendidos en las tiendas.
2. **Clases de Tienda:** Define las diferentes tiendas (`Restaurante`, `Supermercado`, `Farmacia`) y su comportamiento específico.
3. **Programa Principal:** Interactúa con el usuario para gestionar las tiendas, permitiendo ingresar productos, listar productos y realizar ventas.

Cada tipo de tienda tiene características específicas, como la forma en que manejan el stock y las restricciones en la venta de productos.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos:

1. **producto.py:** Contiene la clase `Producto`, que encapsula las propiedades y comportamientos de un producto.
2. **tienda.py:** Define la clase base `Tienda` y las subclases `Restaurante`, `Supermercado`, `Farmacia`, cada una con sus particularidades.
3. **programa.py:** El archivo principal que ejecuta el programa y maneja la interacción con el usuario.

## Funcionalidades Principales

- **Crear Tiendas:** El usuario puede crear tiendas de tipo `Restaurante`, `Supermercado` o `Farmacia`.
- **Ingresar Productos:** Permite al usuario ingresar productos en la tienda seleccionada.
- **Listar Productos:** Muestra los productos disponibles en la tienda, con información específica según el tipo de tienda.
- **Realizar Ventas:** Permite al usuario vender productos, ajustando el stock disponible según las reglas del tipo de tienda.
- **Salir del Programa:** Finaliza la ejecución del programa.

## Instrucciones de Uso

Para utilizar el sistema de gestión de tiendas, sigue los siguientes pasos:

1. Clona el repositorio en tu máquina local.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. Navega al directorio del proyecto.

## Ejecución del Programa

Para ejecutar el programa, usa el siguiente comando en tu terminal:

```bash
python programa.py
