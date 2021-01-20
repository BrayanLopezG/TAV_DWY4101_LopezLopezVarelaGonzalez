from django.shortcuts import render
from .models import Pelicula,Genero,Author

# Create your views here.

def index(request):
    
    num_pelicula = Pelicula.objects.all().count()
    num_authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_pelicula': num_pelicula,'num_authors': num_authors},
    )