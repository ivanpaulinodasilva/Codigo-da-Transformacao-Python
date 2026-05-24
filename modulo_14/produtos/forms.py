# produtos/forms.py
from django import forms
from .models import Produto

# Criamos um formulário baseado no nosso modelo de Produto
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        # Aqui dizemos quais campos queremos que o usuário preencha na tela
        fields = ['nome', 'descricao', 'preco', 'quantidade']
        
        # Estilização básica para as caixas de texto não ficarem feias
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }