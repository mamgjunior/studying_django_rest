from django.shortcuts import render

# Create your views here.

def listar_artigos(request, template_name='artigos/index.html'):
    return render(request, template_name)
