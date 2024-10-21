import sqlite3

def crear_menu(nombre,precio):
    """
    Inserta un nuevo platillo en la tabla "menu" de la base de datos.

    Parámetros:
    - nombre (str): El nombre del platillo.
    - precio (float): El precio del platillo.

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite, ubicada en "database/restaurante".

    2. **Cursor:**
       - Se crea un cursor para ejecutar comandos SQL.

    3. **Inserción de datos:**
       - Se ejecuta una sentencia SQL `INSERT INTO menu (nombre, precio)` para agregar un nuevo platillo con su precio.

    4. **Confirmar cambios:**
       - Se llama a `commit()` para guardar el nuevo platillo en la base de datos.

    5. **Excepción:**
       - Si ocurre un error durante el proceso, se captura y se muestra el mensaje de error.

    6. **Cierre de conexión:**
       - Finalmente, la conexión a la base de datos se cierra.
    """
    try:
        conexion_menu = sqlite3.connect("database/restaurante")
        #mediante el cursor agregamos datos
        cursor = conexion_menu.cursor()
        cursor.execute("""
                       INSERT INTO menu (nombre,precio) VALUES (?,?)""",(nombre,precio))
        conexion_menu.commit()
    except Exception as ex:
        print(ex)
    conexion_menu.close()

def imprimir_menu():
    """
    Recupera y devuelve una lista con todos los platillos del menú almacenados en la tabla "menu".

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite.

    2. **Cursor:**
       - Se crea un cursor para ejecutar consultas SQL.

    3. **Consulta de la tabla de menú:**
       - Se ejecuta la sentencia SQL `SELECT * FROM menu` para obtener todos los registros.

    4. **Almacenar los datos:**
       - Los resultados de la consulta se almacenan en la variable `menu`.
       - Cada platillo se agrega a la lista `listaMenu`.

    5. **Devolver la lista:**
       - La función retorna la lista completa de platillos.

    6. **Excepción:**
       - Si ocurre un error durante la ejecución de la consulta, se captura y se muestra el error.

    7. **Cierre de conexión:**
       - Finalmente, la conexión a la base de datos se cierra.

    Returna:
        listaMenu: Una lista de tuplas, donde cada tupla representa un platillo del menú.
    """
    #crear una lista que retornaremos con los datos de la consulta
    listaMenu = []
    try:
        conexion_menu = sqlite3.connect("database/restaurante")
        #creamos el cursor
        cursor = conexion_menu.cursor()
        #creamos el ejecutable de la base de datos 
        cursor.execute("SELECT * FROM menu")
        menu = cursor.fetchall()
        for platillo in menu:
            #print(platillo)
            listaMenu.append(platillo)
        return listaMenu
    except Exception as ex:
        print(ex)
    conexion_menu.close() 

def eliminar_menu(id):
    """
    Elimina un platillo del menú basado en su clave primaria (ID) en la tabla "menu".

    Parámetros:
    - id (int): El identificador único del platillo que se desea eliminar.

    Funcionamiento:
    1. **Conexión a la base de datos:**
       - Se establece una conexión con la base de datos SQLite.

    2. **Cursor:**
       - Se crea un cursor para ejecutar comandos SQL.

    3. **Eliminar el platillo:**
       - Se ejecuta la sentencia SQL `DELETE FROM menu WHERE clave = ?` para eliminar el registro.

    4. **Confirmar cambios:**
       - Se llama a `commit()` para aplicar los cambios en la base de datos.

    5. **Excepción:**
       - Si ocurre algún error, el mensaje de error es capturado y mostrado.

    6. **Cierre de conexión:**
       - Finalmente, la conexión a la base de datos se cierra.
    """
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("DELETE FROM menu where clave = ?",(id,))
        mi_conexion.commit()
    except Exception as ex:
        print(ex)
    mi_conexion.close()

def actualizar_menu_nombre(clave,nombre):
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE menu SET nombre = ? WHERE clave = ?",(nombre,clave))
        mi_conexion.commit()
    except Exception as ex:
        print(ex)
    mi_conexion.close()

def actualizar_menu_precio(clave,precio):
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE menu SET precio = ? WHERE clave = ?",(precio,clave))
        mi_conexion.commit()    
    except Exception as ex: 
        print(ex)
    mi_conexion.close()

