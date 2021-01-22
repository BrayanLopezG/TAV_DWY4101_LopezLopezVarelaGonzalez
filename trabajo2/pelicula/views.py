from django.shortcuts import render
from .models import Pelicula,Genero,Author
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import DateDetailView,ListView
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

def index(request):
    return render(
        request,
        'index.html',
    )

def ranking(request):
    return render(
        request,
        'ranking.html',
    )

def contacto(request):
    return render(
        request,
        'contacto.html',
    )


class PeliculaCreate(CreateView):
    model = Pelicula
    fields = '__all__'

class PeliculaUpdate(UpdateView):
    model = Pelicula
    fields = ['titulo','descripcion','autor','genero']

class PeliculaDelete(DeleteView):
    model = Pelicula
    success_url = reverse_lazy('index')

class PeliculaDetailView(generic.DetailView):
    model = Pelicula

class PeliculaListView(ListView):
    model = Pelicula
