from rest_framework import viewsets
from artigos.models import Autor, Artigo
from .serializers import AutorSerializer, ArtigoSerializer

# - Pacote para trabalhar com permissões
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
"""
    - IsAuthenticated: Faz com que apenas usuários logados usem a api
    - AllowAny: Permite que qualquer um tenha acesso a api
    - IsAuthenticatedOrReadOnly: Libera o acesso a usuários não logados porem os mesmo não podem alterar nada na api
"""


class AutorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class ArtigoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer
