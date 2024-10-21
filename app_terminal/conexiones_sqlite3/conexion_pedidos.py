import sqlite3

def crear_pedido(cliente,producto,precio):
    """
    Inserta un nuevo pedido en la tabla "pedido" de la base de datos.

    Parámetros:
    - cliente (str): El nombre del cliente que realiza el pedido.
    - producto (str): El nombre del producto que el cliente está solicitando.
    - precio (str): El precio del producto (almacenado como una cadena de caracteres).

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite, que se encuentra en la ruta "database/restaurante".

    2. **Cursor:**
       - Se crea un cursor para ejecutar comandos SQL en la base de datos.

    3. **Inserción de datos:**
       - La sentencia SQL `INSERT INTO pedido (cliente,producto,precio)` agrega un nuevo registro en la tabla `pedido`.
       - Los valores de cliente, producto y precio se insertan en las columnas correspondientes.

    4. **Confirmar cambios:**
       - Se llama a `commit()` para confirmar y guardar el nuevo pedido en la base de datos.

    5. **Excepción:**
       - Si ocurre un error durante el proceso, se captura y se imprime el mensaje de error.

    6. **Cierre de conexión:**
       - Finalmente, la conexión a la base de datos se cierra con `conexion.close()` para liberar recursos.
    """
    try:
        conexion = sqlite3.connect("database/restaurante")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO pedido (cliente,producto,precio) VALUES (?,?,?)",(cliente,producto,precio))
        conexion.commit()
    except Exception as ex:
        print(ex)
    conexion.close()

def imprimir_pedidos():
    """
    Recupera y devuelve una lista de todos los pedidos almacenados en la tabla "pedido".

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite.

    2. **Cursor:**
       - Se crea un cursor para ejecutar consultas SQL en la base de datos.

    3. **Consulta de la tabla de pedidos:**
       - La sentencia SQL `SELECT * FROM pedido` recupera todos los registros de la tabla `pedido`.

    4. **Almacenar pedidos:**
       - Los resultados de la consulta se almacenan en la variable `pedidos`.
       - Cada pedido se agrega a la lista `listaPedidos`.

    5. **Devolver la lista de pedidos:**
       - La función retorna la lista completa de pedidos almacenados.

    6. **Excepción:**
       - Si ocurre un error durante la ejecución de la consulta, el mensaje de error es capturado y mostrado.

    7. **Cierre de conexión:**
       - Finalmente, la conexión a la base de datos se cierra.

    Returna:
        listaPedidos: Una lista de tuplas, donde cada tupla representa un pedido.
    """
    listaPedidos=[]
    try:
        conexion = sqlite3.connect("database/restaurante")
        cursor = conexion.cursor()
        cursor.execute("SELECT * from pedido")
        pedidos = cursor.fetchall()
        for pedido in pedidos:
            listaPedidos.append(pedido)
        return listaPedidos
    except Exception as ex:
        print(ex)
    conexion.close()

def cancelar_pedido(clave):
    """
    Elimina un pedido específico de la tabla "pedido" basado en la clave primaria (ID) del pedido.

    Parámetros:
    - clave (int): El identificador único (clave) del pedido que se desea eliminar.

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite.

    2. **Cursor:**
       - Se crea un cursor para ejecutar comandos SQL.

    3. **Eliminar el pedido:**
       - La sentencia SQL `DELETE FROM pedido WHERE clave = ?` elimina el registro correspondiente a la clave proporcionada.

    4. **Confirmar cambios:**
       - Se llama a `commit()` para confirmar y aplicar los cambios en la base de datos.

    5. **Excepción:**
       - Si ocurre algún error durante el proceso, el mensaje de error es capturado y mostrado.

    6. **Cierre de conexión:**
       - Finalmente, se cierra la conexión a la base de datos.
    """
    try:
        conexion = sqlite3.connect("database/restaurante")
        cursor = conexion.cursor()
        cursor.execute("DELETE from pedido WHERE clave = ?",(clave,)) 
        #cursor.execute("UPDATE pedido SET pedido = pedido - 1 WHERE pedido > ?", (id_pedido,))
        conexion.commit()
    except Exception as ex:
        print(ex)
    conexion.close()
