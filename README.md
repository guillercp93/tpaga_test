# tpaga_test

# Objetivo General:
Crear un sitio web de minicomercio, donde se ofrezca un único servicio o producto y pueda ser pagado con la billetera
móvil.

# Tareas a realizar:
0. Lectura de la documentación (30min)
1. Diseño de la base de datos (30min)
2. Diseño y desarrollo de la acción comprar producto ó servicio. (3h)
4. Diseño y desarrollo de la acción de verificación de comprar de producto ó servicio (2h)
3. Diseño y desarrollo de la acción revertir compra de producto ó servicio. (2h)
5. Registro en logs de lo cambios en las ordenes de compra (1h)
6. Despliegue del sitio web. (2h)

# Desarrollo
Se hizo un trabaj conjunto entre la tarea 0 y 1, ya que al ver los parámetros que se necesitaba al hacer las peticiones y lo que devolvía, se iba haciendo el modelo de datos del sitio web. El tiempo que tardó fué de 40min.

Luego se empezó a hacer el desarrollo de la compra de un producto. Para ello se creó los modelos Order, OrderProducto, Producto y Logs. Se hizo una relación de muchos a muchos entre Order y Product, debido a que una orden de compra tiene varios productos y un producto puede estar en varias ordenes de compra. (Se hizo así en caso de una modificación). Y Logs contendrán los estados de cada orden de compra a lo largo del tiempo.
De la página que recomendaba la documentación para la parte del fronted se escogió la plantilla "Verti", puesto que era la mas sencilla y encajaba muy bien para una muestra de productos. De esa plantilla se instaló en el proyecto de Django los templates y statics necesarios para su funcionamiento. Luego se hizo la función del views y la con su url registrada. También se implementó en un archivo las funciones que consumirán las API de Tpaga. Tiempo total 4horas.
Con la experiencia obtenida en el punto anterior, fue mucho más facil la implementación de la verificación de compra, aunque tuve problemas a la hora de verificar la compra con la APP de prueba, puesto que aparecía un código 409 de Business error: payment request could not be paid y éste no estaba en la documentación. Tiempo total (2h)
Para revertir la compra de un producto, se apoyó en el sitio de administración de Django donde el administrador puede cambiar el estado de una orden de compra. Y este al cambiar a estado "reverted", el sistema consumirá el API para registrar dicha acción, en caso de haber error, el sistema no cambiará el estado de dicha orden. (2h)
Para el registro de los cambios de estado que vayan registrando las ordenes de compra, se crea el modelo Logs, y por medio de las señales de Django, despues de que se modifique una orden, se registrará el id, estado y fecha del cambio. Esto se puede ver en el sitio de administración de django. (1 hora y media)
Para el despligue se utilizó heroku, ya que había tenido experiencia anteriormente haciendo despliegues en esa plataforma. Aunque tuve algunos problemas con los drivers para la base de datos y conflictos de paquetes, incombientes que llevó un buen tiemo investigar su solución. Se logró desplegar en la plataforma. Tiempo total (4h)

# Datos de administrador
El sitio de administración se puede ingresar por la url: https://tpaga-test.herokuapp.com/admin/
# Username
admin
# Password
4dm1n1str4d0r

# Variables de ambiente
Si piensan correr el proyecto, deben tener en cuenta que se necesitan tener presente estas variables de ambiente:
DEBUG=
JAWSDB_URL=
SECRET_KEY=
TPAGA_USERNAME=
TPAGA_PASSWORD=

# Qué podemos mejorar?
He encontrado el error 409 en el API para confirmación de pago. Esta respuesta no está en la documentación. Me gustaría saber cómo funciona ese error, cuál puede ser la posible causa de ello.

# Recomendaciones hacia nosotros

• Qué sitio de plantillas de interneta gratuitas nos recomendaría?
• Qué sitios para alojar la infraestructura recomendaría a otros aspirantes a esta u
otras pruebas en Tpaga?
• Qué libros recomendaría para que las personas que están en el equipo de trabajo
puedan leer y cuenten con las mejores prácticas de vida y desarrollo?
• Qué mejores prácticas compartiría con un desarrollador que admire o con el cual
valdría la pena seguir trabajando y aprendiendo?
