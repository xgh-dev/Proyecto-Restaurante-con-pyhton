import os
from conexiones_sqlite3.conexion_pedidos import crear_pedido,cancelar_pedido

class Pedido:
    def __init__(self,pedido,cliente,producto,precio):
        self.pedido = int(pedido)
        self.cliente = str(cliente)
        self.producto = str(producto)
        self.precio = float(precio)
        self.crear_ticket() #la funcion se llama sin necesidad de pasar argumentos
    def __str__(self):
        return f"""
              Pedido: {self.pedido}
              Cliente: {self.cliente}
              Producto: {self.producto}
              Precio: {self.precio}              
              """
    def crear_ticket(self):
        with open(f"tickets_pedidos/Pedido_{self.pedido}.txt", "w") as archivo:
            archivo.write(f"""
    Cliente: {self.cliente}
    Producto: {self.producto}
    Precio: {self.precio}
    """)
    def eliminar_ticket(self):
        borrar_archivo_txt = f"tickets_pedidos/Pedido_{self.pedido}.txt"
        if os.path.exists(borrar_archivo_txt):
            os.remove(borrar_archivo_txt)
            print(f"Archivo {borrar_archivo_txt} eliminado")
        else:
            print(f"El archivo {borrar_archivo_txt} no existe")
    def borrarPedido(self):
        try:
            cancelar_pedido(self.pedido)
            self.eliminar_ticket()
            print("Pedido eliminado")
        except Exception as err:
            print(err)
def crearPedido(listaClientes,listaMenu):
    print("Para crear un nuevo pedido ingrese los datos del cliente y del platillo del menu")
    cantidad_clientes = []
    cantidad_platillos = []
    for i in range(len(listaClientes)):
        cantidad_clientes.append(i+1)
        print(f"{i+1}.-{listaClientes[i]}")
    seleccionCliente = 0
    while seleccionCliente not in cantidad_clientes:
        seleccionCliente = int(input("Indique el cliente que realiza el pedido: "))
        #clienteSeleccionado = listaClientes[int(input("Ingrese el número del ciente seleccionado: "))-1]
    clienteSeleccionado = listaClientes[seleccionCliente-1]
    for j in range(len(listaMenu)):
        cantidad_platillos.append(j+1)
        print(f"{j+1}.-{listaMenu[j]}")
    seleccionPlatillo = 0
    while seleccionPlatillo not in cantidad_platillos:
        seleccionPlatillo = int(input("Indique el platillo seleccionado: "))       
    platilloSeleccionado = listaMenu[seleccionPlatillo-1]
    crear_pedido(clienteSeleccionado.retornarNombreCliente(),platilloSeleccionado.retornarNombrePlatillo(),platilloSeleccionado.retornarPrecioPlatillo())
    print("Pedido creado")
def cancelarPedido(listaPedidos):
    for i in range(len(listaPedidos)):
        print(f"{i+1}.-{listaPedidos[i]}")
    seleccion = int(input("Seleccione el número del pedido que desea cancelar: "))
    pedidoSeleccionado = listaPedidos[seleccion-1]
    
    pedidoSeleccionado.borrarPedido()

        