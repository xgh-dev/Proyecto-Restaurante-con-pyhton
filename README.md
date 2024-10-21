Proyecto: 
Menu de restaurante con python y flask

Saludo:
Bienvenidos, esta es la documentación de nuestra aplicación de terminal y template web, de nuestra proyecto llamado "Restaurante".

Descripción:
Este es un proyecto que emula a un menu para un restaurante desarrollado con python, este proyecto consta de ddos secciones, la sección que trabaja directamente con la terminal y la sección que que muestra nustros templates html mediante  la implementación de flask. Este proyecto tiene la finalidad de cubrir las necesidades basica de un restaurante, especificamente en la creación de pedidos, manipulación de datos de clientes y de los propios platillos del restaurante mediante la ejecución de este en la terminal y con apoyo de un template web podremos ver los pedidos activos y los datos de este pedidos, con apoyo de la terminal y de la ejecución del programa podremos manipular los datos que estan relacionados con este proyecto, de igual manera el programa nos permite visualizarlos, de igual manera, usamos templates web para la visualización de los datos de los pedidos creados desde la aplicación de consola, este template lo desplegamos mediante flask y su función es solo la visualización de datos de igual manera se puede eliminar algun pedido de ser necesario.

Instalación:
Para poder instalar y ejecutar el proyecto en nuestro entorno local debemos realizar lo siguiente:
1.- Contar con python en nuestras variables de entorno para poder ejecutar el programa.
2.- Descargar el codigo desde el repositorio en github.
3.- Como usamos una libreria externa, en este caso flask, debemos activar el entorno virtual mediante el siguiente comando .\env\Scripts\Activate, con esto de instalara flask en dicho entorno virtual y podremos ejecutar y utlizar dicha libreria.
4.- Una vez activado el entorno virtual podremos ejecutar la aplicación de escritorio y la aplicación de flask.
5.- Para ejecutar la aplicación de escritorio debemos crear una terminal nueva y ejecutar el siguiente comando " & C:/Python312/python.exe d:/python_avanzado_proyecto/app_terminal/main.py ", una vez ejecutado tendremos acceso y control de nuestra aplicación en la terminal.
6.- Para ejecutar la aplicación web debemos crear una terminal nueva y ejecutar el siguiente comando " & C:/Python312/python.exe d:/python_avanzado_proyecto/app_flask/app.py ", una vez ejecutado daremos inicio al sevidor de flask en el cual se aloja nuestra aplicación web.

Uso:
-Aplicación de terminal: al iniciar la ejecución del programa mediante los pasos mencionados, veremos que se despliegua un menu con cuatro opciones cada una con funciones distintas. 
--La funciún núnmero 1 (Pedidos): nos dirige al propio menu de los pedidos, en este menu podremos crear, eliminar y mostras los pedidos que tengamos registrados en la base de datos, para poder crear un pedido debemos tener registros de clientes y menu en la base de datos, de lo contrario no podremos crear un pedido.

--La funciún núnmero 2 (Clientes): nos dirige al propio menu de los clientes, en este menu podremos crear, editar, eliminar y mostrar los datos de los clientes en la base de datos de la tabla clientes.

--La funciún núnmero 3 (CMenú): nos dirige al propio menu de los platillos, en este menu podremos crear, editar, eliminar y mostrar los datos de los platillos que tengamos en la base de datos de la tabla menu.

--La funciún núnmero 4 (Salir): esta función solo termina la ejecución de la aplicación de terminal.

-Aplicación de templates web con flask: al iniciar la ejecución del programa mediante los pasos mencionados, veremos que se despliegua la ejecuciónd el servidor de flask con el siguiente puerto " http://127.0.0.1:5000 ", en el navegador al enviar esta ruta nos mostrara el template web con los pedidos que tengamos creados y registrados en la base de datos. En el template principal en caso de tener registros que se muestren veremos que nos muestra dos opciones una para ver datos de los pedidos y otra para eliminar dichos pedidos.

--Función que muestra los datos del pedido: esta es una función simple, al hacer click nos redirige a otro template en el que se mostraran todos los datos de pedido seleccionado.
--Función que elimina el pedido: esta es una función simple que toma un elemento identificador del dato seleccionado y mediante un función que toma este dato lo elimina de la base de datos y actualiza la tabla del template.

