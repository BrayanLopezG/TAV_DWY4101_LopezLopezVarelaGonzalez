from django.shortcuts import render
from .models import Pelicula,Genero,Author
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

def index(request):
    
    num_pelicula = Pelicula.objects.all().count()
    num_authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_pelicula': num_pelicula,'num_authors': num_authors},
    )

class PeliculaCreate(CreateView):
    model = Pelicula
    fields = '__all__'

class PeliculaUpdate(UpdateView):
    model = Pelicula
    fields = ['titulo','descripcion','autor','genero',]

class PeliculaDelete(DeleteView):
    model = Pelicula
    success_url = reverse_lazy('peliculas')

class PeliculaDetailView(generic.DetailView):
    model = Pelicula