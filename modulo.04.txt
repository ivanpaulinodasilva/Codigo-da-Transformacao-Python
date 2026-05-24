# ======================================================================
# 🚀 Projeto: Minha Primeira Função
# ======================================================================

# 📋 Passo 1: Definir a função
# Usamos 'def' para "definir" a função e damos a ela um nome.
# 'nome' é um parâmetro. É como uma variável que a função espera receber.
def saudacao(nome):
    # O código dentro da função é o que ela vai fazer.
    # Usamos o nome recebido para criar a mensagem personalizada.
    print(f"Olá, {nome}! Que bom te ver por aqui.")

# ======================================================================
# 🔄 Passo 2: Chamar a função
# Agora que a função está pronta, podemos "chamá-la" ou "usá-la".
# O que está entre parênteses é o valor que enviamos para o parâmetro 'nome'.

print("--- Chamando a função 'saudacao' ---")

# Chamada 1: Saudar o usuário
saudacao("João")

# Chamada 2: Saudar outra pessoa
saudacao("Maria")

# Chamada 3: Saudar o próprio nome
meu_nome = "Parceiro de Programação"
saudacao(meu_nome)

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================