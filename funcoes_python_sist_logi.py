# ======================================================================
# 🚀 Desafio Extra: Sistema de Login Simples
# ======================================================================

# 📋 Passo 1: O nosso "banco de dados" de usuários
# Usamos um dicionário onde a CHAVE é o nome do usuário
# e o VALOR é a senha correspondente.
usuarios = {
    "admin": "admin123",
    "joao": "senha123",
    "maria": "abc456"
}

# ======================================================================
# 📋 Passo 2: A função para validar o login
# A função 'validar_login' recebe o nome e a senha digitados.
def validar_login(nome_usuario, senha_digitada):
    # Verificamos se o nome de usuário existe no nosso dicionário.
    if nome_usuario in usuarios:
        # Se existir, verificamos se a senha digitada é igual à senha guardada.
        if usuarios[nome_usuario] == senha_digitada:
            return True  # Login bem-sucedido!
        else:
            return False # Senha incorreta.
    else:
        return False # Usuário não encontrado.

# ======================================================================
# 🔄 Passo 3: O Loop do Programa Principal
# O loop pede o login até que a validação seja verdadeira.
while True:
    print("\n--- Sistema de Login ---")
    nome_usuario = input("Digite seu nome de usuário (ou 'sair' para fechar): ")
    
    # Se o usuário digitar 'sair', o programa termina.
    if nome_usuario.lower() == 'sair':
        print("👋 Fechando o programa. Até mais!")
        break
    
    senha_digitada = input("Digite sua senha: ")

    # Chamamos a nossa função para verificar se o login é válido.
    if validar_login(nome_usuario, senha_digitada):
        print(f"\n🎉 Login bem-sucedido! Bem-vindo(a), {nome_usuario}!")
        break # O login deu certo, então saímos do loop.
    else:
        print("\n❌ Login inválido. Tente novamente.")

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================