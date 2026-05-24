# produtos/models.py

from django.db import models

class Produto(models.Model):
    """
    Representa um produto na loja.
    """
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.nome