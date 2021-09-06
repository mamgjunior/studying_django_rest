from django.db import models
from django.db.models import fields
from rest_framework import serializers
from artigos.models import Autor, Artigo


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ('id', 'nome', 'endereco', 'site', 'email')


class ArtigoSerializer(serializers.ModelSerializer):
    autor = AutorSerializer
    class Meta:
        model = Artigo
        fields = ('id', 'titulo', 'publicado_em', 'atualizado_em', 'texto', 'autor')