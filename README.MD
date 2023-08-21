Entrega Final de CoderHouse - Python - Comisión 43865

Administrador: superadmin / Pass: 123

En esta entrega podemos ver la aplicacion de Coder Cafe. En la página principal se encuentra un banner de Coder Cafe, los tipos de cafes que venden, información sobre la empresa, sus dueños, un pequeño blog, formulario de contacto, ubicacion. En la esquina superior derecha tiene los distintos botones que nos llevará a las distintas vistas de la aplicacion.

Si no estamos logeados están los botones de Login y Registro. Si nos logeamos podemos ver el boton logout, administracion y empleados. Este último nos lleva a una vista con distintos links utiles para los empleados como crear variedades de cafe, dar de alta clientes, sucursales y consultar listados de pedidos.

La aplicacion tiene las siguientes clases: cafe, sucursal, cliente, producto, pedido.

Clickeando en CAFE (miaplicacion/cafe) nos lleva a una sección donde podemos ver los distintos tipos de café. Luego si presionamos en comprar nos redirecciona para crear un pedido (miaplicacion/crear_pedido/), aqui nos pide los distintos datos del cliente. Es necesario estar logueado para poder crear un pedido. El codigo verifica si los datos ingresados coinciden con los de la base de clientes, si no coincide procede a agregarlos a la base. Ademas tambien se agrega el pedido a la base de pedidos.

Volviendo al home, si presionamos en SUCURSALES o en la lupa, nos direcciona al buscador de sucursales (miaplicacion/buscar_sucursales/) donde tenemos un campo para escribir el nombre y nos mostrará las coincidencias.

Como herencia de html usé el navbar.html para heredar la barra superior en las distintas vistas. Ademas tambien usamos diversos blocks del index.html (home) para la confeccion de las vistas.


VIDEO: https://youtu.be/X2PvOgf03oI
