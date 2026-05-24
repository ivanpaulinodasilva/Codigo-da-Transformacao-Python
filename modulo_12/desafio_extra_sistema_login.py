import pytest
from flask import Flask, jsonify, request

# ==============================================================================
# 1. APLICAÇÃO FLASK (O CÓDIGO DA API QUE SERÁ TESTADO)
# ==============================================================================
# Em um cenário real, este bloco estaria em um arquivo separado (ex: app.py).
# Para facilitar a entrega, unificamos o app e os testes neste mesmo arquivo.

app = Flask(__name__)

# Banco de dados temporário simulado na memória para os testes
PRODUTOS = [
    {"id": 1, "nome": "Notebook", "preco": 4500.0},
    {"id": 2, "nome": "Smartphone", "preco": 2500.0}
]

@app.route('/api/produtos', methods=['GET'])
def listar_produtos():
    """Rota que retorna a lista completa de produtos."""
    return jsonify(PRODUTOS), 200

@app.route('/api/produtos/<int:produto_id>', methods=['GET'])
def obter_produto(produto_id):
    """Rota que retorna um produto específico pelo ID."""
    produto = next((p for p in PRODUTOS if p["id"] == produto_id), None)
    if produto:
        return jsonify(produto), 200
    return jsonify({"erro": "Produto não encontrado"}), 404

@app.route('/api/produtos', methods=['POST'])
def criar_produto():
    """Rota que cria um novo produto validando os dados enviados."""
    dados = request.get_json()
    
    # Validação simples de entradas inválidas / campos obrigatórios
    if not dados or 'nome' not in dados or 'preco' not in dados:
        return jsonify({"erro": "Dados inválidos. 'nome' e 'preco' são obrigatórios."}), 400
        
    novo_produto = {
        "id": len(PRODUTOS) + 1,
        "nome": dados['nome'],
        "preco": float(dados['preco'])
    }
    PRODUTOS.append(novo_produto)
    return jsonify(novo_produto), 201


# ==============================================================================
# 2. CONFIGURAÇÃO DOS TESTES (PYTEST FIXTURES)
# ==============================================================================

@pytest.fixture
def client():
    """
    Uma Fixture do pytest que configura o cliente de testes do Flask.
    Este cliente simula requisições HTTP (GET, POST, etc.) sem precisar
    rodar o servidor real na rede.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
        
    # Reset do nosso banco de dados simulado após cada teste para garantir isolamento
    global PRODUTOS
    PRODUTOS = [
        {"id": 1, "nome": "Notebook", "preco": 4500.0},
        {"id": 2, "nome": "Smartphone", "preco": 2500.0}
    ]


# ==============================================================================
# 3. CASOS DE TESTE AUTOMATIZADOS (PYTEST)
# ==============================================================================

def test_listar_produtos_deve_retornar_status_200_e_lista(client):
    """Testa se a rota GET /api/produtos retorna todos os itens corretamente."""
    # Executa a requisição simulada
    resposta = client.get('/api/produtos')
    
    # Asserções (Validações)
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert isinstance(dados, list)
    assert len(dados) == 2
    assert dados[0]['nome'] == "Notebook"

def test_obter_produto_por_id_com_sucesso(client):
    """Testa se a busca de um produto existente pelo ID funciona."""
    resposta = client.get('/api/produtos/2')
    
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert dados['id'] == 2
    assert dados['nome'] == "Smartphone"

def test_obter_produto_inexistente_deve_retornar_404(client):
    """Validação de entrada/ID inválido: busca por um produto que não existe."""
    resposta = client.get('/api/produtos/999')
    
    assert resposta.status_code == 404
    dados = resposta.get_json()
    assert "erro" in dados
    assert dados['erro'] == "Produto não encontrado"

def test_criar_produto_com_sucesso(client):
    """Testa o cadastro de um novo produto via método POST."""
    novo_item = {"nome": "Teclado Mecânico", "preco": 350.0}
    
    # Envia os dados no formato JSON
    resposta = client.post('/api/produtos', json=novo_item)
    
    assert resposta.status_code == 201
    dados = resposta.get_json()
    assert dados['id'] == 3
    assert dados['nome'] == "Teclado Mecânico"

def test_criar_produto_invalido_deve_retornar_400(client):
    """Validação de entrada inválida: tenta criar produto sem o campo obrigatório 'preco'."""
    item_invalido = {"nome": "Monitor Gamer"} # Falta o preço
    
    resposta = client.post('/api/produtos', json=item_invalido)
    
    assert resposta.status_code == 400
    dados = resposta.get_json()
    assert "erro" in dados
    assert "obrigatórios" in dados['erro']