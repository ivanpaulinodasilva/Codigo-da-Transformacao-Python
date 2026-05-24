## 📄 Arquivo `README.md` para o Projeto

```markdown
# 🛒 Sistema de Gerenciamento de Produtos (CRUD Django)

O Django utiliza o padrão MVT (Model-View-Template).

Explique aos alunos que o fluxo de uma requisição web segue estes passos:

O usuário pede uma página (URL).

A View recebe o pedido, conversa com o Model (Banco de Dados) e pega as informações.

A View entrega os dados para o Template (HTML) que renderiza a página bonita para o usuário.

---

## 🛠️ Tecnologias Utilizadas
* **Python** (Linguagem de programação)
* **Django** (Framework Web)
* **SQLite** (Banco de dados padrão)
* **Bootstrap 5** (Estilização visual via CDN)

---

## 🚀 Passo a Passo de Implementação

### Etapa 1: Configuração do Ambiente e Criação do Modelo
1. No terminal, crie a pasta do projeto, instale o Django e inicie a estrutura:
   ```bash
   mkdir aula_django
   cd aula_django
   pip install django
   django-admin startproject config .
   python manage.py startapp produtos

```

2. Adicione o app `'produtos'` dentro da lista `INSTALLED_APPS` no arquivo `config/settings.py`.
3. Defina a estrutura do produto no arquivo `produtos/models.py`:
* Campos: `nome` (CharField), `descricao` (TextField), `preco` (DecimalField) e `quantidade` (IntegerField).


4. Rode as migrações no terminal para criar as tabelas no banco de dados:
```bash
python manage.py makemigrations
python manage.py migrate

```


### Etapa 2: Painel Administrativo e Testes Automatizados

1. Registre o modelo no arquivo `produtos/admin.py` utilizando o decorator `@admin.register(Produto)` e configure o `list_display`.
2. Crie um superusuário no terminal para acessar o painel:
```bash
python manage.py createsuperuser

```


3. Escreva testes no arquivo `produtos/tests.py` herdando de `TestCase` para garantir que o modelo salve os dados corretamente. Rode com:
```bash
python manage.py test

```



### Etapa 3: Criação do CRUD (Views, Forms e Rotas)

1. Crie o arquivo `produtos/forms.py` herdando de `forms.ModelForm` para mapear os campos e aplicar as classes do Bootstrap nos inputs.
2. No arquivo `produtos/views.py`, utilize as *Class-Based Views* do Django:
* `ListView` (Listagem)
* `CreateView` (Cadastro)
* `UpdateView` (Edição)
* `DeleteView` (Exclusão)


3. Crie o arquivo `produtos/urls.py` para mapear as rotas e inclua-o no `config/urls.py` principal usando a função `include()`.
4. Crie a estrutura de pastas `produtos/templates/produtos/` e adicione as telas HTML (`produto_list.html`, `produto_form.html` e `produto_confirm_delete.html`).

### Etapa 4: Desafio Extra (Busca e Paginação)

1. Na `ProdutoListView` (em `views.py`), adicione a propriedade `paginate_by = 5` e sobrescreva o método `get_queryset()` para capturar o parâmetro de busca usando `self.request.GET.get('search')`.
2. No arquivo `produto_list.html`, adicione o formulário de busca no topo e os botões de paginação (`Anterior`/`Próxima`) na parte inferior, lembrando de manter o parâmetro `&search={{ request.GET.search }}` nos links para não perder o filtro ao navegar pelas páginas.

---

## 🏃 Como Rodar o Projeto Localmente

1. Certifique-se de ter o Python instalado.
2. Instale as dependências:
```bash
pip install django

```


3. Execute as migrações (caso mude de computador):
```bash
python manage.py migrate

```


4. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver

```


5. Acesse no seu navegador: `http://127.0.0.1:8000/produtos/`

```

---

