from django.urls import path
from . import views
from .views import (
    AlbumListView, AlbumDetailView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView,
    LeyendaListView, LeyendaDetailView, LeyendaCreateView, LeyendaUpdateView, LeyendaDeleteView,
    PostDeleteView
)

app_name = "blog"

urlpatterns = [
    # Posts
    path("post/list", views.post_list, name="post_list"),
    path("post/create", views.post_create, name="post_create"),
    path('post/eliminar/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path("comentario/create/<int:post_id>/", views.comentario_create, name="comentario_create"),
    
    # Leyendas
    path('leyendas/', LeyendaListView.as_view(), name='leyenda_list'),  
    path('leyendas/create/', LeyendaCreateView.as_view(), name='leyenda_create'),
    path('leyendas/<int:pk>/', LeyendaDetailView.as_view(), name='leyenda_detail'),
    path('leyendas/<int:pk>/update/', LeyendaUpdateView.as_view(), name='leyenda_update'),
    path('leyendas/<int:pk>/delete/', LeyendaDeleteView.as_view(), name='leyenda_delete'),
    
    # Álbumes
    path('albums/', AlbumListView.as_view(), name='album_list'),  
    path('albums/create/', AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('album/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]
