# Adicionamos o 'request' na linha de importação
from flask import Flask, jsonify, request

app = Flask(__name__)

# --- ADAPTAÇÃO: Rota Inicial para evitar o erro 404 no navegador ---
@app.route('/', methods=['GET'])
def pagina_inicial():
    return """
    <html>
        <head><title>Servidor Flask - Questão 2</title></head>
        <body style="font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; background-color: #f4f4f4;">
            <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); display: inline-block;">
                <h2>🚀 Servidor Flask Ativo!</h2>
                <p>O seu servidor está rodando perfeitamente.</p>
                <ul>
                    <li><strong>Para testar o GET (Questão 1):</strong> Acesse <a href="/saudacao">/saudacao</a></li>
                    <li><strong>Para testar o POST (Questão 2):</strong> A rota <code>/cadastrar</code> está pronta! Como o navegador comum não envia POST diretamente, use uma ferramenta de testes (como Postman ou Insomnia) enviando um JSON com 'nome' e 'email'.</li>
                </ul>
            </div>
        </body>
    </html>
    """

# Rota da Questão 1 (Mantida)
@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({"mensagem": "Olá! Seja bem-vindo ao servidor Flask."}), 200

# Rota da Questão 2: Receber dados em formato JSON
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    # O request.get_json() captura o objeto JSON enviado no corpo da requisição
    dados = request.get_json()
    
    # Validação simples: garante que o usuário enviou 'nome' e 'email'
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({"erro": "Dados inválidos. Certifique-se de enviar 'nome' e 'email'."}), 400
    
    # Extrai os dados do JSON recebido
    nome_recebido = dados['nome']
    email_recebido = dados['email']
    
    # Retorna uma resposta de sucesso confirmando o recebimento
    return jsonify({
        "status": "sucesso",
        "mensagem": f"Usuário {nome_recebido} recebido com sucesso no servidor!",
        "dados_enviados": {
            "nome": nome_recebido,
            "email": email_recebido
        }
    }), 201

if __name__ == '__main__':
    app.run(debug=True)