# PROYECTO FINAL

Usuario administrador: **admin**  
Contraseña: **123**  

Soy Ezequiel Basualdo y presento mi proyecto final para la cursada de Python en Coder House, comisión 72690. Este proyecto consiste en un blog diseñado para que guitarristas y bajistas compartan experiencias, pensamientos y reflexiones sobre el mundo de la música, creando así una comunidad. Además, incluye secciones dedicadas a leyendas de la música y álbumes destacados, donde se muestra información relevante sobre artistas y discos históricos.

El proyecto se desarrolló en un entorno virtual (venv) y utiliza Django con Python, HTML, CSS y Bootstrap, implementado en Visual Studio Code. Cuenta con dos aplicaciones: **blog** y **Main**. La aplicación *blog* incluye 14 plantillas HTML, mientras que *Main* cuenta con 6. Todos los templates heredan de `base.html`, excepto `register.html`, que hereda de `login.html` (login proviene de la aplicación Main). 

Blog (blog) se basa en los códigos necesarios para darle imagen y funcionalidad a las publicaciones, leyendas y álbumes. Main (Main) se encarga de la estructura general del sitio web, así como las funcionalidades de registro, inicio de sesión y cierre de sesión.


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

##### ==================================================================== APPS ================================================================================
                                                                    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
##### ==================================================================== BLOG =================================================================================

# ADMIN.PY

La aplicación **blog** cuenta con cuatro administradores personalizados que gestionan diferentes tipos de datos en el panel de administración de Django:

- **PostAdmin**: Administra y muestra los datos de los posteos en la vista de administración.
- **LeyendaAdmin**: Administra y muestra los datos de las leyendas en la vista de administración.
- **AlbumAdmin**: Administra y muestra los datos de los álbumes en la vista de administración.
- **ComentarioAdmin**: Administra y muestra los datos de los comentarios en la vista de administración.


# FORMS.PY

La aplicación incluye varios formularios para manejar las distintas funcionalidades del blog:

- **PostForm**: permite crear y editar publicaciones, solicitando datos como título, contenido, estado y categoría.  
- **ComentarioForm**: facilita la creación de comentarios para las publicaciones, solicitando únicamente el contenido del comentario.  
- **LeyendaForm**: permite registrar y editar leyendas (artistas) incluyendo nombre, fecha de nacimiento, género e historia.  
- **SearchForm**: un formulario simple para realizar búsquedas en el sitio mediante una palabra clave.  
- **AlbumForm**: permite crear y editar álbumes con datos como nombre, fecha de lanzamiento, género, autor y su historia.  



# MODELS.PY

- **Post**: Modelo para los posteos del blog. Cada post tiene un título, contenido, fecha de publicación, autor, estado (borrador o publicado) y categoría (guitarra o bajo).
- **Comentario**: Modelo para los comentarios que los usuarios pueden dejar en los posts. Cada comentario está asociado a un usuario, contiene el contenido, la fecha de creación y se vincula al post correspondiente.
- **Leyenda**: Modelo que representa a un artista legendario de la música. Cada leyenda tiene un nombre, fecha de nacimiento, género musical, una historia relacionada y un autor (usuario).
- **Album**: Modelo que representa un álbum musical. Cada álbum tiene un nombre, fecha de lanzamiento, género musical, autor del álbum, historia relacionada y un autor (usuario) asociado.


# URLS DEL PROYECTO

- **Post**:
  - **post_list**: Muestra una lista de todos los posts del blog.
  - **post_create**: Permite crear un nuevo post en el blog.
  - **post_delete**: Permite eliminar un post existente.
  - **comentario_create**: Permite crear un comentario en un post específico.

- **Leyendas**:
  - **leyenda_list**: Muestra una lista de todas las leyendas (artistas).
  - **leyenda_create**: Permite crear una nueva leyenda (artista).
  - **leyenda_detail**: Muestra los detalles de una leyenda específica.
  - **leyenda_update**: Permite actualizar la información de una leyenda.
  - **leyenda_delete**: Permite eliminar una leyenda.

