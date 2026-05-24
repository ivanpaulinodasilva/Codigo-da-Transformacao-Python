"""
Desafio Extra: Deixe sua mensagem ainda mais legal! 
Use a biblioteca datetime para exibir a hora atual 
junto com a saudação.
"""

# Importa a classe 'datetime' do módulo 'datetime'.
from datetime import datetime

# A função input() solicita uma entrada do usuário e armazena o valor na variável 'nome'.
nome = input("Qual é o seu nome? ")

# Obtém a hora atual do sistema usando a função 'now()' da biblioteca 'datetime'.
hora_atual = datetime.now()

# Formata a hora para exibir apenas a hora e os minutos.
hora_formatada = hora_atual.strftime("%H:%M")

# Exibe a saudação personalizada junto com a hora atual.
print(f"Oi, {nome}! A hora atual é {hora_formatada}.")