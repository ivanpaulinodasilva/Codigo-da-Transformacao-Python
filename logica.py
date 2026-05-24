# Fazendo lógica
print("Fazendo lógica")

nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Bem-vindo ao teste em Python.")

#Modulo 03 - Lógica de Programação, vamos aprender a manipular dados
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
estudante = input("Você é estudante? (sim/não): ").strip().lower()
estudante = estudante == "sim"
print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Estudante: {estudante}")