- **Álbumes**:
  - **album_list**: Muestra una lista de todos los álbumes.
  - **album_create**: Permite crear un nuevo álbum.
  - **album_detail**: Muestra los detalles de un álbum específico.
  - **album_update**: Permite actualizar la información de un álbum.
  - **album_delete**: Permite eliminar un álbum.


# VISTAS DEL PROYECTO

- **Post**:
  - **post_list**: Muestra una lista de todos los posts del blog.
  - **post_create**: Permite crear un nuevo post en el blog.
  - **post_delete**: Permite eliminar un post existente.
  - **comentario_create**: Permite crear un comentario en un post específico.

- **Leyendas**:
  - **leyenda_list**: Muestra una lista de todas las leyendas (artistas).
  - **leyenda_create**: Permite crear una nueva leyenda (artista).
  - **leyenda_detail**: Muestra los detalles de una leyenda específica.
  - **leyenda_update**: Permite actualizar la información de una leyenda.
  - **leyenda_delete**: Permite eliminar una leyenda.

- **Álbumes**:
  - **album_list**: Muestra una lista de todos los álbumes.
  - **album_create**: Permite crear un nuevo álbum.
  - **album_detail**: Muestra los detalles de un álbum específico.
  - **album_update**: Permite actualizar la información de un álbum.
  - **album_delete**: Permite eliminar un álbum.


##### ==================================================================== MAIN =================================================================================

# ADMIN.PY

- **ProfileAdmin**:  
  - Personaliza la vista del modelo `Profile` en el panel de administración de Django. Muestra los campos `user` y `avatar` en la lista de objetos `Profile` dentro del panel de administración.


# FORMS.PY

La aplicación posee 3 formularios personalizados para manejar usuarios y perfiles:

- **CustomUserCreationForm**: permite registrar nuevos usuarios solicitando nombre, apellido, correo electrónico y contraseña. Al registrarse, automáticamente se crea un perfil asociado.  
- **ProfileEditForm**: facilita la edición del avatar del perfil de los usuarios, permitiendo que actualicen su imagen de perfil.  
- **UserEditForm**: permite modificar datos personales como nombre, apellido y correo electrónico. También da la opción de cambiar la contraseña.  


# MODELS.PY

La aplicación define los siguientes modelos para gestionar usuarios y perfiles:

- **CustomUser**: representa una personalización del modelo de usuario. Incluye campos como nombre de usuario, nombre, apellido, correo electrónico y contraseñas.  
- **Profile**: extiende la funcionalidad del usuario mediante un avatar, asociado a cada usuario registrado, con un valor predeterminado en caso de que no se cargue uno personalizado.  


# URLS.PY

La aplicación Main contiene las siguientes rutas:

- **index**: vista principal de la aplicación, muestra la página de inicio.  
- **login**: permite a los usuarios iniciar sesión mediante un formulario de autenticación.  
- **logout**: cierra la sesión de los usuarios y redirige a la página principal.  
- **register**: proporciona un formulario para registrar nuevos usuarios.  
- **about_me**: muestra una página con información sobre el desarrollador o la aplicación.  
- **editarPerfil**: permite a los usuarios editar su perfil, incluida la información personal.  


# VIEWS.PY

La aplicación Main incluye las siguientes vistas para manejar la funcionalidad del sitio web y la gestión de usuarios:

- **index**: renderiza la página de inicio, ubicada en `Main/index.html`.  
- **about_me**: muestra una página con información sobre el desarrollador o la aplicación, ubicada en `Main/about_me.html`.  
- **register**: gestiona el registro de nuevos usuarios utilizando el formulario `CustomUserCreationForm`. Si el registro se realiza con exito, redirige a la página de inicio de sesión.  
- **editarPerfil**: permite a los usuarios autenticados editar su información personal y actualizar su avatar mediante los formularios `UserEditForm` y `ProfileEditForm`. También incluye la funcionalidad para cambiar la contraseña.  



