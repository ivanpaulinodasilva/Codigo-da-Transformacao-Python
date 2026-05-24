# Arquivo: programa_principal.py

# Importa o módulo 'utilidades' que criamos
import utilidades

# Exemplo de uso das funções
num1 = 10
num2 = 5

# Chama a função de soma do módulo utilidades
resultado_soma = utilidades.somar(num1, num2)
print(f"A soma de {num1} e {num2} é: {resultado_soma}")

# Chama a função de subtração
resultado_subtracao = utilidades.subtrair(num1, num2)
print(f"A subtração de {num1} e {num2} é: {resultado_subtracao}")

# Chama a função de potência
resultado_potencia = utilidades.potencia(num1, 2)
print(f"A potência de {num1} elevado a 2 é: {resultado_potencia}")