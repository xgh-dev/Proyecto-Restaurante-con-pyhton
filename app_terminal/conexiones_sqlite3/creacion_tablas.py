import sqlite3
def crear_tablas_restaurante():
    try:
        # Conexión a la base de datos
        mi_conexcion = sqlite3.connect("database/restaurante")
        
        # Crear un cursor para crear las tablas
        cursor = mi_conexcion.cursor()
        
        # Crear tabla de clientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                clave INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre VARCHAR(255), 
                direccion VARCHAR(255), 
                correo_electronico VARCHAR(255), 
                telefono VARCHAR(255)
            )
        """)
        
        # Crear tabla de menú
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menu (
                clave  INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre VARCHAR(255), 
                precio REAL
            )
        """)
        
        # Crear tabla de pedidos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedido (
                clave INTEGER PRIMARY KEY AUTOINCREMENT, 
                cliente VARCHAR(255), 
                producto VARCHAR(255), 
                precio VARCHAR(255)
            )
        """)
        
        # Confirmar los cambios
        mi_conexcion.commit()
        
    except Exception as ex:
        print(ex)
    
    finally:
        # Cerrar la conexión
        if 'mi_conexcion' in locals():
            mi_conexcion.close()