# produtos/models.py

# Aqui estamos importando as ferramentas de banco de dados que o Django já traz prontas.
from django.db import models

# Criamos a classe 'Produto'. Ela herda (models.Model), o que significa que o Django
# vai dar superpoderes para essa classe se conectar e salvar dados no banco de dados.
class Produto(models.Model):
    
    # Campo para o Nome: Usa o 'CharField' que serve para textos curtos (títulos, nomes).
    # O 'max_length=150' define o limite máximo de 150 caracteres para evitar desperdício de memória.
    # O 'verbose_name' é o rótulo "bonito" que vai aparecer escrito na tela para o usuário.
    nome = models.CharField(max_length=128, verbose_name="Nome do Produto")
    
    # Campo para a Descrição: Usa o 'TextField' que é ideal para textos longos (parágrafos).
    # 'blank=True' significa que no formulário da tela o aluno pode deixar esse campo vazio.
    # 'null=True' avisa o banco de dados que ele aceita receber um valor "vazio" (NULL).
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    
    # Campo para o Preço: Usa o 'DecimalField', perfeito para dinheiro porque não arredonda os centavos de forma errada.
    # 'max_digits=10' significa que o preço pode ter no máximo 10 dígitos no total (ex: 99.999.999,99).
    # 'decimal_places=2' garante que teremos exatamente 2 casas decimais após a vírgula (os centavos).
    preco = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Preço")
    
    # Campo para a Quantidade: Usa o 'IntegerField', que aceita apenas números inteiros (0, 1, 2, 50, etc).
    # Não aceita letras nem números quebrados, ideal para contagem de estoque.
    quantidade = models.IntegerField(verbose_name="Quantidade em Estoque")

    # Este método especial em Python diz ao Django como "chamar" o produto textualmente.
    # Se não colocarmos isso, quando listarmos os produtos, o Django vai mostrar algo genérico como: "Produto object (1)".
    # Retornando 'self.nome', o Django vai mostrar diretamente o nome real do produto (ex: "Notebook Dell").
    def __str__(self):
        return self.nome