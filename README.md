### Investiagción y Desarrollo de un CRUD con Django 

Este repositorio ha sido creado como parte de la entrega práctica del bootcamp, contiene dos secciones principales: una investigación teórica sobre el funcionamiento del framework Django, su arquitectura y el flujo de datos; y el desarrollo práctico de una aplicación web (CRUD) para la gestión de un catálogo de libros.

# Investigación y Desarrollo de un CRUD con Django 📚

Este repositorio ha sido creado como parte de la entrega práctica del bootcamp de desarrollo web. Contiene dos secciones principales: una investigación teórica sobre el funcionamiento del framework Django, su arquitectura y el flujo de datos; y el desarrollo práctico de una aplicación web (CRUD) para la gestión de un catálogo de libros.

## 📌 Índice de Contenidos
1. [Parte 1: Investigación Teórica (Preguntas y Respuestas)](#parte-1-investigación-teórica)
2. [Parte 2: Guía de Desarrollo del CRUD](#parte-2-crear-un-crud)
3. [Cómo Ejecutar el Proyecto en Local](#-cómo-ejecutar-el-proyecto-en-local)

---

## 📑 Parte 1: Investigación Teórica

### 1. ¿Qué es un CRUD y cuál es su propósito en el desarrollo de aplicaciones web?

Un **CRUD** es el esqueleto de casi cualquier página web que maneje información. Básicamente, se refiere a las cuatro acciones que podemos hacer con los datos en una web:

* ➕ **Create (Crear):** Añadir información nueva (por ejemplo, registrar un libro).
* 👀 **Read (Leer):** Ver los datos que ya están guardados (Como entrar a la web y revisar el catálogo).
* ✏️ **Update (Actualizar):** Modificar algo que ya existía (Como corregir el nombre del autor).
* 🗑️ **Delete (Eliminar):** Borrar un registro para siempre.

**¿Su propósito?** Darle al usuario el control total sobre la información de la pantalla de forma intuitiva, asegurándonos de que todo se guarde y se sincronice bien por detrás.

> **Un ejemplo real: Instagram**
> Es un CRUD perfecto.Cuando subes una foto estas **creando**; cuando miras el inicio de la app estas **leyendo**; si editasel texto de tu publicación estás **actualizando**; y si borras una foto antigua, estás **eliminando**.

### 2. ¿Qué son los patrones de arquitectura en desarrollo de software?

Para explicarlo de forma sencilla, un **patrón de arquitectura** es como el plano de un arquitecto para construir una casa. En software, es una guía o una estructura ya probada que nos dice como organizar nuestro código para que no sea un caos, sea limpio y cualquier otro programador lo entienda.

* **¿Qué es el patrón MVC (Modelo-Vista-Controlador)?:** Es una manera clásica de organizar las aplicaciones, se dividen en tres capas:
* **Modelo:** Se encarga de los datos puros y la base de datos.
* **Vista:** Es la pantalla, lo que el usuario ve y toca (el diseño).
* **Controlador:** Es el intermediario o "cerebro" que recibe los clics del usuario, le pide los datos al modelo y decide qué mostrar en la vista.

* **¿Qué es el patrón MVT (Modelo-Vista-Template):** Es el patrón propio que usa **Django**. Cambia un poco los nombres del MVC clásico:
* **Modelo** (Model):** Sigue siendo la base de datos (igual que en MVC)
* **Vista (View):** ¡Aquí cambía! La vista en Django es la que lleva la lógica (hace de Controlador).
* **Plantilla (Template):** Es el archivo HTML con los diseños (lo que en MVC se llamaba Vista).

**Diferencias entre MVC y MTV:** La principal diferencia es que en MVC tú tienes que programar manualmente como se conectan el Modelo, la Vista y el Controlador. En cambio, en el MVT de Django, el propio framework ya hace esa conexión por ti de forma automática. Además, los nombres están cruzados (la Vista de Django es el Controlador de MVC).

**¿Cuál usa Django?:** Djngo utiliza el patrón **MVT**

### 3. ¿Cómo se estructura un proyecto en Django?

En la arquitectura de Django, todo el sistema se organiza dividiendo el trabajo en cuatro piezas clave que se pasan el testigo unas a otras para gestionar cada petición que hace un usuario:

* **URLs:** Son el "recepcionista" de la web. Cuando ponemos una dirección en el navegador (ej. `/libros/`), el archivo de URLs mira qué hemos pedido y redirige la petición a la **Vista** adecuada.
* **Vistas (Views):** Son el cerebro del proyecto. Reciben la petición del usuario, deciden qué lógica aplicar, van a buscar los datos que hagan falta y preparan la respuesta.
* **Modelos (Models):** Es la capa que define cómo van a ser nuestras tablas en la base de datos (por ejemplo, estructurar que un libro tenga título, autor, etc.) usando código Python limpio.
* **Templates:** Son las plantillas HTML, es decir, el diseño visual que al final se le muestra al usuario en su pantalla cargado con los datos dinámicos.

### ¿Para qué se usa el signo “%%” en los templates?

*(Nota: Aunque en la pregunta viene escrito como `%%`, en el código real de Django se utiliza la sintaxis `{% %}`).* Se usan para meter "superpoderes" o lógica de programación dentro de un archivo HTML. 

En resumen: Sirve para que tu HTML deje de ser una página estática y se convierta en una web dinámica. El HTML normal es plano y fijo; no sabe lo que es un condicional ni un bucle. Pero cuando estás creando una web con Django, necesitas que la página sea inteligente. Gracias a las etiquetas `{% %}`, puedes hacer magia dentro de la web, haciendo que sea capaz de reaccionar a los datos que le mandas desde Python.

### 4. ¿Cuál es el flujo de datos entre un formulario HTML y la base de datos en Django?

El "viaje" que hacen los datos desde que un usuario interactúa con la pantalla hasta que se guardan de verdad sigue este orden paso a paso:

1. 📝 **El usuario rellena la web:** En el navegador, escribimos los datos del libro en el formulario HTML y hacemos clic en el botón de "Enviar". Esto manda la información mediante una petición segura llamada `POST`.
2. 🗺️ **La URL da paso:** Django recibe esa petición a través de su sistema de **URLs** y se la entrega a la **Vista** que se encarga de controlar ese formulario.
3. 🧠 **La Vista inspecciona:** La **Vista** recoge los datos. Antes de guardarlos, usa un formulario especial de Django (un `ModelForm`) para comprobar que todo sea correcto con la función `.is_valid()`. *(Por ejemplo, revisa que si un campo pide una fecha, no hayamos escrito texto).*
4. 💾 **El ORM hace la magia:** Si todo está en orden, la vista ejecuta la orden `.save()`. Aquí el **Modelo** traduce esa orden de Python a código de base de datos automáticamente, sin que tengamos que escribir SQL.
5. 🗄️ **Almacenamiento:** Los datos quedan guardados para siempre en la **Base de datos**, y la vista suele redirigir al usuario de vuelta al catálogo para que vea su nuevo libro en la lista.

---

### 5. ¿Qué herramientas o comandos ofrece Django para facilitar el desarrollo de un CRUD, para qué es cada una?

Django viene con un asistente en la terminal llamado `manage.py` y varias herramientas que nos ahorran escribir cientos de líneas de código. Las más importantes son:

* 🚀 **`runserver`:** Es el comando que enciende el servidor local de desarrollo. Nos da una dirección (`http://127.0.0.1:8000`) para abrir el proyecto en el navegador y ver cómo va quedando la web en tiempo real.
* 📦 **`startapp`:** Sirve para crear una nueva "aplicación" o módulo dentro de nuestro proyecto (como la carpeta `libros` que creamos). Te genera la estructura de carpetas limpia y lista para programar.
* 📐 **`makemigrations`:** Es como el fotógrafo del código. Analiza nuestro archivo `models.py` y, si ve que hemos creado o cambiado un modelo, saca una "captura" y crea un archivo con las instrucciones de lo que hay que construir.
* 🏗️ **`migrate`:** Es el constructor. Lee las instrucciones que generó el `makemigrations` y aplica los cambios reales en la base de datos, creando las tablas físicas.
* 📝 **ModelForm:** Es una herramienta brutal de Django. En lugar de crear un formulario HTML campo por campo a mano, le decimos: *"Oye, hazme un formulario basado en mi Modelo de Libro"*. Django lee el modelo y te genera el formulario con sus filtros y validaciones de forma automática.
* 👑 **Admin:** Es un panel de control visual que viene ya programado dentro de Django. Te permite gestionar los datos de la base de datos con botones, sin picar código.

---

### 6. ¿Cómo funciona el Admin de Django?

El **Admin de Django** es una de las herramientas más potentes del framework. Funciona leyendo directamente los modelos que nosotros creamos en el archivo `models.py`. 

Cuando registramos un modelo en el panel de administración (en `admin.py`), Django genera automáticamente una interfaz web completa, segura y con diseño profesional. Desde ahí, sin haber programado ni una sola línea de HTML o CSS para esa parte, podemos:
* Ver la lista de registros de la base de datos.
* Añadir nuevos elementos, editarlos o borrarlos con botones visuales (un CRUD interno).
* Filtrar y buscar datos de forma rápida.

Para usarlo, solo necesitamos crear un "superusuario" desde la terminal e iniciar sesión en la dirección `/admin` de nuestra web.

---

### 7. ¿Django usa la arquitectura REST? ¿Qué es Django Rest Framework?

Por defecto, **Django clásico no usa la arquitectura REST**, sino que está pensado para el patrón MVT tradicional (donde el propio servidor de Django genera y "pinta" las páginas HTML que ve el usuario).

Sin embargo, hoy en día es súper común usar Django para crear **APIs REST**. Para poder hacer esto de forma fácil, la comunidad creó una extensión brutal llamada **Django Rest Framework (DRF)**.

* 🔌 **¿Qué es Django Rest Framework?:** Es una librería o "pájaro de tecnologías" que se instala encima de Django para convertirlo en un potente servidor de APIs. 
* 🔄 **¿Cómo funciona?:** En lugar de mandar páginas HTML completas al navegador, DRF transforma los datos de nuestros modelos en formato **JSON** (un texto organizado que entienden perfectamente las aplicaciones de móvil, webs hechas con React/Angular, etc.). Nos da herramientas para controlar quién puede entrar (autenticación) y serializadores para validar la información de forma ultra rápida.