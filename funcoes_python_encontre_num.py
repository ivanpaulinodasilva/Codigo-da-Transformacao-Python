# ======================================================================
# 🚀 Projeto: Encontrar o Maior e o Menor Valor
# ======================================================================

# 📋 Passo 1: Definir a função
# A função 'maior_menor' recebe um parâmetro: uma lista de números.
def maior_menor(lista_de_numeros):
    # Verificamos se a lista não está vazia para evitar um erro.
    if not lista_de_numeros:
        return None, None # Devolve dois valores nulos, caso a lista esteja vazia.

    # Usamos as funções nativas do Python para encontrar o maior e o menor valor.
    maior_valor = max(lista_de_numeros)
    menor_valor = min(lista_de_numeros)
    
    # A função devolve os dois valores de uma vez, separados por vírgula.
    return maior_valor, menor_valor

# ======================================================================
# 🔄 Passo 2: Usar a função com exemplos
# Vamos criar uma lista de números e testar a nossa função.

print("--- Teste com uma lista de números ---")
numeros = [12, 5, 25, 8, 17, 3, 30]

# Chamamos a função e guardamos os dois valores de retorno em variáveis separadas.
maior, menor = maior_menor(numeros)

print(f"A lista de números é: {numeros}")
print(f"O maior valor na lista é: {maior}")
print(f"O menor valor na lista é: {menor}")

print("\n--- Teste com uma lista vazia ---")
lista_vazia = []
maior_vazio, menor_vazio = maior_menor(lista_vazia)

print(f"A lista é: {lista_vazia}")
print(f"Maior valor: {maior_vazio}, Menor valor: {menor_vazio}")

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================