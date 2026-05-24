from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

# ==============================================================================
# 📦 CAIXA DE EXPLICAÇÃO 1: O QUE É ESTE ARQUIVO?
# ==============================================================================
"""
📖 GUIA DA AULA - CONSTRUINDO UMA API COMPLETA
--------------------------------------------------------------------------------
Olá, Dev! Este arquivo é o coração do nosso sistema. Ele mistura duas tecnologias:
1. FLASK: O garçom da internet. Ele recebe os pedidos (requisições HTTP) vindos do
   Thunder Client ou navegador, processa e devolve a resposta.
2. SQLITE: O nosso baú de tesouros (Banco de Dados). É um arquivo local chamado 
   'data-base.db' que guarda as tabelas mesmo se o computador for desligado.

FORMATO DE DADOS - JSON:
Quase todas as rotas conversam usando JSON (JavaScript Object Notation), que parece
um dicionário do Python: {"chave": "valor"}. É o padrão universal da web!
--------------------------------------------------------------------------------
"""

# 1. Inicialização do aplicativo Flask
app = Flask(__name__)


# ==============================================================================
# 💾 CAIXA DE EXPLICAÇÃO 2: BANCO DE DADOS (SQLITE)
# ==============================================================================
"""
🛠️ ABERTURA DO BAÚ: O BANCO DE DADOS
--------------------------------------------------------------------------------
A função abaixo (init_db) roda assim que o servidor liga. Ela garante que nosso
banco tenha duas gavetas (Tabelas):
- 'usuarios': Guarda quem está cadastrado (Garante e-mails únicos com UNIQUE).
- 'posts': Guarda os textos do nosso blog e a data exata em que foram criados.
--------------------------------------------------------------------------------
"""

# 2. Conexão e Inicialização do Banco de Dados
def init_db():
    conn = sqlite3.connect('data-base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            data_criacao TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Chama a função para garantir que as tabelas existem
init_db()


# ==============================================================================
# 🌐 CAIXA DE EXPLICAÇÃO 3: AS ROTAS E OS MÉTODOS HTTP
# ==============================================================================
"""
🚦 ROTAS E VERBOS HTTP (O PROTOCOLO DA WEB)
--------------------------------------------------------------------------------
Cada rota abaixo reage a um "Verbo" HTTP diferente. Explique para a turma:
- GET: Usado para BUSCAR ou LER informações (Não altera nada no servidor).
- POST: Usado para ENVIAR novos dados (Salva coisas novas no banco).
- PUT: Usado para ATUALIZAR ou MODIFICAR algo que já existe.
- DELETE: Usado para APAGAR um registro.
--------------------------------------------------------------------------------
"""

# 3. Rotas do Servidor

@app.route('/saudacao', methods=['GET'])
def saudacao():
    return "Olá! Bem-vindo ao meu servidor Flask!"


@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    # Verifica se o cliente enviou dados no formato correto (JSON)
    if not request.is_json:
        return jsonify({"erro": "O corpo da requisição deve ser JSON"}), 400
    
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    
    if not nome or not email:
        return jsonify({"erro": "Nome e e-mail são obrigatórios"}), 400
        
    try:
        conn = sqlite3.connect('data-base.db')
        cursor = conn.cursor()
        # O uso do (?, ?) protege o banco contra invasões (SQL Injection)
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201
    except sqlite3.IntegrityError:
        # Se o e-mail já existir, o banco bloqueia e cai aqui
        return jsonify({"erro": "Este e-mail já está cadastrado"}), 409
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500


@app.route('/posts', methods=['POST'])
def criar_post():
    if not request.is_json:
        return jsonify({"erro": "O corpo da requisição deve ser JSON"}), 400
        
    dados = request.get_json()
    titulo = dados.get('titulo')
    conteudo = dados.get('conteudo')
    
    if not titulo or not conteudo:
        return jsonify({"erro": "Título e conteúdo são obrigatórios"}), 400
        
    # ISOFORMAT cria uma string padronizada com a data e hora do momento da postagem
    data_criacao = datetime.now().isoformat()
    
    try:
        conn = sqlite3.connect('data-base.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO posts (titulo, conteudo, data_criacao) VALUES (?, ?, ?)",
                       (titulo, conteudo, data_criacao))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Post criado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500


@app.route('/posts', methods=['GET'])
def listar_posts():
    posts = []
    try:
        conn = sqlite3.connect('data-base.db')
        # row_factory transforma as linhas do banco em dicionários fáceis de ler no Python
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts")
        posts_db = cursor.fetchall()
        for post in posts_db:
            posts.append(dict(post))
        conn.close()
        return jsonify(posts), 200
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500


# ==============================================================================
# 🔍 CAIXA DE EXPLICAÇÃO 4: PARÂMETROS NA URL (<int:post_id>)
# ==============================================================================
"""
🎯 ROTAS DINÂMICAS (<int:post_id>)
--------------------------------------------------------------------------------
Repare que as próximas rotas possuem o trecho '<int:post_id>'.
Isso diz ao Flask: 'Se o usuário digitar /posts/3, capture o número 3, transforme
em Inteiro e passe para dentro da função como a variável post_id'.
Dessa forma conseguimos manipular um post específico!
--------------------------------------------------------------------------------
"""

@app.route('/posts/<int:post_id>', methods=['GET'])
def ler_post(post_id):
    try:
        conn = sqlite3.connect('data-base.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
        post = cursor.fetchone()
        conn.close()
        if post is None:
            # 404 significa que o recurso procurado não existe no banco
            return jsonify({"erro": "Post não encontrado"}), 404
        return jsonify(dict(post)), 200
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500


@app.route('/posts/<int:post_id>', methods=['PUT'])
def atualizar_post(post_id):
    if not request.is_json:
        return jsonify({"erro": "O corpo da requisição deve ser JSON"}), 400
        
    dados = request.get_json()
    titulo = dados.get('titulo')
    conteudo = dados.get('conteudo')
    
    if not titulo and not conteudo:
        return jsonify({"erro": "Título ou conteúdo são obrigatórios para a atualização"}), 400
        
    try:
        # ⚠️ PEQUENA CORREÇÃO DE ERRO DIGITAÇÃO: mudado de 'database.db' para 'data-base.db'
        conn = sqlite3.connect('data-base.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
        post = cursor.fetchone()
        
        if post is None:
            conn.close()
            return jsonify({"erro": "Post não encontrado"}), 404
            
        # Montagem dinâmica do comando SQL de atualização baseado no que o usuário enviou
        updates = []
        params = []
        if titulo:
            updates.append("titulo = ?")
            params.append(titulo)
        if conteudo:
            updates.append("conteudo = ?")
            params.append(conteudo)
            
        params.append(post_id)
        query = "UPDATE posts SET " + ", ".join(updates) + " WHERE id = ?"
        cursor.execute(query, tuple(params))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Post updated com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500


@app.route('/posts/<int:post_id>', methods=['DELETE'])
def deletar_post(post_id):
    try:
        conn = sqlite3.connect('data-base.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        # cursor.rowcount nos diz quantas linhas foram alteradas/apagadas no banco
        rows_affected = cursor.rowcount
        conn.commit()
        conn.close()
        
        if rows_affected == 0:
            return jsonify({"erro": "Post não encontrado"}), 404
        return jsonify({"mensagem": "Post deletado com sucesso!"}), 200
    except Exception as e:
        return jsonify({"erro": f"Ocorreu um erro: {e}"}), 500


# 4. Bloco condicional para rodar o servidor
if __name__ == '__main__':
    # debug=True faz o servidor reiniciar sozinho a cada alteração salva no código
    app.run(debug=True)