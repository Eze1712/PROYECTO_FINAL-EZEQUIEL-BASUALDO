from django.db import models
from django.contrib.auth.models import User

# Modelo para los posts
class Post(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'B', 'Borrador'
        PUBLICADO = 'P', 'Publicado'

    class CategoriaInstrumento(models.TextChoices): 
        GUITARRA = 'G', 'Guitarra'
        BAJO = 'B', 'Bajo'

    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Permitimos que sea nulo
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.BORRADOR)
    categoria = models.CharField(max_length=1, choices=CategoriaInstrumento.choices, default=CategoriaInstrumento.GUITARRA)  # Campo para la categoría

    def __str__(self):
        return self.titulo

# Modelo para los comentarios de los posts
class Comentario(models.Model):
    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True,  
        blank=True,  
        default=None  
    )
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")

    def __str__(self):
        return f"Comentario de {self.usuario.username if self.usuario else 'Anónimo'} en {self.post.titulo}"


# Modelo para Leyenda
class Leyenda(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=50)
    historia = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  

    def __str__(self):
        return self.nombre
