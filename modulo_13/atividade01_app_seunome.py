# Importamos a classe Flask e a função jsonify (para responder em formato JSON)
from flask import Flask, jsonify

# Inicializamos a aplicação Flask
app = Flask(__name__)

# Definimos a rota /saudacao que aceita apenas requisições GET
@app.route('/saudacao', methods=['GET'])

def saudacao():
    # Retornamos um dicionário Python convertido para JSON e o status HTTP 200 (Sucesso)
    return jsonify({"mensagem": "Olá! Seja bem-vindo ao servidor Flask."}), 200

@app.route('/', methods=['GET'])

def pagina_inicial():
    return "<h3>Servidor Ativo! Para ver a saudação, acesse <a href='/saudacao'>/saudacao</a></h3>"

# Garante que o servidor só rode se o arquivo for executado diretamente
if __name__ == '__main__':
    # rodamos o app em modo de depuração (debug=True) para atualizar automaticamente se mudarmos o código
    app.run(debug=True)