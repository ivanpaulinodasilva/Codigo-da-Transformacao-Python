"""
Qual é o maior? Faça um programa que peça dois números 
e diga qual deles é o maior usando a estrutura if.
"""

def mostrar_menu():
    """Exibe as opções do menu para o usuário."""
    print("\n--- Menu de Comparação de Números ---")
    print("1. Comparar Dois Números")
    print("2. Sair")
    print("------------------------------------")

def obter_numeros():
    """Solicita e retorna dois números válidos do usuário."""
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input(f"Digite o segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

def verificar_par_impar(numero):
    """Verifica se um número (inteiro) é par ou ímpar."""
    # Convertemos para int para garantir que a operação % funcione corretamente
    # para números como 4.0, que são floats mas representam inteiros.
    if int(numero) % 2 == 0:
        return "par"
    else:
        return "ímpar"

def main():
    """Função principal que executa o menu interativo."""
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1 ou 2): ")

        if escolha == '1':
            num1, num2 = obter_numeros()
            print(f"\nComparando {num1} e {num2}:")

            # Comparação de maior/menor
            if num1 > num2:
                print(f"O maior número é: {num1}")
            elif num2 > num1:
                print(f"O maior número é: {num2}")
            else:
                print("Os números são iguais.")

            # Verificação de par ou ímpar
            # Usamos int() para garantir que números como 4.0 sejam tratados como 4 para a verificação.
            print(f"{num1} é {verificar_par_impar(num1)}.")
            print(f"{num2} é {verificar_par_impar(num2)}.")

        elif escolha == '2':
            print("Saindo do programa. Até mais!")
            break  # Sai do loop while
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()