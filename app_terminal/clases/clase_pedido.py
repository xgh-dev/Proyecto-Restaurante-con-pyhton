import os
from conexiones_sqlite3.conexion_pedidos import crear_pedido,cancelar_pedido

class Pedido:
    def __init__(self,pedido,cliente,producto,precio):
        """
        Inicializa un objeto de la clase Pedido.

        Parámetros:
        - pedido (int): El identificador único del pedido.
        - cliente (str): El nombre del cliente que realiza el pedido.
        - producto (str): El nombre del producto pedido.
        - precio (float): El precio del producto.

        Funcionamiento:
        1. Convierte el número de pedido a entero y lo asigna a `self.pedido`.
        2. Convierte el nombre del cliente a cadena y lo asigna a `self.cliente`.
        3. Convierte el nombre del producto a cadena y lo asigna a `self.producto`.
        4. Convierte el precio a float y lo asigna a `self.precio`.
        5. Llama a la función `crear_ticket()` para generar un ticket de pedido automáticamente.
        """
        self.pedido = int(pedido)
        self.cliente = str(cliente)
        self.producto = str(producto)
        self.precio = float(precio)
        self.crear_ticket() #la funcion se llama sin necesidad de pasar argumentos
    def __str__(self):
        """
        Devuelve una representación en forma de cadena del objeto Pedido.

        Returna:
            str: Información detallada del pedido.
        """
        return f"""
              Pedido: {self.pedido}
              Cliente: {self.cliente}
              Producto: {self.producto}
              Precio: {self.precio}              
              """

    def crear_ticket(self):
        """
        Crea un ticket de pedido y lo guarda en un archivo de texto.

        Funcionamiento:
        1. Abre un archivo en modo escritura con el nombre `Pedido_{self.pedido}.txt` en el directorio `tickets_pedidos/`.
        2. Escribe la información del cliente, producto y precio en el archivo.
        """
        with open(f"tickets_pedidos/Pedido_{self.pedido}.txt", "w") as archivo:
            archivo.write(f"""
    Cliente: {self.cliente}
    Producto: {self.producto}
    Precio: {self.precio}
    """)

    def eliminar_ticket(self):
        """
        Elimina el archivo del ticket asociado a este pedido.

        Funcionamiento:
        1. Crea la ruta del archivo del ticket basado en el número de pedido.
        2. Verifica si el archivo existe.
        3. Si existe, lo elimina y muestra un mensaje de éxito; si no, informa que el archivo no existe.
        """
        borrar_archivo_txt = f"tickets_pedidos/Pedido_{self.pedido}.txt"
        if os.path.exists(borrar_archivo_txt):
            os.remove(borrar_archivo_txt)
            print(f"Archivo {borrar_archivo_txt} eliminado")
        else:
            print(f"El archivo {borrar_archivo_txt} no existe")
    def borrarPedido(self):
        """
        Elimina el pedido y su ticket asociado.

        Funcionamiento:
        1. Llama a la función `cancelar_pedido()` para eliminar el pedido de la base de datos (se asume que esta función está definida en otro lugar).
        2. Llama a `eliminar_ticket()` para eliminar el archivo del ticket.
        3. Imprime un mensaje de confirmación.
        """
        try:
            cancelar_pedido(self.pedido)
            self.eliminar_ticket()
            print("Pedido eliminado")
        except Exception as err:
            print(err)
            
def crearPedido(listaClientes, listaMenu):
    """
    Crea un nuevo pedido solicitando datos del cliente y del menú.

    Parámetros:
    - listaClientes (list): Lista de objetos cliente.
    - listaMenu (list): Lista de objetos menú.

    Funcionamiento:
    1. Imprime instrucciones para crear un pedido.
    2. Muestra la lista de clientes disponibles y solicita la selección de un cliente.
    3. Valida la selección del cliente hasta que se ingrese un número válido.
    4. Muestra la lista de platillos del menú y solicita la selección de un platillo.
    5. Valida la selección del platillo hasta que se ingrese un número válido.
    6. Llama a la función `crear_pedido()` con los datos del cliente y del platillo seleccionados.
    7. Imprime un mensaje de confirmación de que el pedido ha sido creado.
    """
    print("Para crear un nuevo pedido ingrese los datos del cliente y del platillo del menu")
    cantidad_clientes = []
    cantidad_platillos = []

    #Listar clientes
    for i in range(len(listaClientes)):
        cantidad_clientes.append(i + 1)
        print(f"{i + 1}.-{listaClientes[i]}")
    #Seleccionar cliente
    seleccionCliente = 0
    while seleccionCliente not in cantidad_clientes:
        seleccionCliente = int(input("Indique el cliente que realiza el pedido: "))
    clienteSeleccionado = listaClientes[seleccionCliente - 1]
    #Listar platillos
    for j in range(len(listaMenu)):
        cantidad_platillos.append(j + 1)
        print(f"{j + 1}.-{listaMenu[j]}")
    #Seleccionar platillo
    seleccionPlatillo = 0
    while seleccionPlatillo not in cantidad_platillos:
        seleccionPlatillo = int(input("Indique el platillo seleccionado: "))
    platilloSeleccionado = listaMenu[seleccionPlatillo - 1]
    #Crear pedido
    crear_pedido(clienteSeleccionado.retornarNombreCliente(), platilloSeleccionado.retornarNombrePlatillo(), platilloSeleccionado.retornarPrecioPlatillo())
    print("Pedido creado")

def cancelarPedido(listaPedidos):
    """
    Cancela un pedido existente basado en la selección del usuario.

    Parámetros:
    - listaPedidos (list): Lista de objetos pedido.

    Funcionamiento:
    1. Muestra la lista de pedidos existentes.
    2. Solicita al usuario que seleccione un pedido a cancelar.
    3. Cancela el pedido seleccionado llamando al método `borrarPedido()` del objeto pedido.
    """
    for i in range(len(listaPedidos)):
        print(f"-------- Indique el siguiente número la terminar para cancelar el pedido deseado:{i + 1} --------{listaPedidos[i]}")
    seleccion = int(input("Seleccione el número del pedido que desea cancelar: "))
    pedidoSeleccionado = listaPedidos[seleccion - 1]
    #Cancelar el pedido
    pedidoSeleccionado.borrarPedido()

