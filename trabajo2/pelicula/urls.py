from django.urls import path
from . import views

urlpatterns=[ 
    path('', views.index, name='index'),
    path('pelicula/<int:pk>', views.PeliculaDetailView.as_view(), name='pelicula-detail'),
]

urlpatterns+=[
    path('pelicula/create/', views.PeliculaCreate.as_view(), name='pelicula_create'),
    path('pelicula/<int:pk>/update/', views.PeliculaUpdate.as_view(), name='pelicula_update'),
    path('pelicula/<int:pk>/delete/', views.PeliculaDelete.as_view(), name='pelicula_delete'),
]