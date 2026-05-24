# produtos/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoForm

# 1. VIEW DE LISTAGEM (Read)
class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produto_list.html' # Caminho da tela HTML
    context_object_name = 'produtos'             # Nome da variável que usaremos no HTML

# 2. VIEW DE CADASTRO (Create)
class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('produto_list')   # Para onde o usuário vai após cadastrar (volta para a lista)

# 3. VIEW DE ATUALIZAÇÃO (Update)
class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produtos/produto_form.html' # Reutiliza o mesmo HTML do cadastro!
    success_url = reverse_lazy('produto_list')

# 4. VIEW DE EXCLUSÃO (Delete)
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtos/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')