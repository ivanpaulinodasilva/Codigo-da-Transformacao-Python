# ======================================================================
# 🚀 Projeto: Sistema de Notas em Arquivo CSV (com Caminho Específico)
# ======================================================================

# Importamos os módulos necessários: 'csv' para arquivos de tabela e 'os' para caminhos.
import csv
import os

# 📋 Passo 1: Definir o caminho da pasta e o arquivo
# Define o caminho da pasta onde o arquivo será salvo.
caminho_pasta = "GitHub/Codigo-da-Transformacao-Python"
nome_arquivo = "notas.csv"

# Usamos 'os.path.join' para criar o caminho completo de forma segura.
caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

# 📋 Passo 2: A função para adicionar notas
# Esta função salva o nome e a nota no arquivo.
def adicionar_nota(aluno, nota):
    # Abrimos o arquivo no modo 'a' (append) para adicionar no final.
    # Usamos o caminho completo para garantir que o arquivo seja salvo no lugar certo.
    with open(caminho_completo, 'a', newline='') as arquivo_csv:
        # Criamos um "escritor" do CSV.
        escritor_csv = csv.writer(arquivo_csv)
        # Escrevemos a linha com o nome e a nota.
        escritor_csv.writerow([aluno, nota])
    print(f"✅ Nota de '{aluno}' adicionada com sucesso!")

# 📋 Passo 3: A função para carregar notas
# Esta função lê e exibe todas as notas do arquivo.
def carregar_notas():
    # Verificamos se o arquivo existe no caminho completo antes de tentar ler.
    if not os.path.exists(caminho_completo):
        print("📝 O arquivo de notas ainda não foi criado.")
        return

    # Abrimos o arquivo no modo 'r' (read) para ler o conteúdo.
    with open(caminho_completo, 'r', newline='') as arquivo_csv:
        # Criamos um "leitor" do CSV.
        leitor_csv = csv.reader(arquivo_csv)
        print("\n--- Notas Salvas ---")
        # O 'for' percorre cada linha do arquivo.
        for linha in leitor_csv:
            # Cada linha é uma lista com os dados.
            aluno = linha[0]
            nota = linha[1]
            print(f"Aluno: {aluno}, Nota: {nota}")
    print("--------------------")

# ======================================================================
# 🔄 Passo 4: O Loop do Menu Principal
# O programa vai rodar até o usuário escolher sair.
while True:
    print("\n--- Menu do Sistema de Notas ---")
    print("1. Adicionar nota")
    print("2. Visualizar notas")
    print("3. Sair")
    
    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        aluno = input("Nome do aluno: ")
        nota = input("Nota do aluno: ")
        adicionar_nota(aluno, nota)
        
    elif escolha == '2':
        carregar_notas()
            
    elif escolha == '3':
        print("👋 Saindo do sistema. Até a próxima!")
        break
        
    else:
        print("🚫 Opção inválida. Por favor, digite 1, 2 ou 3.")

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================