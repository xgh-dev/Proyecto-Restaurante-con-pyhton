import sqlite3
def crear_clientes(nombre,direccion,correo_electronico,telefono):
    try:
        # Crear la conexion
        mi_conexion = sqlite3.connect("database/restaurante")
        # Crear un cursor para poder agregar datos
        cursor = mi_conexion.cursor()
        cursor.execute("""
            INSERT INTO cliente (nombre, direccion, correo_electronico, telefono) VALUES (?, ?, ?, ?)""", (nombre, direccion, correo_electronico, telefono))
        # Posteriormente debemos confirmar los cambios mediante
        mi_conexion.commit()

    except Exception as ex:
        print(ex)
    mi_conexion.close()
def imprimir_clientes():
    listaDeClientes = []
    try:
        # Crear la conexión a la base de datos
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()

        # Ejecutar la consulta para obtener los datos
        cursor.execute("SELECT * FROM cliente")
        clientes = cursor.fetchall()  # Obtener todos los registros

        # Imprimir los datos de cada cliente
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
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("DELETE FROM cliente where clave = ?",(id,))
        mi_conexion.commit() #con esto guardamos el cambio en la base de datos
    except Exception as ex:
        print(ex)
    mi_conexion.close()
def actualizar_cliente_nombre(clave,nombre):
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE cliente SET nombre = ? WHERE clave = ?",(nombre,clave))
        mi_conexion.commit() 
    except Exception as ex:
        print(ex)
def actualizar_cliente_direccion(clave,direccion):
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE cliente SET direccion = ? WHERE clave = ?",(direccion,clave))
        mi_conexion.commit() 
    except Exception as ex:
        print(ex)
def actualizar_cliente_correo(clave,correo_electronico):
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE cliente SET correo_electronico = ? WHERE clave = ?",(correo_electronico,clave))
        mi_conexion.commit() 
    except Exception as ex:
        print(ex)
def actualizar_cliente_telefono(clave,telefono):
    try:
        mi_conexion = sqlite3.connect("database/restaurante")
        cursor = mi_conexion.cursor()
        cursor.execute("UPDATE cliente SET telefono = ? WHERE clave = ?",(telefono,clave))
        mi_conexion.commit() 
    except Exception as ex:
        print(ex)
