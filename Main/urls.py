from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name="Main"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", LoginView.as_view(template_name='Main/login.html'), name="login"),
    path("logout/", LogoutView.as_view(next_page='Main:index'), name="logout"),
    path("registro/", views.registro, name="registro"),

]