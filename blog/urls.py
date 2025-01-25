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
    path('leyendas/<int:pk>/', views.LeyendaDetailView.as_view(), name='leyenda_detail'),  # Detalle de una leyenda
    path('leyendas/<int:pk>/update/', views.LeyendaUpdateView.as_view(), name='leyenda_update'),  # Actualizar una leyenda
    path('leyendas/<int:pk>/delete/', views.LeyendaDeleteView.as_view(), name='leyenda_delete'),  # Eliminar una leyenda
    
]
