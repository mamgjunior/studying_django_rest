from django.db import router
from django.urls import path, include
from rest_framework import routers
from .views import AutorViewSet, ArtigoViewSet


router = routers.DefaultRouter()

router.register('autor', AutorViewSet)
router.register('artigo', ArtigoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
