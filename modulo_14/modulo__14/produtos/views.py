# produtos/views.py

from django.shortcuts import render
from .models import Produto

def lista_produtos(request):
    """
    Visualização para listar todos os produtos.
    """
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'produtos/listaprodutos.html', context)