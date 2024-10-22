from conexiones_sqlite3.creacion_tablas import crear_tablas_restaurante
from clases.clase_clientes import Cliente, actualizarCliente, agregarCliente, eliminarCliente
from clases.clase_menu import Menu, eliminarProducto, actualizarProducto, agregarProducto
from clases.clase_pedido import Pedido, cancelarPedido, crearPedido
from conexiones_sqlite3.conexion_clientes import imprimir_clientes
from conexiones_sqlite3.conexion_menu import imprimir_menu
from conexiones_sqlite3.conexion_pedidos import imprimir_pedidos

class Restaurante():
    def __init__(self):
        self.iniciarPrograma()
    
    def crearDb(self):
        crear_tablas_restaurante()

    def iniciarPrograma(self):
        """
        Método principal que inicia el menú del restaurante.
        """
        self.crearDb()
        print("Bienvenido al restaurante")
        while True:
            print("""
            Navegue seleccionando alguna opción:
                1) Pedidos
                2) Clientes
                3) Menú
                4) Salir
                  """)
            accion = int(input("Qué acción desea realizar: "))
            if accion == 1:
                self.metodoPedidos()
            elif accion == 2:
                self.metodoClientes()
            elif accion == 3:
                self.metodoMenu()
            elif accion == 4:
                print("Adiós")
                break
            else:
                print("Por favor ingrese una opción válida")

    def metodoPedidos(self):
        """
        Método para gestionar los pedidos del restaurante.
        """
        print("Está en el menú de pedidos, qué desea realizar")
        while True:
            listaClientes = [Cliente(dato[0], dato[1], dato[2], dato[3], dato[4]) for dato in imprimir_clientes()]
            listaMenu = [Menu(dato[0], dato[1], dato[2]) for dato in imprimir_menu()]
            listaPedidos = [Pedido(pedido[0], pedido[1], pedido[2], pedido[3]) for pedido in imprimir_pedidos()]
            print("""
                Seleccione:
                    1) Ver pedidos
                    2) Crear pedido
                    3) Eliminar pedido
                    4) Regresar al menú principal
                  """)
            seleccion = int(input("Seleccione un número: "))
            if seleccion == 1:
                for pedido in listaPedidos:
                    print(pedido)
            elif seleccion == 2:
                crearPedido(listaClientes, listaMenu)
            elif seleccion == 3:
                cancelarPedido(listaPedidos)
            elif seleccion == 4:
                break
            else:
                print("Seleccione una opción válida...")

    def metodoClientes(self):
        """
        Método para gestionar los clientes del restaurante.
        """
        print("Esta en el menú de clientes, qué desea realizar")
        while True:
            listaClientes = [Cliente(dato[0], dato[1], dato[2], dato[3], dato[4]) for dato in imprimir_clientes()]
            print("""
                Seleccione:
                    1) Ver la lista de clientes
                    2) Crear un cliente nuevo
                    3) Actualizar cliente
                    4) Borrar cliente
                    5) Regresar al menú principal
                      """)
            seleccion = int(input("Seleccione un número: "))
            if seleccion == 1:
                for cliente in listaClientes:
                    print(cliente)
            elif seleccion == 2:
                print("Ingrese los datos del nuevo cliente")
                agregarCliente()
            elif seleccion == 3:
                actualizarCliente(listaClientes)
            elif seleccion == 4:
                eliminarCliente(listaClientes)
            elif seleccion == 5:
                break
            else:
                print("Seleccione una opción válida...")

    def metodoMenu(self):
        """
        Método para gestionar los platillos del restaurante.
        """    
        print("Está en el menú del restaurante, qué desea realizar: ")
        while True:
            listaMenu = [Menu(dato[0], dato[1], dato[2]) for dato in imprimir_menu()]
            print("""
                Seleccione:
                    1) Ver menú
                    2) Crear platillo en el menú
                    3) Actualizar platillo del menú
                    4) Borrar platillo del menú
                    5) Regresar al menú principal
                      """)
            seleccion_menu = int(input("Seleccione un número: "))
            if seleccion_menu == 1:
                for platillo in listaMenu:
                    print(platillo)
            elif seleccion_menu == 2:
                agregarProducto()
            elif seleccion_menu == 3:
                actualizarProducto(listaMenu)
            elif seleccion_menu == 4:
                eliminarProducto(listaMenu)
            elif seleccion_menu == 5:
                break
            else:
                print("Seleccione una opción válida...")
            
restaurante = Restaurante()
#restaurante.iniciarPrograma()
