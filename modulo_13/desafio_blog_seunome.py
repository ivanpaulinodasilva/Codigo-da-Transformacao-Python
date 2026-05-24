from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configurações obrigatórias para o funcionamento do JWT
app.config["JWT_SECRET_KEY"] = "chave-super-secreta-do-nosso-blog-2026" 
jwt = JWTManager(app)

DATABASE = 'database-blog.db'

# --- FUNÇÕES DO BANCO DE DADOS ---
def conectar_banco():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_banco():
    with conectar_banco() as conn:
        # Tabela de Usuários (com senhas que serão salvas criptografadas)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        # Tabela de Posts (Vincula o autor_id ao id da tabela usuarios)
        conn.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL,
                autor_id INTEGER NOT NULL,
                FOREIGN KEY (autor_id) REFERENCES usuarios (id)
            )
        ''')
        conn.commit()


#  ROTA INICIAL INFORMATIVA ---
@app.route('/', methods=['GET'])
def pagina_inicial():
    return """
    <html>
        <head><title>API de Blog - Desafio</title></head>
        <body style="font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; background-color: #f4f4f4;">
            <div style="background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); max-width: 600px;">
                <h2>📝 API de Blog Ativa! (Desafio Concluído)</h2>
                <p>Rotas disponíveis na API (todas interagem via JSON):</p>
                <ul>
                    <li><code>POST /auth/registrar</code> - Cadastrar um novo usuário.</li>
                    <li><code>POST /auth/login</code> - Fazer login e receber o Token JWT.</li>
                    <li><code>POST /posts</code> - Criar um post <strong>(Requer o Token JWT)</strong>.</li>
                    <li><code>GET /posts</code> - Listar todos os posts salvos (Público).</li>
                </ul>
                <p>Use o <strong>Thunder Client</strong> no VS Code para realizar os testes!</p>
            </div>
        </body>
    </html>
    """


# 🔐 1. ROTAS DE AUTENTICAÇÃO

@app.route('/auth/registrar', methods=['POST'])
def registrar():
    dados = request.get_json()
    if not dados or 'username' not in dados or 'password' not in dados:
        return jsonify({"erro": "Envie 'username' e 'password' no JSON."}), 400
    
    # generate_password_hash transforma a senha "1234" em algo ilegível como "scrypt:32768..."
    senha_criptografada = generate_password_hash(dados['password'])
    
    try:
        with conectar_banco() as conn:
            conn.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', 
                         (dados['username'], senha_criptografada))
            conn.commit()
        return jsonify({"mensagem": "Usuário registrado com sucesso!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Esse nome de usuário já existe."}), 400


@app.route('/auth/login', methods=['POST'])
def login():
    dados = request.get_json()
    if not dados or 'username' not in dados or 'password' not in dados:
        return jsonify({"erro": "Envie 'username' e 'password'."}), 400
    
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE username = ?', (dados['username'],))
        usuario = cursor.fetchone()
        
    # check_password_hash compara a senha digitada com o hash criptografado salvo no banco
    if usuario and check_password_hash(usuario['password'], dados['password']):
        # Geramos um token de acesso que carrega o ID do usuário de forma segura
        token_acesso = create_access_token(identity=str(usuario['id']))
        return jsonify({
            "mensagem": "Login realizado com sucesso!",
            "token": token_acesso
        }), 200
        
    return jsonify({"erro": "Usuário ou senha incorretos."}), 401


# 📰 2. ROTAS DO BLOG (POSTS)

# Criar Post: Esta rota possui o decorator @jwt_required(), ou seja, está protegida!
@app.route('/posts', methods=['POST'])
@jwt_required()
def criar_post():
    # get_jwt_identity descobre automaticamente quem é o usuário dono do Token que enviou a requisição
    id_autor_logado = get_jwt_identity()
    dados = request.get_json()
    
    if not dados or 'titulo' not in dados or 'conteudo' not in dados:
        return jsonify({"erro": "Envie 'titulo' e 'conteudo'."}), 400
    
    with conectar_banco() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO posts (titulo, conteudo, autor_id) VALUES (?, ?, ?)', 
                       (dados['titulo'], dados['conteudo'], id_autor_logado))
        conn.commit()
        post_id = cursor.lastrowid
        
    return jsonify({
        "mensagem": "Post publicado com sucesso!",
        "post_id": post_id
    }), 201


# Listar Posts: Rota pública. Qualquer um pode ler os posts, mesmo sem estar logado.
@app.route('/posts', methods=['GET'])
def listar_posts():
    with conectar_banco() as conn:
        cursor = conn.cursor()
        # O INNER JOIN serve para trazer o nome real do autor em vez de apenas o número do ID dele
        cursor.execute('''
            SELECT posts.id, posts.titulo, posts.conteudo, usuarios.username AS autor 
            FROM posts 
            INNER JOIN usuarios ON posts.autor_id = usuarios.id
        ''')
        # Converte as linhas do banco de dados em dicionários Python para o jsonify funcionar
        todos_posts = [dict(linha) for linha in cursor.fetchall()]
        
    return jsonify(todos_posts), 200


if __name__ == '__main__':
    inicializar_banco() # Cria o banco 'database-blog.db' e as tabelas necessárias
    app.run(debug=True)