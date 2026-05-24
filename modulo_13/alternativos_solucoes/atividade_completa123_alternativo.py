'''
Servidor Flask Unificado para as Questões 1, 2 e 3

Este código combina as funcionalidades das três questões em um único servidor Flask. Ele inclui:
- Uma rota GET para saudação (Questão 1)
- Uma rota POST para cadastrar usuários recebendo JSON (Questão 2)
- Integração com SQLite para armazenar os usuários cadastrados (Questão 3)

Instruções para Testar:
1. Certifique-se de ter o Flask e o SQLite instalados.
2. Salve este código em um arquivo chamado `app.py`.
3. Execute o servidor com o comando: `python app.py`
4. Teste as rotas:
- Acesse no navegador:
http://127.0.0.1:5000/saudacao. Você verá o JSON de boas-vindas.
- Use o Thunder Client ou Postman para enviar um POST para:
http://127.0.0.1:5000/cadastrar
Com o seguinte JSON no corpo da requisição:
POST http://127.0.0.1:5000/cadastrar
Content-Type: application/json
{
  "nome": "Aluno Exemplo",
  "email": "aluno@escola.com"
}
5. Verifique a resposta JSON para confirmar que o usuário foi salvo no banco de dados.
6. Você pode verificar o conteúdo do banco de dados usando um cliente SQLite ou um comando como
sqlite3 database_completo.db "SELECT * FROM usuarios;"

'''

from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)
DATABASE = 'database_completo.db'

# 💾 CONFIGURAÇÃO DO BANCO DE DADOS (QUESTÃO 3)
def conectar_banco():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome (ex: linha['nome'])
    return conn

def inicializar_banco():
    """Cria a tabela de usuários se ela ainda não existir no sistema."""
    with conectar_banco() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()


# 🌐 ROTAS DA API

# Rota Raiz (Amigável para o Navegador)
@app.route('/', methods=['GET'])
def pagina_inicial():
    return """
    <html>
        <head><title>API Flask Unificada</title></head>
        <body style="font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; background-color: #f4f4f4;">
            <div style="background: white; padding: 25px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); display: inline-block;">
                <h2>🚀 Servidor Flask Unificado (Questões 1, 2 e 3)</h2>
                <p>O servidor está rodando e o SQLite está pronto!</p>
                <hr>
                <h3>📌 Como testar as rotas:</h3>
                <ul>
                    <li><strong>Questão 1 (GET):</strong> Abra no navegador -> <a href="/saudacao">/saudacao</a></li>
                    <li><strong>Questões 2 e 3 (POST + SQLite):</strong> No Thunder Client, envie um <code>POST</code> para <code>/cadastrar</code> com o JSON de usuário.</li>
                </ul>
            </div>
        </body>
    </html>
    """


# QUESTÃO 1: Rota GET simples que responde uma mensagem
@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({
        "mensagem": "Olá! Seja bem-vindo ao servidor Flask.",
        "questao": 1,
        "status": "sucesso"
    }), 200


# QUESTÕES 2 e 3: Rota POST que recebe JSON e salva no SQLite
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    # [Questão 2] Captura o JSON enviado no corpo da requisição
    dados = request.get_json()
    
    # [Questão 2] Validação dos campos obrigatórios
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({"erro": "Dados inválidos. Envie 'nome' e 'email' no JSON."}), 400
    
    nome_recebido = dados['nome']
    email_recebido = dados['email']
    
    # [Questão 3] Tentativa de salvar os dados no banco SQLite
    try:
        with conectar_banco() as conn:
            cursor = conn.cursor()
            # Insere os dados usando interrogações (?) por segurança contra SQL Injection
            cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome_recebido, email_recebido))
            conn.commit()
            novo_id = cursor.lastrowid  # Captura o ID gerado automaticamente
            
        # Resposta de sucesso contendo os dados do banco
        return jsonify({
            "status": "sucesso",
            "mensagem": "Usuário recebido (Q2) e salvo no banco de dados (Q3)!",
            "usuario_salvo": {
                "id": novo_id,
                "nome": nome_recebido,
                "email": email_recebido
            }
        }), 201
        
    except sqlite3.IntegrityError:
        # Erro caso tentem cadastrar o mesmo e-mail duas vezes (UNIQUE constraint)
        return jsonify({"erro": "Este email já está cadastrado no banco de dados."}), 400
    except Exception as e:
        return jsonify({"erro": f"Erro interno no servidor: {str(e)}"}), 500


# 🏃‍♂️ INICIALIZAÇÃO DO SERVIDOR
if __name__ == '__main__':
    inicializar_banco()  # Garante que o arquivo 'database_completo.db' exista antes do app rodar
    app.run(debug=True)