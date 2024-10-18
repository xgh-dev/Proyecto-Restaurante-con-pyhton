import sqlite3
def crear_menu(nombre,precio):
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
def seleccionar_menu():
    pass
def eliminar_menu(id):
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

