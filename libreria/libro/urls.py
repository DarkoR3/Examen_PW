from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('autores', views.autores, name="autores"),
    path('categorias', views.categorias, name="categorias"),
    path('libros', views.libros, name="libros"),
]
