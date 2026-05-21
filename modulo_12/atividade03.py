from flask import Flask, jsonify
import pytest

# 1. Criação de uma API Flask simples para o teste
app = Flask(__name__)

@app.route('/api/somar/<int:num1>/<int:num2>', methods=['GET'])
def api_somar(num1, num2):
    # Rota que recebe dois números pela URL e retorna o resultado em JSON
    resultado = num1 + num2
    return jsonify({"resultado": resultado}), 200

# 2. Configuração do Pytest (Fixture)
@pytest.fixture
def client():
    # Cria um cliente de testes do Flask. Ele simula o navegador/Postman.
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 3. Função de Teste da API
def test_rota_soma_com_sucesso(client):
    # Explicação: Enviamos uma requisição simulada para a rota de soma
    resposta = client.get('/api/somar/5/5')
    
    # Verificamos se o status do servidor é 200 (Sucesso)
    assert resposta.status_code == 200
    
    # Verificamos se os dados retornados no JSON estão corretos
    assert resposta.get_json() == {"resultado": 10}