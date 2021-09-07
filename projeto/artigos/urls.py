from django.urls import path
from .views import listar_artigos

urlpatterns = [
    path('', listar_artigos, name='listar'),
]