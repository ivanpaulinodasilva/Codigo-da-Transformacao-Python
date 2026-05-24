# ======================================================================
# 🚀 Projeto Integrado: Sistema de Notas com Backup Automático
# ======================================================================

# Importamos os módulos:
# 'csv' para trabalhar com a tabela, 'os' para caminhos e 'shutil' para o backup.
import csv
import os
import shutil

# 📋 Passo 1: Definir os caminhos
# O caminho da pasta principal onde o arquivo .csv vai ser salvo.
caminho_principal = "GitHub/Codigo-da-Transformacao-Python"
# O caminho da pasta onde o backup será guardado.
caminho_backup = "GitHub/Backup-Notas"

# O nome do nosso arquivo de notas.
nome_arquivo = "notas.csv"

# O caminho completo para o arquivo principal.
caminho_completo = os.path.join(caminho_principal, nome_arquivo)

# ======================================================================
# 📋 Passo 2: Funções do programa
# Função para adicionar notas ao arquivo CSV.
def adicionar_nota(aluno, nota):
    # Abrimos o arquivo no modo 'a' (append) para adicionar a nota.
    with open(caminho_completo, 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow([aluno, nota])
    print(f"✅ Nota de '{aluno}' adicionada com sucesso!")

# Função para carregar e exibir as notas do arquivo CSV.
def carregar_notas():
    # Verificamos se o arquivo existe antes de ler.
    if not os.path.exists(caminho_completo):
        print("📝 O arquivo de notas ainda não existe.")
        return

    # Abrimos o arquivo para leitura no modo 'r'.
    with open(caminho_completo, 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        print("\n--- Notas Salvas ---")
        for linha in leitor_csv:
            aluno = linha[0]
            nota = linha[1]
            print(f"Aluno: {aluno}, Nota: {nota}")
    print("--------------------")

# A nova função para fazer o backup do arquivo.
def fazer_backup():
    # Verificamos se o arquivo de notas existe para ser copiado.
    if not os.path.exists(caminho_completo):
        print("❌ Erro: O arquivo de notas não existe. Adicione uma nota primeiro.")
        return
    
    # Criamos a pasta de backup se ela não existir.
    os.makedirs(caminho_backup, exist_ok=True)
    
    # Define o caminho completo para o arquivo de backup.
    caminho_backup_completo = os.path.join(caminho_backup, nome_arquivo)
    
    # Usamos shutil.copy2() para copiar o arquivo.
    try:
        shutil.copy2(caminho_completo, caminho_backup_completo)
        print(f"✅ Backup do arquivo '{nome_arquivo}' concluído com sucesso!")
        print(f"O backup foi salvo em: {caminho_backup_completo}")
    except Exception as e:
        print(f"❌ Ocorreu um erro ao fazer o backup: {e}")

# ======================================================================
# 🔄 Passo 3: O Loop do Menu Principal
# O menu principal do programa.
while True:
    print("\n--- Sistema de Notas com Backup ---")
    print("1. Adicionar nota")
    print("2. Visualizar notas")
    print("3. Fazer Backup das Notas")
    print("4. Sair")
    
    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        aluno = input("Nome do aluno: ")
        nota = input("Nota do aluno: ")
        adicionar_nota(aluno, nota)
        
    elif escolha == '2':
        carregar_notas()
            
    elif escolha == '3':
        fazer_backup()
        
    elif escolha == '4':
        print("👋 Saindo do sistema. Até a próxima!")
        break
        
    else:
        print("🚫 Opção inválida. Por favor, digite 1, 2, 3 ou 4.")

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================