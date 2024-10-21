from conexiones_sqlite3.conexion_clientes import crear_clientes,eliminar_cliente_id,actualizar_cliente_nombre,actualizar_cliente_correo,actualizar_cliente_direccion,actualizar_cliente_telefono
#creamos la clase mediante classs "nombre de la clase"
class Cliente:
    #utilizamos __init__ como metodo constructor de la clase
    def __init__(self,clave,nombre,direccion,correo_electronico,telefono):
        #definir los atributos
        self.clave = str(clave)
        self.nombre = str(nombre)
        self.direccion = str(direccion)
        self.correo_electronico = str(correo_electronico)
        self.telefono = str(telefono)
        #crear_clientes(self.clave,self.nombre,self.direccion,self.correo_electronico,self.telefono)
        #una vez definidos los atributos podemos definir los metodos llamaremos a la funcion que nos crea datos en nuestra tabla de clientes
        
    #mediante esta funcion __str__ podemos imprimir datos de clase, sin necesidad de llamar a un metodo, estos datos se mostraran cuando la clase detente un print
    def __str__(self):
        return f"Clave: {self.clave}, Cliente: {self.nombre}, Direccción: {self.direccion}, Tel: {self.telefono}, Email: {self.correo_electronico})"
    def actualizarNombre(self,nuevoNombre):
        self.nombre = nuevoNombre
        try:
            actualizar_cliente_nombre(self.clave,self.nombre)
            print(f"El nombre se actualizo correcctamente, el nuevo nombre es {self.nombre}")
        except Exception as ex:
            print(ex)
    def actualizarDireccion(self,nuevaDireccion):
        self.direccion = nuevaDireccion
        try:
            actualizar_cliente_direccion(self.clave,self.direccion)
            print(f"La dirección se actualizo correctamente, la nueva dirección es {self.direccion}")
        except Exception as ex:
            print(ex)
    def actualizarCorreo(self,nuevoCorreo):
        self.correo_electronico = nuevoCorreo
        try:
            actualizar_cliente_correo(self.clave,self.correo_electronico)
            print(f"El correo se actualizo correctamente, el nuevo correo es {self.correo_electronico}")
        except Exception as ex:
            print(ex)
    def actualizarTelefono(self,nuevoTelefono):
        self.telefono = nuevoTelefono
        try:
            actualizar_cliente_telefono(self.clave,self.telefono)
            print(f"El correo se actualizo correctamente, su nuevo correo es {self.correo_electronico}")
        except Exception as ex:
            print(ex)
    def retornarClaveCliente(self):
        return self.clave
    def retornarNombreCliente(self):
        return self.nombre    
    def borrarPorID(self):
            try:
                eliminar_cliente_id(self.clave)
                print("Cliente eliminado")
            except Exception as err:
                print(err)


def agregarCliente():
    #clave = input("Ingrese la clave del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    correo_electronico = input("Ingrese el correo del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    crear_clientes(nombre,direccion,correo_electronico,telefono)
   #crear_clientes(clave,nombre,direccion,correo_electronico,telefono)
    #clienteNuevo = Cliente(clave,nombre,direccion,correo_electronico,telefono)
    #listaClientes.append(clienteNuevo)
def eliminarCliente(listaClientes):
    print("Indique el cliente que desea eliminar")
    for i in range(len(listaClientes)):
        print(f"{i+1}.-{listaClientes[i]}")
    clienteSeleccionado = listaClientes[int(input("Seleccion: "))-1]
    #print(clienteSeleccionado)
    clienteSeleccionado.borrarPorID() 
def actualizarCliente(listaClientes):
    print("Indique el usuario que desea actualizar")
    for i in range(len(listaClientes)):
        print(f"{i+1}.-{listaClientes[i]}")
    clienteSeleccionado = int(input("Seleccion: "))
    clienteParaActualizar = listaClientes[clienteSeleccionado-1]
    #print(clienteParaActualizar)
    print("Del cliente seleccionado que dato desea actualizar: ")
    while True:
        print("""
            1.- Nombre
            2.- Dirección
            3.- Correo
            4.- Teléfono
            5.- Salir
            """)
        seleccion = int(input("Seleccione el dato que desea actualizar: "))
        if seleccion == 1:
            nombreNuevo = input("Ingrese el nuevo nombre: ")
            clienteParaActualizar.actualizarNombre(nombreNuevo)
        elif seleccion == 2:
            direccionNueva = input("Ingrese la nueva dirección: ")
            clienteParaActualizar.actualizarDireccion(direccionNueva)
        elif seleccion == 3:
            correoNuevo = input("Ingrese su correo nuevo: ")
            clienteParaActualizar.actualizarCorreo(correoNuevo)
        elif seleccion == 4:
            telefonoNuevo = input("Ingrese el nuevo teléfono: ")
            clienteParaActualizar.actualizarTelefono(telefonoNuevo)
        elif seleccion == 5:
            break
        else:
            print("Seleccione una opción valida")
            
#agregarCliente()
#eliminarCliente()
#actualizarCliente()