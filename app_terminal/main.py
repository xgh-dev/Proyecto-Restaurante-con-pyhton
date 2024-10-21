#para ejecutar el programa en la consola poner: python C:\Users\xgh27\OneDrive\Escritorio\proyecto_final_py\src\nombre del archivo.py para que esto funcione debemos estar dentro de la carpeta src
#para activar el entorno virtual desde la consola de power shell .\env\Scripts\Activate
from conexiones_sqlite3.creacion_tablas import crear_tablas_restaurante
from clases.clase_clientes import Cliente,actualizarCliente,agregarCliente,eliminarCliente
from clases.clase_menu import Menu,eliminarProducto,actualizarProducto,agregarProducto
from clases.clase_pedido import Pedido,cancelarPedido,crearPedido
from conexiones_sqlite3.conexion_clientes import imprimir_clientes
from conexiones_sqlite3.conexion_menu import imprimir_menu
from conexiones_sqlite3.conexion_pedidos import imprimir_pedidos

def restaurante():
    """
    Función principal que ejecuta el menú del restaurante. Permite al usuario gestionar pedidos, clientes y el menú.
    Se encarga de crear las tablas necesarias y manejar la interacción con el usuario a través de un bucle.
    """
    crear_tablas_restaurante()
    print("Bienvenido al restaurante")
    while True:
        #listaMenu = [Menu(dato[0],dato[1],dato[0]) for dato in imprimir_menu()]
        print("""
        Navegue seleccionando alguna opcion:
            1) Pedidos
            2) Clientes
            3) Menú
            4) Salir
              """)
        #para que el print no se muestre en cada ejecucion del wile podemos sacarlo del bucle
        accion = int(input("que accion desea realizar: "))
        if (accion == 1):
            print("Esta en el menu de pedidos, que desea realizar")
            while True:
                listaClientes = [Cliente(dato[0],dato[1],dato[2],dato[3],dato[4]) for dato in imprimir_clientes()]
                listaMenu = [Menu(dato[0],dato[1],dato[2]) for dato in imprimir_menu()]
                listaPedidos = [Pedido(pedido[0],pedido[1],pedido[2],pedido[3]) for pedido in imprimir_pedidos()]
                print("""
                    Seleccione:
                        1) Ver pedidos
                        2) Crear pedido
                        3) Eliminar pedido
                        4) Regresar al menu principal
                      """)
                seleccion = int(input("Seleccione un número: "))
                if seleccion == 1:
                    for pedido in listaPedidos:
                        print(pedido)
                elif seleccion == 2:
                    crearPedido(listaClientes,listaMenu)
                elif seleccion == 3:
                    cancelarPedido(listaPedidos)
                elif seleccion == 4:
                    break
                else:
                    print("Seleccione una opción valida")
        elif (accion == 2):
            print("Esta en el menu de clientes, que desea realizar")
            while True:
                #metemos al bucle while una llamada a la lista de clientes para que en cada ejecucion del bucle se actualice la lista de clientes
                listaClientes = [Cliente(dato[0],dato[1],dato[2],dato[3],dato[4]) for dato in imprimir_clientes()]
                print("""
                    Selecione:
                      1) Ver la lista de clientes
                      2) Crear un cliente nuevo
                      3) Actualizar cliente
                      4) Borrar cliente
                      5) Regresar al menu principal
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
                    print("Borrar un cliente")
                    eliminarCliente(listaClientes)
                elif seleccion == 5:
                    break
                else:
                    print("Seleccione una opción valida.")
        elif (accion == 3):
            print("Esta en el menu del restaurante, que desea realizar: ")
            while True:
                listaMenu = [Menu(dato[0],dato[1],dato[2]) for dato in imprimir_menu()]
                print("""
                    Seleccione:
                    1) Ver menu
                    2) Crear menu
                    3) Actualizar platillo del menu
                    4) Borrar platillo del menu
                    5) Regresar al menu principal
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
                    print("Indique un número valido")
        elif (accion == 4):
            print("Adios")
            break
        else:
            print("Por favor ingrese una opción valida")
restaurante()     
