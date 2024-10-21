import sqlite3

def crear_clientes(nombre,direccion,correo_electronico,telefono):
    """
    Inserta un nuevo cliente en la tabla 'cliente' de la base de datos.

    Parámetros:
    - nombre (str): El nombre del cliente.
    - direccion (str): La dirección del cliente.
    - correo_electronico (str): El correo electrónico del cliente.
    - telefono (str): El número de teléfono del cliente.

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite en "database/restaurante".

    2. **Cursor:**
       - Se crea un cursor para ejecutar comandos SQL.

    3. **Inserción de datos:**
       - Se ejecuta una sentencia SQL `INSERT INTO cliente (nombre, direccion, correo_electronico, telefono)` para agregar un nuevo cliente con su información.

    4. **Confirmar cambios:**
       - Se llama a `commit()` para guardar el nuevo registro en la base de datos.

    5. **Excepción:**
       - Si ocurre un error, se captura y muestra el mensaje del error.

    6. **Cierre de conexión:**
       - Finalmente, se cierra la conexión a la base de datos.
    """
    try:
        #Crear la conexion
        mi_conexion = sqlite3.connect("database/restaurante")
        #Crear un cursor para poder agregar datos
        cursor = mi_conexion.cursor()
        cursor.execute("""
            INSERT INTO cliente (nombre, direccion, correo_electronico, telefono) VALUES (?, ?, ?, ?)""", (nombre, direccion, correo_electronico, telefono))
        #Posteriormente debemos confirmar los cambios mediante
        mi_conexion.commit()
    except Exception as ex:
        print(ex)
    mi_conexion.close()

def imprimir_clientes():
    """
    Recupera y devuelve una lista de todos los clientes almacenados en la tabla 'cliente'.

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite.

    2. **Cursor:**
       - Se crea un cursor para ejecutar comandos SQL.

    3. **Consulta de la tabla de clientes:**
       - Se ejecuta la sentencia SQL `SELECT * FROM cliente` para obtener todos los registros.

    4. **Almacenar los datos:**
       - Los resultados de la consulta se almacenan en la variable `clientes`.
       - Cada cliente se agrega a la lista `listaDeClientes`.

    5. **Devolver la lista:**
       - La función retorna la lista completa de clientes.

    6. **Excepción:**
       - Si ocurre un error durante la ejecución, el mensaje se captura y muestra.

    7. **Cierre de conexión:**
       - Finalmente, la conexión a la base de datos se cierra.

    Returna:
        listDeClientes: Una lista de tuplas, donde cada tupla representa un cliente.
    """
    listaDeClientes = []
    try:
        #Crear la conexión a la base de datos
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        #Ejecutar la consulta para obtener los datos
        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall() #Obtener todos los registros
        #Imprimir los datos de cada cliente
        for cliente in clientes:
            #Cuando usas cursor.fetchall() en SQLite, lo que obtienes es una lista de tuplas (cada tupla representa una fila de la tabla). Por lo tanto, para acceder a los datos, deberías usar índices numéricos en lugar de nombres de clave.
            #Supongamos que cada tupla en pedidos tiene esta estructura:
            #pedido[0]: número del pedido
            #pedido[1]: nombre del cliente
            #print(f"""
            #    Clave: {cliente[0]} 
            #    Nombre: {cliente[1]} 
            #    Dirección: {cliente[2]} 
            #    Correo: {cliente[3]}, 
            #    Teléfono: {cliente[4]}""")
            listaDeClientes.append(cliente)
        return listaDeClientes
    except Exception as ex:
        print(ex)
    mi_conexion.close()

def eliminar_cliente_id(id):
    """
    Elimina un cliente de la tabla 'cliente' basado en su clave primaria (ID).

    Parámetros:
    - id (int): El identificador único del cliente que se desea eliminar.

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite.

    2. **Cursor:**
       - Se crea un cursor para ejecutar comandos SQL.

    3. **Eliminar cliente:**
       - Se ejecuta la sentencia SQL `DELETE FROM cliente WHERE clave = ?` para eliminar el registro del cliente.

    4. **Confirmar cambios:**
       - Se llama a `commit()` para aplicar los cambios en la base de datos.

    5. **Excepción:**
       - Si ocurre un error, se captura y muestra el mensaje.

    6. **Cierre de conexión:**
       - Finalmente, se cierra la conexión a la base de datos.
    """
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("DELETE FROM cliente where clave = ?",(id,))
        mi_conexion.commit() #con esto guardamos el cambio en la base de datos
    except Exception as ex:
        print(ex)
    mi_conexion.close()

