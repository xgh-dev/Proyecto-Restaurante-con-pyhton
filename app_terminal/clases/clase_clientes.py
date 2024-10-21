from conexiones_sqlite3.conexion_clientes import crear_clientes,eliminar_cliente_id,actualizar_cliente_nombre,actualizar_cliente_correo,actualizar_cliente_direccion,actualizar_cliente_telefono

#creamos la clase mediante classs "nombre de la clase"
class Cliente:
    #utilizamos __init__ como metodo constructor de la clase
    def __init__(self,clave,nombre,direccion,correo_electronico,telefono):
        """
        Inicializa un nuevo cliente.

        Parámetros:
        - clave (str): Clave del cliente.
        - nombre (str): Nombre del cliente.
        - direccion (str): Dirección del cliente.
        - correo_electronico (str): Correo electrónico del cliente.
        - telefono (str): Teléfono del cliente.
        """
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
        """
        Devuelve una representación en forma de cadena del cliente.

        Retorna:
        - str: Información del cliente.
        """
        return f"Clave: {self.clave}, Cliente: {self.nombre}, Direccción: {self.direccion}, Tel: {self.telefono}, Email: {self.correo_electronico})"
    def actualizarNombre(self,nuevoNombre):
        """
        Actualiza el nombre del cliente.

        Parámetros:
        - nuevoNombre (str): Nuevo nombre del cliente.

        Llama a la función actualizar_cliente_nombre() pasando la clave y el nuevo nombre del cliente.
        Muestra un mensaje de confirmación si la actualización es exitosa.
        """
        self.nombre = nuevoNombre
        try:
            actualizar_cliente_nombre(self.clave,self.nombre)
            print(f"El nombre se actualizo correcctamente, el nuevo nombre es {self.nombre}")
        except Exception as ex:
            print(ex)
    def actualizarDireccion(self,nuevaDireccion):
        """
        Actualiza la dirección del cliente.

        Parámetros:
        - nuevaDireccion (str): Nueva dirección del cliente.

        Llama a la función actualizar_cliente_direccion() pasando la clave y la nueva dirección del cliente.
        Muestra un mensaje de confirmación si la actualización es exitosa.
        """
        self.direccion = nuevaDireccion
        try:
            actualizar_cliente_direccion(self.clave,self.direccion)
            print(f"La dirección se actualizo correctamente, la nueva dirección es {self.direccion}")
        except Exception as ex:
            print(ex)
    def actualizarCorreo(self,nuevoCorreo):
        """
        Actualiza el correo electrónico del cliente.

        Parámetros:
        - nuevoCorreo (str): Nuevo correo electrónico del cliente.

        Llama a la función actualizar_cliente_correo() pasando la clave y el nuevo correo del cliente.
        Muestra un mensaje de confirmación si la actualización es exitosa.
        """
        self.correo_electronico = nuevoCorreo
        try:
            actualizar_cliente_correo(self.clave,self.correo_electronico)
            print(f"El correo se actualizo correctamente, el nuevo correo es {self.correo_electronico}")
        except Exception as ex:
            print(ex)
    def actualizarTelefono(self,nuevoTelefono):
        """
        Actualiza el número de teléfono del cliente.

        Parámetros:
        - nuevoTelefono (str): Nuevo número de teléfono del cliente.

        Llama a la función actualizar_cliente_telefono() pasando la clave y el nuevo teléfono del cliente.
        Muestra un mensaje de confirmación si la actualización es exitosa.
        """
        self.telefono = nuevoTelefono
        try:
            actualizar_cliente_telefono(self.clave,self.telefono)
            print(f"El correo se actualizo correctamente, su nuevo correo es {self.correo_electronico}")
        except Exception as ex:
            print(ex)
    def retornarClaveCliente(self):
        """
        Devuelve la clave del cliente.

        Retorna:
            Clave del cliente.
        """
        return self.clave
    def retornarNombreCliente(self):
        """
        Devuelve el nombre del cliente.

        Retorna:
            Nombre del cliente.
        """
        return self.nombre   
    def borrarPorID(self):
        """
        Elimina el cliente actual de la base de datos.

        Llama a la función eliminar_cliente_id() pasando la clave del cliente.
        """
        try:
            eliminar_cliente_id(self.clave)
            print("Cliente eliminado")
        except Exception as err:
            print(err)

def agregarCliente():
    """
    Agrega un nuevo cliente a la base de datos.

    Solicita al usuario los detalles del cliente (nombre, dirección, correo electrónico y teléfono) 
    y llama a la función crear_clientes() para almacenar la información.
    """
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    correo_electronico = input("Ingrese el correo del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    crear_clientes(nombre, direccion, correo_electronico, telefono)
    # Crear un objeto Cliente (comentado por ahora)
    # clienteNuevo = Cliente(clave, nombre, direccion, correo_electronico, telefono)
    # listaClientes.append(clienteNuevo)

def eliminarCliente(listaClientes):
    """
    Elimina un cliente de la lista de clientes.

    Muestra una lista de los clientes disponibles y permite al usuario seleccionar 
    uno para eliminarlo. Llama al método borrarPorID() del cliente seleccionado para 
    realizar la eliminación.

    Parámetros:
    - listaClientes (list): Lista de objetos Cliente.
    """
    print("Indique el cliente que desea eliminar")
    for i in range(len(listaClientes)):
        print(f"{i+1}.- {listaClientes[i]}")
    clienteSeleccionado = listaClientes[int(input("Seleccion: ")) - 1]
    clienteSeleccionado.borrarPorID()

def actualizarCliente(listaClientes):
    """
    Actualiza la información de un cliente existente.

    Muestra una lista de los clientes disponibles y permite al usuario seleccionar 
    uno para actualizar. Ofrece opciones para actualizar el nombre, dirección, 
    correo electrónico o teléfono del cliente seleccionado.

    Parámetros:
    - listaClientes (list): Lista de objetos Cliente.
    """
    print("Indique el usuario que desea actualizar")
    for i in range(len(listaClientes)):
        print(f"{i+1}.- {listaClientes[i]}")
    clienteSeleccionado = int(input("Seleccion: "))
    clienteParaActualizar = listaClientes[clienteSeleccionado - 1]
    print("Del cliente seleccionado, ¿qué dato desea actualizar?")
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
            print("Seleccione una opción válida")

