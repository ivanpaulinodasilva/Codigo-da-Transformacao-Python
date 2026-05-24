# produtos/admin.py

# Importamos a ferramenta de administração do Django
from django.contrib import admin

# Importamos o modelo Produto que criamos no passo anterior
from .models import Produto

# Aqui dizemos ao Django para mostrar o Produto no painel de controle
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # 'list_display' define quais colunas vão aparecer na tabela de listagem do painel
    list_display = ('nome', 'preco', 'quantidade')
    
    # 'search_fields' cria uma barra de busca dentro do painel administrativo
    search_fields = ('nome',)

'''
admin
admin@mail.com
@Zaq123123
'''