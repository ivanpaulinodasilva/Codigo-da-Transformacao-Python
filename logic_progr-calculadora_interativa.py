"""
Desafio Extra: Crie um menu interativo de calculadora! 
Use um loop while para que o usuário possa escolher entre 
Soma, Subtração e Sair, repetindo a operação até que ele decida parar.
"""

def mostrar_menu():
    """Exibe as opções do menu para o usuário."""
    print("\n--- Menu de Operações ---")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Sair")
    print("------------------------")

def obter_numeros():
    """Solicita e retorna dois números válidos do usuário."""
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

def main():
    """Função principal que executa o menu interativo."""
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1, 2 ou 3): ")

        if escolha == '1':
            num1, num2 = obter_numeros()
            resultado = num1 + num2
            print(f"Resultado da adição: {num1} + {num2} = {resultado}")
        elif escolha == '2':
            num1, num2 = obter_numeros()
            resultado = num1 - num2
            print(f"Resultado da subtração: {num1} - {num2} = {resultado}")
        elif escolha == '3':
            print("Saindo do programa. Até mais!")
            break  # Sai do loop while
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()