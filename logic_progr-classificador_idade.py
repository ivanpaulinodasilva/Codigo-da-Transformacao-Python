"""
Classificando idades: Use if-elif-else para criar um programa
que classifique a idade de uma pessoa em 
"Criança", "Adolescente", "Adulto" ou "Idoso".
"""

from datetime import datetime

def mostrar_menu():
    """Exibe as opções do menu para o usuário."""
    print("\n--- Menu de Verificação de Idade ---")
    print("1. Informar Idade e Descobrir Ano de Nascimento")
    print("2. Sair")
    print("------------------------------------")

def obter_idade_atual():
    """Solicita e retorna a idade atual válida do usuário."""
    while True:
        try:
            idade_str = input("Digite sua idade atual: ")
            idade = int(idade_str)
            
            if 0 <= idade <= 120: # Idade razoável para validação
                return idade
            else:
                print("Idade inválida. Por favor, digite uma idade entre 0 e 120 anos.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a idade.")

def main():
    """Função principal que executa o menu interativo."""
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1 ou 2): ")

        if escolha == '1':
            idade_atual = obter_idade_atual()
            
            ano_atual = datetime.now().year
            ano_nascimento = ano_atual - idade_atual

            print(f"\nConsiderando o ano atual ({ano_atual}) e sua idade de {idade_atual} anos:")
            print(f"Seu ano de nascimento é aproximadamente: {ano_nascimento}")

            if idade_atual >= 18:
                print("Você é **MAIOR** de idade!")
            else:
                print("Você é **MENOR** de idade.")

        elif escolha == '2':
            print("Saindo do programa. Até mais!")
            break  # Sai do loop while
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()