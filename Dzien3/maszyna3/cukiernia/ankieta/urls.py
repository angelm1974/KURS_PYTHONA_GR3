from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pytanie_id>/szczegoly', views.szczegoly, name='szczegoly'),
    path('<int:pytanie_id>/wyniki', views.wyniki, name='wyniki'),
    path('<int:pytanie_id>/glosuj', views.glosuj, name='glosuj'),
    
]
