# produtos/tests.py

# Importamos a ferramenta de testes do Django
from django.test import TestCase

# Importamos o modelo que queremos testar
from .models import Produto

class ProdutoModelTest(TestCase):

    # Este método roda antes do teste para criar um produto de exemplo no banco de dados temporário
    def setUp(self):
        self.produto_exemplo = Produto.objects.create(
            nome="Caneta Azul",
            descricao="Caneta esferográfica azul",
            preco=2.50,
            quantidade=100
        )

    # Este é o teste real. Todo método de teste precisa começar com a palavra 'test_'
    def test_criacao_do_produto(self):
        # O código abaixo verifica se o produto foi salvo com o nome correto
        self.assertEqual(self.produto_exemplo.nome, "Caneta Azul")
        
        # Verifica se o preço foi salvo corretamente
        self.assertEqual(self.produto_exemplo.preco, 2.50)

    # Testamos se o método __str__ que configuramos no modelo está retornando o nome do produto
    def test_retorno_str_do_modelo(self):
        self.assertEqual(str(self.produto_exemplo), "Caneta Azul")