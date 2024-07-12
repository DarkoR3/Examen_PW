from django.db import models

# Create your models here.

class Navbar(models.Model):
  id_nav = models.AutoField(db_column='idNav', primary_key=True)
  nom_nav = models.CharField(max_length=20, blank=False, null=False)    
  url_nav = models.CharField(max_length=100, blank=False, null=False)
  def __str__(self):
    return str(self.nom_nav)

class Autores(models.Model):
  id_autores = models.AutoField(db_column='idAutores', primary_key=True)
  nom_autores = models.CharField(max_length=50, blank=False, null=False)
  nac_autores = models.CharField(max_length=50, blank=False, null=False)
  def __str__(self):
    return str(self.nom_autores)

class Categorias(models.Model):
  id_categorias = models.AutoField(db_column='idCategorias', primary_key=True)
  nom_categorias = models.CharField(max_length=100, blank=False, null=False)
  descrip_categorias = models.CharField(max_length=200, blank=False, null=False)
  def __str__(self):
    return str(self.nom_categorias)

class Libro(models.Model):
  id_libro = models.AutoField(db_column='idLibro', primary_key=True)
  nom_libro = models.CharField(max_length=100, blank=False, null=False)
  annio_libro = models.CharField(max_length=50, blank=False, null=False)
  descrip_libro = models.CharField(max_length=1000, blank=False, null=False)
  def __str__(self):
    return str(self.nom_libro)