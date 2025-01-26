from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("post/list", views.post_list, name="post_list"),
    path("post/create", views.post_create, name="post_create"),
    path('post/eliminar/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path("comentario/create/<int:post_id>/", views.comentario_create, name="comentario_create"),
    path('leyendas/', views.leyenda_list, name='leyenda_list'),
    path('leyendas/create/', views.leyenda_create, name='leyenda_create'), 
    path('leyendas/<int:pk>/', views.LeyendaDetailView.as_view(), name='leyenda_detail'),  
    path('leyendas/<int:pk>/update/', views.LeyendaUpdateView.as_view(), name='leyenda_update'),  
    path('leyendas/<int:pk>/delete/', views.LeyendaDeleteView.as_view(), name='leyenda_delete'),
    path('albums/', views.album_list, name='album_list'),  
    path('create-album/', views.album_create, name='album_create'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('album/<int:pk>/edit/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),

]
