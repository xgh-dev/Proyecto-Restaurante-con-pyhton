import sqlite3

def crear_tablas_restaurante():
    """
    Esta función se encarga de crear las tablas necesarias para una base de datos de restaurante,
    utilizando la biblioteca `sqlite3`. Estas tablas incluyen "cliente", "menu" y "pedido", las 
    cuales almacenarán información relacionada con los clientes, los productos del menú y los pedidos.

    Estructura de la función:

    1. **Conexión a la base de datos:**
       Se establece una conexión con una base de datos SQLite, ubicada en la ruta "database/restaurante".
       Si la base de datos no existe, SQLite la creará automáticamente.

    2. **Cursor:**
       Se crea un cursor, que es un objeto que permite ejecutar comandos SQL dentro de la conexión establecida.

    3. **Crear tabla de clientes (`cliente`):**
       - Esta tabla almacena la información de los clientes del restaurante.
       - Columnas:
         - `clave`: un entero que sirve como clave primaria autoincremental.
         - `nombre`: el nombre del cliente.
         - `direccion`: la dirección del cliente.
         - `correo_electronico`: el correo electrónico del cliente.
         - `telefono`: el número telefónico del cliente.

    4. **Crear tabla de menú (`menu`):**
       - Esta tabla almacena la información de los productos del menú.
       - Columnas:
         - `clave`: un entero que sirve como clave primaria autoincremental.
         - `nombre`: el nombre del producto del menú.
         - `precio`: el precio del producto (un valor de tipo `REAL`).

    5. **Crear tabla de pedidos (`pedido`):**
       - Esta tabla almacena los pedidos realizados por los clientes.
       - Columnas:
         - `clave`: un entero que sirve como clave primaria autoincremental.
         - `cliente`: el nombre del cliente que hizo el pedido.
         - `producto`: el nombre del producto solicitado.
         - `precio`: el precio del producto (almacenado como `VARCHAR` en lugar de `REAL`).

    6. **Confirmar los cambios:**
       Todos los cambios realizados (creación de tablas) se confirman con el comando `commit()`, que guarda permanentemente las modificaciones en la base de datos.

    7. **Excepción y cierre:**
       Si ocurre algún error durante el proceso, se captura y se imprime el mensaje de excepción.
       Finalmente, la conexión a la base de datos se cierra con `mi_conexcion.close()` para liberar los recursos.
    """
    try:
        #Conexión a la base de datos
        mi_conexcion = sqlite3.connect("database/restaurante")
        #Crear un cursor para crear las tablas
        cursor = mi_conexcion.cursor()
        #Crear tabla de clientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                clave INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre VARCHAR(255), 
                direccion VARCHAR(255), 
                correo_electronico VARCHAR(255), 
                telefono VARCHAR(255)
            )
        """)
        #Crear tabla de menú
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menu (
                clave  INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre VARCHAR(255), 
                precio REAL
            )
        """)
        #Crear tabla de pedidos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedido (
                clave INTEGER PRIMARY KEY AUTOINCREMENT, 
                cliente VARCHAR(255), 
                producto VARCHAR(255), 
                precio VARCHAR(255)
            )
        """)
        #Confirmar los cambios
        mi_conexcion.commit()
    except Exception as ex:
        print(ex)
    mi_conexcion.close()