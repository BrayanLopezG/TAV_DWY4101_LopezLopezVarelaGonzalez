from django.urls import path
from . import views

urlpatterns=[ 
    path('', views.index, name='index'),
    path('ranking/', views.ranking, name='ranking'),
    path('contacto/', views.contacto, name='contacto'),
    path('pelicula/<int:pk>', views.PeliculaDetailView.as_view(), name='pelicula_detail'),
    path('author/<int:pk>/',views.AuthorDetailView.as_view(), name='author_detail')
]

urlpatterns+=[
    path('pelicula/', views.PeliculaListView.as_view(), name='pelicula_list'),
    path('pelicula/create/', views.PeliculaCreate.as_view(), name='pelicula_create'),
    path('pelicula/update/<int:pk>/', views.PeliculaUpdate.as_view(), name='pelicula_update'),
    path('pelicula/delete/<int:pk>/', views.PeliculaDelete.as_view(), name='pelicula_delete'),
    path('author/',views.AuthorListView.as_view(), name='author_list'),
    path('author/create/',views.AuthorCreate.as_view(), name='author_create'),
    path('author/update/<int:pk>/',views.AuthorUpdate.as_view(), name='author_update'),
    path('author/delete/<int:pk>/',views.AuthorDelete.as_view(), name='author_delete'),
]