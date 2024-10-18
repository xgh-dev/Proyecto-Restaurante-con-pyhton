from flask import Flask,render_template
import sqlite3
import os
#from conexiones import imprimir_pedidos,cancelar_pedido,seleccionar_pedido

def imprimir_pedidos():
    listaPedidos = []
    try:
        conexion = sqlite3.connect("D:/python_avanzado_proyecto/database/restaurante")
        cursor  = conexion.cursor()
        cursor.execute("SELECT * FROM pedido")
        pedidos = cursor.fetchall()
        for pedido in pedidos:
            listaPedidos.append(pedido)
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()
    return listaPedidos  #no cerramos la conexión aquí

def seleccionar_pedido(clave):
    pedidoSeleccionado = []
    try:
        conexion = sqlite3.connect("D:/python_avanzado_proyecto/database/restaurante")
        cursor  = conexion.cursor()
        cursor.execute("SELECT * FROM pedido WHERE clave = ?", (clave,))
        pedidos = cursor.fetchone()
        pedidoSeleccionado = pedidos
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()
    return pedidoSeleccionado  #no cerramos la conexión aquí

def cancelar_pedido(clave):
    try:
        conexion = sqlite3.connect("D:/python_avanzado_proyecto/database/restaurante")
        cursor  = conexion.cursor()
        cursor.execute("DELETE FROM pedido WHERE clave = ?", (clave,))
        conexion.commit()  #aplicamos los cambios a la base de datos
    except Exception as ex:
        print(ex)
        # No cerramos la conexión aquí
    finally:
        conexion.close()

def eliminar_ticket(idpedido):
        borrar_archivo_txt = f"tickets_pedidos/Pedido_{idpedido}.txt"
        if os.path.exists(borrar_archivo_txt):
            os.remove(borrar_archivo_txt)
            print(f"Archivo {borrar_archivo_txt} eliminado")
        else:
            print(f"El archivo {borrar_archivo_txt} no existe")

app = Flask(__name__)#le pasamos un name para poder realizar una comprobacion para verificar la ruta donde trabajemos
 
@app.route('/')#pasamos un parametro a la url
def pedidos():
    listaPedidos = imprimir_pedidos()
    return render_template("pedidos.html",pedidos=listaPedidos)

@app.route('/pedidos/pedido_info/<int:idPedido>')
def pedido_info(idPedido):
    #realizar una consulta que reciba el id pasado y mediante eso extraiga esos datos de la base de datos
    pedido = list(seleccionar_pedido(idPedido))
    return render_template('pedido_info.html',pedidoInfo=pedido)

@app.route('/pedidos/<int:idPedido>')
def pedido_eliminar(idPedido):
    #ejecutar la función que elimina el pedido
    cancelar_pedido(idPedido)
    eliminar_ticket(idPedido)
    #obtener la lista actualizada de pedidos
    listaPedidos = imprimir_pedidos()
    #renderizar la plantilla 'pedidos.html' con la lista actualizada
    return render_template('pedidos.html', pedidos=listaPedidos)


if __name__=="__main__":
    app.run(debug=True)
#debug=True con esto activamos el modo de depuracion para realizar cambios cuando el servidor este corriendo
#port = numeroDePuerto con esto indicamos el puerto en el cual querramos que se ejecute la app
