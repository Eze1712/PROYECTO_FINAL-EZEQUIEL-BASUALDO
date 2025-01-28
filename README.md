# PROYECTO FINAL

Usuario administrador: **admin**  
Contraseña: **123**  

Soy Ezequiel Basualdo y presento mi proyecto final para la cursada de Python en Coder House, comisión 72690. Este proyecto consiste en un blog diseñado para que guitarristas y bajistas compartan experiencias, pensamientos y reflexiones sobre el mundo de la música, creando así una comunidad. Además, incluye secciones dedicadas a leyendas de la música y álbumes destacados, donde se muestra información relevante sobre artistas y discos históricos.

El proyecto se desarrolló en un entorno virtual (venv) y utiliza Django con Python, HTML, CSS y Bootstrap, implementado en Visual Studio Code. Cuenta con dos aplicaciones: **blog** y **Main**. La aplicación *blog* incluye 14 plantillas HTML, mientras que *Main* cuenta con 6. Todos los templates heredan de `base.html`, excepto `register.html`, que hereda de `login.html`.

## INSTALACIÓN: 
El proyecto se desarrolló en un entorno virtual (venv) y utiliza Django con Python, HTML, CSS y Bootstrap. A continuación, se explican los pasos para instalarlo:

1. **Clonar el repositorio**  
   Descarga el proyecto desde GitHub utilizando el comando:
   ```bash
   git clone <URL_DEL_REPOSITORIO>

2. Crear y activar el entorno virtual:  python -m venv venv
3. Activar el entorno virtual: source venv/bin/activate
4. Instalar dependencias: pip install -r requirements.txt
5. Realizar las migraciones: python manage.py makemigrations
                            python manage.py migrate

6. Cargar archivos estáticos: python manage.py collectstatic
7. Iniciar el servidor: python manage.py runserver






### Funcionalidades principales

- La página principal muestra imágenes representativas (simulando contenido subido por los usuarios) y un menú de navegación. Desde este menú se puede acceder a:
  - **Blogs**: Crear publicaciones para compartir experiencias musicales.
  - **Leyendas**: Añadir datos de artistas destacados, incluyendo su nombre, fecha de nacimiento, género musical e historia.
  - **Álbumes**: Publicar información sobre discos históricos, como su título, fecha de lanzamiento, banda, género y descripción.

- **Restricciones de acceso**:
  - Solo los usuarios registrados pueden crear publicaciones, leyendas o álbumes, así como editar su perfil.
  - Las páginas de inicio y "Acerca de mí" son de acceso público.

Este blog combina funcionalidad y diseño para fomentar la interacción y el intercambio de conocimiento entre músicos. ¡Espero que lo disfruten!

# ---------------------------------------------------------------------------------------------------------------------


# ==================================================================== BLOG =================================================================================

# ADMIN.PY

La aplicación **blog** cuenta con cuatro administradores personalizados que gestionan diferentes tipos de datos en el panel de administración de Django:

- **PostAdmin**: Administra y muestra los datos de los posteos en la vista de administración.
- **LeyendaAdmin**: Administra y muestra los datos de las leyendas en la vista de administración.
- **AlbumAdmin**: Administra y muestra los datos de los álbumes en la vista de administración.
- **ComentarioAdmin**: Administra y muestra los datos de los comentarios en la vista de administración.




# FORMS.PY

La aplicación posee 3 formularios personalizados para manejar usuarios y perfiles:

- **CustomUserCreationForm**: permite registrar nuevos usuarios solicitando nombre, apellido, correo electrónico y contraseña. Al registrarse, automáticamente se crea un perfil asociado.

- **ProfileEditForm**: facilita la edición del avatar del perfil de los usuarios, permitiendo que actualicen su imagen de perfil.

- **UserEditForm**: permite modificar datos personales como nombre, apellido y correo electrónico. También da la opción de cambiar la contraseña.


# MODELS.PY

La aplicación cuenta con dos modelos principales que gestionan la información de los usuarios y sus perfiles:

- **CustomUser**: almacena datos básicos de los usuarios, como nombre de usuario, nombre, apellido, correo electrónico y contraseñas. Garantiza que los nombres de usuario y los correos sean únicos.

- **Profile**: está vinculado a cada usuario mediante una relación uno a uno y permite almacenar un avatar personalizado. Si no se sube un avatar, se asigna una imagen por defecto.














# Templates de blog:
# comentario_create.html: Es el modulo donde se establece el form para agregar comentarios a las publicaciones. Se puede acceder a través de Blog en la pagina inicial.

# leyenda_create.html: Es el modulo donde se establece el form para agregar Leyendas al sitio web, unicamente por administradores registrado por el momento. Se puede acceder a través de Leyendas en la pagina inicial.

# leyenda_list.html : muestra la lista de las leyendas agregadas em el mismo sitio que el de leyenda_create

# post_create.html: Es el modulo donde se establece el form para agregar publicaciones al sitio web. Se puede acceder a través de Blog en la pagina inicial.

# post_list.html: Es el módulo donde se agregan los blogs creados, y se puede acceder igual que post_create.html.



# Templates de Main: 

# base.html: se usa como el template padre, donde se establecen los metadatos en UTF-8, se aplican los bootstraps, y se establecen los links de navegación.

# index.html: utiliza al igual que todos los demas templates, el base.html como template padre, y se establecen los links de navegación, y se agrega un carousel con imagenes de las leyendas agregadas al sitio web.


# -----------------------------------------------------------------------------------------------------------------


# admin.py: solo se encuentra en la app blog, se utiliza para establecer los formularios que se puden trabajar dentro de la vista admin, siendo estos blogs y Leyendas.



# -----------------------------------------------------------------------------------------------------------------

# models.py: se crean los modelos de Posts, Comentarios y Leyendas. Cada uno tiene su formulario en forms.py

# -----------------------------------------------------------------------------------------------------------------

# urls.py: Este código define las URLs (direcciones web) para el blog. Estas son "/post/list", "/post/create", "/comentario/create/int:post_id/", "/leyendas/", "/leyendas/create/"

# -----------------------------------------------------------------------------------------------------------------

# views.py: Este código define las vistas para el blog. Esta gestiona la lógica para el servidor, es decir, lo que no vemos.En este caso, se definen vistas para listar publicaciones, crear publicaciones, crear comentarios, listar leyendas y crear leyendas. También se incluye una vista para buscar contenido en el blog. Cada vista utiliza los modelos y formularios definidos en models.py y forms.py, respectivamente, para interactuar con la base de datos y manejar la lógica de la aplicación.

