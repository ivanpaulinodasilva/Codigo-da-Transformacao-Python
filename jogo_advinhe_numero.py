# Arquivo: jogo_adivinhe_numero.py

import random
import math

# O problema prático: um jogo de adivinhação com dicas

print("Bem-vindo ao Jogo da Adivinhação!")
print("Eu escolhi um número entre 1 e 100.")
print("Tente adivinhá-lo!")

# Gera um número inteiro aleatório entre 1 e 100 (inclusivo)
numero_secreto = random.randint(1, 100)
tentativas = 0

# O loop principal do jogo
while True:
    try:
        # Pede o palpite do jogador
        palpite = int(input("\nDigite seu palpite: "))
        tentativas += 1

        # Dica usando a biblioteca 'math' (exemplo de uso)
        # Note: 'math' não é estritamente necessária para um jogo simples,
        # mas usamos aqui para atender ao requisito da atividade.
        # Por exemplo, podemos usar math.fabs() para calcular a diferença absoluta.
        diferenca = math.fabs(palpite - numero_secreto)

        # Verifica se o jogador acertou
        if palpite == numero_secreto:
            print(f"\nParabéns! Você acertou o número em {tentativas} tentativas!")
            break  # Encerra o jogo

        # Dá dicas se o palpite foi muito alto ou muito baixo
        elif palpite < numero_secreto:
            print(f"Muito baixo! A diferença para o número secreto é de aproximadamente {int(diferenca)}.")
        else:
            print(f"Muito alto! A diferença para o número secreto é de aproximadamente {int(diferenca)}.")

    except ValueError:
        # Trata o erro caso o jogador digite algo que não seja um número
        print("Entrada inválida. Por favor, digite um número inteiro.")