def actualizar_cliente_nombre(clave,nombre):
    """
    Actualiza el nombre de un cliente en la tabla 'cliente' basado en su clave primaria (ID).

    Parámetros:
    - clave (int): El identificador único del cliente.
    - nombre (str): El nuevo nombre del cliente.

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite.

    2. **Cursor:**
       - Se crea un cursor para ejecutar comandos SQL.

    3. **Actualizar nombre:**
       - Se ejecuta la sentencia SQL `UPDATE cliente SET nombre = ? WHERE clave = ?` para actualizar el nombre del cliente.

    4. **Confirmar cambios:**
       - Se llama a `commit()` para aplicar los cambios.

    5. **Excepción:**
       - Si ocurre un error, se captura y muestra el mensaje.

    6. **Cierre de conexión:**
       - Finalmente, se cierra la conexión a la base de datos.
    """
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE cliente SET nombre = ? WHERE clave = ?",(nombre,clave))
        mi_conexion.commit() 
    except Exception as ex:
        print(ex)

def actualizar_cliente_direccion(clave,direccion):
    """
    Actualiza la dirección de un cliente en la tabla 'cliente' basado en su clave primaria (ID).

    Parámetros:
    - clave (int): El identificador único del cliente.
    - direccion (str): La nueva dirección del cliente.

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite.

    2. **Cursor:**
       - Se crea un cursor para ejecutar comandos SQL.

    3. **Actualizar dirección:**
       - Se ejecuta la sentencia SQL `UPDATE cliente SET direccion = ? WHERE clave = ?` para modificar la dirección del cliente.

    4. **Confirmar cambios:**
       - Se llama a `commit()` para aplicar los cambios.

    5. **Excepción:**
       - Si ocurre un error, se captura y muestra el mensaje.

    6. **Cierre de conexión:**
       - Finalmente, se cierra la conexión a la base de datos.
    """
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE cliente SET direccion = ? WHERE clave = ?",(direccion,clave))
        mi_conexion.commit() 
    except Exception as ex:
        print(ex)

def actualizar_cliente_correo(clave,correo_electronico):
    """
    Actualiza el correo electrónico de un cliente en la tabla 'cliente' basado en su clave primaria (ID).

    Parámetros:
    - clave (int): El identificador único del cliente.
    - correo_electronico (str): El nuevo correo electrónico del cliente.

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite.

    2. **Cursor:**
       - Se crea un cursor para ejecutar comandos SQL.

    3. **Actualizar correo:**
       - Se ejecuta la sentencia SQL `UPDATE cliente SET correo_electronico = ? WHERE clave = ?` para actualizar el correo del cliente.

    4. **Confirmar cambios:**
       - Se llama a `commit()` para aplicar los cambios.

    5. **Excepción:**
       - Si ocurre un error, se captura y muestra el mensaje.

    6. **Cierre de conexión:**
       - Finalmente, se cierra la conexión a la base de datos.
    """
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE cliente SET correo_electronico = ? WHERE clave = ?",(correo_electronico,clave))
        mi_conexion.commit() 
    except Exception as ex:
        print(ex)

def actualizar_cliente_telefono(clave,telefono):
    """
    Actualiza el número de teléfono de un cliente en la tabla 'cliente' basado en su clave primaria (ID).

    Parámetros:
    - clave (int): El identificador único del cliente.
    - telefono (str): El nuevo número de teléfono del cliente.

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite.

    2. **Cursor:**
       - Se crea un cursor para ejecutar comandos SQL.

    3. **Actualizar teléfono:**
       - Se ejecuta la sentencia SQL `UPDATE cliente SET telefono = ? WHERE clave = ?` para modificar el número de teléfono del cliente.

    4. **Confirmar cambios:**
       - Se llama a `commit()` para aplicar los cambios.

    5. **Excepción:**
       - Si ocurre un error, se captura y muestra el mensaje.

    6. **Cierre de conexión:**
       - Finalmente, se cierra la conexión a la base de datos.

    """
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE cliente SET telefono = ? WHERE clave = ?",(telefono,clave))
        mi_conexion.commit() 
    except Exception as ex:
        print(ex)
