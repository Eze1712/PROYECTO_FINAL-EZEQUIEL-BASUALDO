from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  
from .models import Post, Comentario, Leyenda, Album
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect


# ============================= PUBLICACIONES(POSTS)=========================================================
def post_list(request):
    query = request.GET.get('q', '')
    if query:
        post_list = Post.objects.filter(
            Q(titulo__icontains=query) | 
            Q(contenido__icontains=query) | 
            Q(autor__username__icontains=query) |
            Q(comentarios__contenido__icontains=query)
        ).distinct()
    else:
        post_list = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': post_list})

# Permite crear una nueva publicación
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  
            post.autor = request.user 
            post.save()  
            return redirect('blog:post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

# ========================CRUD PARA POSTS=========================================================
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        
        if post.autor != self.request.user:
            context['error_message'] = "No tienes permiso para eliminar este post."
            return context
        
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        
        if post.autor != request.user:
            return redirect('blog:post_list')
        
        return super().post(request, *args, **kwargs)
    
    
# ============================= COMENTARIOS DE LOS POSTS=========================================================

# Permite crear un comentario en una publicación específica
def comentario_create(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            
            if request.user.is_authenticated:
                comentario.usuario = request.user
            
            comentario.post = post
            comentario.save()
            return redirect('blog:post_list')
    else:
        form = ComentarioForm()
    
    return render(request, 'blog/comentario_create.html', {"form": form, "post": post})




# ======================== LEYENDAS=========================================================
def leyenda_create(request):
    if request.method == "POST":
        form = LeyendaForm(request.POST)
        if form.is_valid():
            leyenda = form.save(commit=False)  # No guarda inmediatamente
            leyenda.usuario = request.user  # Asigna el usuario autenticado automáticamente
            leyenda.save()  # Guarda la leyenda en la base de datos
            return redirect('blog:leyenda_list')
    else:
        form = LeyendaForm()
    return render(request, 'blog/leyenda_create.html', {'form': form})


# Muestra una lista de leyendas creadas
def leyenda_list(request):
    leyendas = Leyenda.objects.all()
    return render(request, 'blog/leyenda_list.html', {'leyendas': leyendas})

# ========================CRUD PARA LEYENDAS=========================================================
# Lista todas las leyendas creadas
class LeyendaListView(ListView):
    model = Leyenda
    template_name = 'leyenda_list.html'
    context_object_name = 'leyendas'

# Muestra los detalles de una leyenda específica
class LeyendaDetailView(DetailView):
    model = Leyenda
    template_name = 'blog/leyenda_detail.html'
    context_object_name = 'leyenda'

# Permite crear una nueva leyenda
class LeyendaCreateView(CreateView):
    model = Leyenda
    template_name = 'leyenda_create.html'
    fields = ['titulo', 'contenido', 'autor']
    success_url = reverse_lazy('leyenda_list')

# Permite actualizar una leyenda existente
class LeyendaUpdateView(UpdateView):
    model = Leyenda
    template_name = 'blog/leyenda_update.html'
    fields = ['nombre', 'fecha_nacimiento', 'genero', 'historia']
    success_url = reverse_lazy('blog:leyenda_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        leyenda = self.get_object()

        # Verificar si el usuario es el autor de la leyenda
        if leyenda.autor != self.request.user:
            context['error_message'] = "No tienes permiso para editar esta leyenda."
            # Al no permitir editar, deshabilitamos el formulario
            context['form'] = None
            return context
        
        return context

    def form_valid(self, form):
        leyenda = form.save(commit=False)
        leyenda.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))  

# Permite eliminar una leyenda existente
class LeyendaDeleteView(DeleteView):
    model = Leyenda
    template_name = 'blog/leyenda_delete.html'
    context_object_name = 'leyenda'
    success_url = reverse_lazy('blog:leyenda_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        leyenda = self.get_object()
        
        if leyenda.autor != self.request.user:
            context['error_message'] = "No tienes permiso para eliminar esta leyenda."
            return context
        
        return context

    def post(self, request, *args, **kwargs):
        leyenda = self.get_object()
        
        if leyenda.autor != request.user:
            return redirect('blog:leyenda_list')
        
        return super().post(request, *args, **kwargs)


#====================================== ALBUMES VISTAS =========================================
# Vista de creación de álbumes
def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.usuario = request.user  
            album.save()
            return redirect('blog:album_list')  
    else:
        form = AlbumForm()

    return render(request, 'blog/album_create.html', {'form': form})


# Vista de lista de albumes
def album_list(request):
    albums = Album.objects.all()  # Obtener todos los álbumes
    return render(request, 'blog/album_list.html', {'albums': albums})


#====================================== CRUD PARA ÁLBUMES =========================================
# Lista todos los álbumes creados
class AlbumListView(ListView):
    model = Album
    template_name = 'blog/album_list.html'
    context_object_name = 'albums'


# Muestra los detalles de un álbum específico
class AlbumDetailView(DetailView):
    model = Album
    template_name = 'blog/album_detail.html'
    context_object_name = 'album'


# Permite crear un nuevo álbum
class AlbumCreateView(CreateView):
    model = Album
    template_name = 'blog/album_create.html'
    fields = ['nombre', 'fecha_lanzamiento', 'genero', 'autor_album', 'historia']
    success_url = reverse_lazy('blog:album_list')

    def form_valid(self, form):
        album = form.save(commit=False)
        album.autor = self.request.user  # Asignar el autor automáticamente al usuario actual
        album.save()
        return redirect(self.success_url)


# Permite actualizar un álbum existente
class AlbumUpdateView(UpdateView):
    model = Album
    template_name = 'blog/album_update.html'
    fields = ['nombre', 'descripcion', 'genero', 'autor_album']
    success_url = reverse_lazy('blog:album_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()

        # Verificar si el usuario es el autor del álbum
        if album.autor_album != self.request.user:
            context['error_message'] = "No tienes permiso para editar este álbum."
            context['form'] = None  # Deshabilitamos el formulario si no tiene permisos
            return context
        
        return context

    def form_valid(self, form):
        album = form.save(commit=False)
        album.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


# Permite eliminar un álbum existente
class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'blog/album_delete.html'
    context_object_name = 'album'
    success_url = reverse_lazy('blog:album_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()

        if album.autor != self.request.user:
            context['error_message'] = "No tienes permiso para eliminar este álbum."
            return context
        
        return context

    def post(self, request, *args, **kwargs):
        album = self.get_object()

        if album.autor != request.user:
            return redirect('blog:album_list')

        return super().post(request, *args, **kwargs)
