from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "estado", "fecha_publicacion"]
    list_filter = ["estado", "autor"]
    raw_id_fields = ["autor"]
    ordering = ["-fecha_publicacion"]

@admin.register(Leyenda)
class LeyendaAdmin(admin.ModelAdmin):
    list_display = ["nombre", "genero", "fecha_nacimiento"]
    list_filter = ["genero"]
    search_fields = ["nombre", "genero"]
    ordering = ["nombre"]

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_lanzamiento', 'genero', 'autor_album')
    search_fields = ('nombre', 'genero', 'autor_album')
    list_filter = ('genero', 'autor_album')
    ordering = ('-fecha_lanzamiento',)

    def get_queryset(self, request):
        """Filtrar los álbumes solo a los que el usuario ha creado"""
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            queryset = queryset.filter(autor_album=request.user)
        return queryset


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'post', 'fecha_creacion', 'contenido_corto')
    list_filter = ('fecha_creacion', 'usuario', 'post')
    search_fields = ('contenido', 'usuario__username', 'post__titulo')
    ordering = ('-fecha_creacion',)

    def contenido_corto(self, obj):
        return obj.contenido[:50] + '...' if len(obj.contenido) > 50 else obj.contenido
    contenido_corto.short_description = 'Contenido'