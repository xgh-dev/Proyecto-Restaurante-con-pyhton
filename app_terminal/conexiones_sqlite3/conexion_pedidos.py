import sqlite3

def crear_pedido(cliente,producto,precio):
    try:
        conexion = sqlite3.connect("database/restaurante")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO pedido (cliente,producto,precio) VALUES (?,?,?)",(cliente,producto,precio))
        conexion.commit()
    except Exception as ex:
        print(ex)
    conexion.close()
def imprimir_pedidos():
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
    try:
        conexion = sqlite3.connect("database/restaurante")
        cursor = conexion.cursor()
        cursor.execute("DELETE from pedido WHERE clave = ?",(clave,)) 
        #cursor.execute("UPDATE pedido SET pedido = pedido - 1 WHERE pedido > ?", (id_pedido,))
        conexion.commit()
    except Exception as ex:
        print(ex)
    conexion.close()
