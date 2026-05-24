# ======================================================================
# 🚀 Projeto: Manipulação de Arquivos .txt
# ======================================================================

# Importamos o módulo 'os' para trabalhar com caminhos de arquivos de forma segura.
import os

# 📋 Passo 1: Definir o caminho da pasta e o nome do arquivo
# Define o caminho da pasta que você especificou.
caminho_pasta = "GitHub/Codigo-da-Transformacao-Python"
nome_arquivo = "meu_primeiro_arquivo.txt"

# Usamos 'os.path.join' para unir o caminho da pasta e o nome do arquivo.
# Isso garante que a barra divisória (/) seja a correta para o seu sistema.
caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

# ======================================================================
# 🔄 Passo 2: Escrever no arquivo
# Usamos 'with open(...)' para abrir o arquivo. O 'with' garante que o
# arquivo seja fechado automaticamente, mesmo se der algum erro.
# O modo 'w' significa "write" (escrever). Ele cria ou sobrescreve o arquivo.
print("--- Escrevendo no arquivo... ---")
with open(caminho_completo, 'w') as arquivo:
    arquivo.write("Olá, este é o meu primeiro arquivo de texto criado com Python!\n")
    arquivo.write("Estou aprendendo a salvar informações. Que legal!\n")
    print("Conteúdo escrito com sucesso!")

# ======================================================================
# 👁️ Passo 3: Ler o conteúdo do arquivo
# Agora vamos abrir o mesmo arquivo novamente, mas no modo de leitura 'r'.
# O 'r' significa "read" (ler).
print("\n--- Lendo o conteúdo do arquivo... ---")
with open(caminho_completo, 'r') as arquivo:
    # A função 'read()' lê todo o conteúdo do arquivo.
    conteudo = arquivo.read()
    print("Conteúdo lido:")
    print(conteudo)

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================