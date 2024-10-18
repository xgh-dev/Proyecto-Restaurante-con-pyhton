from conexiones_sqlite3.conexion_menu import crear_menu,eliminar_menu,actualizar_menu_nombre,actualizar_menu_precio

class Menu:
    def __init__(self,clave,nombre,precio):
        self.clave = str(clave)
        self.nombre = str(nombre)
        self.precio = float(precio) 
    def __str__(self):
        return f"Nombre: {self.nombre} -- Precio: {self.precio}"
    def actualizarClave(self,nuevaClave):
        self.clave = nuevaClave
    def actualizarNombre(self,nuevoNombre):
        self.nombre = nuevoNombre
        try:
            actualizar_menu_nombre(self.clave,self.nombre)
            print(f"El nuevo nombre del platillo es {self.nombre}")
        except Exception as ex:
            print(ex)
    def actualizarPrecio(self,nuevoPrecio):
        self.precio = nuevoPrecio
        try:
            actualizar_menu_precio(self.clave,self.precio)
            print(f"El nuevo precio del platillo es {self.precio}")
        except Exception as ex:
            print(ex)
    def retornarClavePlatillo(self):
        return self.clave
    def retornarNombrePlatillo(self):
        return self.nombre
    def retornarPrecioPlatillo(self):
        return self.precio
    def borrarPlatillo(self):
        try:
            eliminar_menu(self.clave)
            print("Platillo eliminado")
        except Exception as err:
            print(err)
    
def agregarProducto():
    nombre = input("Ingrese el nombre del platillo: ")
    precio = input("Ingrese el precio del platillo: ")
    crear_menu(nombre,precio)
def eliminarProducto(listaMenu):
    print("Indique el platillo que desea eliminar: ")
    for i in range(len(listaMenu)):
        print(f"{i+1}.- {listaMenu[i]}")
    platilloSeleccionado = int(input("Seleccione un platillo para borrar: "))
    platilloSeleccionadoBorrar = listaMenu[platilloSeleccionado-1]
    platilloSeleccionadoBorrar.borrarPlatillo()           
def actualizarProducto(listaMenu):
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

