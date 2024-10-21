from conexiones_sqlite3.conexion_menu import crear_menu,eliminar_menu,actualizar_menu_nombre,actualizar_menu_precio

class Menu:
    def __init__(self,clave,nombre,precio):
        """
        Inicializa un objeto Menu con los atributos clave, nombre y precio.

        Parámetros:
        - clave (str): Clave del platillo.
        - nombre (str): Nombre del platillo.
        - precio (float): Precio del platillo.
        """
        self.clave = str(clave)
        self.nombre = str(nombre)
        self.precio = float(precio) 
    def __str__(self):
        """
        Devuelve una representación en forma de cadena del objeto Menu.

        Returna:
            str: Información del platillo, incluyendo nombre y precio.
        """
        return f"Nombre: {self.nombre} -- Precio: {self.precio}"
    def actualizarClave(self,nuevaClave):
        """
        Actualiza la clave del platillo.

        Parámetros:
        - nuevaClave (str): Nueva clave para el platillo.
        """
        self.clave = nuevaClave
    def actualizarNombre(self,nuevoNombre):
        """
        Actualiza el nombre del platillo en el objeto y en la base de datos.

        Parámetros:
        - nuevoNombre (str): Nuevo nombre para el platillo.
        """
        self.nombre = nuevoNombre
        try:
            actualizar_menu_nombre(self.clave,self.nombre)
            print(f"El nuevo nombre del platillo es {self.nombre}")
        except Exception as ex:
            print(ex)
    def actualizarPrecio(self,nuevoPrecio):
        """
        Actualiza el precio del platillo en el objeto y en la base de datos.

        Parámetros:
        - nuevoPrecio (float): Nuevo precio para el platillo.
        """
        self.precio = nuevoPrecio
        try:
            actualizar_menu_precio(self.clave,self.precio)
            print(f"El nuevo precio del platillo es {self.precio}")
        except Exception as ex:
            print(ex)
    def retornarClavePlatillo(self):
        """
        Devuelve la clave del platillo.

        Return:
            Clave del platillo.
        """
        return self.clave
    def retornarNombrePlatillo(self):
        """
        Devuelve el nombre del platillo.

        Returna:
            Nombre del platillo.
        """
        return self.nombre
    def retornarPrecioPlatillo(self):
        """
        Devuelve el precio del platillo.

        Returna:
            Precio del platillo.
        """
        return self.precio
    def borrarPlatillo(self):
        """
        Elimina el platillo de la base de datos.

        Raises:
            Exception: Si ocurre un error al eliminar el platillo.
        """
        try:
            eliminar_menu(self.clave)
            print("Platillo eliminado")
        except Exception as err:
            print(err)
    
def agregarProducto():
    """
    Agrega un nuevo platillo al menú.

    Solicita al usuario el nombre y el precio del platillo,
    y lo agrega a la base de datos llamando a la función crear_menu.
    """
    nombre = input("Ingrese el nombre del platillo: ")
    precio = input("Ingrese el precio del platillo: ")
    crear_menu(nombre,precio)

def eliminarProducto(listaMenu):
    """
    Elimina un platillo del menú.

    Muestra una lista de platillos disponibles y solicita al usuario
    que seleccione un platillo para eliminar. Luego llama a
    borrarPlatillo() del objeto del platillo seleccionado.

    Parámetros:
    - listaMenu (list): Lista de objetos Menu disponibles.
    """
    print("Indique el platillo que desea eliminar: ")
    for i in range(len(listaMenu)):
        print(f"{i+1}.- {listaMenu[i]}")
    platilloSeleccionado = int(input("Seleccione un platillo para borrar: "))
    platilloSeleccionadoBorrar = listaMenu[platilloSeleccionado-1]
    platilloSeleccionadoBorrar.borrarPlatillo() 
          
def actualizarProducto(listaMenu):
    """
    Actualiza un platillo existente en el menú.

    Muestra una lista de platillos y permite al usuario seleccionar
    un platillo para actualizar su nombre o precio. Las actualizaciones
    se realizan a través de los métodos de la clase Menu.

    Parámetros:
    - listaMenu (list): Lista de objetos Menu disponibles.
    """
    print("Indique el platillo que desea actualizar")
    for i in range(len(listaMenu)):
        print(f"{i+1} {listaMenu[i]}")
    platilloSeleccionado = int(input("Seleccione su platillo: "))
    platilloParaActualizar = listaMenu[platilloSeleccionado-1]
    print(f"Que desea actualizar del siguiente platillo {platilloParaActualizar}")
    while True:
        print("""
              1) Nombre
              2) Precio
              3) Regresar al menu
              """)
        seleccion = int(input("Selección: "))
        if seleccion == 1:
            nuevoNombre = input("Ingrese el nuevo nombre para el platillo: ")
            platilloParaActualizar.actualizarNombre(nuevoNombre)
        elif seleccion == 2:
            nuevoPrecio = input("Ingrese el nuevo precio para el platillo: ")
            platilloParaActualizar.actualizarPrecio(nuevoPrecio)
        elif seleccion == 3:
            break
        else: 
            print("Seleccione una opcion valdia")

