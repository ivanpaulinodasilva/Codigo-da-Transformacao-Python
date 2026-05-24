from flask import Flask, jsonify, request
import sqlite3 # Importamos o módulo nativo do SQLite

app = Flask(__name__)
DATABASE = 'modulo13-database.db' # Nome do arquivo onde os dados serão salvos

# --- FUNÇÃO AUXILIAR: Conecta ao arquivo de banco de dados ---
def conectar_banco():
    conn = sqlite3.connect(DATABASE)
    # Isso permite que a gente acesse os resultados como dicionários (pelo nome da coluna)
    conn.row_factory = sqlite3.Row 
    return conn

# --- FUNÇÃO AUXILIAR: Cria a tabela se ela ainda não existir ---
def inicializar_banco():
    with conectar_banco() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()


# --- ROTA INICIAL (Para evitar erro 404 no navegador) ---
@app.route('/', methods=['GET'])
def pagina_inicial():
    return """
    <html>
        <head><title>Servidor Flask - Questão 3</title></head>
        <body style="font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; background-color: #f4f4f4;">
            <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); display: inline-block;">
                <h2>💾 Servidor com Banco de Dados Ativo!</h2>
                <p>Os dados enviados agora são salvos no SQLite de verdade.</p>
                <ul>
                    <li><strong>Para testar o GET (Questão 1):</strong> Acesse <a href="/saudacao">/saudacao</a></li>
                    <li><strong>Para testar o POST (Questão 3):</strong> Envie o JSON no Insomnia para <code>/cadastrar</code></li>
                </ul>
            </div>
        </body>
    </html>
    """

# Rota da Questão 1 (Mantida)
@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({"mensagem": "Olá! Seja bem-vindo ao servidor Flask."}), 200


# --- QUESTÃO 3: ROTA POST CONECTADA AO SQLITE ---
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.get_json()
    
    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({"erro": "Dados inválidos. Certifique-se de enviar 'nome' e 'email'."}), 400
    
    nome_recebido = dados['nome']
    email_recebido = dados['email']
    
    try:
        # 1. Abre a conexão com o banco
        with conectar_banco() as conn:
            cursor = conn.cursor()
            # 2. Executa o comando SQL para inserir o usuário com segurança (?) contra SQL Injection
            cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome_recebido, email_recebido))
            # 3. Salva a alteração no banco de dados
            conn.commit()
            # 4. Pega o ID gerado automaticamente para o novo usuário
            usuario_id = cursor.lastrowid
            
        return jsonify({
            "status": "sucesso",
            "mensagem": "Usuário salvo no SQLite com sucesso!",
            "usuario_salvo": {
                "id": usuario_id,
                "nome": nome_recebido,
                "email": email_recebido
            }
        }), 201
        
    except sqlite3.IntegrityError:
        # O SQLite gera esse erro caso tentem cadastrar um e-mail que já existe (regra UNIQUE)
        return jsonify({"erro": "Este email já está cadastrado no banco de dados."}), 400
    except Exception as e:
        return jsonify({"erro": f"Erro interno no servidor: {str(e)}"}), 500

import requests

@app.route('/teste-rapido', methods=['GET'])
def teste_rapido():
    # Preparamos os dados que queremos cadastrar no banco
    dados_teste = {
        "nome": "Cliente de Teste",
        "email": "teste_direto_no_navegador@email.com"
    }
    
    # O próprio servidor faz um disparo POST para a rota /cadastrar
    resposta = requests.post("http://127.0.0.1:5000/cadastrar", json=dados_teste)
    
    # Mostra o resultado do cadastro direto na tela do navegador
    return jsonify({
        "info": "Esta rota simulou um envio POST nos bastidores!",
        "resposta_do_banco": resposta.json()
    }), resposta.status_code


if __name__ == '__main__':
    inicializar_banco() # Cria o arquivo de banco e a tabela ANTES de rodar o servidor
    app.run(debug=True)