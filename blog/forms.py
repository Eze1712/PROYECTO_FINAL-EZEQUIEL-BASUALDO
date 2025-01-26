from django import forms
from .models import Album, Post, Comentario, Leyenda 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'estado', 'categoria']

   
    categoria = forms.ChoiceField(
        choices=Post._meta.get_field('categoria').choices,  
        required=True  
    )

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido'] 

class LeyendaForm(forms.ModelForm):
    class Meta:
        model = Leyenda
        fields = ['nombre', 'fecha_nacimiento', 'genero', 'historia']

class SearchForm(forms.Form):
    query = forms.CharField(label="Buscar", max_length=100)


#=================================== ALBUMES FORM ===============================================
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nombre', 'fecha_lanzamiento', 'genero', 'historia', 'autor_album']