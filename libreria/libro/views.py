from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
	navbar = Navbar.objects.all() #llama a todos los objetos de la tabla navbar en modelos
	context = {
		'navbar' : navbar
	}
	return render (request, 'libro/index.html', context)

def autores(request):
	navbar = Navbar.objects.all()
	autores = Autores.objects.all()
	context = {
		'navbar' : navbar,
		'autores' : autores
	}
	return render (request, 'libro/autores.html', context)

def libros(request):
	navbar = Navbar.objects.all()
	libros = Libro.objects.all()
	context = {
		'navbar' : navbar,
		'libros' : libros
	}
	return render (request, 'libro/libros.html', context)

def categorias(request):
	categorias = Categorias.objects.all()
	navbar = Navbar.objects.all()
	context = {
		'navbar' : navbar,
		'categorias' : categorias
	}
	return render (request, 'libro/categorias.html', context)


