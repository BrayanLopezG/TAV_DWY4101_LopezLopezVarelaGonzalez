from pelicula.models import Author
from django.test import TestCase
from  Peliculas.models import Pelicula, Genero


class PeliculaModelTest(TestCase):

    @classmethod

    def setUpTestData(self):
        Pelicula.objects.create(titulo='Piratas del Caribe', 
        descripcion='la peliculaaaaaaaaaaaaaaaaaaa', 
        Autor='Jhon carter adsds', genero='accion')

    def setUpTestData(self):
        Genero.objects.create(nombre='Accion')    

    def test_Pelicula(self):
        Peliculaa=Pelicula.objects.get(id=1)
        field_label= Peliculaa._meta.get_field('Titulo').verbose_name
        self.assertEquals(field_label,'Titulo')

    def test_Genero(self):
        Generoo=Genero.objects.get(nombre='Accion')
        field_label= Generoo._meta.get_field('Nombre').verbose_name
        self.assertEquals(field_label,'Nombre')

    def test_first_titulo_label(self):
        Peliculaa=Pelicula.objects.get(id=1)
        field_label= Peliculaa._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_get_absolute_url(self):
        pelicula=Pelicula.objects.get(id=1)
        self.assertEquals(pelicula.get_absolute_url(),'/pelicula/pelicula/1')



            
    

