from flask import Flask,render_template
import sqlite3
import os
#from conexiones import imprimir_pedidos,cancelar_pedido,seleccionar_pedido

from flask import Flask, render_template
import sqlite3
import os

def imprimir_pedidos():
    """
    Obtiene la lista de todos los pedidos almacenados en la base de datos.

    Realiza una consulta SQL para seleccionar todos los pedidos en la tabla 'pedido'
    y devuelve una lista de estos pedidos.

    Retorna:
    - listaPedidos (list): Lista de todos los pedidos.
    """
    listaPedidos = []
    try:
        conexion = sqlite3.connect("D:/python_avanzado_proyecto/database/restaurante")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pedido")
        pedidos = cursor.fetchall()
        for pedido in pedidos:
            listaPedidos.append(pedido)
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()
    return listaPedidos

def seleccionar_pedido(clave):
    """
    Selecciona un pedido específico basado en su clave.

    Realiza una consulta SQL para seleccionar el pedido que coincide con la clave proporcionada.

    Parámetros:
    - clave (int): La clave (ID) del pedido a seleccionar.

    Retorna:
    - pedidoSeleccionado (tuple): Datos del pedido seleccionado.
    """
    pedidoSeleccionado = []
    try:
        conexion = sqlite3.connect("D:/python_avanzado_proyecto/database/restaurante")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM pedido WHERE clave = ?", (clave,))
        pedidos = cursor.fetchone()
        pedidoSeleccionado = pedidos
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()
    return pedidoSeleccionado

def cancelar_pedido(clave):
    """
    Elimina un pedido de la base de datos basado en su clave.

    Realiza una consulta SQL DELETE para eliminar el pedido que coincide con la clave proporcionada.

    Parámetros:
    - clave (int): La clave (ID) del pedido a eliminar.
    """
    try:
        conexion = sqlite3.connect("D:/python_avanzado_proyecto/database/restaurante")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM pedido WHERE clave = ?", (clave,))
        conexion.commit()  # Aplicamos los cambios a la base de datos
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()

def eliminar_ticket(idpedido):
    """
    Elimina el archivo de texto asociado a un pedido específico.

    Elimina el archivo que contiene el ticket del pedido si existe en la carpeta 'tickets_pedidos'.

    Parámetros:
    - idpedido (int): El ID del pedido cuyo archivo se va a eliminar.
    """
    borrar_archivo_txt = f"tickets_pedidos/Pedido_{idpedido}.txt"
    if os.path.exists(borrar_archivo_txt):
        os.remove(borrar_archivo_txt)
        print(f"Archivo {borrar_archivo_txt} eliminado")
    else:
        print(f"El archivo {borrar_archivo_txt} no existe")

#creamos la llamda a flask
app = Flask(__name__)

@app.route('/')  #Ruta principal para mostrar todos los pedidos
def pedidos():
    """
    Renderiza la página principal que muestra la lista de pedidos.

    Obtiene la lista de pedidos de la base de datos y la pasa al template 'pedidos.html'.
    """
    listaPedidos = imprimir_pedidos()
    return render_template("pedidos.html", pedidos=listaPedidos)

@app.route('/pedido_info/<int:idPedido>')  #Ruta para ver la información de un pedido específico
def pedido_info(idPedido):
    """
    Muestra la información detallada de un pedido.

    Parámetros:
    - idPedido (int): El ID del pedido a mostrar.

    Retorna:
    - Renderiza el template 'pedido_info.html' con la información del pedido seleccionado.
    """
    pedido = list(seleccionar_pedido(idPedido))
    return render_template('pedido_info.html', pedidoInfo=pedido)

@app.route('/pedidos/<int:idPedido>')  #Ruta para eliminar un pedido
def pedido_eliminar(idPedido):
    """
    Elimina un pedido y su ticket asociado, luego actualiza la lista de pedidos.

    Parámetros:
    - idPedido (int): El ID del pedido a eliminar.

    Retorna:
    - Renderiza el template 'pedidos.html' con la lista actualizada de pedidos.
    """
    cancelar_pedido(idPedido)
    eliminar_ticket(idPedido)
    listaPedidos = imprimir_pedidos()
    return render_template('pedidos.html', pedidos=listaPedidos)

if __name__=="__main__":
    app.run(debug=True)
#debug=True con esto activamos el modo de depuracion para realizar cambios cuando el servidor este corriendo
#port = numeroDePuerto con esto indicamos el puerto en el cual querramos que se ejecute la app
